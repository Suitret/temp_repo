#include "sort.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * getMax - Returns the greater value
 *
 * @arr: The array to be sorted
 * @n: Number of elements in @array
 * Return: mx
 */
int getMax(int arr[], int n)
{
	int mx = arr[0], i;

	for (i = 1; i < n; i++)
		if (arr[i] > mx)
			mx = arr[i];
	return (mx);
}

/**
 * countSort - Sorts using counting sort algorithm
 *
 * @arr: The array to be sorted
 * @n: Number of elements in @array
 * @exp: Current digit
 */
void countSort(int arr[], size_t n, int exp)
{
	int *output;
	int i, count[10] = { 0 };

	output = malloc(n * sizeof(int));
	if (!output)
		return;

	for (i = 0; i < (int)n; i++)
		count[(arr[i] / exp) % 10]++;

	for (i = 1; i < 10; i++)
		count[i] += count[i - 1];

	for (i = n - 1; i >= 0; i--)
	{
		output[count[(arr[i] / exp) % 10] - 1] = arr[i];
		count[(arr[i] / exp) % 10]--;
	}

	for (i = 0; i < (int)n; i++)
		arr[i] = output[i];

	free(output);
}

/**
 * radix_sort - Sorts using radix sort algorithm
 *
 * @arr: The array to be sorted
 * @n: Number of elements in @array
 */
void radix_sort(int arr[], size_t n)
{
	int m, exp;

	if (!arr || n < 2)
		return;

	m = getMax(arr, n);
	for (exp = 1; m / exp > 0; exp *= 10)
	{
		countSort(arr, n, exp);
		print_array(arr, n);
	}
}
