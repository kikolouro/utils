import random, string, sys

pw = ''
for i in range(int(sys.argv[1])):
    pw += random.choice(string.ascii_letters + "?!\"#$%&/()=:;,.-_1234567890")
print(pw)