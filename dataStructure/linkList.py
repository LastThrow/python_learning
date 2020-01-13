class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList(object):

    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head == None  # 比较内容

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next
        print(cur.data)

    # 头插法
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    # 尾插法
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node


