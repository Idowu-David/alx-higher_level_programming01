#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: number to be added
 * Return: the address of the new node, or NULL of it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new;

	ptr = *head;
	if (ptr == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	/* add at beginning */
	if (new->n < ptr->n)
	{
		new->next = ptr;
		*head = new;
	}
	else
	{
		while (ptr->next != NULL)
		{
			if (new->n > ptr->n)
				ptr = ptr->next;
			else
				break;
		}
		/* add at end */
		if (ptr->next == NULL)
		{
			new->next = NULL;
			ptr->next = new;
		}
		/* add at middle */
		else
		{
			new->next = ptr->next;
			ptr->next = new;
		}
	}
	return (new);
}
