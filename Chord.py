from Music_Scales import Scales
import os

class Chord_Structure:
    def __init__(self):
        os.system("cls")

    def Chord(self, key, scale_type, chord_type):
        self.key = key.upper()
        self.scale_type = scale_type.lower()
        self.chord_type = chord_type.lower()
        scale = Scales()
        scale_result = scale.Scale(self.key, self.scale_type)
        if self.chord_type == "triad":
            result = self.Triad(scale_result)
        if self.chord_type == "sus2":
            result = self.Sus2(scale_result)
        if self.chord_type == "sus4":
            result = self.Sus4(scale_result)
        return(result)

    def Triad(self, scale): # 1-3-5 chord
        chord = scale[0] + "-" + scale[2] + "-" + scale[4]
        return(chord)
    def Sus2(self, scale): # 1-2-5 chord
        chord = scale[0] + "-" + scale[1] + "-" + scale[4]
        return(chord)
    def Sus4(self, scale): # 1-2-5 chord
        chord = scale[0] + "-" + scale[3] + "-" + scale[4]
        return(chord)
        
