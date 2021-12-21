import random, string, sys

pw = ''.join(
    random.choice(string.ascii_letters + "?!\"#$%&/()=:;,.-_1234567890")
    for _ in range(int(sys.argv[1]))
)

print(pw)