n = int(input().strip())

bits = n.bit_length()
mask = (1 << bits) - 1
toggle = n ^ mask
print(toggle)