import hashlib
from mnemonic import Mnemonic

# 1. Define your exact custom string
custom_string = "Neloni@1999"

# 2. Hash the string using SHA-256 to generate raw bytes
hash_bytes = hashlib.sha256(custom_string.encode('utf-8')).digest()

# 3. Extract exactly 128 bits (16 bytes) of entropy from the hash
entropy_128_bits = hash_bytes[:16]

# 4. Generate the BIP39 seed phrase using that specific entropy
mnemo = Mnemonic("english")
seed_phrase = mnemo.to_mnemonic(entropy_128_bits)

print("Your 12-word seed phrase:")
print(seed_phrase)