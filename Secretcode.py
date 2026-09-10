import random
import time

code = "".join(random.choice("0123456789ABCDEFGHIJ")
            for _ in range(20))

print("Encrypted code:")
print(code)

print("\nDecrypting code...")

for i in range(0,101,10):
    print(f"\r[{i}%]", end="%")
    time.sleep(0.15)

decoded_code = "ACCESS" + str(int(code) % 1000000)
 # Simple decryption by reversing the string
print("\nDecrypted code:")

print(decoded_code)


