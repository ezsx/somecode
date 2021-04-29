
from collections import Counter
from _bisect import bisect_left

class Edge:
    def __init__(self, ver_a, ver_b, p):
        self.ver_a = ver_a
        self.ver_b = ver_b
        self.p = p

    def __eq__(self, other):
        b = (self.ver_a.num == other.ver_a.num and self.ver_b.num == other.ver_b.num) or \
         (self.ver_a.num == other.ver_b.num and self.ver_b.num == other.ver_a.num)
        return b

    def __repr__(self):
        return 'edge('+str(self.ver_a) + str(self.ver_b)+' weight= ' + str(self.p)+')'

    def __hash__(self):
        v_min = min(self.ver_a.num, self.ver_b.num)
        v_max = max(self.ver_a.num, self.ver_b.num)
        return hash(str(v_min) + str(v_max) + str(self.p))

class Vertex:
   def __init__(self, num):
       self.pai = 0
       self.num =num
       self.list_edge = list()

   def add_edge(self, l: Edge):
       self.list_edge.append(l)
   def color (self,pai):
       pass

   def __repr__(self):
        return 'Vertex('+str(self.num)+')'

   def __str__(self):
       return self.__repr__()

   def get_path_to(self, v_calling, v_looking, l: list):
        # сформировать список соседей вершин
        list_vertex = [e.ver_a if e.ver_a != self else e.ver_b for e in self.list_edge]
        # Проверить среди своих соседей, есть ли вершина v_looking
        # Цикл по соседям
        for v in list_vertex:
            # если есть, то добавить в список l, себя, найденную вершину и вернуть значение 1
            if v == v_looking:
                l.append(v_looking)
                l.append(self)
                return 1

        # Продолжаем если не нашли
        # Цикл по соседям
        for v in list_vertex:
            # вызвать get_path_to для каждого из соседа, кроме вызывающего
            if v == v_calling:
                continue
            a = v.get_path_to(v_calling=self, v_looking=v_looking, l=l)
            # если 0, то продолжаем
            # если 1, то  добавляем себя в список и возвращаем 1.
            if a == 1:
                l.append(self)
                return 1

        # возвращаем 0
        return 0


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

    def get(self, num_A, is_create=True):
        for v in self.verticals:
            if v.num == num_A:
                return v
        if is_create:
            v_new = Vertex(num_A)
            self.verticals.append(v_new)
            return v_new
        else:
            return None
    def load_file(self, file):
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
        #for p in self.verticals:
        #    print(p)
        #    p.print()
        for p in self.edges:
            print(p)

    def add_edge(self, e: Edge):
        # найти вершину а и найти вершину б
        ver0 = self.get(e.ver_a.num, False)
        ver1 = self.get(e.ver_b.num, False)
        # если вершины в графе нет то вернуть 0
        if ver0 == ver1 and len(self.verticals)!=0: # если оба None
            return 0
        if (ver0 != None) and (ver1 != None):
            return -1
        # берем вершину а и вершину б создаем эдж
        ver0 = self.get(e.ver_a.num)
        ver1 = self.get(e.ver_b.num)
        # добавляем эдж в граф
        self.edges.append(Edge(ver0, ver1, e.p))
        return 1

    def get_ostav(self):
        vGraph_r = Graph()
        # Копируем список ребер исходного графа
        list0 = list(self.edges)
        list_deffer = list()
        # Перебираем исходный список, пока не закончатся ребра
        while len(list0) > 0:
            # Перебор копии ребер исходного графа
            for e in list0:
                # добавляем ребро в новый граф
                res = vGraph_r.add_edge(e)
                # 1 - добавил, -1 не требует добавления, 0 - рано добавлять
                # если рано добавлять, сохраняем в отложенном списке.
                if res == 0:
                    list_deffer.append(e)

            # перенести список отложенных в исходный
            list0 = list_deffer
            list_deffer = list()
        for e in vGraph_r.edges:
            e.ver_a.add_edge(e)
            e.ver_b.add_edge(e)
        return vGraph_r

    def get_diff_edges(self, graph):
        list0 = list(self.edges)
        list1 = list(graph.edges)
        set0 = set(list0)
        set1 = set(list1)
        # хэшировать списки самостоятельно
        set2 = set0-set1
        print("___________------___________", set2)
        return set2

    def get_cycle_list(self, edge_list):
        ### создаем и наполняем список cycle_list_r
        cycle_list_r = list()
        #### в цикле по полученным ребрам
        for e in edge_list:
            # берем ребро из списка ребер
            # создаем список под вершины цикла lv
            lv = list()
            # берем одну вершину и спрашииваем у нее путь до второй из ребра, передавая lv
            ver0 = self.get(e.ver_a.num)
            ver1 = self.get(e.ver_b.num)
            ver0.get_path_to(ver0, ver1, lv)
            # получаем список lv и добавляем его в cycle_list_r
            cycle_list_r.append(lv)
        return cycle_list_r

def print_cycles(cycle_list_r):
    for c in cycle_list_r:
        print(c)
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
    cycle_list =g_ostav.get_cycle_list(edge_list)

    # Выводим каждую из найденных цепей
    print("_________*")
    print_cycles(cycle_list)
    print("_________*")
    # Выводим G_ostav
    g_ostav.print()
    print("_________")
    for p in edge_list:
        print(p)

main()