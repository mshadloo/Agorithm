class MaxHeap:
    def __init__(self, arr):
        self.heap=arr;

        for i in range(math.ceil(len(self.heap)//2)-1,-1,-1):
            self.heapify(i)
    def heapify(self,index):
        while(index<len(self.heap)):
            temp_i=index
            maximum=self.heap[index]
            if(2*(index+1)-1<len(self.heap)):
                if(self.heap[2*(index+1)-1]>self.heap[index]):
                    temp_i=2*(index+1)-1
                    maximum=self.heap[2*(index+1)-1]
                if(2*(index+1)<len(self.heap)):
                    if(self.heap[2*(index+1)]>maximum):
                       temp_i=2*(index+1)

            self.switch(index,temp_i)
            index=temp_i           

    def switch(self,i,j):
        temp=self.heap[i];
        self.heap[i]=self.heap[j]
        self.heap[j]=temp;




