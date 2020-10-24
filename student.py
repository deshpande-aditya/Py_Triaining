#Create class for student

class student:
    def __init__(self, name, speciality, percent, year):
        self.name = name
        self.speciality = speciality
        self.percent = percent
        self.year = year

    def on_honor_roll(self):
        if self.percent >=75:
            return True
        else:
            return False

