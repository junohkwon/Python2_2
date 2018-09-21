###############################################################################
# 3 Max Heap
###############################################################################

import queue


class MaxHeap(object):

    # maxheap initialization
    def __init__(self, lst):
        self.lst = lst
        self.heapArray = []
        self.inorderArray = []
        self.heapArray = self.heaparray()
        # self.pq = PriorityQueue()
        # You can add additional code here

    def left(self, i):
        # Go to left subtree and return index
        return i * 2

    def right(self, i):
        # Go to right subtree and return index\
        return i * 2 + 1

    def inorder(self, i):

        if (self.heapArray[i] != None):  # If heapArray is not empty,
            # If left subtree exists,
            if(self.heapArray[self.left(i)] != None):
                self.inorder(self.left(i))

            self.inorderArray.append(self.heapArray[i])  # Append node itself

            if (self.heapArray[self.right(i)] != None):
            # If right subtree exists,
                self.inorder(self.right(i))

            self.inorderArray.append(self.heapArray[i])  # Append node itself

    def __str__(self):
        self.inorder(0)  # Build inorder list
        return str(self.inorderArray)


    def heaparray(self):
        # Make heap array
        for n in lst:
            self.heapArray.append(n)

            i = len(self.heapArray) - 1  # Last index
            while i > 1:   # root로 올때까지 부모와 비교하며 더 작으면 바꿔주고 반복한다.
                parent = int(i/2)

                if self.heapArray[i] < self.heapArray[parent]:
                    temp = self.heapArray[i]
                    self.heapArray[i] = self.heapArray[parent]
                    self.heapArray[parent] = temp

                    i = parent
                else:  # 만약 부모가 더 작으면 거기서 끝.
                    break

        return self.heapArray

    def heapsort(self):
        ls = []
        while not self.pq.empty():
            # dequeue one element
            # add to ls
            return str(ls)

    def enqueue(self, a):
        # Fill here
        pass

    def dequeue(self):
        # Fill here
        pass

    # isEmpty function의 반대
    def isNotEmpty(self):
        if (self.pq.empty == False):
            return True
        else:
            return False

    def heapsort(maxheap):
        print(maxheap.heapsort())


lst = [5, 3, 1, 4, 2]
h = MaxHeap(lst)
print(h)
# heapsort(h)