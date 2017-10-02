// Created on Sat Sep 30  2017
//
// @author: Aboozar Mapar
// @email: A.Mapar@gmail.com
// 
//
//
// Goal: Demonstrate your ability to design and write C++ applications.
//
// Implement a CircularArray class in C++ that supports an array - like data structure which can be efficiently rotated.
// If possible, the class should be generic and support iteration via the range - based for loop of C++11. 
// Write a driver program in C++ (i.e., a main() function) that demonstrates your class's capabilities in various ways. 
//
// This code reads two integers from the command line. The first integer is the length of the array. The second integer is the amount of the shift. 
// Positive values of the second integer shift the array to the right and negative intergers shift the array to the left.
//

#include "stdafx.h"

#include <iostream>
#include <vector>


// A class to rotate arrays.
// There are two functions
// Prive function GCD that computes the Greatest Common Divisor
// Public function shiftArray(std::vector<int> &arrayRef, int shift) that shifts the arrayRef.
class CircularArray {
private:
	// finding Greatest Common Divisor
	unsigned GCD(unsigned a, unsigned b) {
		if (b == 0) return a;
		else return GCD(b, a%b);
	}

public:
	void shiftArray(std::vector<int> &arrayRef, int shift)
	{
		
		unsigned int arraySize = arrayRef.size();

		// Terminate if no shift is needed
		if (shift == 0) { 
			return;
		}

		// If abs(shift) > arraySize we need to calculate the abs(shift) % arraySize
		// For negative shifts, we calculated arraySize - (-shift % arraySize) the gives us the equivalent positive shift.
		if (shift < 0) {
			shift = arraySize - (-shift % arraySize);
		}
		else {
			shift %= arraySize;
		}

		// Breaking the array into sets based on the GCD arraySize and shift
		for (unsigned sets = GCD(arraySize, shift); sets; --sets) {
			unsigned i = 0;
			unsigned element = arraySize - shift;
			// Using a temp variable to rotate elements within each set
			for (int temp = arrayRef[element + sets - 1]; element; i = element) {
				element = (i + shift) % arraySize;
				std::swap(temp, arrayRef[i + sets - 1]);
			}
		}
	}
};

int main()
{
	CircularArray CA;
	int arraySize = 0;
	int shift = 0;
	std::cout << "Enter the length of the array: "; std::cin >> arraySize;
	
	std::cout << "\nHow many shifts? \nEnter positive integers for shifting to right\n  and negative intergers for shifting to left: "; std::cin >> shift;
	std::cout << "\n";
	
	std::vector<int> myArray(arraySize);

	
	
	// Printing the array before rotation
	std::cout << "Before rotation: ";
	for (int i = 0; i < arraySize; ++i) {
			myArray[i]= i;
			std::cout << myArray[i] << " ";
		}
	std::cout << "\n\n";

	// Using CircularArray class to rotate myArray
	CA.shiftArray(myArray, shift);

	// Printing the array after rotation
	std::cout << "After rotation:  ";
	for (int i = 0; i < arraySize; ++i) {
		std::cout << myArray[i] << " ";
	}
	std::cout << "\n\n";

	system("pause");

    return 0;
}

