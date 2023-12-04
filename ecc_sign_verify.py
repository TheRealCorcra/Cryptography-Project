from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import os
import time

total_sign_time = 0
total_verify_time = 0

for i in range(10):
    private_key = ec.generate_private_key(
        ec.SECP256R1()  # Adjust the curve as needed, however 256 bit is only one that is available
    )

    public_key = private_key.public_key()

    message = os.urandom(80)

    # Signing
    before_sign = time.perf_counter()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after_sign = time.perf_counter()
    sign_time = after_sign - before_sign
    total_sign_time += sign_time

    # Verification
    before_verify = time.perf_counter()
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    after_verify = time.perf_counter()
    verify_time = after_verify - before_verify
    total_verify_time += verify_time

    print("\nMessage:", message.hex())
    print("\nSignature:", signature.hex())

    print("\nTime taken for signing: {:.5f} seconds".format(sign_time))
    print("Time taken for verification: {:.5f} seconds".format(verify_time))

print("\nTotal time for signing over 10 iterations: {:.5f} seconds".format(total_sign_time))
print("Total time for verification over 10 iterations: {:.5f} seconds".format(total_verify_time))
