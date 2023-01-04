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
	listint_t *ptr, *new, *current;

	if (*head == NULL)
		return (NULL);
	ptr = current = *head;
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
		current = ptr->next;
		while (ptr->next != NULL)
		{
			if (new->n > current->n)
			{
				ptr = current;
				current = current->next;
			}
			else
				break;
		}
		new->next = current;
		ptr->next = new;
	}
	return (new);
}
