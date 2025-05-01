
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root : root
        array = []
        def createArray(root, level):

            if root is None:
                return
            if len(array) <= level:
                    array.append([])

            # Add current node's data to its corresponding level
            array[level].append(root)

            # Recur for left and right children
            createArray(root.left, level + 1)
            createArray(root.right, level + 1)

        createArray(root, 0)
        for row in array:
            for i in range(len(row)):
                if i < len(row)-1:
                    row[i].next = row[i+1]
                  
        return root
        print(array)


        

        