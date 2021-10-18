"""Tree class and tree node class."""


class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)



class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)


if __name__ == '__main__':
    # Make an example tree and search for things in it
    
    dotted_black = Node("dotted black", [])
    faded_blue = Node("faded blue", [])
    dark_olive = Node("dark olive", [faded_blue])
    vibrant_plum = Node("vibrant plum", [dotted_black, faded_blue])
    shiny_gold = Node("shiny gold", [dark_olive, vibrant_plum])
    bright_white = Node("bright white", [shiny_gold])
    muted_yellow = Node("muted yellow", [faded_blue, shiny_gold])
    root = Node("light red", [muted_yellow, bright_white])

    tree = Tree(root)
    print(tree)
    print("new tree =", tree.find_in_tree("muted yellow"))  # should find
    # print("style.css = ", tree.find_in_tree("style.css"))  # should not find
