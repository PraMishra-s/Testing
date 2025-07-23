class Tree:
    def __init__(self):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    root = Tree()
    child1 = Tree()
    child1.add_child(Tree('Children 1'))
    child1.add_child(Tree('Children 2'))
    child1.add_child(Tree('Children 3'))

    child2 = Tree()
    child2.add_child(Tree('Children 4'))
    child2.add_child(Tree('Children 5'))
    child2.add_child(Tree('Children 6'))

    child3 = Tree()
    child3.add_child(Tree('Children 7'))
    child3.add_child(Tree('Children 8'))
    child3.add_child(Tree('Children 9'))

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    
    return root


        