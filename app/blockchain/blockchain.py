import os
import json
import hashlib
import datetime
import secrets
from pdf import extract_pdf
from block import Block
from proof import proof_of_work

PDF_PATH = "./res/belami.pdf"
CONTRIBUTOR_ID = b"\x00" + secrets.token_bytes(5) + b"\x00"


class Blockchain:
    difficulty = 1

    def __init__(self):
        self.unconfirmed_transactions = []
        self.data = []
        self.chain = []

    @property
    def last_block(self):
        return self.chain[-1]

    def create_genesis_block(self):
        b = Block(index=0,
                  timestamp=str(datetime.datetime.now()),
                  data="Chôv's implementation of blockchain, with data queried from Bel Ami, from Guy de Maupassant",
                  contributor_id='0000000000',
                  previous_hash='0',
                  nonce=1,
                  difficulty=0)

        self.chain.append(b)

    def create_new_block(self, contributor_id):
        if (len(self.chain) == 0):
            self.create_genesis_block()
            print(self.last_block)
        else:
            index = self.last_block.index + 1
            previous_hash = self.last_block.hash
            timestamp = str(datetime.datetime.now())
            data = extract_pdf(PDF_PATH, self.last_block.index * 5 + 1)
            contributor_id = contributor_id
            nonce, difficulty = proof_of_work(previous_hash)

            b = Block(index=index,
                      timestamp=timestamp,
                      data=data,
                      contributor_id=contributor_id,
                      previous_hash=previous_hash,
                      nonce=nonce,
                      difficulty=difficulty)

            self.chain.append(b)
            return b

    def _return_hash(self, previous_hash, nonce):
        sha = hashlib.sha256()
        sha.update(
            str(previous_hash).encode('utf-8') +
            str(nonce).encode('utf-8')
        )
        return sha.hexdigest()

    def _read_chain(self):
        return self.chain

    def _validate_hash(self, _hash, difficulty):
        if str(_hash[:difficulty]) != "0" * difficulty:  # checks for leading zeros
            msg = 'Invalid chain.'
            raise ValueError(msg)
        else:
            return True

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # remove the hash field to recompute the hash again
            # using `compute_hash` method.
            delattr(block, "hash")

            if not cls.is_valid_proof(block, block.hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        print(block)
        return True
