#include "lists.h"

/**
 * insert_node - insert number at node
 * @head: head of node list
 * @number: number to insert
 *
 * Return: Node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;

	current = *head;
	while (current->next != NULL)
	{
		if (current->n == )
		{
			current->n = number;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}

