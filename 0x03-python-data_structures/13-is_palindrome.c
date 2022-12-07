#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * linked_length - function that checks the length of a linked list
 * @head: head pointer
 * Return: nothing
 */
int linked_length(listint_t *head)
{
	listint_t *temp;
	int count = 0;

	temp = head;

	while (temp != 0)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}

/**
 * is_palindrome - function in C that checks if a singly linked list
 * is a palindrome
 * @head: head pointer of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *last;
	int index, i = 0, j;

	first = last = *head;
	index = linked_length(*head);

	if (*head == NULL)
		return (1);
	while (i != index / 2)
	{
		first = last = *head;
		for (j = 0; j < i; j++)
			first = first->next;
		for (j = 0; j < index - (i + 1); j++)
			last = last->next;
		if (first->n != last->n)
			return (0);
		i++;
	}
	return (1);
}
