import pygame as py
import sys
from data import *

vec = py.math.Vector2

class Shown_Graph:

    def __init__(self, calculate_graph):
        py.init()

        self.g = calculate_graph
        self.dist = self.g.dist

        self.clock = py.time.Clock()
        py.display.set_caption("Dijkstra")
        self.screen = py.display.set_mode((WIDTH, HEIGHT))

        self.last_update = py.time.get_ticks()
        self.interpolation = 0
        self.start_pos = vec(0,0)
        self.end_pos = vec(5,5)
        self.moving_pos = self.start_pos.lerp(self.end_pos, self.interpolation)
        self.animating = False
        self.connection = 0
        
        self.font_name = py.font.match_font("microsoftyaheiui") 
        self.running = True
        
        self.V = []
        
    def update(self):

        if self.animating: 
            
            self.moving_pos = self.start_pos.lerp(self.end_pos, self.interpolation)
            self.interpolation+= 0.025

            if self.interpolation >= 1:
                self.animating = False
                self.interpolation = 0
                if not isinstance(self.g.x, bool) and not isinstance(self.g.y, bool):
                    E_weights[self.connection][1] = ORANGE
                    self.g.update_adj_vertex(self.g.x, self.g.y)

    def draw(self):
        self.screen.fill(BLACK)
        self.edge_connect()
        self.make_node()

        py.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = py.font.Font(self.font_name, size)   
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        text_rect.midtop = (x,y-text_rect.height/2)
        self.screen.blit(text_surface, text_rect)

    def make_node(self):
        for i, node_pos in enumerate(V_positions):
            py.draw.circle(self.screen, node_pos[2], 
                           (node_pos[0], node_pos[1]), RADIUS)
            self.draw_text(str(i), TX_SIZE, WHITE, 
                           node_pos[0], node_pos[1]+TX_OFFSET)
            
            if self.g.dist[i] == sys.maxsize:
                self.draw_text("inf", TX_SIZE, BLUE, 
                           node_pos[0], node_pos[1]-TX_OFFSET)
            else:
                self.draw_text(str(self.g.dist[i]), TX_SIZE, BLUE, 
                           node_pos[0], node_pos[1]-TX_OFFSET)


    def edge_connect(self):
        for edges in E_weights.keys():

            edge_color = E_weights[edges][1]
    
            points = [(V_positions[x][0:2]) for x in edges]
            py.draw.line(self.screen, edge_color, points[0], points[1], 7)

            x = 0
            y = 0
            i_same = 0
            same = False
            for i in points:
                i_same = i[1]
                if i_same == y:
                    same = True
                x+=i[0]
                y+=i[1]

            x = x/2 - 28

            if same:
                y= y/2 - 25
            else:
                y = y/2
            
            self.draw_text(str(E_weights[edges][0]), TX_SIZE, 
                           WHITE, x, y)

        if self.animating:

            py.draw.line(self.screen, ORANGE, 
                            (self.start_pos.x, self.start_pos.y),
                            (self.moving_pos.x, self.moving_pos.y) , 14)
        
    def animate_arrow(self, start_v, end_v):
        self.animating = True
        self.connection = self.get_right_key(start_v, end_v)
        

        starting_point = (V_positions[start_v][0:2])
        ending_point = (V_positions[end_v][0:2])

        
        self.start_pos = vec(starting_point)
        self.end_pos = vec(ending_point)

        self.moving_pos = self.start_pos.lerp(self.end_pos, 0)
                
        

    def get_right_key(self,x,y):
        if (x, y) in E_weights:
            return (x, y)
        elif (y, x) in E_weights: 
            return (y, x)