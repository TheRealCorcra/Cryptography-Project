from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os
import time

total_encrypt = 0
total_decrypt = 0

for i in range(10):
    # Key generation
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048  # 2048, 3072, 7680, 15360
    )

    public_key = private_key.public_key()

    short_plaintext = os.urandom(112)  # bits, change accordingly

    # Encryption
    before_encrypt = time.perf_counter()
    short_ciphertext = public_key.encrypt(
        short_plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    after_encrypt = time.perf_counter()
    total_encrypt += (after_encrypt - before_encrypt)

    # Decryption
    before_decrypt = time.perf_counter()
    short_plaintext_2 = private_key.decrypt(
        short_ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    after_decrypt = time.perf_counter()
    total_decrypt += (after_decrypt - before_decrypt)

    # Print results for each iteration
    print()
    print("Plaintext:", short_plaintext.hex())
    print()
    print("Ciphertext:", short_ciphertext.hex())
    print()
    print("Original Plaintext:", short_plaintext_2.hex())

average_time_encrypt = total_encrypt / 10
average_time_decrypt = total_decrypt / 10

print("\nAverage Encryption Time: {:.5f} seconds".format(average_time_encrypt))
print("Average Decryption Time: {:.5f} seconds".format(average_time_decrypt))
