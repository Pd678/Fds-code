#include <iostream>
#include <string>
using namespace std;

struct Node {
    string data;
    Node* next;
};

Node* createNode(string data) {
    Node* newNode = new Node;
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insert(Node*& head, string data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void display(Node* head) {
    while (head != NULL) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

Node* setIntersection(Node* setA, Node* setB) {
    Node* intersection = NULL;

    while (setA != NULL) {
        Node* tempB = setB;
        while (tempB != NULL) {
            if (setA->data == tempB->data) {
                insert(intersection, setA->data);
                break;
            }
            tempB = tempB->next;
        }
        setA = setA->next;
    }

    return intersection;
}
Node* SetEitheror(Node* setA, Node* setB){
	Node* tempB = setB;
}
int main() {
    Node* setA = NULL;
    Node* setB = NULL;

    int t, c1, c2, i, j;
    string bs, vn;

    cout << "Enter total Number of students: ";
    cin >> t;

    cout << "Enter Number of Students who like Butterscotch: ";
    cin >> c1;

    for (i = 1; i <= c1; i++) {
        cout << "Enter roll no of student who likes Butterscotch: ";
        cin >> bs;
        insert(setA, bs);
    }

    cout << "Enter Number of Students who like Vanilla: ";
    cin >> c2;

    for (j = 1; j <= c2; j++) {
        cout << "Enter roll no of student who likes Vanilla: ";
        cin >> vn;
        insert(setB, vn);
    }

    cout << "Set A: ";
    display(setA);
    cout << "Set B: ";
    display(setB);

    Node* intersection = setIntersection(setA, setB);

    cout << "Students who like both Vanilla and Butterscotch: ";
    display(intersection);

    int intersectionCount = 0;

    Node* tempInter = intersection;
    while (tempInter != NULL) {
        intersectionCount++;
        tempInter = tempInter->next;
    }

    int totalStudentsNotBoth = t - (c1 + c2 - 2 * intersectionCount);

    cout << "Number of students who like neither Vanilla nor Butterscotch: " << totalStudentsNotBoth << endl;

    int totalStudentsEitherOr = c1 + c2 - intersectionCount;

    cout << "Students who like either Vanilla or Butterscotch or not both: "<<display(SetEitheror) << endl;

    return 0;
}
