#include "sort.h"
#include <stddef.h>

/**
 * quick_sort - Sorts an array using the quick sort algorithm.
 * @array: The array to sort.
 * @size: The size of the array.
 *
 * description:  This function sorts the array in ascending order.
 * Return: a void type
 */

void quick_sort(int *array, size_t size)
{
	quick_sort_(array, 0, (int)size - 1);
}

/**
 * quick_sort_ - Sorts an array using the quick sort algorithm.
 * @a: The array to sort.
 * @beg: The begining of the array.
 * @end: The end of the array.
 *
 * description -  This function sorts the array in ascending order.
 * Return: a void type
 */
void quick_sort_(int *a, int beg, int end)
{
	int loc;

	if (beg < end)
	{
		loc = partition(a, beg, end);
		quick_sort_(a, beg, loc - 1);
		quick_sort_(a, loc + 1, end);
	}
}

/**
 * partition - a function for the quick sort
 * @a: The array to sort.
 * @beg: The begining of the array.
 * @end: The end of the array.
 *
 * description: partition function
 * Return:  a void type
 */
int partition(int a[], int beg, int end)
{
	int left, right, temp, loc, flag;

	loc = left = beg;
	right = end;
	flag = 0;
	while (flag != 1)
	{
		while ((a[loc] <= a[right]) && (loc != right))
			right--;
		if (loc == right)
			flag = 1;
		else if (a[loc] > a[right])
		{
			temp = a[loc];
			a[loc] = a[right];
			a[right] = temp;
			loc = right;
			print_array(a, (size_t)end);
		}
		if (flag != 1)
		{
			while ((a[loc] >= a[left]) && (loc != left))
				left++;
			if (loc == left)
				flag = 1;
			else if (a[loc] < a[left])
			{
				temp = a[loc];
				a[loc] = a[left];
				a[left] = temp;
				loc = left;
				print_array(a, (size_t)end);
			}
		}
	}
	return (loc);
}
