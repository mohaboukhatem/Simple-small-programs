
class calcul():
    def __init__(self,text):
        self.text=text
    
    def __repr__(self):
        return str("\n"
        f"mot : {self.text} \n"
        f"len : {len(self.text)}")

print(calcul("abc"))    