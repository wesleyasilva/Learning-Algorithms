binary = int(input('Type a decimal number: '))
binr = ""

while(True):
    binr += str(binary%2)
    binary //= 2
    if binary == 0:
        break

binr = binr[::-1]
binr = int(binr)
print('Converted to Binary: ',binr)


decimal = str(input('\nType a binary number: '))
decimal = decimal[::-1]
dec = 0

for x in range(len(decimal)):
    if decimal[x] == "1":
        dec += 2**x

print('Converted to Decimal: ',dec)
