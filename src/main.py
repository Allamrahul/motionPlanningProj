from matplotlib import pyplot as plt
from Obstacle import *
from config import *
import plot

def obsOob(obstacle):
    return obstacle.parameters[0] < ws_limits[0][0] or obstacle.parameters[0] > ws_limits[0][1] or \
                    obstacle.parameters[1] < ws_limits[1][0] or obstacle.parameters[1] > ws_limits[1][1]

def inBoun(obstacle):
    return obstacle.parameters[0] > ws_limits[0][0] and obstacle.parameters[0] < ws_limits[0][1] and \
                        obstacle.parameters[1] > ws_limits[1][0] and obstacle.parameters[1] < ws_limits[1][1]

def dynamicObstacleStateChanger(Obstacles):

    for obstacle in Obstacles:
        if obstacle.type == 'Dynamic':
            if obsOob(obstacle):
                continue
            obstacle.Model()
    plot.plot_simulation_obs(Obstacles, ax, False, False, Experiment_No)
    for obstacle in Obstacles:
        if obstacle.type == 'Dynamic':
            if inBoun(obstacle):
                dynamicObstacleStateChanger(Obstacles)
                break


if __name__ == '__main__':

    # Define Plot Limits
    fig, ax = plt.subplots()
    # fig.canvas.manager.full_screen_toggle()
    xlim = np.array([-18, 278]) # 278
    ylim = np.array([-5, 155]) # 155
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ws_limits = [[0, 260], [0, 140]]

    # Uncomment this for the Example of Big Simulation
    plot.plot_map(ax)

    # Plot the Static Obstacles
    for obstacle in Obstacles:
        if obstacle.type == 'Static':
            obstacle.plot(ax)

    dynamicObstacleStateChanger(Obstacles)













