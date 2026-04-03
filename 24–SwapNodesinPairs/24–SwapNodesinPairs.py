class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


def create_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


arr = [1, 2, 3, 4]
head = create_list(arr)
new_head = swapPairs(head)
print_list(new_head)