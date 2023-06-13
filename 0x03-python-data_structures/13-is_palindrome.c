#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int ar[2048], i, j, size = 0;
	listint_t *curr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	curr = *head;
	for (i = 0; curr != NULL; i++)
	{
		ar[i] = curr->n;
		curr = curr->next;
		size++;
	}
	for (j = 0; j < size / 2; j++)
	{
		if (ar[j] != ar[size - 1 - j])
			return (0);
	}
	return (1);
}
