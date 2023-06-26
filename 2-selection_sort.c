#include "sort.h"
#include <stdio.h>

/**
 * selection_sort - Sorts using selection sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void selection_sort(int *array, size_t size)
{
	int temp, min_i, min_v;
	size_t i, j;

	if (size > 1 && array)
	{
		for (i = 0; i < size; i++)
		{
			min_v = array[i];
			for (j = i + 1; j < size; j++)
			{
				if (array[j] < min_v)
				{
					min_v = array[j];
					min_i = j;
				}
			}
			if (array[i] != min_v)
			{
				temp = array[i];
				array[i] = min_v;
				array[min_i] = temp;
				print_array(array, size);
			}
		}
	}
}
