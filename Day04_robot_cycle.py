"""(이전내용 실습) 1단계"""

objects = [
    {"name": "red_block", "x": 30, "y": 40},
    {"name": "blue_block", "x": 120, "y": 50},
]


def find_object(objects, command):
    for obj in objects:
        if obj["name"] == command:
            return obj
    return None


target = find_object(objects, "red_block")
print(target)

"""2단계 경계값 0과 100도 안전범위에 포함 """


def is_in_workspace(x, y):
    x_min, x_max = 0, 100
    y_min, y_max = 0, 100

    if x_min <= x <= x_max and y_min <= y <= y_max:
        return True
    return False


print(is_in_workspace(30, 40))  # True
print(is_in_workspace(120, 50))  # False
print(is_in_workspace(0, 100))  # True

"""3단계"""


def create_move_command(obj):
    if is_in_workspace(obj["x"], obj["y"]):
        return {"action": "move", "x": obj["x"], "y": obj["y"]}
    return None


safe_object = {"name": "red_block", "x": 30, "y": 40}
unsafe_object = {"name": "blue_block", "x": 120, "y": 50}

print(create_move_command(safe_object))
print(create_move_command(unsafe_object))

"""4단계-함수 통합"""


def run_robot_once(objects, command):
    target = find_object(objects, command)

    if target is None:
        return {"status": "not_found", "command": None}

    move_command = create_move_command(target)

    if move_command is None:
        return {"status": "unsafe", "command": None}

    return {"status": "success", "command": move_command}


objects = [
    {"name": "red_block", "x": 30, "y": 40},
    {"name": "blue_block", "x": 120, "y": 50},
]

print(run_robot_once(objects, "red_block"))
print(run_robot_once(objects, "green_block"))
print(run_robot_once(objects, "blue_block"))

# 여러번 스캔하며 재시도하기
scans = [
    [{"name": "red_block", "x": 30, "y": 40}],
    [{"name": "blue_block", "x": 120, "y": 50}],
    [{"name": "blue_block", "x": 70, "y": 50}],
]


def run_robot_cycle(scans, command, max_retries):
    attempt = 0

    while attempt < max_retries and attempt < len(scans):
        objects = scans[attempt]
        result = run_robot_once(objects, command)

        print(f"{attempt + 1}차 시도:", result["status"])

        if result["status"] == "success":
            return result
        attempt = attempt + 1
    return {"status": "failed", "command": None}


scans = [
    [{"name": "red_block", "x": 30, "y": 40}],
    [{"name": "blue_block", "x": 120, "y": 50}],
    [{"name": "blue_block", "x": 70, "y": 50}],
]

result = run_robot_cycle(scans, "blue_block", 3)
print("최종 결과:", result)

result = run_robot_cycle(scans, "blue_block", 2)
print("최종 결과:", result)
