# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodeList = [ListNode()]
        i = 0
        carryover = 0
        temp1 = l1
        temp2 = l2
        while(temp1 or temp2 or carryover):
            sum = temp1.val + temp2.val + carryover
            carryover = 0
            currentDigit = ListNode(sum % 10, )
            nodeList[i].val = sum % 10
            carryover = int(sum/10)
            # Store carryover and then break
            if(temp1.next is None and temp2.next is None):
                if carryover == 1:
                    nodeList.append(ListNode())
                    nodeList[i+1].val = 1
                    break
            else:
                nodeList.append(ListNode())
                nodeList[i].next = nodeList[i+1]
                i = i + 1
                if temp1.next is not None:
                    temp1 = temp1.next
                else:
                    temp1 = ListNode()
                if temp2.next is not None:
                    temp2 = temp2.next
                else:
                    temp2 = ListNode()
        return nodeList[0]