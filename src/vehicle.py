import numpy as np

# Assumption: all the angles are in radians and velocity is in m/s
class vehicle:
    def __init__(self,id,start,sampling_time,begin_time,inital_control_input):
        # Vehicle dimensions and parameters
        self.L = 3 # Wheel base
        self.id = id


        x_start = start[0]
        y_start = start[1]
        theta_start = start[2]
        delta_start = start[3]

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

        



