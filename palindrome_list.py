class Node:
    def __init__(self, data=None) -> None:
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop_last(self):
        current = self.head
        previous = self.head
        if self.head is None:
            return
        else:
            while current.next:
                previous = current
                current = current.next

            previous.next = None
            self.size -= 1
            return current.data

    def pop_first(self):
        current = self.head
        self.head = self.head.next
        return current.data

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


if __name__ == "__main__":
    def palindrome_list(arr):
        for x in range(arr.size):
            last, first = arr.pop_last(), arr.pop_first()
            if last == first:
                continue
            else:
                break



    linkedlist = LinkedList()
    nums = [21, 10, 19, 10, 21]
    [linkedlist.append(num) for num in nums]
    print(linkedlist.size)
    print(palindrome_list(linkedlist))

