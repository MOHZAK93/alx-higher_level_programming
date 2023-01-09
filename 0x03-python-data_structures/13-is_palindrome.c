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
    int i = -1, n = 0;
    int *arr1, *arr2;
    const listint_t *current, *new;

    current = *head;
    new = *head;
    while (current != NULL)
    {
        current = current->next;
        n++;
    }
    arr1 = malloc(sizeof(arr1) * n);
    arr2 = malloc(sizeof(arr2) * n);

    while (new != NULL)
    {
        i++;
        n--;
        arr1[i] = new->n;
        arr2[n] = new->n;
        new = new->next;
    }
    while (i >= 0)
    {
        if (arr1[i] != arr2[i])
            return (0);
        i--;
    }
    return (1);
}
