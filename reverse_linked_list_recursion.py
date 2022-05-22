def reverseList(head): 
      #base cases, if it's none, return none
      #if head.next == None i.e once we've traversed the entirity
      #of the list, then we can "return head", or, pop off 
      #those values one by one, and state how we wish to reverse the list
      if head == None or head.next == None:
          return head
      
      #since we're popping off the head's one by one, and creating a new head,
      #with new directional arrows, we need to assign the reverselist function call 
      #to a variable
      #the function call is exercised first with node.next since we want to
      #traverse down the nodes to the end
      newHead = self.reverseList(head.next)
      
      #now we can begin to manipulate the directional arrows
      #take the current node, and change the node after its pointer, to point to it
      head.next.next = head
			#once the node in front points to curr. We can change curr's pointer
			#to point to None. So to we don't have directional arrows pointing to one another
      head.next = None
          
      return newHead