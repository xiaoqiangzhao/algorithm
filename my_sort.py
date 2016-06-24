
class my_sort:
    def __init__(self):
        pass

    def insert_sort(self,list):
        for i in range(1,len(list)):
            item = list[i]
            print(item)
            for j in reversed(range(i)):
                if list[j] > item:
                    list[j+1] = list[j]
                    list[j] = item
                else:
                    list[j+1] = item
                    break
            print(list)
        print(list)

    def rec_sort(self,list):
        length = len(list)
        temp = 0
        print(list)
        def merge(lista,listb):
            print("lista : {}  listb: {}".format(lista,listb))
            r_list = []
            for i in range(len(lista)+len(listb)):
                if lista and listb:
                    if lista[0] < listb[0]:
                        r_list.append(lista.pop(0))
                    else:
                        r_list.append(listb.pop(0))
                else:
                    break
            if lista or listb:
                r_list = r_list + lista + listb
            print("merged : {}".format(r_list))
            return r_list

        if length == 1:
            return list
        if length == 2:
            if list[0] > list[1]:
                temp = list[1]
                list[1] = list[0]
                list[0] = temp
            return list
        sep = int(length/2)
        return merge(self.rec_sort(list[:sep]),self.rec_sort(list[sep:]))


if __name__ == '__main__':
    my_list = [2,3,1,5,4,8,7,-1,-4,-8,6]
    m_s = my_sort()
    my_rec_list = m_s.rec_sort(my_list)
    print(my_rec_list)
    # m_s.insert_sort(my_list)
