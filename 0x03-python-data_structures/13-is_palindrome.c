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
	int *ar, i, j;
	int size = 0;
	listint_t *curr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (curr != NULL)
	{
		size++;
		curr = curr->next;
	}
	ar = malloc(sizeof(int) * size);
	if (ar == NULL)
		return (0);
	curr = *head;
	for (i = 0; i < size; i++)
	{
		ar[i] = curr->n;
		curr = curr->next;
	}
	for (i = 0, j = size - 1; i < j; i++, j--)
	{
		if (ar[i] != ar[j])
		{
			free(ar);
			return (0);
		}
	}
	free(ar);
	return (1);
}
