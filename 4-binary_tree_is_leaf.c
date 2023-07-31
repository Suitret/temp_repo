#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_is_leaf - checks if a node is a leaf
 *
 * @node: pointer to the node to check
 *
 * Return: 1 if node is a leaf, otherwise 0
 * If node is NULL, return 0
 */
int binary_tree_is_leaf(const binary_tree_t *node)
{
	if (!node)
		return (0);
	else if (!node->right && !node->left)
		return (1);
	else
		return (0);
}
