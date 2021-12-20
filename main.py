# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


class Perceptron:
    def __init__(self):
        self.areas = np.array([1, 4, 3, 3])
        self.perimeters = np.array([4, 8, 8, 8])
        self.etiquettes = np.array([1, 1, -1, -1])
        self.weights = np.array([0, 0, 0])

    def train(self, alpha):
        counter = 0
        iterator = 0
        self.totalIterations = 0
        while counter != 4:
            x = np.array([1, self.areas[iterator], self.perimeters[iterator]])
            outSignal = np.dot(np.transpose(self.weights), x)
            #signum function
            if outSignal > 0:
                outSignal = 1
            elif outSignal == 0:
                outSignal = 0
            else:
                outSignal = -1
            #checking condition for changing weights
            if outSignal == self.etiquettes[iterator]:
                counter = counter + 1
            else:
                counter = 0
                self.weights = self.weights + alpha * self.etiquettes[iterator] * x
            #changing point
            iterator = iterator + 1
            if iterator > 3:
                iterator = 0
            self.totalIterations = self.totalIterations + 1

    def getWeights(self):
        print('iterations: ', self.totalIterations, '\n')
        print('weights: ', self.weights)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    perceptron = Perceptron()
    perceptron.train(0.1)
    perceptron.getWeights()