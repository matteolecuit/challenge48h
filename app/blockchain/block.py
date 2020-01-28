import hashlib


class Block:
    def __init__(self, index, timestamp, data, contributor_id, previous_hash, nonce, difficulty):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.contributor_id = contributor_id
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.difficulty = difficulty
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index).encode('utf-8')
            + str(self.timestamp).encode('utf-8')
            + str(self.data).encode('utf-8')
            + str(self.contributor_id).encode('utf-8')
            + str(self.previous_hash).encode('utf-8')
            + str(self.nonce).encode('utf-8')
            + str(self.difficulty).encode('utf-8')
        )
        return sha.hexdigest()

    def get_block_data(self):
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'contributor_id': self.contributor_id,
                'previous_hash': self.previous_hash,
                'nonce': self.nonce,
                'difficulty': self.difficulty,
                'hash': self.hash}
