#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function that checks for cycle in linked list
 * @list: list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ahead = list;
	listint_t *behind = list;

	if (list == 0)
		return (0);

	while (ahead && behind && ahead->next)
	{
		behind = behind->next;
		ahead = ahead->next->next;

		if (behind == ahead)
			return (1);
	}

	return (0);
}
