from Obstacle import *
from helper import *
from vehicle import vehicle
import numpy as np
Experiment_No = 1
# Simulation Parameters:
sampling_time = 0.2
prediction_horizon = 15
offset = [40, 80]

# Map config 1
def mapConfigs():
    obstacles = []
    if MAP_CONFIG_OPT == 1:
        d_obs_1 = Dynamic([70.0, 10.0], 2.5, [50, 90, 0], "../Object_Photos/police.png")
        d_obs_2 = Dynamic([200.0, 120.0], 2.5, [50, 270, 0], "../Object_Photos/police.png")

        # obstacle_1 = Obstacle(1, "Static", sampling_time, Circle([130, 105], 20))  # CC
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

        obstacles = [
                    obstacle_1,
                     obstacle_2,
                     obstacle_3,
                     obstacle_4,
                     obstacle_5,
                     obstacle_6,
                     obstacle_7,
                     obstacle_8,
                     obstacle_9,
                     obstacle_10,
                     obstacle_11
                     ]

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
        Start_1 = [15, 110, 0, 0]
        Goal_1 = [
            [75.0, 110.0, 0.0, 0.0],
                  [125.0, 110.0, 0.0, 0.0],
            [155.0, 110.0, 0.0, 0.0],
            [185.0, 90.0, 270.0, 0.0],
            [185.0, 60.0, 270.0, 0.0],
            [200.0, 40.0, 0.0, 0.0],
            [245.0, 40.0, 0.0, 0.0]
                  # [210.0, 90.0, -90.0, 0.0],
                  # [210.0, 10.0, -90.0, 0.0]
                  ]
        inital_control_input_1 = [30.0, 0.0]


        start_time_1 = 0
        vehicle1 = vehicle(1,
                           start=Start_1,
                           goal_list=Goal_1,
                           inital_control_input=inital_control_input_1,
                           max_v=120.0,
                           max_phi=10,
                           max_delta=30,
                           start_time=start_time_1,
                           sampling_time=sampling_time,
                           prediction_horizon=prediction_horizon,
                           Obstacles=[Obstacles[-1], Obstacles[-2], Obstacles[-3], Obstacles[-4], Obstacles[0]],
                           offset=offset,
                           VO_Type="VO",
                           COLOR="#3498db",
                           COLOR_NAME="Yellow",
                           path="../Object_Photos/aventador_y.png",
                           ZOOM=0.01)

        Start_2 = [15, 40, 0, 0]
        Goal_2 = [
                  [70.0, 40, 180.0, 0.0],
                  [100.0, 50, 135.0, 0.0],
                  [100.0, 90.0, 90.0, 0.0],
                  [130.0, 110.0, 0.0, 0.0],
                  [185.0, 110.0, 0.0, 0.0],
                  [250.0, 110.0, 0.0, 0.0]]
        inital_control_input_2 = [30.0, 0.0]

        start_time_2 = 0

        vehicle2 = vehicle(2,
                           start=Start_2,
                           goal_list=Goal_2,
                           inital_control_input=inital_control_input_2,
                           max_v=120.0,
                           max_phi=10,
                           max_delta=30,
                           start_time=start_time_2,
                           sampling_time=sampling_time,
                           prediction_horizon=prediction_horizon,
                           Obstacles=[Obstacles[-1], Obstacles[-2], Obstacles[-3], Obstacles[-4], Obstacles[0]],
                           offset=offset,
                           VO_Type="VO",
                           COLOR="#f1c40f",
                           COLOR_NAME="Yellow",
                           path="../Object_Photos/ferrari_2.png",
                           ZOOM=0.03)

        Vehicles = [vehicle1,
                    vehicle2
                    ]
    elif MAP_CONFIG_OPT == 2:
        Start_1 = [25, 140, -90, 0]
        Goal_1 = [
             [25, 120, 0, 0],
             [35, 100, 0, 0],
             [90, 100, 0, 0],
             [120, 100, 0, 0],
             [155, 100, 0, 0],
             [170, 85, 0, 0],
             [170, 60, 0, 0],
             [190, 50, 0, 0],
             [215, 50, 0, 0],
             [235, 40, 0, 0],
             [240, 10, 0, 0]
        ]
        inital_control_input_1 = [30.0, 0.0]

        start_time_1 = 0
        vehicle1 = vehicle(1,
                           start=Start_1,
                           goal_list=Goal_1,
                           inital_control_input=inital_control_input_1,
                           max_v=120.0,
                           max_phi=10,
                           max_delta=30,
                           start_time=start_time_1,
                           sampling_time=sampling_time,
                           prediction_horizon=prediction_horizon,
                           Obstacles=[Obstacles[-1], Obstacles[-2], Obstacles[-3], Obstacles[-4], Obstacles[0]],
                           offset=offset,
                           VO_Type="VO",
                           COLOR="#3498db",
                           COLOR_NAME="Yellow",
                           path="../Object_Photos/aventador_y.png",
                           ZOOM=0.01)

        Start_2 = [240, 130, -90, 0]
        Goal_2 = [
            [240, 115, 0, 0],
            [225, 100, 0, 0],
            [190, 100, 0, 0],
            [160, 100, 0, 0],
            [130, 100, 0, 0],
            [90, 85, 0, 0],
            [90, 60, 0, 0],
            [70, 50, 0, 0],
            [35, 50, 0, 0],
            [25, 35, 0, 0],
            [20, 15, 0, 0]
            ]
        inital_control_input_2 = [30.0, 0.0]

        start_time_2 = 0

        vehicle2 = vehicle(2,
                           start=Start_2,
                           goal_list=Goal_2,
                           inital_control_input=inital_control_input_2,
                           max_v=120.0,
                           max_phi=10,
                           max_delta=30,
                           start_time=start_time_2,
                           sampling_time=sampling_time,
                           prediction_horizon=prediction_horizon,
                           Obstacles=[Obstacles[-1], Obstacles[-2], Obstacles[-3], Obstacles[-4], Obstacles[0]],
                           offset=offset,
                           VO_Type="VO",
                           COLOR="#f1c40f",
                           COLOR_NAME="Yellow",
                           path="../Object_Photos/ferrari_2.png",
                           ZOOM=0.03)

        Vehicles = [vehicle1,
                    vehicle2]

    return Vehicles


MAP_CONFIG_OPT = 2
Obstacles = mapConfigs()
Vehicles = get_vehicles()

