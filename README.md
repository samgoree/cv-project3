# Project 3: Handwritten Digits
In this project, you’re going to be developing a computer program that can look at math on a whiteboard and check it. To keep things focused on the visual side, it will only check addition between positive whole numbers.

Like the previous projects, the warm-up sections are optional, just for you to practice what we’ve been doing in class. The submit section is for a grade.

### Warm-up: Keypoints

* Load in the two photos of Notre Dame cathedral in Paris. 
* Use SIFT to find keypoints in each image. Draw the top 50 matches between them.
* Using the SIFT matches, find the projective transformation matrix to map between them.
* *(Challenge)* Given that these two cameras were both taken by a camera with a focal
length of 2.4 cm and notre dame is 70 meters tall, can you find the distance in meters
between these two photographers? No code necessary, just use ✨geometry✨

### Warm-up: Machine Learning

* Using the code in mnist_starter.py, load the MNIST dataset of handwritten digits. 
If it is not downloaded, the torch code will download it for you.
* Using scikit-learn, train a LogisticRegressionClassifier on the training set, then 
measure the classification accuracy on the test set.
* Using scikit-learn, use K means clustering on the images with K=10. Figure out which
cluster corresponds to which digit.
* Principal component analysis is a dimensionality reduction algorithm, which is another
type of unsupervised learning. Using scikit-learn, run PCA on the images with
n_components=2. Plot the output using a scatterplot.
* *(Challenge)* Create a very large image and add MNIST digits to the image in locations which correspond to the PCA components to create something like this:

### Submit: Automatic Math Checker

The six images in the github repo all show two rows of digits, representing two numbers, followed by a horizontal line and a third row of numbers, which is supposedly the sum of the previous two. You can assume that all of the numbers are positive, whole numbers and the numbers are roughly right-aligned.

Write a program (either in Python or C++) to:
* Locate all of the digits in the image
* Show correct detections by draw bounding boxes around them
* Classify them correctly using a machine learning approach
* Print out the implied equation
* Decide whether the addition has been completed correctly

For the machine learning step, I recommend a small convolutional neural network. 
Please use the MNIST dataset discussed in class as training data and verify that 
it is trained correctly by measuring accuracy on the test set. You should get 
above 95% accuracy. Some starter code to download and open the MNIST image files 
using PyTorch is included in mnist_starter.py. If you have not done so already, 
you may have to install PyTorch. Follow the instructions at this link: 
https://pytorch.org/get-started/locally/ and choose CPU. You can run pip in the 
anaconda prompt that comes with the anaconda distribution of python. If PyTorch 
doesn’t work on your computer, you can use one of the models from scikit-learn instead.

It is up to you to figure out how to do each step. You shouldn’t need anything 
we haven’t learned in class. I will test your code on additional images that 
you do not have access to, so you cannot hard-code the positions of the digits, 
or the number of digits in each row (though you can assume all numbers will fit 
in a 32-bit integer).

You are free to mess around in Jupyter notebooks, but please submit either a 
.py or .cpp file that runs your project.
