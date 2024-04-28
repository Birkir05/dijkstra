import random

WIDTH = 1800
HEIGHT = 1000
RADIUS = 55
WHITE = (255, 255, 255)
RED = (220, 40, 60)
GREEN = (0, 170, 60)
YELLOW = (255, 191, 0)
ORANGE = (225, 110, 51)
BLACK = (0, 0, 0)
BLUE = (82, 192, 248)
TX_SIZE = 40
TX_OFFSET = 25


ACC = 0.15

V_positions = [
    [(1/6)*WIDTH, (1/2)*HEIGHT, RED],
    [(2/6)*WIDTH, (1/5)*HEIGHT, RED],
    [(2/6)*WIDTH, (4/5)*HEIGHT, RED],
    [(3/6)*WIDTH, (1/5)*HEIGHT, RED],
    [(3/6)*WIDTH, (4/5)*HEIGHT, RED],
    [(3/6)*WIDTH, (1/2)*HEIGHT, RED],
    [(4/6)*WIDTH, (4/5)*HEIGHT, RED],
    [(4/6)*WIDTH, (1/5)*HEIGHT, RED],
    [(5/6)*WIDTH, (1/2)*HEIGHT, RED]
]

E_r_connections = {
    0: [random.randint(0,5) for i in range(random.randint(1,3))],
    1: [random.randint(2,4) for i in range(random.randint(1,2))],
    2: [random.randint(0,4) for i in range(random.randint(1,3))],
    3: [random.randint(2,4) for i in range(random.randint(1,3))],
    4: [random.randint(1,7) for i in range(random.randint(1,2))],
    5: [random.randint(5,6) for i in range(random.randint(1,3))],
    6: [random.randint(4,8) for i in range(random.randint(1,3))],
    7: [random.randint(3,5) for i in range(random.randint(1,2))],
    8: [random.randint(5,8) for i in range(random.randint(1,3))]
}
E_connections = {
    0: [1, 2],
    1: [2, 3],
    2: [4, 5],
    3: [5, 6, 7],
    4: [6],
    5: [2, 3, 4],
    6: [8],
    7: [6, 8]   
}

E_weights = {
    (0,1): [4, WHITE], 
    (0,2): [8, WHITE],
    (1,2): [11, WHITE],
    (1,3): [8, WHITE],
    (2,5): [7, WHITE],
    (2,4): [1, WHITE],
    (3,5): [2, WHITE],
    (3,6): [4, WHITE], 
    (3,7): [7, WHITE],
    (5,4): [6, WHITE], 
    (4,6): [2, WHITE],
    (6,7): [14, WHITE],
    (7,8): [9, WHITE],
    (6,8): [10, WHITE],
}


adj_m_repr = [[0 for column in range(len(V_positions))] 
                for row in range(len(V_positions))]

for i in E_weights.keys():
    weight = E_weights[i][0]
    adj_m_repr[i[0]][i[1]] = weight
    adj_m_repr[i[1]][i[0]] = weight


E_r_weights = []

for k in E_connections.keys():
    for x in E_connections[k]:
        E_r_weights.append([k,x])

E = set(tuple(sorted(connection)) 
                for connection in E_weights)

E_r_weights = {}
for edge in E:
    weight = random.randint(1, 10)
    E_r_weights[edge] = weight