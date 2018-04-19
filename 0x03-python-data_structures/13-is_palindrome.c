#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


/**
 * checker_is_palindrome - This checks the function for is_palindrome
 * @head: This is the beginning of the list.
 * @ending: This is the end of the list.
 *
 * Return: 1 for True and 0 for False.
 */

int checker_is_palindrome(listint_t **head, listint_t *ending)
{
	if (ending == NULL)
		return (1);
	if (checker_is_palindrome(head, ending->next) && (*head)->n == ending->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - Checks if singly linked list is palindrome
 * @head: This is a double ponter to our head
 *
 * Return: 0 if failed, 1 if success
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || *head == NULL)
		return (1);
	return (checker_is_palindrome(head, *head));
}
