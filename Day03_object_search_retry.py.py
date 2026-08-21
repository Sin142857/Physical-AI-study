objects = [
    {"name": "red_block", "x": 120, "y": 80},
    {"name": "blue_block", "x": 420, "y": 180},
    {"name": "green_block", "x": 550, "y": 200},
]

command = "blue_block"


retry = 0
found = False

while retry < 3:
    print("물체 탐색")
    retry = retry + 1
    for obj in objects:
        if obj["name"] == command:
            target_x = obj["x"]
            target_y = obj["y"]
            found = True
            break

if found:
    print("목표 발견")
else:
    print("탐색 실패")


# 실제 Physical AI에서 로직 유추
while retry < 3 and not found:

    # objects = get_objects_from_camera()   # 새로 관찰

    for obj in objects:
        if obj["name"] == command:
            target_x = obj["x"]
            target_y = obj["y"]
            found = True
            break

    retry = retry + 1

# 최종 다시 점검
retry = 0
found = False
command = "blue_block"

scans = [
    [{"name": "red_block", "x": 120, "y": 80}],
    [{"name": "red_block", "x": 125, "y": 82}],
    [{"name": "blue_block", "x": 420, "y": 180}],
]

while retry < 3 and not found:
    objects = scans[retry]
    retry = retry + 1

    for obj in objects:
        if obj["name"] == command:
            target_x = obj["x"]
            target_y = obj["y"]
            found = True
            break

if found:
    print("목표 발견")
    print(target_x, target_y)
else:
    print("탐색 실패")


#### 재탐색 → 목표 발견 → 안전범위 검사 → 이동 허용/차단 ###
retry = 0
found = False
command = "blue_block"

x_min = 0
x_max = 500
y_min = 0
y_max = 300

scans = [
    [{"name": "red_block", "x": 120, "y": 80}],
    [
        {"name": "red_block", "x": 125, "y": 82},
        {"name": "blue_block", "x": 420, "y": 180},
    ],
    [{"name": "green_block", "x": 300, "y": 150}],
]


def is_in_workspace(x, y):
    if x_min <= x <= x_max and y_min <= y <= y_max:
        return True
    else:
        return False


while retry < 3 and not found:
    objects = scans[retry]
    retry = retry + 1
    for obj in objects:
        if obj["name"] == command:
            target_x = obj["x"]
            target_y = obj["y"]
            found = True
            break

if found:
    safe = is_in_workspace(target_x, target_y)
    if safe:
        print("목표 발견")
        print("이동 시작")
    else:
        print("목표 발견")
        print("이동 금지")

else:
    print("탐색 실패")
