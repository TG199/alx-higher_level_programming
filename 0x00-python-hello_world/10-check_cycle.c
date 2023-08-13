#include "lists.h"
#include <stdio.h>

/**
 * check_cyle - checks for a circle in a singly linked list
 * @list: head of list
 *
 * Return: 1 if true, 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
    	if (list == NULL)
    	{
        	return (0);
    	}

    	slow = list;
    	fast = list;

    	while (fast != NULL && fast->next != NULL)
    	{
        	slow = slow->next;
        	fast = fast->next->next;

        	if (slow == fast)
		{
            	return (1);
        	}
    	}

    	return (0);
}
/*int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
	{
		printf("List is empty");
		return (-1);
	}

	temp = list;

	if (temp->next == NULL)
	{
		printf("List is not cycle");
		return (0);
	}

	if (temp->next == list)
	{
		printf("List is cycle");
		return (1);
	}
	else
	{
		temp = temp->next;
		check_cycle(temp);
	}

	return (0);

}*/

