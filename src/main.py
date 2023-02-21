
from matplotlib import pyplot as plt
from Obstacle import *
from config import *
import plot
from vehicle import *


def obsOob(obstacle):
    x, y = obstacle.obs.pos[0], obstacle.obs.pos[1]
    return x < ws_limits[0][0] or x > ws_limits[0][1] or \
                    y < ws_limits[1][0] or y > ws_limits[1][1]

def inBoun(obstacle):
    x, y = obstacle.obs.pos[0], obstacle.obs.pos[1]
    return x > ws_limits[0][0] and x < ws_limits[0][1] and \
                        y > ws_limits[1][0] and y < ws_limits[1][1]

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


    control_inputs = [[10,10],[10,10],[10,10],[10,10],[10,10],[10,10]]
    vehicle1 = vehicle(1,[0,0,2,0],0.1,0,[2,0.5])
    for i in control_inputs:
        vehicle1.vehicle_model(i[0],i[1])

    # vehicle1.vehicle_model(2,0.8)
    print("\n",vehicle1.state)
    print("\n",vehicle1.state_history)
    # print(vehicle1.state_history[:][0])
    x_pos = [x[0] for x in vehicle1.state_history]
    y_pos = [y[1] for y in vehicle1.state_history]
    plt.plot(x_pos, y_pos)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.axis('equal')
    plt.show()

