

roads = [[36, 34, 31, 28, 17],
 [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
 [39, 36, 21, 19, 9, 7, 4],
 [35, 20, 15, 11, 6],
 [39, 36, 21, 19, 9, 7, 2],
 [32, 16, 14],
 [35, 20, 15, 11, 1, 3],
 [39, 36, 22, 21, 19, 9, 2, 4],
 [33, 30, 14],
 [36, 21, 19, 2, 4, 7],
 [31, 27, 26, 25, 24, 18, 17, 13],
 [35, 20, 15, 3, 6],
 [37, 34, 31, 28, 22, 17],
 [27, 24, 18, 10],
 [33, 30, 16, 5, 8],
 [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
 [37, 30, 5, 14],
 [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
 [31, 27, 26, 25, 24, 1, 10, 13, 17],
 [21, 2, 4, 7, 9],
 [35, 26, 1, 3, 6, 11, 15],
 [2, 4, 7, 9, 19],
 [39, 37, 29, 7, 12],
 [38, 32, 29],
 [27, 10, 13, 18],
 [34, 31, 27, 26, 1, 10, 15, 17, 18],
 [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
 [31, 1, 10, 13, 18, 24, 25, 26],
 [39, 36, 34, 31, 0, 12, 17],
 [38, 37, 32, 22, 23],
 [33, 8, 14, 16],
 [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
 [38, 5, 23, 29],
 [8, 14, 30],
 [0, 12, 17, 25, 26, 28, 31],
 [1, 3, 6, 11, 15, 20],
 [39, 0, 2, 4, 7, 9, 28],
 [12, 16, 22, 29],
 [23, 29, 32],
 [2, 4, 7, 22, 28, 36]]

intersections = {0: [0.7801603911549438, 0.49474860768712914],
 1: [0.5249831588690298, 0.14953665513987202],
 2: [0.8085335344099086, 0.7696330846542071],
 3: [0.2599134798656856, 0.14485659826020547],
 4: [0.7353838928272886, 0.8089961609345658],
 5: [0.09088671576431506, 0.7222846879290787],
 6: [0.313999018186756, 0.01876171413125327],
 7: [0.6824813442515916, 0.8016111783687677],
 8: [0.20128789391122526, 0.43196344222361227],
 9: [0.8551947714242674, 0.9011339078096633],
 10: [0.7581736589784409, 0.24026772497187532],
 11: [0.25311953895059136, 0.10321622277398101],
 12: [0.4813859169876731, 0.5006237737207431],
 13: [0.9112422509614865, 0.1839028760606296],
 14: [0.04580558670435442, 0.5886703168399895],
 15: [0.4582523173083307, 0.1735506267461867],
 16: [0.12939557977525573, 0.690016328140396],
 17: [0.607698913404794, 0.362322730884702],
 18: [0.719569201584275, 0.13985272363426526],
 19: [0.8860336256842246, 0.891868301175821],
 20: [0.4238357358399233, 0.026771817842421997],
 21: [0.8252497121120052, 0.9532681441921305],
 22: [0.47415009287034726, 0.7353428557575755],
 23: [0.26253385360950576, 0.9768234503830939],
 24: [0.9363713903322148, 0.13022993020357043],
 25: [0.6243437191127235, 0.21665962402659544],
 26: [0.5572917679006295, 0.2083567880838434],
 27: [0.7482655725962591, 0.12631654071213483],
 28: [0.6435799740880603, 0.5488515965193208],
 29: [0.34509802713919313, 0.8800306496459869],
 30: [0.021423673670808885, 0.4666482714834408],
 31: [0.640952694324525, 0.3232711412508066],
 32: [0.17440205342790494, 0.9528527425842739],
 33: [0.1332965908314021, 0.3996510641743197],
 34: [0.583993110207876, 0.42704536740474663],
 35: [0.3073865727705063, 0.09186645974288632],
 36: [0.740625863119245, 0.68128520136847],
 37: [0.3345284735051981, 0.6569436279895382],
 38: [0.17972981733780147, 0.999395685828547],
 39: [0.6315322816286787, 0.7311657634689946]}


# from math import sqrt
#
# def shortest_path(roads, intersections, start, goal):
#     path = [start]
#
#     g_cost = [0]*len(roads)
#     f_cost = [0]*len(roads)
#     visited_nodes = []
#     curr_node = start
#     while curr_node != goal:
#         f_cost_curr_neighbors = [0]*len(roads[curr_node])
#         for i , node in enumerate(roads[curr_node]):
#             g_cost[node] += euclidean_distance_heuristic(intersections[curr_node], intersections[node])
#             f_cost[node] += g_cost[node] + euclidean_distance_heuristic(intersections[node], intersections[goal])
#             f_cost_curr_neighbors[i] += g_cost[node] + euclidean_distance_heuristic(intersections[node], intersections[goal])
#
#         idx = f_cost_curr_neighbors.index(min(f_cost_curr_neighbors))
#         if curr_node in visited_nodes:
#             curr_node = roads[curr_node][idx]
#             continue
#         path.append(roads[curr_node][idx])
#         visited_nodes.append(curr_node)
#         curr_node = roads[curr_node][idx]
#
#     return path
#
#
# def euclidean_distance_heuristic(start_coordinate, goal_coordinate):
#     return sqrt(((start_coordinate[0] - goal_coordinate[0]) ** 2) + ((start_coordinate[1] - goal_coordinate[1]) ** 2))


from queue import PriorityQueue
import ast
from math import sqrt
from collections import defaultdict
def shortest_path(roads, intersections, start, goal):

    path = [start]
    visited_nodes = []
    path_g_dict = defaultdict(int)
    curr_node = start
    frontier_path = ('[]', [])
    while curr_node != goal:
        #path_g_dict = defaultdict(int)
        for i , node in enumerate(roads[curr_node]):
            if node not in visited_nodes:
                this_path = list((curr_node,node))
                if not ast.literal_eval(frontier_path[0]):
                     this_path = list(set(ast.literal_eval(frontier_path[0]) + this_path))
                else:
                     this_path.remove(list(set(ast.literal_eval(frontier_path[0])) & set(this_path))[0])
                     this_path = ast.literal_eval(frontier_path[0])+this_path
                if not ast.literal_eval(frontier_path[0]):
                    path_g_dict[str(this_path)] += euclidean_distance_heuristic(intersections[curr_node], intersections[node])
                else:
                    if frontier_path[0] in path_g_dict.keys():
                        path_g_dict.pop(frontier_path[0])
                    path_g_dict[str(this_path)] += frontier_path[1] + euclidean_distance_heuristic(intersections[curr_node], intersections[node])

                path_g_dict[str(this_path)] += euclidean_distance_heuristic(intersections[node], intersections[goal])

        frontier_path = sorted(path_g_dict.items(), key=lambda k_v: k_v[1])[0]
        visited_nodes.append(curr_node)
        curr_node = ast.literal_eval(frontier_path[0])[-1]
        while curr_node in visited_nodes:
            copy_path_g_dict = sorted(path_g_dict.items(), key=lambda k_v: k_v[1]).copy()
            copy_path_g_dict.remove(copy_path_g_dict[0])
            curr_node = ast.literal_eval(copy_path_g_dict[0][0])[-1]

    return path


def euclidean_distance_heuristic(start_coordinate, goal_coordinate):
    return sqrt(((start_coordinate[0] - goal_coordinate[0]) ** 2) + ((start_coordinate[1] - goal_coordinate[1]) ** 2))

start = 8
goal  = 24
path = shortest_path(roads, intersections, start, goal)

print(path)

