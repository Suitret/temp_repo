#include <stdio.h>
#include <stdlib.h>
#include "binary_trees.h"

/**
 * binary_tree_is_perfect - checks if a binary tree is perfect
 *
 * To check if a binary tree is perfect, you need to verify two conditions:
 * The tree is balanced(i.e., the left and right subtrees have the same height)
 * All internal nodes have two children.
 *
 * @tree: pointer to the root node of the tree to check
 *
 * Return: 1 if the tree is perfect, 0 otherwise.
 */
int binary_tree_is_perfect(const binary_tree_t *tree)
{
	size_t left_height, right_height;

	if (!tree)
		return (0);

	left_height = binary_tree_height(tree->left);
	right_height = binary_tree_height(tree->right);

	if (left_height != right_height)
		return (0);

	if (tree->left == NULL && tree->right == NULL)
		return (1);

	return (binary_tree_is_perfect(tree->left) &&
			binary_tree_is_perfect(tree->right));
}

/**
 * binary_tree_height - Measures the height of a binary tree.
 *
 * @tree: A pointer to the root node of the tree.
 *
 * Return: Height of the tree, 0 if tree is NULL.
 */
size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t left_height, right_height;

	if (!tree)
		return (0);

	left_height = binary_tree_height(tree->left);
	right_height = binary_tree_height(tree->right);

	return ((left_height > right_height ? left_height : right_height) + 1);
}
