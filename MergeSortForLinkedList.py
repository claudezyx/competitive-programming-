class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SortLinkedList(object):
    def sort(self,head):
        if (head == None): return None 
        if (head.next == None): return head 
      
        mid = self.findMidPoint(head)
        temp = mid.next 
        mid.next = None 
        left = head 
        right = temp 
        left = self.sort(left)
        right = self.sort(right) 
        
        return self.mergeTwoList(left, right) 
    
    def mergeTwoList(self, left, right): 
        head = temp = ListNode(None)
        while (left != None and right != None): 
            if (left.val <= right.val): 
                temp.next = left
                left = left.next 
            else: 
                temp.next = right 
                right = right.next 
            temp = temp.next 
            
        if (left == None): temp.next = right 
        else: temp.next = left 
        
        return head.next 
        
        
    def findMidPoint(self,head):
        if (head == None): return None
        
        slow = fast = ListNode(None) 
        slow.next = head 
        
        while (fast != None and fast.next != None): 
            fast = fast.next.next
            slow = slow.next 
        
        return slow 

## Below is used for testing purpose
"""
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(5)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(11)
head.next.next.next.next.next = ListNode(1)
a = SortLinkedList()
b = a.sort(head)
while (b != None):
    print(b.val)
    b = b.next 
"""
