import sys 
import pygame as py
from visuals import *


class calculate_Graph():

    def __init__(self, vertices):

        self.start(vertices)
        self.shown = Shown_Graph(self)


    def start(self, vertices):
        self.v = vertices
        self.graph = adj_m_repr
        
        self.dist = [sys.maxsize] * self.v
        self.dist[0] = 0
        self.x = 0 
        self.y = 0
        self.sptSet = [False] * self.v

        self.iteration = 0
        self.iteration_1 = 0
        self.curr_v = 0
        self.last_v = 0

    def events(self):
        for e in py.event.get():
            if e.type == py.QUIT:
                self.shown.running = False
            if e.type == py.KEYDOWN and e.key == py.K_SPACE:
                if self.iteration < 9:
                    self.last_v = self.curr_v
                    V_positions[self.last_v][2] = GREEN
                    self.curr_v = self.shortest_vertex()
                self.iteration += 1

                # if self.iteration_1 < 9:
                #     for _ in range(self.v):
                #         self.update_adj_vertex(self.curr_v, self.iteration_1)


            if e.type == py.KEYDOWN and e.key == py.K_RIGHT:
                if self.iteration_1 < 9:
                    
                    self.x, self.y = self.get_adj_vertex(self.curr_v, self.iteration_1)
                    if isinstance(self.x, bool) and isinstance(self.y, bool):
                        pass
                    elif isinstance(self.x, int) and isinstance(self.y, int):
                        self.shown.animate_arrow(self.x, self.y)
            
            if e.type ==py.KEYDOWN and e.key == py.K_r:
                
                self.start(len(V_positions))
                for x in E_weights.keys():
                    E_weights[x][1] = WHITE
                for i in V_positions:
                    i[2] = RED
                    

    # Fall sem finnur lægstu heildar vegun á nódu
    # sem er ekki hluti af sptSet (hefur ekki verið skoðað en)
     
    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        # leita að nóduni
        for u in range(self.v):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
            
        return min_index

    def shortest_vertex(self):
        x = self.minDistance(self.dist, self.sptSet)

        self.sptSet[x] = True
        V_positions[x][2] = YELLOW
        return x

    def update_adj_vertex(self, x, y):
        self.dist[y] = self.dist[x] + self.graph[x][y]
        
        
    def get_adj_vertex(self, x, y):
        update = self.graph[x][y] > 0 and self.sptSet[y] == False and \
                    self.dist[y] > self.dist[x] + self.graph[x][y]
        
        while not update:    

            self.iteration_1 +=1
            y = self.iteration_1

            if self.iteration_1 == 9:
                self.iteration_1 = 0
                return False, False
        
            update = self.graph[x][y] > 0 and self.sptSet[y] == False and \
                    self.dist[y] > self.dist[x] + self.graph[x][y]
        
        return x, y
        
        

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.v
        dist[source] = source
        sptSet = [False] * self.v
        
        for _ in range(self.v):

            # velja nódu sem er ekki hluti af trénu 
            # (sem sýnir stystu leiðina til allra punkta, frá upphafs p.)
            
            x = self.minDistance(dist, sptSet)

            # fyrst að stysta nódan var fundin 
            # setja hana þá í tréð 
            sptSet[x] = True


            # athuga nódur í kringum nýju stystu valda nóduna, x
            # og uppfæra vegalengdir þeirra 

            for y in range(self.v):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]


g = calculate_Graph(len(V_positions))
g.dijkstra(0)

while g.shown.running:
    g.events()
    g.shown.update()
    g.shown.draw()

    g.shown.clock.tick(60)


py.quit()
