#include "LinkedList.h"

template <class T>

LinkedList<T>::LinkedList()
{
    this->head = NULL;
    this->tail = NULL;
}

template <class T>

void LinkedList<T>::addNode(T data)
{
    Node<T> *tmp = new Node<T>(data);

    if (this->head == NULL)
    {
        this->head = tmp;
        this->tail = tmp;
    }
    else
    {
        tail->next = tmp;
        this->tail = this->tail->next;
    }
}

template <class T>
void LinkedList<T>::printList(){
    Node<T> *tmp = this->head;
    while(tmp){
        if(tmp->next == NULL) printf("%d", tmp->data);
        else printf("%d->", tmp->data);
        tmp = tmp->next;
    }
    printf("\n");
}
template <class T>

Node<T>*LinkedList<T>::getHead(){
    return this->head;
}

template <class T>

Node<T>*LinkedList<T>::getTail(){
    return this->tail;
}