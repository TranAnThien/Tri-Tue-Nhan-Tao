import queue
import random
import math

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_new_states(state):
    blank_x, blank_y = find_blank(state)
    new_states = []

    for dx, dy in MOVES:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            new_states.append(tuple(tuple(row) for row in new_state))

    return new_states

def bfs_solve(start, goal):
    q = queue.Queue()
    q.put((start, []))
    visited = set()
    visited.add(start)

    while not q.empty():
        current, path = q.get()
        if current == goal:
            return path

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                q.put((new_state, path + [new_state]))

    return None

def dfs_solve(start, goal):
    stack = [(start, [])]
    visited = set()
    visited.add(start)

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [new_state]))

    return None

def ucs_solve(start, goal):
    pq = queue.PriorityQueue()
    pq.put((0, start, []))
    visited = set()
    visited.add(start)

    while not pq.empty():
        cost, current, path = pq.get()
        if current == goal:
            return path

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                pq.put((cost + 1, new_state, path + [new_state]))

    return None

def ids_solve(start, goal):
    depth = 0
    while True:
        result = depth_limited_search(start, goal, depth)
        if result is not None:
            return result
        depth += 1

def depth_limited_search(start, goal, max_depth):
    q = queue.Queue()
    q.put((start, [], 0))

    visited = set()

    while not q.empty():
        current, path, depth = q.get()

        if current == goal:
            return path

        if depth < max_depth:
            for new_state in generate_new_states(current):
                if new_state not in visited:
                    visited.add(new_state)
                    q.put((new_state, path + [new_state], depth + 1))

    return None


def manhattan(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == state[i][j]:
                            distance += abs(i - x) + abs(j - y)
                            break
                    else:
                        continue
                    break
    return distance


def greedy_solve(start, goal):
    pq = queue.PriorityQueue()
    pq.put((manhattan(start, goal), start, []))
    visited = set()

    while not pq.empty():
        h, current, path = pq.get()

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for new_state in generate_new_states(current):
            if new_state not in visited:
                pq.put((manhattan(new_state, goal), new_state, path + [new_state]))

    return None

def a_star_solve(start, goal):
    pq = queue.PriorityQueue()
    pq.put((manhattan(start, goal), 0, start, []))
    visited = {}

    while not pq.empty():
        f, g, current, path = pq.get()

        if current == goal:
            return path

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        for new_state in generate_new_states(current):
            new_g = g + 1
            new_f = new_g + manhattan(new_state, goal)
            pq.put((new_f, new_g, new_state, path + [new_state]))

    return None

def ida_star_solve(start, goal):
    threshold = manhattan(start, goal)
    
    while True:
        q = queue.Queue()
        q.put((start, [], 0))
        visited = set()
        min_threshold = float('inf')

        while not q.empty():
            current, path, g = q.get()
            f = g + manhattan(current, goal)

            if f > threshold:
                min_threshold = min(min_threshold, f)
                continue

            if current == goal:
                return path

            visited.add(current)

            for new_state in generate_new_states(current):
                if new_state not in visited:
                    q.put((new_state, path + [new_state], g + 1))

        if min_threshold == float('inf'):
            return None

        threshold = min_threshold

def simple_hill_climbing_solve(start, goal):
    q = queue.Queue()
    q.put((start, [start])) 

    while not q.empty():
        current, path = q.get()

        if current == goal:
            return path

        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        for new_state in generate_new_states(current):
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                best_manhattan = h
                best_state = new_state
                break

        if best_state:
            q.put((best_state, path + [best_state]))
        else:
            return None

    return None

def hill_climbing_solve(start, goal):
    q = queue.Queue()
    q.put((start, [start])) 

    while not q.empty():
        current, path = q.get()

        if current == goal:
            return path

        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        for new_state in generate_new_states(current):
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                best_manhattan = h
                best_state = new_state

        if best_state:
            q.put((best_state, path + [best_state]))
        else:
            return None

    return None

def Stochastic_hill_climbing_solve(start, goal):
    q = queue.Queue()
    q.put((start, [start])) 

    while not q.empty():
        current, path = q.get()

        if current == goal:
            return path

        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        neighbors = generate_new_states(current)
        for i in range(len(neighbors)):
            new_state = random.choice(neighbors)
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                best_manhattan = h
                best_state = new_state
                break
            else:
                neighbors.remove(new_state)

        if best_state:
            q.put((best_state, path + [best_state]))
        else:
            return None

    return None

def Simulated_Annealing_solve(start, goal):
    q = queue.Queue()
    q.put((start, [start])) 
    T = pow(10, 4)
    alpha = 0.99

    while not q.empty():
        current, path = q.get()

        if current == goal:
            return path

        current_manhattan = manhattan(current, goal)
        best_state = None

        neighbors = generate_new_states(current)
        for i in range(len(neighbors)):
            new_state = random.choice(neighbors)
            h = manhattan(new_state, goal)
            if current_manhattan >= h:
                best_state = new_state
                break
            else:
                p = math.exp(-(current_manhattan - h)/T)
                if 0 <= p <= 1:
                    best_state = new_state
                    break
            neighbors.remove(new_state)
        T *= alpha

        if best_state:
            q.put((best_state, path + [best_state]))
        else:
            return None

    return None

def beam_search_solve(starts, goal, k=2):
    q = queue.Queue()

    if not isinstance(starts, list):
        starts = [starts]

    for start in starts:
        q.put((start, [start]))

    while not q.empty():
        candidates = []

        for _ in range(min(k, q.qsize())):
            current, path = q.get()

            if current == goal:
                return path

            neighbors = generate_new_states(current)

            for state in neighbors:
                dist = manhattan(state, goal)
                candidates.append((state, path + [state], dist))

        candidates.sort(key=lambda x: x[2])

        for candidate in candidates[:k]:
            q.put((candidate[0], candidate[1]))

    return None

# def and_or_graph_search(start, goal):
#     def or_search(state, path, goal):
#         if state == goal:
#             return []
#         if state in path:
#             return None
#         for new_state in generate_new_states(state):
#             if new_state in path:
#                 continue
#             plan = and_search([new_state], path + [state], goal)
#             if plan is not None:
#                 return [(state, plan)]
#         return None

#     def and_search(states, path, goal):
#         plans = []
#         for state in states:
#             plan = or_search(state, path, goal)
#             if plan is None:
#                 return None
#             plans.append((state, plan))
#         return plans

#     return or_search(start, [], goal)

def apply_moves(state, moves):
    current = state
    for move in moves:
        blank_x, blank_y = find_blank(current)
        dx, dy = move
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in current]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            current = tuple(tuple(row) for row in new_state)
    return current

def random_individual(length=30):
    return [random.choice(MOVES) for _ in range(length)]

def fitness(individual, start, goal):
    end_state = apply_moves(start, individual)
    return -manhattan(end_state, goal)  # càng gần goal thì điểm càng cao (âm manhattan)

def mutate(individual, mutation_rate=0.1):
    new_individual = individual[:]
    for i in range(len(new_individual)):
        if random.random() < mutation_rate:
            new_individual[i] = random.choice(MOVES)
    return new_individual

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + parent2[cut:]
    return child

def genetic_algorithm_solve(start, goal, population_size=100, generations=200, mutation_rate=0.1):
    population = [random_individual() for _ in range(population_size)]

    for gen in range(generations):
        scored_population = [(fitness(ind, start, goal), ind) for ind in population]
        scored_population.sort(reverse=True)

        parent1 = scored_population[0][1]
        parent2 = scored_population[1][1]

        child = crossover(parent1, parent2)

        child = mutate(child, mutation_rate)

        result_state = apply_moves(start, child)
        if result_state == goal:
            path = []
            temp_state = start
            for move in child:
                blank_x, blank_y = find_blank(temp_state)
                dx, dy = move
                new_x, new_y = blank_x + dx, blank_y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_state = [list(row) for row in temp_state]
                    new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
                    temp_state = tuple(tuple(row) for row in new_state)
                    path.append(temp_state)
            return path

        population = [mutate(crossover(parent1, parent2), mutation_rate) for _ in range(population_size)]

    return None