class Robot:
    def __init__(self, model, series, designation):
        self.model = model
        self.series = series 
        self.designation = designation

robot1 = Robot("R1", 1, "Agriculture")

print(robot1.model,robot1.series)