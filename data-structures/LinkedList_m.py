class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if(self.head is None):
            self.head = Node(data)
        else:
            currentNode = self.head
            while(currentNode.next is not None and currentNode.next.data is not None):
                currentNode = currentNode.next
            currentNode.next = Node(data)

    def delete(self, data):
        if(self.head.data == data):
            self.head = self.head.next
            return

        currentNode = self.head
        while(currentNode is not None and currentNode.data != data):
            previousNode = currentNode
            currentNode = currentNode.next
        if(currentNode is None):
            print('can not find')
            return
        else:
            previousNode.next = currentNode.next

    def toString(self):
        currentNode = self.head
        s = []
        while(currentNode is not None and currentNode.data is not None):

            s.append(currentNode.data)
            currentNode = currentNode.next

        return '->'.join(map(str, s))

    def deleteNode(self, node):
        if(node is None):
            print('node is None')
            return
        if(node.next is None):
            node = None
            return

        node.data = node.next.data
        node.next = node.next.next

    def find(self, data):
        currentNode = self.head
        while(currentNode is not None and currentNode.data != data):
            currentNode = currentNode.next
        return currentNode

    def iterator(self):
        currentNode = self.head
        while(currentNode is not None):
            yield currentNode.data
            currentNode = currentNode.next
        return

    def nodeIterator(self):
        currentNode = self.head
        while(currentNode is not None):
            yield currentNode
            currentNode = currentNode.next
        return

    def insertAfter(self, node, newNode):
        newNode.next = node.next
        node.next = newNode

    def insertFirst(self, newNode):
        if(self.head is None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode


def removeDuplicates1(linkedList):
    n1 = linkedList.head
    if(n1 is None):
        print("the linked list is empty")
        return
    while(n1 is not None):
        n2 = n1.next
        while(n2 is not None):
            if (n2.data == n1.data):
                linkedList.deleteNode(n2)
            else:
                n2 = n2.next
        n1 = n1.next


def removeDuplicates2(linkedList):
    hash = {}
    if(linkedList.head is None):
        return
    currentNode = linkedList.head
    while(currentNode is not None):
        item = currentNode.data
        if(hash.get(item) is None):
            hash[item] = item
            previousNode = currentNode
            currentNode = currentNode.next
        else:
            if(currentNode.next is not None):
                linkedList.deleteNode(currentNode)
            else:
                currentNode = None
                previousNode.next = None


def partition(linkedList, threshold):
    currentNode = linkedList.head
    lastLessNode = None
    previousNode = None
    while(currentNode is not None):
        if(currentNode.data < threshold):
            newNode = Node(currentNode.data)
            if(currentNode.next is None):
                currentNode = None
                previousNode.next = None
            else:
                linkedList.deleteNode(currentNode)
            if(lastLessNode is None):
                linkedList.insertFirst(newNode)

            else:
                linkedList.insertAfter(lastLessNode, newNode)
            lastLessNode = newNode
        else:
            previousNode = currentNode
            currentNode = currentNode.next


def reversed(linkedList):
    head = linkedList.head
    node = head.next
    head.next = None
    while(node is not None):
        temp = node.next
        node.next = head
        head = node
        node = temp
    linkedList.head = head


def findNthNode(linkedlist, n):
    n1 = linkedList.head
    k = 1
    n2 = n1
    while(n1 is not None and k < n):
        k += 1
        n1 = n1.next
    if(k < n):
        print('the number of nodes is less than ' + str(n))
        return
    while(n1.next is not None):
        n1 = n1.next
        n2 = n2.next
    return n2
# def getNode(linkedList, data):
#     for


l = [3, 6, 5, 9, 3, 8, 5, 1, 2]
linkedList = LinkedList()
for i in l:
    linkedList.insert(i)
print(linkedList.toString())

# for item in linkedList.nodeIterator():
#     print(item.data)
# linkedList.deleteNode(item)
# print(linkedList.toString())
# print(sorted(linkedList.nodeIterator(), key=lambda a: a.data))
# print(sorted(linkedList.iterator()))
# print(set(linkedList.iterator()))
# removeDuplicates2(linkedList)
# print(linkedList.toString())
# partition(linkedList, 4)
# print(linkedList.toString())
# print(findNthNode(linkedList, 12).data)
reversed(linkedList)
print(linkedList.toString())
# node = linkedList.find(6)
# if(node is not None):
#     linkedList.delete(node)
# print(linkedList.toString())
# print(map(int,'345'))
# linkedList.delete(5)
# linkedList.toString()
# linkedList.delete(3)
# linkedList.toString()
