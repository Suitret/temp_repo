#include "binary_trees.h"
#include <stdlib.h>
#include <sys/types.h>


/**
 * binary_tree_is_root - check if a given node is a root
 * @node: the node to check
 *
 * Return: an integer
 */

int binary_tree_is_root(const binary_tree_t *node)
{
	if (!node)
		return (0);
	if (node->parent)
		return (0);
	return (1);
}
