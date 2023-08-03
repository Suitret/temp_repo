#include "binary_trees.h"


/**
 * binary_tree_sibling - function that finds
 * the sibling of a node
 * @node: pointer to the root node of the tree to check
 *
 * Return: an integer
 * If tree is NULL, the function must return 0
 */
binary_tree_t *binary_tree_sibling(binary_tree_t *node)
{
	if (node == NULL || node->parent == NULL)
		return (NULL);

	if (!node->parent->left || !node->parent->right)
		return (NULL);

	if (node->parent->left == node)
		return (node->parent->right);

	if (node->parent->right == node)
		return (node->parent->left);

	return (0);
}

