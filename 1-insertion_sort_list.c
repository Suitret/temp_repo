#include "sort.h"

/**
* insertion_sort_list - implementation of insertion algorithm
* for doubly linked list
* @list: Head of list
*
* Return: void
*/

void insertion_sort_list(listint_t **list)
{
	int n;
	listint_t *cur, *ptr, *tmp;

	cur = *list;
	if (cur->next == NULL)
		return;
	cur = cur->next;
	while (cur != NULL)
	{
		n = 0;
		ptr = cur;
		tmp = cur->prev;
		cur = cur->next;
		while (tmp != NULL && tmp->n > ptr->n)
		{
			n++;
			tmp = tmp->prev;
		}

		if (n)
		{
			ptr->prev->next = ptr->next;
			if (ptr->next != NULL)
				ptr->next->prev = ptr->prev;
			swap_and_print(tmp, list, ptr);

		}
	}
}

/**
* swap_and_print - Swaps the values of two
* nodes in a linked list and prints the linked list.
* @tmp: The temporary node.
* @list: The pointer to the head of the linked list.
* @ptr: The node that is being swapped.
*
* Return: a type void
*/

void swap_and_print(listint_t *tmp, listint_t **list, listint_t *ptr)
{
	if (tmp == NULL)
	{
		tmp = *list;
		ptr->prev = NULL;
		ptr->next = tmp;
		ptr->next->prev = ptr;
		*list = ptr;
		print_list(*list);
	}
	else
	{
		tmp = tmp->next;
		tmp->prev->next = ptr;
		ptr->prev = tmp->prev;
		tmp->prev = ptr;
		ptr->next = tmp;
		print_list(*list);
	}
}
