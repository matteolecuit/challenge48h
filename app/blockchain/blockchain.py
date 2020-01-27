import os
import json
import hashlib
import datetime

from pdf import extract_pdf
from block import Block
from proof import proof_of_work

PDF_PATH = "./res/belami.pdf"
CONTRIBUTOR_ID = "insert your contributor_id here (40bit)"


CHAIN_NAME = 'belami.txt'


class Blockchain:

    def __init__(self):
        # path to chain
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.chainfile = os.path.join(dir_path, 'res', CHAIN_NAME)

        self._create_chain_if_not_exists()
        # create genesis block if chainfile is empty
        if os.stat(self.chainfile).st_size == 0:
            self._create_genesis_block()

        self.validate_chain()
        self.data = []

    def _create_chain_if_not_exists(self):
        if not os.path.isfile(self.chainfile):
            f = open(self.chainfile, 'w')
            f.close()
        return

    def _create_genesis_block(self):
        b = Block(index=0,
                  timestamp=str(datetime.datetime.now()),
                  data="Chôv's implementation of blockchain, with data queried from Bel Ami, from Guy de Maupassant",
                  contributor_id='0000000000',
                  previous_hash='0',
                  nonce=1,
                  difficulty=0)

        self._write_to_chain(b.get_block_data())
        return

    def _write_to_chain(self, block_dictionary):
        with open(self.chainfile, 'a') as f:
            f.write(json.dumps(block_dictionary) + '\n')
            f.close()
        return

    def create_new_block(self):
        with open(self.chainfile, 'r') as f:
            previous_block = f.readlines()[-1]
            previous_block = json.loads(previous_block)
            f.close()

        index = previous_block['index'] + 1
        previous_hash = previous_block['hash']
        timestamp = str(datetime.datetime.now())
        data = extract_pdf(PDF_PATH, previous_block['index'] * 5 + 1)
        contributor_id = CONTRIBUTOR_ID
        nonce, difficulty = proof_of_work(previous_hash)

        self.block = Block(index=index,
                           timestamp=timestamp,
                           data=data,
                           contributor_id=contributor_id,
                           previous_hash=previous_hash,
                           nonce=nonce,
                           difficulty=difficulty)

        self._write_to_chain(self.block.get_block_data())
        self.data = []
        return

    def _return_hash(self, previous_hash, nonce):
        sha = hashlib.sha256()
        sha.update(
            str(previous_hash).encode('utf-8') +
            str(nonce).encode('utf-8')
        )
        return sha.hexdigest()

    def _validate_hash(self, _hash, difficulty):
        if str(_hash[:difficulty]) != "0" * difficulty:  # checks for leading zeros
            msg = 'Invalid chain.'
            raise ValueError(msg)
        else:
            return True

    def validate_chain(self, chain=''):
        num_of_indexes_at_0 = 0

        if not chain:
            chain = self.chainfile

        with open(chain, 'r') as f:
            for line in f:
                block_to_validate = json.loads(line)

                difficulty = block_to_validate['difficulty']
                nonce = block_to_validate['nonce']
                index = block_to_validate['index']
                previous_hash = block_to_validate['previous_hash']

                if index == 0:
                    num_of_indexes_at_0 += 1
                else:
                    if not _hash == previous_hash:
                        msg = 'Incorrect hashes. Broken chain.'
                        print(msg)
                        raise ValueError(msg)

                _hash = block_to_validate['hash']
                _hash_to_validate = self._return_hash(previous_hash, nonce)
                self._validate_hash(_hash_to_validate, difficulty)

        if num_of_indexes_at_0 > 1:
            msg = 'Multiple genesis blocks.'
            print(msg)
            raise ValueError(msg)

        return True


b = Blockchain()
count = 0
while (count < 141):
    b.create_new_block()
    b.validate_chain()
    count += 1
