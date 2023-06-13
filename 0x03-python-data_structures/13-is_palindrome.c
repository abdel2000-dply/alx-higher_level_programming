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
	int ar[20480], i, j;
	listint_t *curr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	curr = *head;
	for (i = 0; curr != NULL; i++)
	{
		ar[i] = curr->n;
		curr = curr->next;
	}
	for (j = 0; j < i; j++, i--)
	{
		if (ar[j] != ar[i])
			return (0);
	}
	return (1);
}
