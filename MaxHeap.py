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
        print(self.heapArray)

    def __str__(self):
        self.inorder(0)  # Build inorder list
        return str(self.inorderArray)

    def swap(self, l, r):
        temp = self.heapArray[l]
        self.heapArray[l] = self.heapArray[r]
        self.heapArray[r] = temp

    def heaparray(self):
        # Make heap array
        for n in self.lst:
            self.heapArray.append(n)

            i = len(self.heapArray) - 1  # Last index
            while i > 1:
                parent = int(i/2)
                if self.heapArray[i] < self.heapArray[parent]:
                    self.swap(i, parent)
                    i = parent
                else:
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



# listin = [15, 35, 65, 20, 17, 80, 12, 45, 2, 4]
# m = MaxHeap(listin)
# print(m)

# print("    before: ", listin)
# print("Heapsorted: ", m.Heapshort())
#
#
#
lst = [20,12,35,15,10,80,30,17,2,1]
h = MaxHeap(lst)
print(h)
# # heapsort(h)