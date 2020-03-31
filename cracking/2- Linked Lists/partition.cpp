// Write code to partition a linked list around a value x, such
// that all nodes less than x come before all nodes greater than or equal to x.
// If x is in the list, the values of x only need to be after the elements less than x.
// The partition element x can appear anywhere in the right partition, it doesn't need to appear
 //between the left and right partitions.

// Input: 3 -> 5 -> 8 -> 10 -> 2 -> 1, x = 5
// Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

#include <bits/stdc++.h>
#include "LinkedList.h"

using namespace std;

// void partition(LinkedList<int> l1, int x){
//     Node<int> *head = l1.getHead();
//     Node<int> *aux = head;

//     if(aux == NULL) return;
//     while (aux)
// }

int main(){
    LinkedList<int> *l1 = new LinkedList<int>();
    l1->addNode(3);
    l1->addNode(5);
    l1->addNode(8);
    l1->addNode(10);
    l1->addNode(2);
    l1->addNode(1);
    int x = 5;
    l1->printList();
}