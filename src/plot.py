from matplotlib import pyplot as plt
import numpy as np

def plot_simulation_obs(Obstacles, ax, save=False, virtual_state_flag=True, Experiment_No=1):

    OBSTACLE_FIG, OBSTACLE_PHOTO = ([] for i in range(2))

    for obstacle in Obstacles:
        if obstacle.type != 'Static':
            obstacle_fig, obstacle_photo = obstacle.plot(ax)
            OBSTACLE_FIG.append(obstacle_fig)
            OBSTACLE_PHOTO.append(obstacle_photo)

    plt.draw()
    plt.pause(1)

    for i in range(len(OBSTACLE_FIG)):
        OBSTACLE_FIG[i].remove()
        if OBSTACLE_PHOTO[i] != None:
            OBSTACLE_PHOTO[i].remove()

def plot_map(ax):
    map = plt.Rectangle((0, 0), 260, 150, facecolor="None", edgecolor='black')
    ax.add_artist(map)


