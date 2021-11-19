from math import sqrt
import copy

class Path(object):
    def __init__(self, node_list=None, _map=None, g_cost=0, f_cost=0, goal_node=None):
        self.node_list = node_list
        self.map = _map
        self.goal_node = goal_node
        self.frontier_node = self._get_frontier()
        self.prev_frontier_node = None
        self.g_cost = g_cost
        self.f_cost = f_cost

    def insert(self, new_node):
        self.node_list.append(new_node)
        self._update_f_insertion()
        self.frontier_node = self._get_frontier()

    def _update_f_insertion(self):
        if len(self.node_list) >= 2:
            g_new = euclidean_distance(self.map.intersections[self.node_list[-2]], self.map.intersections[self.node_list[-1]])
            h_new = euclidean_distance(self.map.intersections[self.node_list[-1]], self.map.intersections[self.goal_node])
            self.g_cost += g_new
            self.f_cost = self.g_cost + h_new
            return
        self.f_cost = 0

    def pop(self):
        self._update_f_pop()
        self.node_list = self.node_list[:-1]
        #self.node_list.pop()

    def _update_f_pop(self):
        if len(self.node_list) >= 2:
            g_loss = euclidean_distance(self.map.intersections[self.node_list[-2]], self.map.intersections[self.node_list[-1]])
            h_prev = euclidean_distance(self.map.intersections[self.node_list[-2]], self.map.intersections[self.goal_node])
            self.g_cost -= g_loss
            self.f_cost = self.g_cost + h_prev
            return

    def _get_frontier(self):
        if self.node_list:
            return self.node_list[-1]
        else:
            return None


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        data_copy = copy.deepcopy(data) # deep copy of data so downstream operations won't change its value
        self.queue.append(data_copy)

    # for popping an element based on Priority
    def pop(self):
        try:
            _min = 0 # f_cost is always non-negative so this works
            for i in range(len(self.queue)):
                if self.queue[i].f_cost < self.queue[_min].f_cost:
                    _min = i
            item = self.queue[_min]
            del self.queue[_min]
            return item
        except IndexError:
            pass


def euclidean_distance(start_coordinate, goal_coordinate):
    return sqrt(((start_coordinate[0] - goal_coordinate[0]) ** 2) +
                ((start_coordinate[1] - goal_coordinate[1]) ** 2))


def shortest_path(_map, start, goal):

    all_paths = PriorityQueue()
    curr_node = start

    # handle edge case where start and goal are the same
    if start == goal:
        return [start]

    while curr_node != goal:
        for node in _map.roads[curr_node]:
            if curr_node == start:
                cheapest_path = Path(node_list = [start], _map=_map, goal_node = goal)
                cheapest_path.insert(node)
            else:
                if node in cheapest_path.node_list:
                    continue
                if cheapest_path.prev_frontier_node != cheapest_path.node_list[-1]:
                    cheapest_path.pop()
                cheapest_path.insert(node)
            all_paths.insert(cheapest_path)

        cheapest_path = all_paths.pop()
        curr_node = cheapest_path.frontier_node
        cheapest_path.prev_frontier_node = cheapest_path.frontier_node

    return cheapest_path.node_list