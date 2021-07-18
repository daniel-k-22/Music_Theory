from Music_Scales import Scales
from Chord_Family import Chords
from Chord import Chord_Structure
import os 


class Music_Theory():
    def __init__(self, author):
        os.system("cls")
        print("Welcome to the Music Theory...!!!")
        print(f"Author : {author}")
        print("Date : 17th July 2021")
        print()
    
    def Print_Scale(self):
        key = input("Enter the key of the Scale :")
        scale_type = input("Enter the Scale Type :")
        scale = Scales()
        result = scale.Scale(key,scale_type)
        print(f"{key} {scale_type} Scale : {result}")
    
    def Print_Major_Scales(self):
        scale_type = "Major"
        scale = Scales()
        for root in scale.notes:
            result = scale.Scale(root,scale_type)
            print(f"{root} {scale_type} Scale : {result}")

    def Print_Minor_Scales(self):
        scale_type = "Minor"
        scale = Scales()
        for root in scale.notes:
            result = scale.Scale(root,scale_type)
            print(f"{root} {scale_type} Scale : {result}")
    
    def Print_Chord_Family(self):
        key = input("Enter the key of the Scale :")
        scale_type = input("Enter the Scale Type :")
        chords = Chords()
        chords_result = chords.Chords(key,scale_type)
        print(f"{key} {scale_type} Chord Family : {chords_result}")
    
    def Print_Chord(self):
        key = input("Enter the key of the chord :")
        scale_type = input("Enter the Scale Type :")
        chord_type = input("Enter the Type of Chord :") 
        chord = Chord_Structure()
        chord_result = chord.Chord(key, scale_type, chord_type)
        print(f"{key} {scale_type} {chord_type} : {chord_result}")