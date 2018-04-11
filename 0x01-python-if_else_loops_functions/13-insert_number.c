#include "lists.h"

/**
 * insert_node - Inserts node into sorted singly linked list.
 * @head: This points to the head of linked list.
 * @number: This is the number we are inserting into sorted linked list.
 *
 * Return: address of new node, or NULL if failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *singly;
	listint_t *insertion;

	insertion = malloc(sizeof(listint_t));
	if (insertion == NULL)
		return (NULL);
	insertion->n = number;
	if (*head == NULL || (*head)->n >= insertion->n)
	{
		insertion->next = *head;
		*head = insertion;
	}
	else
	{
		singly = *head;
		while (singly->next != NULL && singly->next->n < insertion->n)
		{
			insertion->next = singly->next;
			singly->next = insertion;
		}
	}
	return (*head);
}
