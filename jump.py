from node import node
class jump:
    def __init__(self):
        self.top = node("top")
        pass


    def jump_step(self, n):
        children = []
        if n == 1 :
            node_child = node(1)
            children.append(node_child)
            return children
        if n >=2 :
            for i in [1,2]:
                node_child = node(i)
                if self.jump_step(n-i):
                    node_child.add_child(*self.jump_step(n-i))
                children.append(node_child)
            return children

if __name__ =="__main__":
    my_jump = jump()
    top = node(" ")
    children = my_jump.jump_step(7)
    top.add_child(*children)
    print(top.get_path_num())
    paths = top.get_paths()
    for path in paths:
        for item in path:
            print(item,end=" ")
        print("\n")
    # for i in top.depth_show():
        # print(i)

    # for ch in children:
        # print(ch)
        # for i in ch.depth_show():
            # print(i)
    # for i in range)-(16):
        # print(next(my_steps))
    # for i in my_steps:
        # print(i)
