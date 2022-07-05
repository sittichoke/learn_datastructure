class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing  data that matches the key
        Retun the node or 'None' if not found

        Takes O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node  
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
            return
        
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node
        
    def remove(self, key):
        current = self.head;
        previous = None
        found = False

        self.search(key)

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                return current
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                return current
            else:
                previous = current
                current = current.next_node

        return None

    def __repr__(self):
            """
            Return a string representation of the list.
            Takes O(n) time.
            """
            nodes = []
            current = self.head
            while current:
                if current is self.head:
                    nodes.append("[Head: %s]" % current.data)
                elif current.next_node is None:
                    nodes.append("[Tail: %s]" % current.data)
                else:
                    nodes.append("[%s]" % current.data)
                current = current.next_node
            return  '-> '.join(nodes)



