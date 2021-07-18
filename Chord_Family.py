from Music_Scales import Scales
import os

class Chords:
    major_scale = ["Major", "Minor", "Minor", "Major", "Major", "Minor", "Diminished", "Major"]
    minor_scale = ["Minor", "Diminished", "Major", "Major", "Minor", "Minor", "Major", "Major"]
    def __init__(self):
        os.system("cls")
    
    def Chords(self, key, scale_type):
        chord_family = {}
        self.key = key.upper()
        self.scale_type = scale_type.lower()
        scale = Scales()
        scale_result = scale.Scale(self.key, self.scale_type)
        if self.scale_type == "major":
            for note,chord in zip(scale_result, self.major_scale):
                chord_family[note] = chord
        elif self.scale_type == "minor":
            for note,chord in zip(scale_result, self.minor_scale):
                chord_family[note] = chord
        else :
            print("Enter valid Scale Type..!!!!")
        return(chord_family)
        



    
    