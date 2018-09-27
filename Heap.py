class MaxHeap:

    def __init__(self, items=[]):
        self.heap = [0]
        # 더미로 0을 넣어 놓는 상태로 합니다.
        # 이유는 index가 1부터 시작하는것처럼 만들고 싶어서
        # 1부터 시작하면 부모와 자식을 판별 용이
        # len(self.heap) - 1 이 자기 자신의 index이

        for i in items:
            self.heap.append(i)
            # print(i,len(self.heap) - 1)
            self.__floatUp(len(self.heap) - 1)
            # 마지막에 더한다음에는 항상 자신의 부모와 바꾸어야 하는지 검토 교과서 Page 38

        print(self.heap)


    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)
        # 마지막에 더한다음에는 항상 자신의 부모와 바꾸어야 하는지 검토 교과서 Page 38

    # 가장 큰 값이 얼마인지만 넘겨줌. 비어있으면(1개) False 리턴
    def peek(self):
        # print("Length:%s",len(self.heap))
        if len(self.heap) > 1:
            if self.heap[1]:
                return self.heap[1]
            else:
                return False
        else:
            return False

    # 가장 큰 값을 보내주고 그자리를 채워줌 removeMax 교과서 page 40
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
            # 교과서와는 순서가 조금 다릅니다만.. 맨뒤와 맨앞을 순서를 먼저바꾸어주고 값을 내보내고(pop)
            # 그후에 맨위로 올라간 친구의 순서를 아래로 내릴 것을 검토한다.

        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    # 일력된 데이터를 pop해서 그 max heap sort결과를 리스트로 내보냄
    def Heapshort(self):

        Heap_sorted = []

        while True:
            if self.peek():
                Heap_sorted.append(self.pop())
            else:
                break

        return Heap_sorted

    # i번째와 j번째의 데이터를 바꾸어준다
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 부모와 위치를 바꾸는 경우
    def __floatUp(self, index):
        parent = index // 2  # 부모의 경우 인덱스를 둘로 나눈 목
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:  # 내가 부모보다 크다면 바꾸고 재검토 교과서TEXT 39page
            self.__swap(index, parent)
            self.__floatUp(parent)

            # 자식과 위치를 바꾸는 경우 교과서 41page 참조

    def __bubbleDown(self, index):
        left = index * 2  # 왼쪽 자식의 경우 인덱스를 두배로
        right = index * 2 + 1  # 왼쪽 자식의 경우 인덱스를 두배+1 위치
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


listin = [15, 35, 65, 20, 17, 80, 12, 45, 2, 4]
m = MaxHeap(listin)

print("    before: ", listin)
print("Heapsorted: ", m.Heapshort())
