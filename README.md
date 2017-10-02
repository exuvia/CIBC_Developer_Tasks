# Solutions to  CIBC_Developer_Tasks
This repository contains my solutions to Tasks 1-3 and Bonus tasks 1 -2. 

## Required Task 1
_Goal: Demonstrate your ability to work with common collaboration tools for software development._

Create a public GitHub repository to share any code and documents that you will be writing for the tasks below.

### Solution for Task 1
The first task was to create this repository.  

## Required Task 2
_Goal: Demonstrate your ability to design and write C++ applications._

Implement a `CircularArray` class in C++ that supports an array-like data structure which can be efficiently rotated. If possible, the class should be generic and support iteration via the range-based for loop of C++11. Write a driver program in C++ (i.e., a `main()` function) that demonstrates your class's capabilities in various ways. Summarize briefly how this system could be tested.

### Solution for Task 2
The soultion to this task is in file `Task2.cpp`. It contains a `CircularArray` class in C++ rotates an array. This is an interactive code and asks the user to input two integers. The first parameter is a positive integer which defines the length of the array to be rotated. The second integer is the amount of the shift.  Positive values of the second integer shift the array to the right and negative intergers shift the array to the left. 


## Required Task 3
_Goal: Demonstrate your ability to build Python scripts._

In python generate a script that will load in two 2D color images and evaluate the differences between them.  The script must somehow quantify the differences between images. 

You can use common python packages in you implementations (numpy, scipy, etc). Write some pytest code to test your implementations with the included test data.  

For sample input data, download [this zip](https://www.dropbox.com/s/k13v6pa2kr1z5we/test_data.zip?dl=0). 

### Solution for Task 3
The code in Task3.py loads two 2D images and computes Mean-Square Error (MSE) and Structural Similarity Index (SSIM) between the two.

## Bonus Task 1
_Goal: Assess algorithmic knowledge._

**Build order**: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE

Input:

`projects: a, b, c, d, e, f`

`dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)`

Output:

`f, e, a, b, d, c`

Use any language you like for this one.

### Solution for Bonus Task 1
This task was done in Python. It uses Networkx to define a directional graph to find the dependencies. The code is in Bonus1.py.


## Bonus Task 2 
_Goal: Scientific and numerical computing._

Continuing from Required Task 3 above, create a Python function that will find the affine transformation between two sets of 2D or 3D correspondence points.  The affine transformation is a linear transformation and translation that can be expressed in a single matrix, 3x3 in the 2D case and 4x4 in the 3D case.  See the [Wikipedia page](https://en.wikipedia.org/wiki/Affine_transformation) for more information.  With a set of corresponding points, the affine transformation can be found by solving for the coefficients of the affine transformation in the least squared sense.  

Create a Python function that will use the affine transformation calculated for 2D points to combine two images into one.  Create some test code using pytest.  

### Solution for Bonus Task 2
This code, Bonus2.py, was written in Python and uses openCV capabilities. The code finds the affine transfer based on two sets of 2D points and uses the results to combine two images .
