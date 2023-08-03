#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_size - function that measures the
 * height of a binary tree
 * @tree: a pointer to the root node of
 * the tree to measure the height.
 *
 * Return: an int
 */

size_t binary_tree_size(const binary_tree_t *tree)
{
	size_t left_height, right_height;

	if (tree == NULL)
		return (0);

	left_height = binary_tree_height(tree->left);
	right_height = binary_tree_height(tree->right);

	return (left_height + right_height + 1);
}
