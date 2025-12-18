from Encrypt import encrypt # The encrypt funtion is defined in encrypt.py

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def find_rotors(message:str, cipher:str) -> str:
    for a in ALPHABET:
        for b in ALPHABET:        # Systematically tries every possible rotor setting
            for c in ALPHABET:
                rotors = a + b + c
                if encrypt(rotors, message)==cipher: # Checks if output of encrypt() matches the cipher
                    return rotors # If match found return the corresponding rotors
    return "Not found" # If no match found 
