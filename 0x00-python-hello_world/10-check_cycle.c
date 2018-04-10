#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - This function checks if a singly linked list has a cycle in it
 * @list: This is our singly linked list.
 *
 * Returns: 0 if no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slowerloop = list;
	listint_t *fasterloop = list;

	while (slowerloop && fasterloop && fasterloop->next)
	{
		slowerloop = slowerloop->next;
		fasterloop = fasterloop->next->next;
		if (slowerloop == fasterloop)
		{
			return (1);
		}
	}
	return (0);
}
