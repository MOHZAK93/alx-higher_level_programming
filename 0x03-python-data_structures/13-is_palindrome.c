#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  *is_palindrome - checks if a singly linked list is a palindrome
  *
  *@head: start of linked list
  *
  *Return: 0 or 1
  */

int is_palindrome(listint_t **head)
{
	int i = -1, n = 0, j = 0;
	int *arr1;
	const listint_t *current, *new;

	current = *head;
	new = *head;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	arr1 = malloc(sizeof(arr1) * n);
	if (arr1 == NULL)
		return (1);

	while (new != NULL)
	{
		i++;
		arr1[i] = new->n;
		new = new->next;
	}
	while (i >= 0)
	{
		if (arr1[i] != arr1[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}
