import commlib as cl
import matplotlib.pyplot as plt

# Creates PAM waveforms for given M
def create_pam(bits, M):
    
    linebreak = "========================================"
    
    # Creates an object of the pam_constellation class for given M
    pam = cl.pam_constellation(M)
    m = pam.m
    
    # To add extra bits if needed
    while ( len(bits) % m ) != 0:
        bits = bits + '0'
        
    # The symbols for each bitgroup of the name
    symbols, bitgroups = pam.bits_to_symbols(bits, return_groups=True)
    
    bitgroups_length = len(bitgroups)
    
    # Prints diagnostics
    print()
    print(linebreak)
    print()
    print(f'For M = {M}')
    print('The map in general is: \n')
    for key, value in pam.map.items():
        print(key, ":", "{:>5}".format(value))
    print()
    print(f'The map for the given input has {bitgroups_length} bitgroups and is: \n')
    for i, bitgroup in enumerate(bitgroups):
        print( ('0' + str(i) if i < 10 else str(i))  + ')', 
              bitgroup, ":", "{:>5}".format(symbols[i]))
    
    Rb = 1e+9
    Tb = 1 / Rb
    Ts = Tb * m

    title = f'{M}-PAM'
    tguard = 10 * Ts
    
    # Plots the PAM waveform for current M
    pam_wave = cl.digital_signal(Ts, 1000, 0, tguard, pam)
    pam_wave.modulate_from_symbols(symbols)
    pam_wave.plot(pam_title = title)

# Converts the name to a string of bits
def to_binary(name):
    return ''.join(format(ord(i),'b').zfill(8) for i in name)

# name = input("Give an input: ")
name = "Kevin Stana"

bits = to_binary(name)
bits_length = len(bits)

print(f'\nThe input you gave is: {name}\n')

print(f'The input as binary has {bits_length} bits and is the folowing:\n{bits}')

plt.close('all')

for M in [2, 4, 8, 16]: 
    
    create_pam(bits, M)

plt.show()




