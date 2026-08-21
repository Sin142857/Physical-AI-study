"""Physical AI Boot Camp Day 2

학습 내용: 작업공간 안전범위 검사
"""


def is_in_workspace(x, y):
    x_min = 0
    x_max = 100
    y_min = 0
    y_max = 100

    return x_min <= x <= x_max and y_min <= y <= y_max


objects = [
    {"name": "red_block", "x": 30, "y": 40},
    {"name": "blue_block", "x": 120, "y": 50},
]

command = "blue_block"
found = False

for obj in objects:
    if obj["name"] == command:
        object_x = obj["x"]
        object_y = obj["y"]
        found = True
        break

if found:
    safe = is_in_workspace(object_x, object_y)

    print("선택한 객체:", command)
    print("객체 좌표:", object_x, object_y)

    if safe:
        print("안전한 좌표입니다. 이동을 시작합니다.")
    else:
        print("작업공간 밖의 좌표입니다. 이동을 차단합니다.")
else:
    print("명령한 객체를 찾지 못했습니다:", command)
