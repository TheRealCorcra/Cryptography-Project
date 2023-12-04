from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import os
import time

total = 0
after = 0
for i in range(3):
    before = time.perf_counter()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=15360 # 2048, 3072, 7680, 15360
    )
    public_key = private_key.public_key()
    after = time.perf_counter()
    total=total+ (after - before)
average_time = total/100
print(str(average_time))
    