from Obstacle import *
from helper import *
Experiment_No = 1
# Simulation Parameters:
sampling_time = 0.2


# Map config 1
def mapConfigs(map_config: int = 1):
    obstacles = []
    if map_config == 1:
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

    elif map_config == 2:


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


MAP_CONFIG_OPT = 2
Obstacles = mapConfigs(MAP_CONFIG_OPT)
