class Node:

## A linked list (LL) node
## to store a queue entry
  def __init__(self,data):
    self.data = data
    self.next = None


## A class to represent a queue

#The queue, front stores the front Node

class LQueue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0


  def isEmpty(self):
    return self.size == 0

  ##enQueue() This operation adds a new node after rear and moves rear to the next node.



  def EnQueue(self,item):
    new = Node(item) #data blir tidelt self.data i et Node object
    print(str(item) + " has been queued")
    if self.isEmpty():
      self.front = new
    else:
      self.rear.next = new
    self.rear = new
    self.size +=1

  ###deQueue() This operation removes the front node and moves front to the next node.

  def DeQueue(self):
    if self.isEmpty():
      print("queue is empty")
      return
    temp = self.front
    print(str(temp.data) + " has been dequed")
    self.front = temp.next

    if(self.front == None):
      self.rear= None


  def LSearch(self, item):
    x = item
    temp = self.front

    while(temp):
      if( x == temp.data ):
        return print(str(x) +" has been found")
      temp = temp.next
    return False


  def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True # data found

            current = current.next

        return False # Data Not found



  def printQueue(self):
    temp = self.front
    while(temp):
      print(temp.data)
      temp = temp.next


if __name__ == '__main__':
  q =LQueue()
  q.EnQueue(10)
  q.EnQueue(20)
  #q.DeQueue()
  #q.DeQueue()
  q.EnQueue(50)
  #q.DeQueue()
  print("Queue Front " + str(q.front.data))
  print("Queue Rear " + str(q.rear.data))
  #q.printQueue()
  q.LSearch(20)
