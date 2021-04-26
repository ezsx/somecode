




class Edge:
    def __init__(self, ver_a, ver_b, p):
        self.ver_a = ver_a
        self.ver_b = ver_b
        self.p     = p

    def __eq__(self, other):
        b =(self.ver_a==other.ver_a and self.ver_b == other.ver_b) or \
        (self.ver_a == other.ver_b and self.ver_b == other.ver_a)
        return b

    def __repr__(self):
        return 'edge('+str(self.ver_a) + str(self.ver_b)+' weight= ' + str(self.p)+')'


class Vertex:
   def __init__(self,num):
       self.pai = 0
       self.num =num
       self.list_edge= list()

   def add_edge(self, l:Edge):
       self.list_edge.append(l)
   def color (self,pai):
       pass

   def __repr__(self):
        return 'Vertex('+str(self.num)+')'

   def __str__(self):
       return self.__repr__()



   def print(self):
       for l in self.list_edge:
           print(l)

class Cycles:
    pass

class Graph:
    def __init__(self):
        self.verticals =list()
        self.edges = list()

    def is_exist(self,l):
        for i in self.edges:
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
            L=Edge(ver_a, ver_b, v[2])
            if not self.is_exist(L):
                ver_a.list_edge.append(L)
                ver_b.list_edge.append(L)
                self.edges.append(L)
    def print(self):
        for p in self.verticals:
            print(p)
            p.print()

    def add_edge(self,e:Edge):
        pass

    def get_ostav(self):
        vGraph_r = Graph()
        # Копируем список ребер исходного графа
        list0 = list(self.edges)
        list_deffer = list()
        # Перебираем исходный список, пока не закончатся ребра
        while(len(list0) > 0):
            # Перебор ребер исходного графа
                # добавляем ребро в новый граф
                # 1 - добавил, -1 не требует добавления, 0 - рано добавлять
                # если рано добавлять, сохраняем в отложенном списке.
           # перенести список отложенных в исходный
            list0 = list_deffer
            list_deffer = list()
        return vGraph_r

    def get_diff_edges(self,graph):
        pass

    def get_cycle_list(self,edge_list):
        pass

def print_cycles(c):
    pass

def main():
    # Поиск фундаментальных циклов графа.
    # Загружаем граф. - g_main
    g_main = Graph()
    g_main.load_file('data/test_1.txt')
    # Находим оставное дерево графа g_ostav
    g_ostav = g_main.get_ostav()
    # Находим разницу множеств ребер из G_main и G_ostav
    # это ребра образующие основные циклы.
    edge_list = g_main.get_diff_edges(g_ostav)
    # нахоидм цепи (циклы) по каждому из ребер
    cycle_list =  g_main.get_cycle_list(edge_list)

    # Выводим каждую из найденных цепей
    print_cycles(cycle_list)
    # Выводим G_ostav
    g_ostav.print()



main()