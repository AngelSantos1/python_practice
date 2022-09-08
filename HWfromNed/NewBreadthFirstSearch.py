""" type Tree struct {
  value int
  left *Tree
  right *Tree
}

//                3
//               / \
//              5   7
//             / \   \
//            2   9   4
//           /
//          1

// 3,5,2,1,9,7,4
// 2,5,9
// 3,7,4
// First base case None
//  """

"""             5
               / \
              3   7
             / \   \
            2   4   8
                 \
                  8
            """

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] #List of visited nodes
queue = [] #Initialize queue - FIFO 

def breadthFirstSearch(visited , graph, node):
    visited.append(node)
    queue.append(node)

    while queue:    #Create loop to visit each node
        m = queue.pop(0)
        print (m, end = " ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

#Driver Code
print("Following is the Breadth-First Search")
breadthFirstSearch(visited, graph, '5')


    

        


#DepthFirstSearch()

""" def DepthFirstSearch(root, search):
    left = root.left, search
    #for node in range(tree - 1):
    if root == None:
        return None

    if search == root.value:
        return root """


"""  if search == root.value:
  	return root
  
  l = DepthFirstSearch(root.left, search)
	if l != None:
  	return l
  r = DepthFirstSearch(root.right, search)
  if r != None:
  	return r
  
	return None """
