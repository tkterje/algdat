# !/usr/bin/python3
# coding=utf-8
class Node:

## A linked list (LL) node
## to store a queue entry
  def __init__(self,data):
    self.data = data
    self.next = None


class Queue:
    def __init__(self, max_size):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size

    def enqueue(self, value):
        if self.isFull():
            return
        new = Node(value)
        if self.isEmpty():
          self.front = self.rear = new
          self.front.next = self.rear
        else:
          self.rear.next = new
        self.rear = new
        self.size +=1

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        if temp.next:
            self.front = temp.next
        else:
            self.front == None
            self.rear == None
        self.size -=1
        return temp.data

    def isFull(self):
        return self.max_size == self.size
    def isEmpty(self):
        return self.size == 0


def tester(values, sequence, max_size):
    """
    Tester en oppgitt sekvens av operasjoner og sjekker at verdiene
    (values) kommer ut i riktig rekkefølge.
    """
    index = 0
    queue = Queue(max_size)
    output = []
    for action in sequence:
        if action == "enqueue":
            queue.enqueue(values[index])
            index += 1
        elif action == "dequeue":
            output.append(queue.dequeue())

    if output != values:
        print(
            "Feilet for følgende sekvens av operasjoner "
            + "'{:}' med verdiene ".format(", ".join(sequence))
            + "'{:}' og maksimal størrelse".format(", ".join(map(str, values)))
            + "'{:}'".format(max_size)
        )
        return True
    return False


tests = (
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        3,
    ),
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        1,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "dequeue",
            "dequeue",
        ),
        4,
    ),
)

failed = False

for values, sequence, max_size in tests:
    failed |= tester(values, sequence, max_size)

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
