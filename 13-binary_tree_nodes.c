#include "binary_trees.h"


/**
 * binary_tree_nodes - function that counts the nodes with
 * at least 1 child in a binary tree
 * @tree: pointer to the root node of the tree to count the number of nodes
 *
 * Return: number of leaves
 * If tree is NULL, the function must return 0
 */
size_t binary_tree_nodes(const binary_tree_t *tree)
{
	size_t number = 0, num = 0;

	if (tree == NULL)
		return (0);

	if (tree->left || tree->right)
	{
		number = binary_tree_nodes(tree->left);
		num = binary_tree_nodes(tree->right);
		return (number + num + 1);
	}

	return (0);
}
