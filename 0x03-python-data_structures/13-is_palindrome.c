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
	int ar[10000000], i, j;
	int size = 0;
	listint_t *curr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (curr != NULL)
	{
		size++;
		curr = curr->next;
	}
	curr = *head;
	for (i = 0; i < size; i++)
	{
		ar[i] = curr->n;
		curr = curr->next;
	}
	for (i = 0, j = size - 1; i < j; i++, j--)
	{
		if (ar[i] != ar[j])
			return (0);
	}
	return (1);
}
