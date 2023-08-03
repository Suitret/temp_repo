#include "binary_trees.h"
#include <stdio.h>

/**
 * binary_tree_inorder - a function that goes through a
 * binary tree using in-order traversal
 * @tree: is a pointer to the root node of
 * the tree to traverse
 * @tree: a pointer to the root node of the tree to traverse
 * @func: a pointer to a function to call for each node
 *
 * Return: a type void
 */

void binary_tree_inorder(const binary_tree_t *tree, void (*func)(int))
{
	if (tree == NULL || func == NULL)
		return;

	binary_tree_inorder(tree->left, func);
	func(tree->n);
	binary_tree_inorder(tree->right, func);
}
