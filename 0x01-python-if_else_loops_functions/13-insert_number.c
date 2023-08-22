#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Head node
 * @number: number to insert
 *
 * Return: newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{

		temp = *head;
		while (temp->next != NULL && temp->next->n < number)
		{
			temp = temp->next;

		}
		new_node->next = temp->next;
		temp->next = new_node;
		return (new_node);
	}

	return (NULL);
}
