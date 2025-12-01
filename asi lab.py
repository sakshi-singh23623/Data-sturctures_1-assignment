


#include <stdio.h>
#define MAX 5

int queue[MAX];
int front = -1, rear = -1;

void enqueue(int ticket) {
    if (rear == MAX - 1) {
        printf("Queue is FULL! Cannot add more tickets.\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = ticket;
    printf("Ticket %d added successfully.\n", ticket);
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue is EMPTY! No tickets to process.\n");
        return;
    }
    printf("Processing Ticket: %d\n", queue[front]);
    front++;
}

void display() {
    if (front == -1 || front > rear) {
        printf("No pending tickets.\n");
        return;
    }
    printf("Pending Tickets: ");
    for (int i = front; i <= rear; i++)
        printf("%d ", queue[i]);
    printf("\n");
}

int main() {
    int choice, ticket;

    while (1) {
        printf("\n--- Ticketing System (Linear Queue) ---\n");
        printf("1. Add Ticket (Enqueue)\n");
        printf("2. Process Ticket (Dequeue)\n");
        printf("3. Display Pending Tickets\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter ticket number: ");
                scanf("%d", &ticket);
                enqueue(ticket);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                return 0;
            default:
                printf("Invalid choice! Try again.\n");
        }
    }
}






--- Ticketing System (Linear Queue) ---
1. Add Ticket
2. Process Ticket
3. Display Pending Tickets
4. Exit

Enter ticket number: 101
Ticket 101 added successfully.

Pending Tickets: 101 102 103
Processing Ticket: 101

















#include <stdio.h>
#include <stdlib.h>

// Structure for a node
struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

// Function to insert a node at the end
void insert(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
        printf("Node inserted: %d\n", value);
        return;
    }

    struct Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    printf("Node inserted: %d\n", value);
}

// Function to delete a node by value
void delete(int value) {
    if (head == NULL) {
        printf("List is empty! Cannot delete.\n");
        return;
    }

    struct Node* temp = head;
    struct Node* prev = NULL;

    // Node to be deleted is head
    if (temp != NULL && temp->data == value) {
        head = temp->next;
        free(temp);
        printf("Node deleted: %d\n", value);
        return;
    }

    // Search for the node to delete
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }

    // Node not found
    if (temp == NULL) {
        printf("Node not found!\n");
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("Node deleted: %d\n", value);
}

// Function to search for a value
void search(int value) {
    struct Node* temp = head;
    int position = 1;

    while (temp != NULL) {
        if (temp->data == value) {
            printf("Value %d found at position %d\n", value, position);
            return;
        }
        temp = temp->next;
        position++;
    }

    printf("Value %d not found in the list.\n", value);
}

// Function to display the linked list
void display() {
    if (head == NULL) {
        printf("List is empty!\n");
        return;
    }

    struct Node* temp = head;
    printf("Linked List: ");

    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }

    printf("NULL\n");
}

int main() {
    int choice, value;

    while (1) {
        printf("\n--- Singly Linked List Operations ---\n");
        printf("1. Insert Node\n");
        printf("2. Delete Node\n");
        printf("3. Search Node\n");
        printf("4. Display List\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(value);
                break;

            case 2:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                delete(value);
                break;

            case 3:
                printf("Enter value to search: ");
                scanf("%d", &value);
                search(value);
                break;

            case 4:
                display();
                break;

            case 5:
                exit(0);

            default:
                printf("Invalid choice! Try again.\n");
        }
    }
}











--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 1
Enter value to insert: 10
Node inserted: 10

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 1
Enter value to insert: 20
Node inserted: 20

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 1
Enter value to insert: 30
Node inserted: 30

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 4
Linked List: 10 -> 20 -> 30 -> NULL

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 3
Enter value to search: 20
Value 20 found at position 2

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 2
Enter value to delete: 10
Node deleted: 10

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 4
Linked List: 20 -> 30 -> NULL

--- Singly Linked List Operations ---
1. Insert Node
2. Delete Node
3. Search Node
4. Display List
5. Exit
Enter your choice: 5






#include <stdio.h>
#include <string.h>

#define MAX 100

char stack[MAX];
int top = -1;

// Push function
void push(char c) {
    if (top == MAX - 1) {
        printf("Stack Overflow!\n");
        return;
    }
    stack[++top] = c;
}

// Pop function
char pop() {
    if (top == -1) {
        printf("Stack Underflow!\n");
        return '\0';
    }
    return stack[top--];
}

int main() {
    char str[MAX], reversed[MAX];
    int i = 0;

    printf("Enter a string: ");
    fgets(str, MAX, stdin);

    // Remove newline if present
    str[strcspn(str, "\n")] = '\0';

    // Push all characters onto stack
    for (i = 0; str[i] != '\0'; i++) {
        push(str[i]);
    }

    // Pop characters to form reversed string
    i = 0;
    while (top != -1) {
        reversed[i++] = pop();
    }
    reversed[i] = '\0';

    printf("Reversed String: %s\n", reversed);

    return 0;
}




Enter a string: HELLO WORLD
Reversed String: DLROW OLLEH








class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Qty: {self.quantity}, Price: {self.price}"


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("Item ID already exists!")
        else:
            self.items[item.item_id] = item
            print("Item added successfully.")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id in self.items:
            if quantity is not None:
                self.items[item_id].quantity = quantity
            if price is not None:
                self.items[item_id].price = price
            print("Item updated successfully.")
        else:
            print("Item not found!")

    def search_item(self, item_id):
        if item_id in self.items:
            print("Item Found:")
            print(self.items[item_id])
        else:
            print("Item not found!")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully.")
        else:
            print("Item not found!")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty!")
        else:
            print("\n--- Inventory Items ---")
            for item in self.items.values():
                print(item)


def main():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Search Item")
        print("4. Delete Item")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            inventory.add_item(Item(item_id, name, quantity, price))

        elif choice == '2':
            item_id = input("Enter Item ID to update: ")
            quantity = input("Enter new Quantity (leave blank to skip): ")
            price = input("Enter new Price (leave blank to skip): ")

            inventory.update_item(
                item_id,
                int(quantity) if quantity else None,
                float(price) if price else None
            )

        elif choice == '3':
            item_id = input("Enter Item ID to search: ")
            inventory.search_item(item_id)

        elif choice == '4':
            item_id = input("Enter Item ID to delete: ")
            inventory.delete_item(item_id)

        elif choice == '5':
            inventory.display_inventory()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()














    --- Inventory Management System ---
1. Add Item
2. Update Item
3. Search Item
4. Delete Item
5. Display Inventory
6. Exit
Enter your choice: 1
Enter Item ID: 101
Enter Item Name: Laptop
Enter Quantity: 5
Enter Price: 45000
Item added successfully.

--- Inventory Management System ---
1. Add Item
2. Update Item
3. Search Item
4. Delete Item
5. Display Inventory
6. Exit
Enter your choice: 1
Enter Item ID: 102
Enter Item Name: Mouse
Enter Quantity: 20
Enter Price: 500
Item added successfully.

--- Inventory Management System ---
Enter your choice: 5

--- Inventory Items ---
ID: 101, Name: Laptop, Qty: 5, Price: 45000.0
ID: 102, Name: Mouse, Qty: 20, Price: 500.0

--- Inventory Management System ---
Enter your choice: 3
Enter Item ID to search: 102
Item Found:
ID: 102, Name: Mouse, Qty: 20, Price: 500.0

--- Inventory Management System ---
Enter your choice: 2
Enter Item ID to update: 101
Enter new Quantity (leave blank to skip): 7
Enter new Price (leave blank to skip): 46000
Item updated successfully.

--- Inventory Management System ---
Enter your choice: 4
Enter Item ID to delete: 102
Item deleted successfully.

--- Inventory Management System ---
Enter your choice: 5

--- Inventory Items ---
ID: 101, Name: Laptop, Qty: 7, Price: 46000.0

--- Inventory Management System ---
Enter your choice: 6
Exiting...


















































































