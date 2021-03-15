
class Regimen:
    def __init__(self,name):
        self.name=name

        self.workout1 = {"mon": "Chest", "tue": "Biceps", "wed": "Rest", "thu": "Back", "Fri": "Triceps", "sat": "Rest",
                         "sun": "Rest"}
        self.workout2 = {"mon": "Chest", "tue": "Biceps", "wed": "Cardio/Abs", "thu": "Back", "Fri": "Triceps",
                         "sat": "Legs", "sun": "Rest"}
        self.workout3 = {"mon": "Chest", "tue": "Biceps", "wed": "Cardio/Abs", "thu": "Back", "Fri": "Triceps",
                         "sat": "Legs", "sun": "Cardio"}
        self.workout4 = {"mon": "Chest", "tue": "Biceps", "wed": "Cardio", "thu": "Back", "Fri": "Triceps",
                         "sat": "Cardio", "sun": "Cardio"}




    def workouts(self,bmi):
        self.bmi = bmi
        #self.name=name
        if self.bmi < 18.5:
            self.workout = self.workout1

        elif self.bmi < 25:
            self.workout = self.workout2
        elif self.bmi < 30:
            self.workout = self.workout3
        elif self.bmi > 30:
            self.workout = self.workout4
        return self.workout
