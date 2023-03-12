import scipy.special
import numpy as np
# scipy.speciaial for the sigmoid function exp it()


class neuronalNetwork:
    def __init__(self,
                 inputnodes,
                 outputnodes,
                 hiddenode,
                 learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddenode
        self.onodes = outputnodes
        # Gewichte der Knoten
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5),
                                    (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5),
                                    (self.onodes, self.hnodes))
        # activation function is the sigmoid function
        self.activation_function \
            = lambda x: scipy.special.expit(x)

    def train(self):
        print("in train")

    def qury(self):
        hidden_inputs = np.dot(self.wih, self.inodes)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)


def main():
    # a = np.zeros((3, 2))
    # plt.imshow(a, interpolation="nearest")  # 2D array
    # plt.show()
    input_nodes = 3
    output_nodes = 3
    hidden_nodes = 3
    learning_rate = 0.3

    n = neuronalNetwork(
        input_nodes, output_nodes, hidden_nodes, learning_rate)


if __name__ == "__main__":
    main()
