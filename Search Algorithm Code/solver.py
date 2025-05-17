import queue
import random
import math
import time
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

        while not q.empty():
            current, path, g = q.get()
            total_node += 1
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

        for _ in range(min(k, q.qsize())):
            current, path = q.get()
            node_count += 1

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

def and_or_graph_search(start, goal, max_depth=30):
    visited = {}

    def or_search(state, path, depth):

        if state == goal:
            return [state]

        if state in path:
            return None

        if depth > max_depth:
            return None

        if state in visited:
            return visited[state]

        new_path = path + [state]
        
        action_deltas = get_possible_actions(state)

        for delta in action_deltas:
            state_single = apply_moves(state, [delta])

            action_deltas_next = get_possible_actions(state_single)
            while True:
                state_double = apply_moves(state_single, [random.choice(action_deltas_next)])
                if state_double != state:
                    break
            
            if random.random() < 0.7:
                outcomes = [state_single]
            else:
                outcomes = [state_single, state_double]
            
            plans_from_and = and_search(outcomes, new_path, depth + 1)

            if plans_from_and is not None:
                path_ok = plans_from_and[0]
                
                current_plan = [state] + path_ok
                visited[state] = current_plan
                return current_plan
        
        visited[state] = None 
        return None

    def and_search(states, path, depth):
        plans = []
        for i, s_outcome in enumerate(states):
            plan_for_outcome = or_search(s_outcome, path, depth) 
            
            if plan_for_outcome is None:
                return None
            plans.append(plan_for_outcome)
        
        return plans
    
    
    result_path_of_tuples = or_search(start, [], 0)
    if result_path_of_tuples:
        return [list(map(list, s_tuple)) for s_tuple in result_path_of_tuples]
    
    return None

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
    i = 0
    while True:
        i += 1
        print(i)
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

def backtracking():
    variables = 9
    domains = [list(range(9)) for _ in range(variables)]
    assignment = []
    trace_log = []

    def is_valid(assignment, value):
        if value in assignment:
            return False
        if assignment:
            if value >= assignment[-1]:
                return False
        return True

    def backtrack():
        idx = len(assignment)
        if idx == variables:
            return assignment.copy()

        for value in domains[idx]:
            trace_log.append(f"Xét ô {idx}: Giá trị {value} ")
            if is_valid(assignment, value):
                trace_log[-1] += "✔ hợp lệ"
                assignment.append(value)

                result = backtrack()
                if result is not None:
                    return result

                trace_log.append(f"⤴️ Không có giá trị hợp lệ ở ô {idx + 1} → Quay lui")
                assignment.pop()
            else:
                trace_log[-1] += "❌ không hợp lệ"

        return None

    solution = backtrack()
    return solution, trace_log

def constraint(constraint_type, xi_val, xj_val, xi_idx, xj_idx):
    if constraint_type == "increasing":
        return (xi_idx < xj_idx and xi_val < xj_val) or (xi_idx > xj_idx and xi_val > xj_val)
    elif constraint_type == "sum":
        return xi_val + xj_val >= (xi_idx + xj_idx)

def ac3(constraint_type):
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

        revised = revise(domains, xi, xj, constraint_type)

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

def revise(current_domain, xi, xj, constraint_type):
    removed = False

    domain_xi_value = list(current_domain[xi])
    for x_val in domain_xi_value:
        found_support = False
        for y_val in current_domain[xj]:
            if x_val == y_val:
                continue
            if constraint(constraint_type, x_val, y_val, xi, xj):
                found_support = True
                break

        if not found_support:
            current_domain[xi].remove(x_val)
            removed = True
    return removed

def get_possible_actions(state_tuple):
    actions = []
    blank_r, blank_c = find_blank(state_tuple)

    potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in potential_moves:
        new_blank_r, new_blank_c = blank_r + dr, blank_c + dc
        if 0 <= new_blank_r < 3 and 0 <= new_blank_c < 3:
            actions.append((dr, dc))
    return actions

def choose_q_learning_action(state, current_q_table, epsilon):
    """
    Chọn một hành động sử dụng chiến lược epsilon-greedy.
    current_q_table là một dict thông thường.
    """
    possible_actions = get_possible_actions(state)
    if not possible_actions:
        return None

    if random.random() < epsilon:
        return random.choice(possible_actions)
    else:
        if state not in current_q_table:
            return random.choice(possible_actions)

        q_values_for_state = current_q_table[state]

        max_q = -float('inf')
        best_actions = []
        for action in possible_actions:
            q_val = q_values_for_state.get(action, 0.0) 
            if q_val > max_q:
                max_q = q_val
                best_actions = [action]
            elif q_val == max_q:
                best_actions.append(action)

        return random.choice(best_actions) if best_actions else random.choice(possible_actions)

def q_learning_train(start_config_state, goal_state, q_table_to_train,
                       num_episodes=20000,
                       alpha=0.1, gamma=0.95,
                       initial_epsilon=1.0, epsilon_decay=0.99995,
                       min_epsilon=0.01,
                       max_steps_per_episode=1000):
    """
    Huấn luyện tác tử Q-learning.
    q_table_to_train là một dict thông thường {} được truyền vào.
    """
    current_q_table = q_table_to_train 
    epsilon = initial_epsilon
    

    for episode in range(num_episodes):
        current_state = start_config_state
        episode_path_length = 0

        for step in range(max_steps_per_episode):
            action = choose_q_learning_action(current_state, current_q_table, epsilon)
            if action is None: 
                break

            next_state = apply_moves(current_state, [action])
            episode_path_length +=1

            reward = -1  
            if next_state == goal_state:
                reward = 100  
            
            if current_state not in current_q_table:
                current_q_table[current_state] = {}
            old_q_value = current_q_table[current_state].get(action, 0.0)
            
            max_future_q = 0.0
            if next_state != goal_state:
                next_possible_actions = get_possible_actions(next_state)
                if next_possible_actions:
                    if next_state in current_q_table:
                        q_values_for_next_state_dict = current_q_table[next_state]
                        action_qs = [q_values_for_next_state_dict.get(next_act, 0.0) for next_act in next_possible_actions]
                        if action_qs: 
                           max_future_q = max(action_qs)

            
            new_q_value = old_q_value + alpha * (reward + gamma * max_future_q - old_q_value)
            
            current_q_table[current_state][action] = new_q_value

            current_state = next_state
            if current_state == goal_state:
                break
        
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        
        if (episode + 1) % (max(1, num_episodes // 20)) == 0 or episode == num_episodes - 1:
            status = "Đạt đích" if current_state == goal_state else "Chưa đạt đích"
            print(f"Q-Train Episode {episode + 1}/{num_episodes}. Epsilon: {epsilon:.4f}. Độ dài path: {episode_path_length}. {status}")
            
    return current_q_table

def q_learning_get_path(start_state, goal_state, trained_q_table, max_path_length=100):
    """
    Trích xuất đường đi từ Q-table (dict thông thường) đã huấn luyện.
    (Nội dung hàm này không thay đổi nhiều vì đã sử dụng .get() hợp lý)
    """
    current_state = start_state
    path = [current_state]
    steps_taken = 0

    for _ in range(max_path_length):
        steps_taken += 1
        if current_state == goal_state:
            return path, steps_taken

        possible_actions = get_possible_actions(current_state)
        if not possible_actions:
            return None, steps_taken 

        q_values_for_state_dict = trained_q_table.get(current_state) 
        if not q_values_for_state_dict: 
            return None, steps_taken 

        best_q_value = -float('inf')
        best_actions = []
        for action in possible_actions:
            action_q_value = q_values_for_state_dict.get(action, -float('inf')) 
            if action_q_value > best_q_value:
                best_q_value = action_q_value
                best_actions = [action]
            elif action_q_value == best_q_value:
                best_actions.append(action)
        
        if not best_actions: 
            return None, steps_taken
        
        chosen_action = random.choice(best_actions)
        next_state_candidate = apply_moves(current_state, [chosen_action])

        if next_state_candidate in path:
            alternative_good_actions = []
            for alt_action in best_actions:
                if alt_action == chosen_action:
                    continue
                alt_next_state = apply_moves(current_state, [alt_action])
                if alt_next_state not in path:
                    alternative_good_actions.append(alt_action)
            
            if alternative_good_actions:
                chosen_action = random.choice(alternative_good_actions)
                next_state = apply_moves(current_state, [chosen_action])
            else:
                return None, steps_taken 
        else:
            next_state = next_state_candidate
            
        path.append(next_state)
        current_state = next_state

    return None, steps_taken

def q_learning(start_state, goal_state,
                     num_episodes=20000, 
                     alpha=0.1, 
                     gamma=0.95,
                     initial_epsilon=1.0, 
                     epsilon_decay=0.99995,
                     min_epsilon=0.01,
                     max_steps_per_episode=1000,
                     max_path_length_eval=50):
    """
    Giải quyết 8-puzzle bằng Q-learning, sử dụng dict thông thường cho Q-table.
    """
    if not is_solvable(start_state, goal_state): 
        print("Puzzle không thể giải được.")
        return None, 0

    q_table = {}

    print(f"Bắt đầu Q-learning với các tham số: episodes={num_episodes}, alpha={alpha}, gamma={gamma}, epsilon_init={initial_epsilon}")

    trained_q_table = q_learning_train(
        start_config_state=start_state, 
        goal_state=goal_state,
        q_table_to_train=q_table,
        num_episodes=num_episodes, 
        alpha=alpha, 
        gamma=gamma,
        initial_epsilon=initial_epsilon, 
        epsilon_decay=epsilon_decay,
        min_epsilon=min_epsilon,
        max_steps_per_episode=max_steps_per_episode
    )
    
    training_duration_msg = f"Huấn luyện Q-learning hoàn tất. Kích thước Q-table: {len(trained_q_table)} trạng thái."
    print(training_duration_msg)
    print("Đang trích xuất đường đi từ Q-table...")
    path, node_count = q_learning_get_path(start_state, goal_state, trained_q_table, max_path_length=max_path_length_eval)

    if path:
        print(f"Tìm thấy đường đi bằng Q-learning với {len(path)-1} bước di chuyển.")
    else:
        print("Không thể tìm thấy đường đi bằng Q-table đã học trong các ràng buộc đã cho.")
    
    return path