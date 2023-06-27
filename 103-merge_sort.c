#include "sort.h"
#include <stddef.h>

/**
 * merge - this is an implementation
 * of the merge sorting algorithm
 * @arr: the array to be sorted
 * @tempArray: a tempory array
 * @lowerIndex: an int element
 * @middleIndex: an int element
 * @upperIndex: an int element
 *
 * Return: a type void element
 */

void merge(int *arr, int *tempArray, int lowerIndex,
	   int middleIndex, int upperIndex)
{
	int lowerStart = lowerIndex;
	int lowerStop = middleIndex;
	int upperStart = middleIndex + 1;
	int upperStop = upperIndex;
	int count = lowerIndex;
	int i;

	while (lowerStart <= lowerStop && upperStart <= upperStop)
	{
		if (arr[lowerStart] < arr[upperStart])
			tempArray[count++] = arr[lowerStart++];
		else
			tempArray[count++] = arr[upperStart++];
	}

	while (lowerStart <= lowerStop)
	{
		tempArray[count++] = arr[lowerStart++];
	}
	while (upperStart <= upperStop)
	{
		tempArray[count++] = arr[upperStart++];
	}
	for (i = lowerIndex; i <= upperIndex; i++)
		arr[i] = tempArray[i];
}

/**
 * mergeSrt - this is an implementation
 * of the merge sorting algorithm
 * @arr: the array to be sorted
 * @tempArray: a tempory array
 * @lowerIndex: an int element
 * @upperIndex: an int element
 *
 * Return: a type void element
 */

void mergeSrt(int *arr, int *tempArray, int lowerIndex, int upperIndex)
{
	int middleIndex;

	if (lowerIndex >= upperIndex)
		return;

	middleIndex = (lowerIndex + upperIndex) / 2;
	mergeSrt(arr, tempArray, lowerIndex, middleIndex);
	mergeSrt(arr, tempArray, middleIndex + 1, upperIndex);
	merge(arr, tempArray, lowerIndex, middleIndex, upperIndex);
}

/**
 * merge_sort - this is an implementation
 * of the merge sorting algorithm
 * @arr: the array to be sorted
 * @size: size of the array
 *
 * Return: a type void element
 */

void merge_sort(int *arr, size_t size)
{
	int *tempArray = (int *)malloc(size * sizeof(int));

	mergeSrt(arr, tempArray, 0, (int)size - 1);
}
