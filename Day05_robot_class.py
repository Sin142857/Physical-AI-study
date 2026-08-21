"""
1단계 — 클래스와 객체
쉽게 비유하면:
- 클래스: 로봇을 만드는 설계도
- 객체: 설계도로 실제 생성한 개별 로봇
- 속성: 로봇이 기억하는 이름과 좌표
- 메서드: 로봇이 수행할 수 있는 행동


# Step.1
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


robot1 = Robot("robot_A", 30, 40)
robot2 = Robot("robot_B", 70, 80)
print(robot1.name, robot1.x, robot1.y)
print(robot2.name, robot2.x, robot2.y)



# Step.2
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def is_in_workspace(self):
        x_min, x_max = 0, 100
        y_min, y_max = 0, 100

        return x_min <= self.x <= x_max and y_min <= self.y <= y_max


robot1 = Robot("robot_A", 30, 40)
robot2 = Robot("robot_B", 120, 80)

print(robot1.is_in_workspace())
print(robot2.is_in_workspace())


# Step3
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def is_in_workspace(self, x, y):
        return 0 <= x <= 100 and 0 <= y <= 100

    def move_to(self, new_x, new_y):
        if self.is_in_workspace(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return {"status": "success", "x": self.x, "y": self.y}
        return {"status": "unsafe", "x": self.x, "y": self.y}


robot = Robot("robot_A", 10, 20)

print(robot.move_to(30, 40))
print(robot.move_to(120, 50))
print("최종 위치:", robot.x, robot.y)
"""


# Step.4
class Robot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.status = "ready"

    def is_in_workspace(self, x, y):
        return 0 <= x <= 100 and 0 <= y <= 100

    def move_to(self, new_x, new_y):
        if self.is_in_workspace(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.status = "success"

            return {"status": self.status, "x": self.x, "y": self.y}

        self.status = "unsafe"

        return {"status": self.status, "x": self.x, "y": self.y}


robot1 = Robot("robot_A", 10, 20)
robot2 = Robot("robot_B", 50, 60)

robot1.move_to(30, 40)
robot2.move_to(120, 50)

print(robot1.name, robot1.x, robot1.y, robot1.status)
print(robot2.name, robot2.x, robot2.y, robot2.status)
