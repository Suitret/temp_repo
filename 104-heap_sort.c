#include "sort.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * swap - Swaps two elements
 *
 * @a: first element
 * @b: second element
 */
void swap(int *a, int *b)
{
	int temp = *a;

	*a = *b;
	*b = temp;
}

/**
 * heap_sort - Sorts using heap sort algorithm
 *
 * @arr: The array to be sorted
 * @size: Number of elements in @array
 */
void heap_sort(int arr[], size_t size)
{
	int i;

	for (i = size / 2 - 1; i >= 0; i--)
		heapify(arr, size, (int)size, i);

	for (i = size - 1; i >= 0; i--)
	{
		swap(&arr[0], &arr[i]);
		if (i)
			print_array(arr, size);
		heapify(arr, size, i, 0);
	}
}

/**
 * heapify - Sorts using heap sort algorithm
 *
 * @arr: The array to be sorted
 * @size: Number of elements in @array
 * @end: limit
 * @i: Index to work with
 */
void heapify(int arr[], size_t size, int end, int i)
{
	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;

	if (left < (int)end && arr[left] > arr[largest])
		largest = left;

	if (right < (int)end && arr[right] > arr[largest])
		largest = right;

	if (largest != i)
	{
		swap(&arr[i], &arr[largest]);
		print_array(arr, size);
		heapify(arr, size, end, largest);
	}
}
