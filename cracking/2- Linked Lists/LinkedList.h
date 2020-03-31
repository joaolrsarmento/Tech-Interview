#ifndef _LINKEDLIST_H
#define _LINKEDLIST_H

#include <bits/stdc++.h>

using namespace std;

template <class T>
class Node
{
public:
    Node(){}
    Node(T n){
        this->data = n;
        this->next = NULL;
    }
    T data;
    Node *next;
};

template <class T>
class LinkedList
{
private:
    Node<T> *head, *tail;

public:
    LinkedList();
    void addNode(T data);
    void printList();
    Node<T> *getHead();
    Node<T> *getTail();
};

#endif