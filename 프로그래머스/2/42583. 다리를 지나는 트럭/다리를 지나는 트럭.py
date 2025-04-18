from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 1
    queue = deque([truck_weights[0]])
    wait_trucks = deque(truck_weights[1:])
    current_weight = truck_weights[0]
    current_length = 1
    while current_weight > 0:
        if wait_trucks:
            truck = wait_trucks[0]
            if current_length == bridge_length:
                w = queue.popleft()
                current_length -= 1
                current_weight -= w   
            
            if current_weight + truck <= weight:
                wait_trucks.popleft()
                queue.append(truck)
                current_length += 1
                current_weight += truck
            else:
                queue.append(0)
                current_length += 1
                current_weight += 0
        else:
            if current_length == bridge_length:
                w = queue.popleft()
                current_length -= 1
                current_weight -= w 
            queue.append(0)
            current_length += 1
            current_weight += 0
        time += 1
    return time