from hashlib import sha256
import json
import datetime
import os

from flask import Flask, request, jsonify
import requests

from blockchain import *

app = Flask(__name__)

CONTRIBUTOR_ID = b"\x00" + secrets.token_bytes(5) + b"\x00"
# CONTRIBUTOR_ID = 'coucou'
print(CONTRIBUTOR_ID)

# the node's copy of blockchain
blockchain = Blockchain()

# the address to other participating members of the network
peers = set(['127.0.0.1:8001', '127.0.0.1:8002',
             '127.0.0.1:8003', '127.0.0.1:8004'])


# endpoint to return the node's copy of the chain.
# Our application will be using this endpoint to query
# all the posts to display.
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = blockchain._read_chain()
    print(len(blockchain.chain))
    print(chain_data[0].data)
    print(chain_data[0].data)
    print(len(chain_data))
    return json.dumps({"length": len(chain_data),
                       "chain": [p for p in chain_data],
                       "peers": list(peers)})


# endpoint to add new peers to the network.
@app.route('/register_node', methods=['POST'])
def register_new_peers():
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    # Add the node to the peer list
    peers.add(node_address)

    # Return the consensus blockchain to the newly registered node
    # so that he can sync
    return get_chain()


@app.route('/register_with', methods=['POST'])
def register_with_existing_node():
    """
    Internally calls the `register_node` endpoint to
    register current node with the node specified in the
    request, and sync the blockchain as well as peer data.
    """
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    data = {"node_address": request.host_url}
    headers = {'Content-Type': "application/json"}

    # Make a request to register with remote node and obtain information
    response = requests.post(node_address + "/register_node",
                             data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        global blockchain
        global peers
        # update chain and the peers
        chain_dump = response.json()['chain']
        blockchain = create_chain_from_dump(chain_dump)
        peers.update(response.json()['peers'])
        return "Registration successful", 200
    else:
        # if something goes wrong, pass it on to the API response
        return response.content, response.status_code


def create_chain_from_dump(chain_dump):
    generated_blockchain = Blockchain()
    for idx, block_data in enumerate(chain_dump):
        if idx == 0:
            continue  # skip genesis block
        block = Block(block_data["index"],
                      block_data["data"],
                      block_data["contributor_id"],
                      block_data["timestamp"],
                      block_data["previous_hash"],
                      block_data["nonce"],
                      block_data["difficulty"])
        proof = block_data['hash']
        added = generated_blockchain.add_block(block, proof)
        if not added:
            raise Exception("The chain dump is tampered!!")
    return generated_blockchain


# endpoint to add a block mined by someone else to
# the node's chain. The block is first verified by the node
# and then added to the chain.
@app.route('/add_block', methods=['POST'])
def verify_and_add_block():
    block_data = request.get_json()
    block = Block(block_data["index"],
                  block_data["data"],
                  block_data["contributor_id"],
                  block_data["timestamp"],
                  block_data["previous_hash"],
                  block_data["nonce"],
                  block_data["difficulty"])

    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "The block was discarded by the node", 400

    return "Block added to the chain", 201


# endpoint to query unconfirmed data
@app.route('/pending')
def get_pending():
    return json.dumps(blockchain.unconfirmed_data)


def consensus():
    """
    Our naive consensus algorithm. If a longer valid chain is
    found, our chain is replaced with it.
    """
    global blockchain

    longest_chain = None
    current_len = len(blockchain.chain)

    for node in peers:
        response = requests.get('{}chain'.format(node))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False


def announce_new_block(block):
    """
    A function to announce to the network once a block has been mined.
    Other blocks can simply verify the proof of work and add it to their
    respective chains.
    """
    for peer in peers:
        url = "{}add_block".format(peer)
        headers = {'Content-Type': "application/json"}
        requests.post(url,
                      data=json.dumps(block.__dict__, sort_keys=True),
                      headers=headers)


@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    result = blockchain.create_new_block(CONTRIBUTOR_ID)
    print(result)
    if not result:
        return "No transactions to mine"
    else:
        # Making sure we have the longest chain before announcing to the network
        chain_length = len(blockchain.chain)
        # consensus()
        # if chain_length == len(blockchain.chain):
        # announce the recently mined block to the network
        # announce_new_block(blockchain.last_block)
        res = "id:" + str(blockchain.last_block.index) + "\ntimestamp: " + str(blockchain.last_block.timestamp) + "\ndata: " + str(blockchain.last_block.data) + "\ncontributor_id: " + str(blockchain.last_block.contributor_id) + \
            "\nprevious_hash: " + str(blockchain.last_block.previous_hash) + \
            "\nnonce: " + str(blockchain.last_block.nonce) + \
            "\ndifficulty: " + str(blockchain.last_block.difficulty)
        return res


b = Blockchain()
app.run(port=8000)
# count = 0
# while (count < 141):
# ablock = b.create_new_block(CONTRIBUTOR_ID)
# print(ablock)
# count += 1
