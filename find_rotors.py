from Encrypt import encrypt # The encrypt funtion is defined in encrypt.py. It will exist when repository is merged.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def find_rotors(message:str, cipher:str) -> str:
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                rotors = a + b + c
                if encrypt(rotors, message)==cipher:
                    return rotors
    return "Not found"