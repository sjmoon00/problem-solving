N = int(input())
answer = []
tree = {}
for i in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

def preorder(root):
    if root == '.':
        return
    print(root, end='')
    left, right = tree[root]
    preorder(left)
    preorder(right)


def inorder(root):
    if root == '.':
        return
    left, right = tree[root]
    inorder(left)
    print(root, end='')
    inorder(right)

def postorder(root):
    if root == '.':
        return
    left, right = tree[root]
    postorder(left)
    postorder(right)
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')