#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function that insert into a sorted linked list
 * @head: pointer to the head of the linked list
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *node;

	node = (struct listint_s *)malloc(sizeof(struct listint_s));
	if (node == 0)
		return (NULL);

	node->n = number;

	if (temp == NULL || temp->n >= number)
	{
		node->next = temp;
		*head = node;
		return (node);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	node->next = temp->next;
	temp->next = node;

	return (node);
}

