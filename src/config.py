from Obstacle import *

Experiment_No = 1
# Simulation Parameters:
sampling_time = 0.2

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

Obstacle_1 = Obstacle(1, "Static", [130, 70, 5.5, 0.0, 0.0, 0.0], sampling_time)
Obstacle_2 = Obstacle(2, "Static", [160, 80, 7.5, 0.0, 0.0, 0.0], sampling_time)
Obstacle_3 = Obstacle(3, "Dynamic", [40.0, 50.0, 2.5, 68, 90, 0], sampling_time, "../Object_Photos/police.png")


#Form a List (Do not forget to add Obstacles in this list and also add them to the Vehicles Parameters
Obstacles = [Obstacle_1, Obstacle_2, Obstacle_3]
