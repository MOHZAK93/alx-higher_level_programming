#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: linked list
 *
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (!slow || !fast)
			return (0);
		if (slow == fast)
			return (1);
	}
	return (0);
}
