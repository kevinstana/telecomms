import matplotlib.pyplot as plt
from meros_2a import create_pam

def to_binary(name):
    return ''.join(format(ord(i),'b').zfill(8) for i in name)

plt.close('all')
linebreak = "========================================"

name = "Kevin Stana"

# Converts the name to a string of bits
bits = to_binary(name)
bits_length = str(len(bits))

print("The input you gave is: " + name)
print("The input as binary has " + bits_length + " bits " 
      + "and is the folowing: \n" + bits)
print()
print(linebreak)
print()

for M in [2, 4, 8, 16]:
    
    create_pam(bits, M, linebreak)
    