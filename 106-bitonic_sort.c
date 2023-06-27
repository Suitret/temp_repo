#include "sort.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * bitonic_sort - Sorts using bitonic sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void bitonic_sort(int *array, size_t size)
{
	if (array && size > 1)
		bitonicSort(array, 0, size, 1, size);
}

/**
 * compAndSwap - Compares and swaps elements
 *
 * @a: The array to be sorted
 * @i: The first index
 * @j: The second index
 * @dir: The direction (1 = ascending & 0 = descending)
 * @size: Number of elements in @array
*/
void compAndSwap(int a[], int i, int j, int dir, int size)
{
	int temp;

	if (dir == (a[i] > a[j]))
	{
		temp = a[i];
		a[i] = a[j];
		a[j] = temp;
		print_array(a, size);
	}
}

/**
 * bitonicMerge - Performs merging
 *
 * @a: The array to be sorted
 * @low: The starting index
 * @cnt: The number of elements to be sorted
 * @dir: The direction (1 = ascending & 0 = descending)
 * @size: Number of elements in @a
*/
void bitonicMerge(int a[], int low, int cnt, int dir, int size)
{
	int i, k;

	if (cnt > 1)
	{
		k = cnt / 2;
		for (i = low; i < low + k; i++)
			compAndSwap(a, i, i + k, dir, size);

		bitonicMerge(a, low, k, dir, size);
		bitonicMerge(a, low + k, k, dir, size);
	}
}

/**
 * bitonicSort - Performs merging
 *
 * @a: The array to be sorted
 * @low: The starting index
 * @cnt: The number of elements to be sorted
 * @dir: The direction (1 = ascending & 0 = descending)
 * @size: Number of elements in @a
*/
void bitonicSort(int a[], int low, int cnt, int dir, int size)
{
	int k;

	if (cnt > 1)
	{
		k = cnt / 2;
		bitonicSort(a, low, k, 1, size);
		bitonicSort(a, low + k, k, 0, size);
		bitonicMerge(a, low, cnt, dir, size);
	}
}
