from collections import defaultdict
def solution(points, routes):
    answer = 0
    R = len(routes)
    paths = [[] for _ in range(R)]
    
    def calc_path(path, s_point, e_point):
        pos = s_point[::]
        t = tuple(pos)
        if not path or (path and path[-1] != t):
            path.append(t)
        while pos != e_point:
            x_diff, y_diff = pos[0] - e_point[0], pos[1] - e_point[1]
            if x_diff != 0:
                pos[0] += 1 if x_diff < 0 else -1
                path.append(tuple(pos))
            elif y_diff != 0:
                pos[1] += 1 if y_diff < 0 else -1
                path.append(tuple(pos))
    
    for robot_i, path in enumerate(paths):
        route = routes[robot_i]
        for i in range(len(route)-1):
            s_point, e_point = points[route[i]-1], points[route[i+1]-1]
            calc_path(path, s_point, e_point)

    mmax = max([len(x) for x in paths])
    for i in range(mmax):
        d = defaultdict(int)
        for robot_i in range(R):
            path = paths[robot_i]
            if i >= len(path):
                continue    
            d[path[i]] += 1
        
        for x in d.values():
            if x > 1:
                answer += 1
    
    return answer