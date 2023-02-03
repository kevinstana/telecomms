import commlib as cl

# Creates PAM waveforms for given M
def create_pam(bits, M, linebreak):
    
    # Creates an object of the pam_constellation class for given M
    pam = cl.pam_constellation(M)
    m = pam.m
    
    # To add extra bits if needed
    if (len(bits) % m) != 0:        
        while ( len(bits) % m ) != 0:
            bits = bits + '0'
        
    # The symbols for each bitgroup of the binary_name
    symbols, bitgroups = pam.bits_to_symbols(bits, return_groups=True)
    
    # Prints diagnostics to give an idea of what is going on
    print("For M =", M)
    print("The map in general is: \n")
    for key, value in pam.map.items():
        print(key, ":", "{:>5}".format(value))
    print()
    print("The map for the given input has " + str(len(bitgroups)) + 
          " bitgroups and is: \n")
    for i, bitgroup in enumerate(bitgroups):
        print( ('0' + str(i) if i < 10 else str(i))  + ')', 
              bitgroup, ":", "{:>5}".format(symbols[i]))
    print()
    print(linebreak)
    print()
    
    # Plots the PAM waveform for current M
    pam_wave = cl.digital_signal(1e-9, 1000, 0, 0.0, pam)
    pam_wave.modulate_from_symbols(symbols)
    pam_wave.plot()