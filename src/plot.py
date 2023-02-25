from matplotlib import pyplot as plt
import numpy as np

def plot_simulation_obs(Obstacles, Vehicles, ax, save=False, virtual_state_flag=True, Experiment_No=1):
    VEHICLE_PLOT, ARROW_PLOT, VEHICLE_PHOTO_PLOT = ([] for i in range(3))
    OBSTACLE_FIG, OBSTACLE_PHOTO = ([] for i in range(2))

    for obstacle in Obstacles:
        if obstacle.type != 'Static':
            obstacle_fig, obstacle_photo = obstacle.plot(ax)
            OBSTACLE_FIG.append(obstacle_fig)
            OBSTACLE_PHOTO.append(obstacle_photo)

    for vehicle in Vehicles:
        vehicle_plot, arrow_plot, vehicle_photo_plot = vehicle.plot(ax)
        VEHICLE_PLOT.append(vehicle_plot)
        ARROW_PLOT.append(arrow_plot)
        VEHICLE_PHOTO_PLOT.append(vehicle_photo_plot)
    # plt.savefig('MapCfg2.png')
    plt.draw()
    plt.pause(1)
    # plt.savefig("Final1.png")

    for i in range(len(VEHICLE_PLOT)):
        VEHICLE_PLOT[i].remove()
        ARROW_PLOT[i].remove()
        if VEHICLE_PHOTO_PLOT[i] != None:
            VEHICLE_PHOTO_PLOT[i].remove()

    for i in range(len(OBSTACLE_FIG)):
        OBSTACLE_FIG[i].remove()
        if OBSTACLE_PHOTO[i] != None:
            OBSTACLE_PHOTO[i].remove()



def plot_map(ax):
    map = plt.Rectangle((0, 0), 260, 150, facecolor="None", edgecolor='black')
    ax.add_artist(map)


