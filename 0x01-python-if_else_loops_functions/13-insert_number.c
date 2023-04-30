#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: head of list
 * @number: number to insert
 *
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node, *tmp = *head;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	if ((*head)->n > new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (tmp->next)
	{
		if (new_node->n < tmp->next->n)
		{
			node = tmp->next;
			tmp->next = new_node;
			new_node->next = node;
			return (new_node);
		}
		tmp = tmp->next;
	}
	new_node->next = NULL;
	tmp->next = new_node;
	return (new_node);
}
