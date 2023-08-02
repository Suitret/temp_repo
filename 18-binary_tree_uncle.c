#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_uncle - finds the uncle of a node
 *
 * @node: pointer to the node to find the uncle
 *
 * Return: pointer to the uncle node
 */
binary_tree_t *binary_tree_uncle(binary_tree_t *node)
{
	binary_tree_t *temp;

	if (!node)
		return (node);

	if (!node->parent)
		return (node->parent);

	if (!node->parent->parent)
		return (node->parent->parent);

	temp = node->parent->parent;

	return (temp->right == node->parent ? temp->left : temp->right);
}
