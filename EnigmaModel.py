# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

from EnigmaView import EnigmaView


class Rotor:
    def __init__(self,permutation,location):
        self.permutation = permutation
        self.location = location
        self.inverse = invert_permutation(permutation)

    def advance(self):
         self.location = (self.location + 1) % 26
         return self.location == 0

from EnigmaConstants import ALPHABET
reflector_permutation = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

def apply_permutation(letter,permutation,offset):
    index = ALPHABET.index(letter)
    shifted_index = (index + offset) % 26
    permuted_letter = permutation[shifted_index]
    final_index = (ALPHABET.index(permuted_letter) - offset) % 26
    return ALPHABET[final_index] 
def invert_permutation(permutation):
    inverse = [''] * 26
    for i in range(26):
        letter = permutation[i]
        location = ALPHABET.index(letter)
        inverse[location] = ALPHABET[i]
    return "".join(inverse)





class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self.slow_rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",0)
        self.medium_rotor = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE",0) 
        self.fast_rotor = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO",0) 
        self.slow_rotor.inverse = invert_permutation(self.slow_rotor.permutation)
        self.medium_rotor.inverse = invert_permutation(self.medium_rotor.permutation)
        self.fast_rotor.inverse = invert_permutation(self.fast_rotor.permutation)
        self.key_dict = { "A": False,
            "B": False,
            "C": False,
            "D": False,
            "E": False,
            "F": False,
            "G": False,
            "H": False,
            "I": False,
            "J": False,
            "K": False,
            "L": False,
            "M": False,
            "N": False,
            "O": False,
            "P": False,
            "Q": False,
            "R": False,
            "S": False,
            "T": False,
            "U": False,
            "V": False,
            "W": False,
            "X": False,
            "Y": False,
            "Z": False
        }
        self.lamp_dict = {"A": False,
            "B": False,
            "C": False,
            "D": False,
            "E": False,
            "F": False,
            "G": False,
            "H": False,
            "I": False,
            "J": False,
            "K": False,
            "L": False,
            "M": False,
            "N": False,
            "O": False,
            "P": False,
            "Q": False,
            "R": False,
            "S": False,
            "T": False,
            "U": False,
            "V": False,
            "W": False,
            "X": False,
            "Y": False,
            "Z": False
        }
    

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.key_dict[letter]

    def is_lamp_on(self, letter):
        return self.lamp_dict[letter]       # In the stub version, lamps are always off

    def key_pressed(self, letter):
        self.key_dict[letter] = True
        self.fast_rotor.advance()

        carry_fast = self.fast_rotor.advance()
        if carry_fast:
            carry_medium = self.medium_rotor.advance()
            if carry_medium:
                self.slow_rotor.advance()
        
        fast_out =apply_permutation(letter,self.fast_rotor.permutation,self.fast_rotor.location)
        medium_out =apply_permutation(fast_out,self.medium_rotor.permutation,self.medium_rotor.location)
        slow_out =apply_permutation(medium_out,self.slow_rotor.permutation,self.slow_rotor.location)
        reflector_out = apply_permutation(slow_out,reflector_permutation, 0)
        slow_back = apply_permutation(reflector_out,self.slow_rotor.inverse,self.slow_rotor.location)
        medium_back = apply_permutation(slow_back,self.medium_rotor.inverse,self.slow_rotor.location)
        output_letter = apply_permutation(medium_back,self.fast_rotor.inverse,self.fast_rotor.location)

        for key in self.lamp_dict:
            self.lamp_dict[key] = False
        self.lamp_dict[output_letter] = True
        self.update()

    def key_released(self, letter):
        self.key_dict[letter] = False

        for key in self.lamp_dict:
            self.lamp_dict[key] = False

        self.update()

    def get_rotor_letter(self, index):
        if index == 0:
            return self.slow_rotor.permutation[self.slow_rotor.location]#In the stub version, all rotors are set to "A"
        elif index == 1:
            return self.medium_rotor.permutation[self.medium_rotor.location]#self.medium_Rotor.value()
        elif index == 2:
            return self.fast_rotor.permutation[self.fast_rotor.location]#self.fast_Rotor.value()

    def rotor_clicked(self, index):
        if index == 0:
            self.slow_rotor.advance()
        elif index == 1:
            self.medium_rotor.advance()
        elif index == 2:
            self.fast_rotor.advance()
          # You need to fill in this code
        self.update()

        
def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)
    model.update()

# Startup code

if __name__ == "__main__":
    enigma()
