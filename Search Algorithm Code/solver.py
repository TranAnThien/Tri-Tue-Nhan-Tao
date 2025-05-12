import queue
import random
import math
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def count_inversions(state):
    flat_list = []
    for row in state:
        for tile in row:
            if tile != 0:
                flat_list.append(tile)

    inversion_count = 0
    list_len = len(flat_list)
    for i in range(list_len):
        for j in range(i + 1, list_len):
            if flat_list[i] > flat_list[j]:
                inversion_count += 1

    return inversion_count

def is_solvable(start_state, goal_state):
    start_inversions = count_inversions(start_state)
    goal_inversions = count_inversions(goal_state)

    return (start_inversions % 2) == (goal_inversions % 2)

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
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    q = queue.Queue()
    q.put((start, [start]))
    visited = set()
    visited.add(start)

    while not q.empty():
        current, path = q.get()
        node_count += 1
        if current == goal:
            return path, node_count

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                q.put((new_state, path + [new_state]))

    return None, node_count

def dfs_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        current, path = stack.pop()
        node_count += 1
        if current == goal:
            return path, node_count

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                stack.append((new_state, path + [new_state]))

    return None, node_count

def ucs_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    pq = queue.PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()
    visited.add(start)

    while not pq.empty():
        cost, current, path = pq.get()
        node_count += 1
        if current == goal:
            return path, node_count

        for new_state in generate_new_states(current):
            if new_state not in visited:
                visited.add(new_state)
                pq.put((cost + 1, new_state, path + [new_state]))

    return None, node_count

def ids_solve(start, goal):
    total_node = 0
    if not is_solvable(start, goal):
        return None, total_node
    depth = 0
    while True:
        result, node_count = depth_limited_search(start, goal, depth)
        total_node += node_count
        if result is not None:
            return result, total_node
        depth += 1

def depth_limited_search(start, goal, max_depth):
    q = queue.Queue()
    q.put((start, [start], 0))

    visited = set()
    node_count = 0

    while not q.empty():
        current, path, depth = q.get()
        node_count += 1

        if current == goal:
            return path, node_count

        if depth < max_depth:
            for new_state in generate_new_states(current):
                if new_state not in visited:
                    visited.add(new_state)
                    q.put((new_state, path + [new_state], depth + 1))

    return None, node_count


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
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    pq = queue.PriorityQueue()
    pq.put((manhattan(start, goal), start, [start]))
    visited = set()

    while not pq.empty():
        h, current, path = pq.get()
        node_count += 1

        if current == goal:
            return path, node_count

        if current in visited:
            continue
        visited.add(current)

        for new_state in generate_new_states(current):
            if new_state not in visited:
                pq.put((manhattan(new_state, goal), new_state, path + [new_state]))

    return None, node_count

def a_star_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    pq = queue.PriorityQueue()
    pq.put((manhattan(start, goal), 0, start, [start]))
    visited = {}

    while not pq.empty():
        f, g, current, path = pq.get()
        node_count += 1

        if current == goal:
            return path, node_count

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        for new_state in generate_new_states(current):
            new_g = g + 1
            new_f = new_g + manhattan(new_state, goal)
            pq.put((new_f, new_g, new_state, path + [new_state]))

    return None, node_count

def ida_star_solve(start, goal):
    total_node = 0
    if not is_solvable(start, goal):
        return None, total_node
    threshold = manhattan(start, goal)
    
    while True:
        q = queue.Queue()
        q.put((start, [start], 0))
        visited = set()
        min_threshold = float('inf')
        node_count = 0

        while not q.empty():
            current, path, g = q.get()
            node_count += 1
            f = g + manhattan(current, goal)

            if f > threshold:
                min_threshold = min(min_threshold, f)
                continue

            if current == goal:
                return path, total_node

            visited.add(current)

            for new_state in generate_new_states(current):
                if new_state not in visited:
                    q.put((new_state, path + [new_state], g + 1))

        total_node += node_count
        if min_threshold == float('inf'):
            return None, total_node

        threshold = min_threshold

def simple_hill_climbing_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count

    current = start
    path = [current]
    visited = set()
    visited.add(current)

    while current != goal:
        node_count += 1
        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        for new_state in generate_new_states(current):
            if new_state in visited:
                continue
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                best_manhattan = h
                best_state = new_state
                break

        if best_state:
            visited.add(best_state)
            current = best_state
            path.append(current)
        else:
            return None, node_count
    return path, node_count

def hill_climbing_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count

    current = start
    path = [current]
    visited = set()
    visited.add(current)

    while current != goal:
        node_count += 1
        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        for new_state in generate_new_states(current):
            if new_state in visited:
                continue
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                best_manhattan = h
                best_state = new_state

        if best_state:
            visited.add(best_state)
            current = best_state
            path.append(current)
        else:
            return None, node_count
    return path, node_count

def Stochastic_hill_climbing_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    
    current = start
    path = [current]
    visited = set()
    visited.add(current)

    while current != goal:
        node_count += 1
        current_manhattan = manhattan(current, goal)
        best_state = None
        best_manhattan = current_manhattan

        list_better_states = []
        for new_state in generate_new_states(current):
            h = manhattan(new_state, goal)
            if h < best_manhattan:
                list_better_states.append(new_state)

        if list_better_states:
            best_state = random.choice(list_better_states)
            visited.add(best_state)
            current = best_state
            path.append(current)
        else:
            return None, node_count

    return path, node_count

def Simulated_Annealing_solve(start, goal):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    current = start
    path = [current]
    T = pow(10, 4)
    alpha = 0.99

    while current != goal:
        node_count += 1
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
            path.append(best_state)
            current = best_state
        else:
            return None, node_count

    return path, node_count

def beam_search_solve(start, goal, k=2):
    node_count = 0
    if not is_solvable(start, goal):
        return None, node_count
    q = queue.Queue()

    if not isinstance(start, list):
        start = [start]

    for s in start:
        q.put((s, [s]))

    while not q.empty():
        candidates = []
        node_count += k

        for _ in range(min(k, q.qsize())):
            current, path = q.get()

            if current == goal:
                return path, node_count

            neighbors = generate_new_states(current)

            for state in neighbors:
                dist = manhattan(state, goal)
                candidates.append((state, path + [state], dist))

        candidates.sort(key=lambda x: x[2])

        for candidate in candidates[:k]:
            q.put((candidate[0], candidate[1]))

    return None, node_count

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
    return -manhattan(end_state, goal)

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
    if not is_solvable(start, goal):
        return None
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
            path = [start]
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

def and_or_graph_search(start, goal, max_depth=20):
    if not is_solvable(start, goal):
        return None
    def or_search(state, path, goal, visited, depth):
        if state == goal:
            return [state]
        if state in visited:
            return None
        if depth > max_depth:
            return None

        visited.add(state)

        for new_state in generate_new_states(state):
            if new_state in visited:
                continue

            plan = and_search([new_state], path + [state], goal, visited.copy(), depth + 1)
            if plan is not None:
                return [state] + plan[0]

        return None

    def and_search(states, path, goal, visited, depth):
        if depth > max_depth:
            return None
        plans = []
        for state in states:
            plan = or_search(state, path, goal, visited.copy(), depth)
            if plan is None:
                return None
            plans.append(plan)
        return plans

    return or_search(start, [], goal, set(), 0)

def generate_random_valid_state():
    nums = list(range(9))
    random.shuffle(nums)
    state = []
    for i in range(0, 9, 3):
        state.append(tuple(nums[i:i+3]))
    return tuple(state)


def no_observation_search(num_starts=3, num_goals=3):
    start_states = [generate_random_valid_state() for _ in range(num_starts)]
    goal_states = [generate_random_valid_state() for _ in range(num_goals)]
    results = []
    for goal in goal_states:
        path = []
        for start in start_states:
            if not is_solvable(start, goal):
                break
            found_path_for_this_goal, node = a_star_solve(start, goal)

            if found_path_for_this_goal is not None:
                path.append(found_path_for_this_goal)
            else:
                break
        
        if len(path) == num_starts:
            for i in range(num_starts):
                results.append({
                    'start': start_states[i],
                    'goal': goal,
                    'path': path[i]
                })
            break
    return results, start_states, goal_states

def generate_random_goal_state(goal):
    state = [list(row) for row in goal]
    nums = list(range(9))
    for i in range(3):
        for j in range(3):
            if goal[i][j] != 0:
                nums.remove(goal[i][j])
    if len(nums) > 0:
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0 and len(nums) > 0:
                    state[i][j] = nums.pop(0)
    return tuple(tuple(row) for row in state)


def partial_observation_search(goal_first, num_starts=3, num_goals=3):
    start_states = [generate_random_valid_state() for _ in range(num_starts)]
    goal_states = [generate_random_goal_state(goal_first) for _ in range(num_goals)]
    results = []
    for goal in goal_states:
        path = []
        for start in start_states:
            if not is_solvable(start, goal):
                break
            found_path_for_this_goal, node = a_star_solve(start, goal)

            if found_path_for_this_goal is not None:
                path.append(found_path_for_this_goal)
            else:
                break
        
        if len(path) == num_starts:
            for i in range(num_starts):
                results.append({
                    'start': start_states[i],
                    'goal': goal,
                    'path': path[i]
                })
            break
    return results, start_states, goal_states

def generate_and_test(goal):
    start = []
    results = []
    while True:
        start = generate_random_valid_state()
        path = []
        if not is_solvable(start, goal):
            results.append({
                    'start': start,
                    'goal': goal,
                    'path': path
                })
            continue

        path, node = a_star_solve(start, goal)
        results.append({
                    'start': start,
                    'goal': goal,
                    'path': path
                })
        if path is not None:
            return results

def backtracking_search(start_state, goal_state, max_depth=30):
    return recursive_backtracking(start_state, goal_state, [start_state], set(), max_depth)

def recursive_backtracking(current_state, goal_state, path, visited_in_path, max_depth):
    if current_state == goal_state:
        return path

    if len(path) > max_depth:
        return None
    visited_in_path.add(current_state)

    possible_next_states = generate_new_states(current_state)

    for next_state in possible_next_states:
        is_consistent_here = (next_state not in visited_in_path)

        if is_consistent_here:
            result_path = recursive_backtracking(
                next_state,
                goal_state,
                path + [next_state],
                visited_in_path,
                max_depth
            )
            if result_path is not None:
                return result_path

    visited_in_path.remove(current_state)
    return None

def ac3():
    domain = set(range(9))
    domains = [domain.copy() for _ in range(9)]
    results = []
        
    queue = deque()
    for i in range(9):
        for j in range(9):
            if i != j:
                queue.append((i, j))
    
    while queue:
        xi, xj = queue.popleft()

        xi_domain_before = list(domains[xi].copy())
        xj_domain_before = list(domains[xj].copy())

        revised = revise(domains, xi, xj)

        xi_domain_after = list(domains[xi].copy())
        xj_domain_after = list(domains[xj].copy())

        results.append({
            'arc_processed': (f'Ô {xi}', f'Ô {xj}'),
            'xi_domain_before': xi_domain_before,
            'xj_domain_before': xj_domain_before,
            'xi_domain_after_revise': xi_domain_after,
            'xj_domain_after_revise': xj_domain_after,
            'was_revised': revised
        })

        if revised:
            if not domains[xi]:
                return None, results
        
            for xk in range(len(domains)):
                if xk != xi and xk != xj:
                    if (xk, xi) not in queue: 
                        queue.append((xk, xi))
    
    return domains, results

def revise(current_domain, xi, xj):
    removed = False

    domain_xi_value = list(current_domain[xi])
    for x_val in domain_xi_value:
        found_support = False
        for y_val in current_domain[xj]:
            if x_val == y_val:
                continue
            if (xi > xj and x_val > y_val) or (xi < xj and x_val < y_val):
                found_support = True
                break

        if not found_support:
            current_domain[xi].remove(x_val)
            removed = True
    return removed