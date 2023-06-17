#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the list.
 * @number: the number to be inserted.
 * Return: new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr = *head, *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (!head)
		return (NULL);

	new->n = number;
	new->node->next = NULL;

	if (*head == NULL || curr->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (curr != NULL && number > curr->n)
	{
		prev = curr;
		curr = curr->next;
	}

	new->next = curr;
	prev->next = new;

	return (new);
}
