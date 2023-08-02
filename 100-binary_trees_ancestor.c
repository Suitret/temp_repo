#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_trees_ancestor - Finds the lowest common ancestor of two nodes.
 *
 * @first: A pointer to the first node.
 * @second: A pointer to the second node.
 *
 * Return: Pointer to the lowest common ancestor node or NULL if not found.
 */
binary_tree_t *binary_trees_ancestor(const binary_tree_t *first,
		const binary_tree_t *second)
{
	const binary_tree_t *node1, *node2;

	if (first == NULL || second == NULL)
		return (NULL);

	if (first == second)
		return ((binary_tree_t *)first);

	node1 = first;
	node2 = second;

	while (node1 != NULL)
	{
		while (node2 != NULL)
		{
			if (node1 == node2)
				return ((binary_tree_t *)node1);
			node2 = node2->parent;
		}
		node1 = node1->parent;
		node2 = second;
	}

	return (NULL);
}
