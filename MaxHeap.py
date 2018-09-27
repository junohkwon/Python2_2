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
        # self.pq = PriorityQueue()
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
        # print('this is i : ', i, end='\n')
        # print('this is len : ', len(self.heapArray)-1)
        res = []
        if len(self.heapArray)-1 > i and self.heapArray is not None:
            res = self.inorderTraversal(self.left(i))
            res.append(self.heapArray[i])
            res = res + self.inorderTraversal(self.right(i))
        else:
            return res


    def __str__(self):
        #self.inorderTraversal(1)
        #self.inorder(1)  # Build inorder list
        return str(self.inorderArray)

    def swap(self, l, r):
        self.heapArray[l], self.heapArray[r] = self.heapArray[r], self.heapArray[l]

    def heaparray(self,lst):
        # Make heap array
        for n in lst:
            self.heapArray.append(n)
            self.moveup(len(self.heapArray) - 1)

    def moveup(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heapArray[index] > self.heapArray[parent]:
            self.swap(index, parent)
            self.moveup(parent)

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

    # while not self.pq.empty():
    #     # dequeue one element
    #     # add to ls
    #     return str(ls)

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

    # def heapsort(maxheap):
    #     print(maxheap.heapsort())



listin = [15, 35, 65, 20, 17, 80, 12, 45, 2, 4]
m = MaxHeap(listin)
print('MaxHeap : ',m)
#print('Sorted : ', m.heapsort())
res = m.inorderTraversal(1)
print('this is res : ', res)
# print("    before: ", listin)
# print("Heapsorted: ", m.Heapshort())
#
#
#
# lst = [15, 35, 65, 20, 17, 80, 12, 45, 2, 4]
# h = MaxHeap(lst)
# print(h)


