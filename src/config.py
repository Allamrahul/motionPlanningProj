from Obstacle import *
from helper import *
from vehicle import vehicle
import numpy as np
Experiment_No = 1
# Simulation Parameters:
sampling_time = 0.2


# Map config 1
def mapConfigs():
    obstacles = []
    if MAP_CONFIG_OPT == 1:
        d_obs_1 = Dynamic([70.0, 10.0], 2.5, [68, 90, 0], "../Object_Photos/police.png")
        d_obs_2 = Dynamic([200.0, 140.0], 2.5, [50, 270, 0], "../Object_Photos/taxi.png")

        obstacle_1 = Obstacle(1, "Static", sampling_time, Circle([130, 75], 20)) # CC
        obstacle_2 = Obstacle(2, "Static", sampling_time, Rectangle([0, 0], [30, 20]))  # LL
        obstacle_3 = Obstacle(3, "Static", sampling_time, Rectangle([0, 55], [30, 40]))  # ML
        obstacle_4 = Obstacle(4, "Static", sampling_time, Rectangle([0, 130], [30, 20]))  # UL
        obstacle_5 = Obstacle(5, "Static", sampling_time, Rectangle([115, 130], [30, 20]))  # UM
        obstacle_6 = Obstacle(6, "Static", sampling_time, Rectangle([230, 130], [30, 20]))  # UR
        obstacle_7 = Obstacle(7, "Static", sampling_time, Rectangle([230, 55], [30, 40]))  # MR
        obstacle_8 = Obstacle(8, "Static", sampling_time, Rectangle([230, 0], [30, 20]))  # LR
        obstacle_9 = Obstacle(9, "Static", sampling_time, Rectangle([115, 0], [30, 20]))  # LM
        obstacle_10 = Obstacle(10, "Dynamic", sampling_time, d_obs_1)
        obstacle_11 = Obstacle(11, "Dynamic", sampling_time, d_obs_2)

        # Form a List (Do not forget to add Obstacles in this list and also add them to the Vehicles Parameters

        obstacles = [obstacle_1,
                     obstacle_2,
                     obstacle_3,
                     obstacle_4,
                     obstacle_5,
                     obstacle_6,
                     obstacle_7,
                     obstacle_8,
                     obstacle_9,
                     obstacle_10,
                     obstacle_11]

    elif MAP_CONFIG_OPT == 2:


        # obstacle_1 = Obstacle(1, "Static", sampling_time, Circle([130, 75], 20))  # CC
        obstacle_1 = Obstacle(1, "Static", sampling_time, Rectangle([35, 115], [30, 20]))  # LL
        obstacle_2 = Obstacle(2, "Static", sampling_time, Rectangle([115, 115], [30, 20]))  # ML
        obstacle_3 = Obstacle(3, "Static", sampling_time, Rectangle([195, 115], [30, 20]))  # UL

        obstacle_4 = Obstacle(4, "Static", sampling_time, Rectangle([35, 65], [30, 20]))  # LL
        obstacle_5 = Obstacle(5, "Static", sampling_time, Circle([130, 75], 13))  # ML
        obstacle_6 = Obstacle(6, "Static", sampling_time, Rectangle([195, 65], [30, 20]))  # UL

        obstacle_7 = Obstacle(7, "Static", sampling_time, Rectangle([35, 15], [30, 20]))  # LL
        obstacle_8 = Obstacle(8, "Static", sampling_time, Rectangle([115, 15], [30, 20]))  # ML
        obstacle_9 = Obstacle(9, "Static", sampling_time, Rectangle([195, 15], [30, 20]))  # UL

        d_obs_1 = Dynamic([10.0, 100.0], 2.5, [100, 360, 0], "../Object_Photos/police.png")
        d_obs_2 = Dynamic([240.0, 50.0], 2.5, [100, 180, 0], "../Object_Photos/taxi.png")
        obstacle_10 = Obstacle(10, "Dynamic", sampling_time, d_obs_1)
        obstacle_11 = Obstacle(11, "Dynamic", sampling_time, d_obs_2)

        # Form a List (Do not forget to add Obstacles in this list and also add them to the Vehicles Parameters

        obstacles = [obstacle_1,
                     obstacle_2,
                     obstacle_3,
                     obstacle_4,
                     obstacle_5,
                     obstacle_6,
                     obstacle_7,
                     obstacle_8,
                     obstacle_9,
                     obstacle_10,
                     obstacle_11]

    return obstacles


def get_vehicles():
    if MAP_CONFIG_OPT == 1:
        vehicle1 = vehicle(1,
                           start=[15, 110, 0, 0],
                           goal=[[250, 110]],
                           sampling_time=0.1,
                           begin_time=0,
                           inital_control_input=[50, 0],
                           path="../Object_Photos/aventador_y.png",
                           COLOR="#3498db",
                           ZOOM=0.01)

        vehicle2 = vehicle(2,
                           start=[15, 40, 0, 0],
                           goal=[[250, 40]],
                           sampling_time=0.1,
                           begin_time=0,
                           inital_control_input=[50, 0],
                           path="../Object_Photos/ferrari_2.png",
                           ZOOM=0.03)

        Vehicles = [vehicle1,
                    vehicle2]
    elif MAP_CONFIG_OPT == 2:
        vehicle1 = vehicle(1,
                           start=[90, 140, -np.pi/2, 0],
                           goal=[[90, 10]],
                           sampling_time=0.1,
                           begin_time=0,
                           inital_control_input=[50, 0],
                           path="../Object_Photos/aventador_y.png",
                           COLOR="#3498db",
                           ZOOM=0.01)

        vehicle2 = vehicle(2,
                           start=[170, 140, -np.pi/2, 0],
                           goal=[[170, 10]],
                           sampling_time=0.1,
                           begin_time=0,
                           inital_control_input=[50, 0],
                           path="../Object_Photos/ferrari_2.png",
                           ZOOM=0.03)

        Vehicles = [vehicle1,
                    vehicle2]

    return Vehicles


MAP_CONFIG_OPT = 2
Obstacles = mapConfigs()
Vehicles = get_vehicles()

