



class Link:
    def __init__(self, ver_a, ver_b, p):
        self.ver_a = ver_a
        self.ver_b = ver_b
        self.p     = p

    def __eq__(self, other):
        b =(self.ver_a==other.ver_a and self.ver_b == other.ver_b) or \
        (self.ver_a == other.ver_b and self.ver_b == other.ver_a)
        return b

    def __repr__(self):
        return 'Link('+str(self.ver_a) + str(self.ver_b)+' weight= ' + str(self.p)+')'


class Vertex:
   def __init__(self,num):
       self.pai = 0
       self.num =num
       self.list_link= list()

   def add_link(self,l:Link):
       self.list_link.append(l)
   def color (self,pai):
       pass

   def __repr__(self):
        return 'Vertex('+str(self.num)+')'

   def __str__(self):
       return self.__repr__()



   def print(self):
       for l in self.list_link:
           print(l)

class Graph:
    def __init__(self):
        self.verticals =list()
        self.links = list()
    def is_exist(self,l):
        for i in self.links:
            if l==i:
                return True
        return False

    def get(self,num_A):
        for v in self.verticals:
            if v.num == num_A:
                return v
        v_new = Vertex(num_A)
        self.verticals.append(v_new)
        return v_new

    def load_file(self,file):
        f = open(file)

        for line in f:
            strs = line.split(' ')
            v=[]
            for s in strs:
                if s != '':
                    v.append(int(s))
            ver_a = self.get(v[0])
            ver_b = self.get(v[1])
            L=Link(ver_a,ver_b,v[2])
            if not self.is_exist(L):
                ver_a.list_link.append(L)
                ver_b.list_link.append(L)
                self.links.append(L)
    def print(self):
        for p in self.verticals:
            print(p)
            p.print()


def main():
    # Поиск фундаментальных циклов графа.
    # Загружаем граф. - g_main
    g = Graph()
    g.load_file('data/test_1.txt')
    # Находим оставное дерево графа G_ostav
    # Находим разницу множеств ребер из G_main и G_ostav
    # это ребра образующие основные циклы.
    # нахоидм цепи по каждому из ребер
    # Выводим каждую из найденных цепей
    # Выводим G_ostav
    g.print()
    pass



main()