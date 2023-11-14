import random
import hashlib

'''
A mnemonic seed generator is a tool or algorithm used to generate a sequence of words, known as a mnemonic seed or mnemonic phrase, that serves as a human-readable representation of a cryptographic key or seed.
 Mnemonic seeds are commonly used in the context of cryptocurrency wallets, particularly those that implement Hierarchical Deterministic (HD) key generation.

The different components of such generator include:
Entropy Generator
Checksum Calculator
Word list
Word list selection
Human readable representation
'''

def generate_entropy(bits):
    # Generate random bits for entropy
    entropy = ''.join(str(random.randint(0, 1)) for _ in range(bits))
    return entropy

def calculate_checksum(entropy):
    # Calculate the SHA256 hash of the entropy
    hash_result = hashlib.sha256(entropy.encode()).hexdigest()
    # Take the first 'checksum_bits' bits as checksum
    checksum_bits = len(entropy) // 32  # For example, 128 bits for 4,096-bit entropy
    checksum = bin(int(hash_result, 16))[2:].zfill(len(entropy))[:checksum_bits]
    return checksum

def generate_mnemonic(bits=128, checksum_bits=4):
    # Generate entropy
    entropy = generate_entropy(bits)
    # Calculate checksum
    checksum = calculate_checksum(entropy)
    # Combine entropy and checksum
    combined_bits = entropy + checksum
    # Divide the combined bits into groups of 11 bits
    groups_of_11_bits = [combined_bits[i:i+11] for i in range(0, len(combined_bits), 11)]
    # Map each group to a word in a predefined word list
    word_list = ["ubuntu", "ughali", "eko", "ukwa", "akwaaba", "asante", "lome"]
    mnemonic = ' '.join([word_list[int(group, 2)] for group in groups_of_11_bits])
    return mnemonic

# Example usage
mnemonic = generate_mnemonic()
print("Generated Mnemonic:", mnemonic)
