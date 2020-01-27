import hashlib as hasher
import datetime as date
from random import randint
from time import sleep
from pdf import extract_pdf

pdf_path = "./res/belami.pdf"
contributor_id = "insert your contributor_id here (40bit)"


class Block:
  # Block definition
    def __init__(self, index, previous_hash, contributor_id, data, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.contributor_id = contributor_id
        self.data = data
        self.timestamp = timestamp
        self.hash = self.hash_block()

  # Hash definition
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.contributor_id).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.timestamp).encode('utf-8'))
        return sha.hexdigest()

# Genesis block


def create_genesis_block():
    return Block(0, "0", "0000000000", extract_pdf(pdf_path, 1), date.datetime.now())

# Generate all later blocks in the blockchain


def next_block(last_block):
    this_index = last_block.index + 1
    this_hash = last_block.hash
    this_contributor_id = contributor_id
    this_data = extract_pdf(pdf_path, this_index)
    this_timestamp = date.datetime.now()
    return Block(this_index, this_hash, this_contributor_id, this_data, this_timestamp)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 5

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    sleep(randint(0, 30))
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print(block_to_add.index)
    print(block_to_add.data)
    print(block_to_add.contributor_id)
    print(block_to_add.timestamp)
    print(block_to_add.hash)
