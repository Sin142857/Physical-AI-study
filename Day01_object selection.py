"""Physical AI Boot Camp Day 1

학습 내용: Dictionary + 객체 선택
"""

objects = [
    {"name": "red_block", "x": 30, "y": 40},
    {"name": "blue_block", "x": 70, "y": 80},
    {"name": "green_block", "x": 50, "y": 20},
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
    print("선택한 객체:", command)
    print("객체의 X 좌표:", object_x)
    print("객체의 Y 좌표:", object_y)
else:
    print("명령한 객체를 찾지 못했습니다:", command)
