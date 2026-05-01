class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    cur = head
    result = []
    while cur:
        result.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(result))