#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first node of the linked list
 *
 * Return: 0, if not palindrome. 1, if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev, *curr;
	int nodes = 1, counter;

	prev = curr = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (curr->next != NULL)
	{
		curr = curr->next;
		nodes++;
	}
	while (1)
	{
		if (prev->n == curr->n)
		{
			prev = prev->next;
			curr = prev;
			nodes -= 2;
			counter = nodes;
			while (counter > 1)
			{
				curr = curr->next;
				counter--;
			}
			if (nodes <= 1)
				return (1);
		}
		else
			break;
	}
	return (0);
}
