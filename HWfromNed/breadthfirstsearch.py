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

func DepthFirstSearch(root *Tree, search int) *Tree {
  return nil
}

def DepthFirstSearch(root, search):
  if root == None:
  	return None
  if search == root.value
  	return root
  
  l = DepthFirstSearch(root.left, search)
	if l != None:
  	return l
  r = DepthFirstSearch(root.right, search)
  if r != None:
  	return r
  
	return None

DepthFirstSearch()

func BreadthFirstSearch(root *Tree, search int) *Tree {
  return nil
}



