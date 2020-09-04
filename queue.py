class Queue:

  #init function
  def __init__(self, capacity):
    self.front = self.size = 0
    self.rear = capacity -1
    self.Q = [None] * capacity
    self.capacity = capacity

  #Queue is full when size becomes equal to capacity
  def isFull(self):
    return self.size == self.capacity

  #Queue is empty when size is 0
  def isEmpty(self):
    return self.size == 0

  #Function to add item to Queue
  #It changes rear and size
  def EnQueue(self, item):
    if self.isFull():
        print("Queue is full")
        return

    self.rear = (self.rear + 1) % (self.capacity)
    self.Q[self.rear] = item
    self.size = self.size + 1
    print("% s enqueued to queue" % str(item))


  def DeQueue(self):
    if self.isEmpty():
      print("Queue is empty")
      return

    print("% s dequeued from queue" % str(self.Q[self.front]))
    x = self.Q.pop(self.front)
    self.rear = self.rear -1
