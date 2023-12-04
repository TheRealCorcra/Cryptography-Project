from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, ec
import os
import time

total = 0
after = 0
for i in range(10):
    before = time.perf_counter()
    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )
    public_key = private_key.public_key()
    message = os.urandom(50)

    after = time.perf_counter()
    total=total+ (after - before)
average_time = total/100
print(str(average_time))