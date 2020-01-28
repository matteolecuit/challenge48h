import hashlib


def proof_of_work(previous_hash, difficulty=1):
    nonce = None
    incrementor = 0
    leading_zeroes = '0' * difficulty

    while not nonce:
        sha = hashlib.sha256()
        sha.update(
            str(previous_hash).encode('utf-8') +
            str(incrementor).encode('utf-8')
        )
        challenge_hash = sha.hexdigest()
        if str(challenge_hash[:difficulty]) == leading_zeroes:
            nonce = incrementor
        else:
            incrementor += 1
    return nonce, difficulty
