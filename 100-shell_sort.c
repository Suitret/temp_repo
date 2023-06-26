#include "sort.h"
#include <stdio.h>

/**
 * shell_sort - Sorts using shell sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void shell_sort(int *array, size_t size)
{
	int gap, temp, j;
	size_t i;

	if (size > 1 && array)
	{
		for (gap = size / 2; gap > 0; gap /= 2)
		{
			for (i = gap; i < size; i += 1)
			{
				temp = array[i];
				for (j = i; j >= gap && array[j - gap] > temp; j -= gap)
					array[j] = array[j - gap];
				array[j] = temp;
			}
			print_array(array, size);
		}
	}
}
