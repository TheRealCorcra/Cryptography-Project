from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, dsa
import os
import time

total = 0
after = 0
for i in range(10):
    before = time.perf_counter()
    private_key = dsa.generate_private_key(
        key_size=7680 # 2048, 3072, 7680, 15360
    )
    public_key = private_key.public_key()
    after = time.perf_counter()
    total=total+ (after - before)
average_time = total/100
print(str(average_time))
    