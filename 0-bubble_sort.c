#include "sort.h"
#include <stdio.h>

/**
 * bubble_sort - Sorts using bubble sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void bubble_sort(int *array, size_t size)
{
	int flag, temp;
	size_t i;

	if (size > 1 && array)
	{
		do {
			flag = 0;

			for (i = 1; i < size; i++)
			{
				if (array[i - 1] > array[i])
				{
					temp = array[i];
					array[i] = array[i - 1];
					array[i - 1] = temp;
					flag = 1;
					print_array(array, size);
				}
			}
		} while (flag);
	}
}
