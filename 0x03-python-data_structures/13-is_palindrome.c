#include "lists.h"


/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: head node of list
 *
 * Return: (1) on sucess else (0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *head_node, *tail_node, *prev, *curr, *next_node, *p1, *p2;

	if (*head == NULL)
		return (1);

	tail_node = *head;
	head_node = *head;

	while (tail_node != NULL && tail_node->next != NULL)
	{
		head_node = head_node->next;
		tail_node = tail_node->next->next;
	}
	prev = NULL;
	curr = head_node->next;
	while (curr != NULL)
	{
		next_node = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next_node;
	}
	p1 = *head;
	p2 = prev;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	return (1);
}
