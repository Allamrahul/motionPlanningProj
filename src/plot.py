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
    # box1 = plt.Rectangle((0, 0), 30, 10, facecolor="None", edgecolor='black', hatch="/")
    # box2 = plt.Rectangle((0, 50), 30, 40, facecolor="None", edgecolor='black', hatch="/")
    # box3 = plt.Rectangle((0, 130), 30, 20, facecolor="None", edgecolor='black', hatch="/")
    # box4 = plt.Rectangle((70, 130), 40, 20, facecolor="None", edgecolor='black', hatch="/")
    # box5 = plt.Rectangle((150, 130), 40, 20, facecolor="None", edgecolor='black', hatch="/")
    # box6 = plt.Rectangle((230, 130), 30, 20, facecolor="None", edgecolor='black', hatch="/")
    # box7 = plt.Rectangle((70, 0), 40, 10, facecolor="None", edgecolor='black', hatch="/")
    # box8 = plt.Rectangle((150, 0), 40, 10, facecolor="None", edgecolor='black', hatch="/")
    # box9 = plt.Rectangle((230, 0), 30, 10, facecolor="None", edgecolor='black', hatch="/")
    # box10 = plt.Rectangle((230, 50), 30, 40, facecolor="None", edgecolor='black', hatch="/")
    # box11 = plt.Rectangle((70, 50), 10, 40, facecolor="None", edgecolor='black', hatch="/")
    # box12 = plt.Rectangle((180, 50), 10, 40, facecolor="None", edgecolor='black', hatch="/")
    # round_about = plt.Circle((130, 70), 15, facecolor="None", edgecolor='black', hatch="/")

    ax.add_artist(map)
    # ax.add_artist(box1)
    # ax.add_artist(box2)
    # ax.add_artist(box3)
    # ax.add_artist(box4)
    # ax.add_artist(box5)
    # ax.add_artist(box6)
    # ax.add_artist(box7)
    # ax.add_artist(box8)
    # ax.add_artist(box9)
    # ax.add_artist(box10)
    # ax.add_artist(box11)
    # ax.add_artist(box12)
    # ax.add_artist(round_about)

