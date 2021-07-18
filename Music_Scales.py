import os

class Scales:
    key = ""
    scale_type = ""
    notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    M_inc = [2,2,1,2,2,2,1]
    m_inc = [2,1,2,2,1,2,2]
    def __init__(self):
        os.system("cls")
        print("Notes in Music :", self.notes)
        print()

    def Scale(self, key, scale_type):
        self.key = key.upper()
        self.scale_type = scale_type.lower()
        if self.scale_type == "major":
            M_scale = []
            M_steps = []
            # Root
            root_index = self.notes.index(self.key)
            M_steps.append(root_index)
            M_scale.append(self.key)
            # Other notes
            start = root_index
            for ind in self.M_inc:
                step = start + ind
                M_steps.append(step)
                if step == 12:
                    step = 0
                elif step == 13:
                    step = 1
                else:
                    pass
                M_scale.append(self.notes[step])
                start = step
            #print(f"{self.key} {self.scale_type} Scale : {M_scale}")
            #print(f"Steps : {M_steps}")
            return(M_scale)
    
        elif self.scale_type.lower() == "minor":
            m_scale = []
            m_steps = []
            # Root
            root_index = self.notes.index(self.key)
            m_steps.append(root_index)
            m_scale.append(self.key)
            # Other notes
            start = root_index
            for ind in self.m_inc:
                step = start + ind
                m_steps.append(step)
                if step == 12:
                    step = 0
                elif step == 13:
                    step = 1
                else:
                    pass
                m_scale.append(self.notes[step])
                start = step
            #print(f"{self.key} {self.scale_type} Scale : {m_scale}")
            #print(f"Steps : {m_steps}")
            return(m_scale)
        else :
            print("Enter Valid Scale Type....!!!!")
