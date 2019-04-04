import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Draw:

    @staticmethod
    def Draw_OR_LineChart(array_weight, array_x):
        size_array_input = len(array_x)
        values_X = [-1, 2]
        values_Y = -(array_weight[1] * values_X + array_weight[0]) / array_weight[2]

        #Draw line
        plt.plot(values_X, values_Y)

        #Draw point
        plt.plot(array_x[0][1], array_x[0][2], 'ro')
        
        for i in range(size_array_input-1):
            plt.plot(array_x[i+1][1], array_x[i+1][2], 'bo')

        plt.axis([-1, 2, -1, 2])
        plt.show()

    @staticmethod
    def Draw_AND_LineChart(array_weight, array_x):
        size_array_input = len(array_x)
        values_X = [-1, 2]
        values_Y = -(array_weight[1] * values_X + array_weight[0]) / array_weight[2]

        #Draw line
        plt.plot(values_X, values_Y)

        #Draw point
        plt.plot(array_x[3][1], array_x[3][2], 'bo')
        
        for i in range(size_array_input-1):
            plt.plot(array_x[i][1], array_x[i][2], 'ro')

        plt.axis([-1, 2, -1, 2])
        plt.show()

    @staticmethod
    def Draw_XOR_LineChart(array_weight):
        # Initialita share 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #Draw point
        ax.scatter3D(0, 0, 0, c='r');
        ax.scatter3D(0, 1, 0, c='g');
        ax.scatter3D(1, 0, 0, c='g');
        ax.scatter3D(1, 1, 1, c='r');

        #Set Labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        #Create grid
        xx, yy = np.meshgrid([0, 1], [0, 1])
        zz = -(array_weight[1] * xx + array_weight[0] * yy + array_weight[2]) / array_weight[3]
        ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, cmap='cubehelix', edgecolor='none')
        plt.show()

    @staticmethod
    def Draw_Error_LineChart(list_error):
        array_error = np.asarray(list_error)
        plt.plot(array_error)
        plt.show()