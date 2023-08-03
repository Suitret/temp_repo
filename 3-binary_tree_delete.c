#include "binary_trees.h"
#include <stdlib.h>
#include <sys/types.h>


/**
 * binary_tree_delete - delete an entire binary tree
 * @tree: the binary tree to be deleted
 *
 * Return: a type void
*/

void binary_tree_delete(binary_tree_t *tree)
{
	if (tree == NULL)
		return;

	binary_tree_delete(tree->left);
	binary_tree_delete(tree->right);

	free(tree);
}
