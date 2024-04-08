import numpy as np
import matplotlib.pyplot as plt

class VectorFieldVis:

    def __init__(self, field, x_range = (-10,10), y_range = (-10,10), step = 1):
        self.field = field
        self.x_range = x_range
        self.y_range = y_range
        self.step = step

    def generate_grid(self):
        """Will generate a grid of points over the specified range."""

        x , y = np.meshgrid(np.arange(self.x_range[0],self.x_range[1],self.step),
                            np.arange(self.y_range[0], self.y_range[1], self.step))

        return x, y

    def compute_field_vectors(self, x, y):
        """Computes the vector field values for each point within the grid."""

        u , v = np.zeros(x.shape), np.zeros(y.shape)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                vector = self.field.get_vector_at( x[ i, j], y[ i, j])
                u[ i, j], v[ i, j] = vector.x, vector.y
        return u,v

    def plot_field(self, x, y, u, v):
        """Plots the vector field using the computed vectors"""

        plt.figure(figsize = (8,8))
        plt.quiver( x, y, u, v)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Vector Field Visualization')
        plt.grid(True)
        plt.show()

    def visualize(self):
        """Main method to visualize the vector field"""

        x, y = self.generate_grid()
        u, v = self.compute_field_vectors(x,y)

        self.plot_field( x, y, u, v)