import matplotlib.pyplot as plt
from vehicle import *


if __name__=="__main__":
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
