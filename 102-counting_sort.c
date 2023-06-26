#include "sort.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * counting_sort - Sorts using counting sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void counting_sort(int *array, size_t size)
{
	int *cmp_tab, max = 0, i, k = 0;
	size_t j;

	if (size > 1 && array)
	{
		for (i = 0; i < (int)size; i++)
		{
			if (array[i] > max)
				max = array[i];
		}

		cmp_tab = malloc((max + 1) * sizeof(int));
		if (!cmp_tab)
			return;

		for (i = 0; i < max + 1; i++)
			cmp_tab[i] = 0;

		for (j = 0; j < size; j++)
			cmp_tab[array[j]]++;

		j = 0;
		for (i = 0; i < max + 1; i++)
		{
			for (j = cmp_tab[i]; j != 0; j--)
			{
				array[k] = i;
				k++;
			}
		}

		k = 0;
		for (i = 0; i < max + 1; i++)
		{
			k += cmp_tab[i];
			cmp_tab[i] = k;
		}
		print_array(cmp_tab, max + 1);
		free(cmp_tab);
	}
}
