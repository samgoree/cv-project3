import torch
import torchvision
# download the MNIST dataset of handwritten digits
mnist_train = torchvision.datasets.mnist.MNIST(root='./mnist', train=True, download=True, transform=None)

X = mnist_train.data.float() / 256
Y = mnist_train.targets

mnist_test = torchvision.datasets.mnist.MNIST(root='./mnist', train=False, download=True, transform=None)

X_test = mnist_test.data.float() / 256
Y_test = mnist_test.targets