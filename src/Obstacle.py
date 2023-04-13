from PIL import Image
import autograd.numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from scipy.misc import face


class Obstacle:
    def __init__(self, id, obstacle_type, sampling_time, obs, COLOR="#c0392b", ZOOM=0.035,
                 collided=False):

        # Obstacle Details
        self.id = id
        self.type = obstacle_type  # Static or Dynamic?
        self.collided = collided
        self.obs = obs

        # Description of the Obstacle
        velocity, angle, acceleration = self.obs.get_params()

        if self.obs.__class__.__name__ == "Dynamic":
            velocity = velocity * 5 / 18  # m/s conv
            angle = angle * np.pi / 180  # radian conv

        self.obs.set_params([velocity, angle, acceleration])

        #self.parameters = [x_pos, y_pos, radius, velocity, angle, acceleration]

        # Store History
        # self.history = []
        # self.history.append([x_pos, y_pos, radius, velocity, angle, acceleration])

        self.sampling_time = sampling_time

        # Load Image from Path
        if self.obs.imagePath != None:
            self.image = Image.open(self.obs.imagePath)
        else:
            self.image = None

        if self.type == "Static":
            self.COLOR = COLOR  # Default Color for Static = Red
        else:
            self.COLOR = "#8e44ad"  # Default Color For Dynamic = Purple
        self.ZOOM = ZOOM

        x_pos = self.obs.pos[0]
        y_pos = self.obs.pos[1]
        radius = self.obs.radius

        # Store History
        self.history = []
        self.history.append([x_pos, y_pos, radius, velocity, angle, acceleration])

    def Model(self):
        velocity, angle, acceleration = self.obs.get_params()

        velocity += acceleration * self.sampling_time

        self.obs.pos[0] += velocity * np.cos(angle) * self.sampling_time
        self.obs.pos[1] += velocity * np.sin(angle) * self.sampling_time

        self.obs.set_params([velocity, angle, acceleration])

        x_pos = self.obs.pos[0]
        y_pos = self.obs.pos[1]
        radius = self.obs.radius

        self.history.append([x_pos, y_pos, radius, velocity, angle, acceleration])

    def plot(self, ax):
        if self.image is None:
            if self.obs.__class__.__name__ == "Circle":
                obstacle = plt.Circle((self.obs.pos[0], self.obs.pos[1]), self.obs.radius, facecolor=self.COLOR,
                                      edgecolor='black')
                ax.add_artist(obstacle)
                obstacle_photo = None
            elif self.obs.__class__.__name__ == "Rectangle":
                obstacle = plt.Rectangle((self.obs.pos[0], self.obs.pos[1]), self.obs.dim[0], self.obs.dim[1], facecolor=self.COLOR,
                                      edgecolor='black')
                ax.add_artist(obstacle)
                obstacle_photo = None

        else:
            obstacle = plt.Circle((self.obs.pos[0], self.obs.pos[1]), self.obs.radius, facecolor='None',
                                  edgecolor='black')
            angle = self.obs.get_params()[1]
            ax.add_artist(obstacle)
            img = self.image.rotate(angle * 180 / np.pi, expand=1)
            obstacle_photo = AnnotationBbox(OffsetImage(img, zoom=self.ZOOM), (self.obs.pos[0], self.obs.pos[1]),
                                            frameon=False)
            ax.add_artist(obstacle_photo)

        return obstacle, obstacle_photo