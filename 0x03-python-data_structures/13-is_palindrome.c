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
	int n, i = 0, j = 0;
	int *arr1;
	const listint_t *new;

	new = *head;
	n = list_len(head);
	arr1 = malloc(sizeof(arr1) * n);
	if (arr1 == NULL)
		return (1);

	while (new != NULL)
	{
		arr1[i] = new->n;
		new = new->next;
		i++;
	}
	i--;
	while (i >= 0)
	{
		printf("%d  %d\n", arr1[i], arr1[j]);
		if (arr1[i] != arr1[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}

/**
 * list_len - gets length of the list
 *
 * @head: list
 *
 * Return: length of list
 */
int list_len(listint_t **head)
{
	int n;
	listint_t *current = *head;

	while (current != NULL)
	{
		n++;
		current = current->next;
	}
	return (n);
}
