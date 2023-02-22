import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# Assumption: all the angles are in radians and velocity is in m/s
class vehicle:
    def __init__(self, id, start, goal, sampling_time, begin_time, inital_control_input, path=None, COLOR="#f1c40f", ZOOM=0.05):
        # Vehicle dimensions and parameters
        self.L = 3 # Wheel base
        self.size = 4.78
        self.id = id
        self.Reach = False

        x_start = start[0]
        y_start = start[1]
        theta_start = start[2]
        delta_start = start[3]
        self.start = [x_start, y_start, theta_start, delta_start]
        self.goal_list=goal
        self.goal = goal[0]
        self.time = begin_time
        self.sampling_time = sampling_time 
        self.state = [x_start, y_start, theta_start, delta_start]

        initial_v = inital_control_input[0]
        initial_phi = inital_control_input[1]
        self.control_input = [initial_v, initial_phi]

        self.time_history = [begin_time]
        # self.time_history.append(begin_time)
        
        self.control_input_history = [[initial_v, initial_phi]]
        # self.control_input_history.append([initial_v, initial_phi])

        # History of the Vehicle
        self.state_history = [[x_start, y_start, theta_start, delta_start]]
        # self.state_history.append([x_start, y_start, theta_start, delta_start])

        self.COLOR = COLOR
        self.ZOOM = ZOOM

        if path != None:
            self.image = Image.open(path)
        else:
            self.image = None

        if self.goal_list:
            self.goal_bound = self.size * 2
        else:
            self.goal_bound = self.size

    def vehicle_model(self,v,phi):

        pos_x = self.state[0]
        pos_y = self.state[1]
        theta = self.state[2]
        delta = self.state[3]

        state = [pos_x,pos_y,theta,delta]
        # Non-linear dynamics
        x_dot = v*np.cos(theta)
        y_dot = v*np.sin(theta)
        theta_dot = v*np.tan(delta)/self.L # Where L is the wheelbase
        delta_dot = phi

        state[0] = state[0] + x_dot*self.sampling_time
        state[1] = state[1] + y_dot*self.sampling_time
        state[2] = state[2] + theta_dot*self.sampling_time
        state[3] = state[3] + delta_dot*self.sampling_time

        self.state = state
        x = self.state[0]
        y = self.state[1]
        theta = self.state[2]
        delta = self.state[3]

        self.state_history.append([x, y, theta, delta])
        self.control_input_history.append([v,phi])
        self.time += self.sampling_time
        self.time_history.append(self.time)

    def distance(self, x1, x2):
        return np.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2)

    def global_plot(self, ax):

        plt.plot(self.start[0], self.start[1], marker='*', markersize=15, color=self.COLOR, markeredgecolor='black')

        plt.plot([self.start[0], self.goal[0]], [self.start[1], self.goal[1]], '--', color=self.COLOR, alpha=0.5)

        if len(self.goal_list) > 0:
            plt.plot([self.goal_list[0][0], self.goal[0]], [self.goal_list[0][1], self.goal[1]], '--', marker='s',
                     markersize=10, color=self.COLOR, markeredgecolor='black', alpha=0.5)
            plt.plot(np.array(self.goal_list)[:, 0], np.array(self.goal_list)[:, 1], '--', marker='s', markersize=10,
                     color=self.COLOR, markeredgecolor='black', alpha=0.5)
            plt.plot(self.goal_list[-1][0], self.goal_list[-1][1], marker='D', markersize=15, color=self.COLOR,
                     markeredgecolor='black')
        else:
            plt.plot(self.goal[0], self.goal[1], marker='D', markersize=15, color=self.COLOR, markeredgecolor='black')

    def plot(self, ax, virtual_state_flag=True):
        # blue: #003b77
        # red: #f50116
        # yellow: #f1c40f
        # green: #79a824
        # purple: #8e44ad
        if self.image == None:
            vehicle = plt.Circle((self.state[0], self.state[1]), self.size / 2, facecolor=self.COLOR, edgecolor='black')
            ax.add_artist(vehicle)
            vehicle_photo = None
        else:
            vehicle = plt.Circle((self.state[0], self.state[1]), self.size / 2, facecolor="None", edgecolor='black',
                                 linestyle='--')
            ax.add_artist(vehicle)
            img = self.image
            img = img.rotate(self.state[2] * 180 / np.pi, expand=1)
            vehicle_photo = AnnotationBbox(OffsetImage(img, zoom=self.ZOOM), (self.state[0], self.state[1]),
                                           frameon=False)
            ax.add_artist(vehicle_photo)

        # if virtual_state_flag == True and self.Reach == False:
        #     virtual_states = plt.scatter(np.array(self.virtual_state_history)[0:self.prediction_horizon, 0]._value,
        #                                  np.array(self.virtual_state_history)[0:self.prediction_horizon, 1]._value,
        #                                  edgecolor='black', color=self.COLOR)
        #     dynamic_region = plt.Circle((self.state[0], self.state[1]), self.dynamic_offset, facecolor=self.COLOR,
        #                                 edgecolor='black', linestyle=':', alpha=0.2)
        #     static_region = plt.Circle((self.state[0], self.state[1]), self.static_offset, facecolor=self.COLOR,
        #                                edgecolor='black', linestyle=':', alpha=0.2)
        # else:
        #     virtual_states = plt.scatter(self.state[0], self.state[1], color=self.COLOR)
        #     dynamic_region = plt.Circle((self.state[0], self.state[1]), 0, facecolor=self.COLOR, edgecolor='black',
        #                                 linestyle=':', alpha=0.2)
        #     static_region = plt.Circle((self.state[0], self.state[1]), 0, facecolor=self.COLOR, edgecolor='black',
        #                                linestyle=':', alpha=0.2)
        #
        # ax.add_artist(static_region)
        # ax.add_artist(dynamic_region)

        arrow = plt.arrow(self.state[0], self.state[1], 4 * np.cos(self.state[2]), 4 * np.sin(self.state[2]), width=0.6,
                          facecolor=self.COLOR, edgecolor='black')
        plt.plot(np.array(self.state_history)[:, 0], np.array(self.state_history)[:, 1], color=self.COLOR)

        return vehicle, arrow, vehicle_photo
