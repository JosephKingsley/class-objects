
class Student:
    
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, change_name):
        self.change_name = change_name
        print("The Student new name is", change_name)

    def change_age(self, change_age):
        self.change_age = change_age
        print("The student new age is", change_age)

    def add_tracks(self, add_tracks):
        self.add_tracks = add_tracks
        print("The Student new track is", add_tracks)

    def get_score(self):
    
        print(f"The Student new Score is",self.score)

Rito = Student(name="Rito", age=34, tracks=["FE","BE"],score=70.60)
# Expected methods
Rito.change_name("Ajas")
Rito.change_age(26)
Rito.add_tracks("Elect/Elect")
print (Rito.get_score())
