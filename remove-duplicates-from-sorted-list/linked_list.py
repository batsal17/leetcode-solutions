class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("No elements in the linked list")
            return

        itr = self.head
        iistr = ''

        while itr:
            iistr = iistr + (str(itr.data) + '-->' if itr.next else str(itr.data))
            itr = itr.next

        print(iistr)

    def remove_duplicate(self):
        itr = self.head

        while itr and itr.next:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else:
                itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(1)
    ll.head.next = Node(1)
    ll.head.next.next = Node(2)
    ll.head.next.next.next = Node(3)
    ll.head.next.next.next.next = Node(3)

    print("Before removing duplicates:")
    ll.print()

    ll.remove_duplicate()

    print("After removing duplicates:")
    ll.print()