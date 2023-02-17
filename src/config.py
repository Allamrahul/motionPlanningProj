from Obstacle import *

Experiment_No = 1
# Simulation Parameters:
sampling_time = 0.2

class Static:
    def __init__(self):
        self.params = (0.0, 0.0, 0.0)
        self.imagePath = None
    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params
class Circle(Static):
    def __init__(self, pos, r):
        super(Circle, self).__init__()
        self.pos = pos
        self.radius = r

class Rectangle(Static):
    def __init__(self, pos, dim):
        super(Rectangle, self).__init__()
        self.pos = pos
        self.dim = dim

class Dynamic:
    def __init__(self, pos, r, params, path):
        self.pos = pos
        self.radius = r
        self.params = params
        self.imagePath = path

    def set_params(self, params):
        self.params = params
    def get_params(self):
        return self.params

'''
Define the Obstacles (Read Obstacle Class for Better understanding)
Sample:
Obstacle_"Name" = Obstacle  (id,
                            "Obstacle Type",
                            ["X Position", "Y Position", "Radius", "Velocity(Km/h)", "Angle(Deg)", Acceleration (m/s^2)],
                            "Sampling Time",
                            "Image Path",
                            "Color of Obstacle",
                            "Zoom for the Photo")
'''

# static obstacles

s_obs_1 = Circle([130, 70], 5.5)
s_obs_2 = Rectangle([0, 0], [30, 10])
d_obs_1 = Dynamic([40.0, 50.0], 2.5, [68, 90, 0], "../Object_Photos/police.png")

Obstacle_1 = Obstacle(1, "Static", sampling_time, s_obs_2)
Obstacle_2 = Obstacle(2, "Dynamic", sampling_time, d_obs_1)
# Obstacle_2 = Obstacle(2, "Static", [160, 80, 7.5, 0.0, 0.0, 0.0], sampling_time)
# Obstacle_3 = Obstacle(3, "Dynamic", [40.0, 50.0, 2.5, 68, 90, 0], sampling_time, "../Object_Photos/police.png")


#Form a List (Do not forget to add Obstacles in this list and also add them to the Vehicles Parameters
Obstacles = [Obstacle_1, Obstacle_2]#Obstacle_3]
