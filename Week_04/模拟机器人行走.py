class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #方向字典： 当为up时，0表示横坐标，1表纵坐标移动，"left"表左转后的方向，"right"表右转后的方向
        dir_map = {"up":[0, 1, "left", "right"],
                    "down":[0, -1, "right","left"],
                    "left":[-1, 0, "down", "up"],
                    "right":[1, 0, "up", "down"]}
        res, (x, y),dir_cur = 0, (0, 0), "up"
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:
                for i in range(command):
                    if (x+dir_map[dir_cur][0], y+ dir_map[dir_cur][1]) in obstacles: break
                    x+=dir_map[dir_cur][0]
                    y+=dir_map[dir_cur][1]
                res = max(res, x*x + y*y)
                
            elif command == -1:
                dir_cur = dir_map[dir_cur][3]
            elif command == -2:
                dir_cur = dir_map[dir_cur][2]
        return res