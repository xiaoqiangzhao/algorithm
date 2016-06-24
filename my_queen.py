from node import node
class my_queen:
    def __init__(self,n):
        self.n_queen = n
        self.set_x = set(range(n))
        self.set_y = set(range(n))

    def Point_valid(self,point,exclude):
        # print("exclude: {}".format(exclude))
        if exclude:
            for i in exclude:
                if abs(point[0] - i[0]) == abs(point[1] - i[1]):
                    return False
        return True
    def get_map(self, n, set_x, set_y, exclude):

        # print(n,set_x,set_y)
        children = []
        next_exclude = exclude
        if n == 1:
            for x in set_x:
                for y in set_y:
                    print("exclude: {}".format(exclude))
                    if self.Point_valid((x,y), exclude):
                        node_child = node((x,y))
                        children.append(node_child)
            return children
        else:
            for x in set_x:
                for y in set_y:
                    s_x = set([x])
                    s_y = set([y])
                    # print("gaaga")
                    # print(set_x,set_y,s_x,s_y)
                    if self.Point_valid((x,y),exclude):
                        if exclude:
                            print("get exclude")
                            print(exclude)
                            next_exclude.append((x,y))
                            print("next exclude: {}".format(next_exclude))
                        else:
                            next_exclude = [(x,y)]
                        print("next exclude: {}".format(next_exclude))
                        node_child = node((x, y))
                        if n-1 >0:
                            node_child.add_child(*self.get_map(n-1, set_x - s_x, set_y - s_y, next_exclude))
                        children.append(node_child)
            return children

if __name__ == "__main__":
    queen = my_queen(4)
    queen_map = queen.get_map(queen.n_queen, queen.set_x, queen.set_y, [])
    top = node(" ")
    top.add_child(*queen_map)
    for ch in queen_map:
        print(ch)
    print(top.get_path_num())
    paths = top.get_paths()
    for p in paths:
        if len(p) == 5:
            for i,path in enumerate(p):
                print(i,path)



