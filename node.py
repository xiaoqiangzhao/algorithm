
class node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.paths = []

    def add_child(self,*child):
        for ch in child:
            self.children.append(ch)

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        return iter(self.children)

    def get_paths(self):
        paths = []
        if not self.children:
            paths.append([self])
            return paths
        for ch in self.children:
            for path in ch.get_paths():
                paths.append([self]+path)
        return paths


    def get_path_num(self):
        num = 0
        if self.children:
            for ch in self:
                num += ch.get_path_num()
            return num
        return 1

    def depth_show(self):
        yield self
        for ch in self:
            yield from ch.depth_show()
