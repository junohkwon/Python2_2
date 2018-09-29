###############################################################################
# 3 Max Heap
###############################################################################

import queue


class MaxHeap(object):


    # maxheap initialization
    def __init__(self, lst):
        self.heapArray = [None]
        self.inorderArray = []
        self.heaparray(lst)
        self.pq = queue.PriorityQueue()
        # You can add additional code here


    def left(self, i):
        # Go to left subtree and return index
        return i * 2

    def right(self, i):
        # Go to right subtree and return index
        return i * 2 + 1

    def inorder(self, i):
        print(self.heapArray)

    def inorderTraversal(self, i):
        ls = []

        if len(self.heapArray) > i:
            ls = self.inorderTraversal(self.left(i))
            ls.append(self.heapArray[i])
            ls = ls + self.inorderTraversal(self.right(i))

        return ls

    def __str__(self):
        print('this is inorder traversal - ',self.inorderTraversal(1))
        return str(self.inorderArray)

    def swap(self, l, r):
        self.heapArray[l], self.heapArray[r] = self.heapArray[r], self.heapArray[l]

    def heaparray(self,lst):
        # Make heap array
        self.pq = queue.PriorityQueue()
        for n in lst:
            self.heapArray.append(n)
            self.moveup_v2(len(self.heapArray) - 1)

    def moveup(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heapArray[index] > self.heapArray[parent]:
            self.swap(index, parent)
            self.moveup(parent)

    def moveup_v2(self, index):
        parent = index // 2
        if index <= 1:
            return
        else:
            self.enqueue(self.heapArray[index])
            self.enqueue(self.heapArray[parent])

            self.heapArray[index] = self.dequeue()
            self.heapArray[parent] = self.dequeue()

            self.moveup_v2(parent)

    def movedown(self, index):
        left = self.left(index)
        right = self.right(index)
        maxidx = index

        if len(self.heapArray) > left and self.heapArray[maxidx] < self.heapArray[left]:
            maxidx = left

        if len(self.heapArray) > right and self.heapArray[maxidx] < self.heapArray[right]:
            maxidx = right

        if maxidx != index:
            self.swap(index, maxidx)
            self.movedown(maxidx)


    def top(self):
        if len(self.heapArray) > 1:
            if self.heapArray[1]:
                return self.heapArray[1]
            else:
                return False
        else:
            return False

    def pop(self): #max value return
        #print('this is heapArray : ', self.heapArray)
        if len(self.heapArray) > 2:
            self.swap(1, len(self.heapArray) - 1)
            maxvalue = self.heapArray.pop()
            self.movedown(1)
        elif len(self.heapArray) == 2:
            maxvalue = self.heapArray.pop()
        else:
            maxvalue = False
        return maxvalue

    def heapsort(self):
        ls = []
        while True:
            if self.top():
                ls.append(self.pop())
            else:
                break

        return ls

    def heapsort_v2(self):

        for data in self.heapArray:
            if data is not None:
                self.pq.put(-1*data)

        ls= []
        while not self.pq.empty():
            data = self.pq.get()
            ls.append(-1*data)
        return str(ls)


    def enqueue(self, a):
        self.pq.put(a)
        pass

    def dequeue(self):
        return self.pq.get()


    # isEmpty function의 반대
    def isNotEmpty(self):
        if (self.pq.empty == False):
            return True
        else:
            return False

    # def heapsort(maxheap):
    #     print(maxheap.heapsort())



listin = [20,12,35,15,10,80,30,17,2,1]
m = MaxHeap(listin)
print('MaxHeap : ', m.heapArray)
print('InOrder Traversal : ', m)
print('Sorted V2 : ', m.heapsort_v2())
print('Sorted V1 : ', m.heapsort())

#print('Sorted : ', m.heapsort())
# print("    before: ", listin)
# print("Heapsorted: ", m.Heapshort())
#
#
#
# lst = [15, 35, 65, 20, 17, 80, 12, 45, 2, 4]
# h = MaxHeap(lst)
# print(h)


