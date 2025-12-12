import rclpy
import DR_init
improt sys

def dance(movej, posj, loops=2):
    # 기본 포즈 
    home = [0, 0, 90, 0, 90, 0]

    # 1) 좌우 흔들기(waist/shoulder 느낌) 
    sway = [
        [ 20,   0,  90,  0,  90,  0],
        [-20,   0,  90,  0,  90,  0],
        [ 15,   0,  90,  0,  90,  0],
        [-15,   0,  90,  0,  90,  0],
        [  0,   0,  90,  0,  90,  0],
    ]

    # 2) 끄덕/펌프(팔꿈치/어깨) 
    pump = [
        [0, -20,  80,  0,  90,  0],
        [0,  10, 100,  0,  90,  0],
        [0, -15,  85,  0,  90,  0],
        [0,  15,  95,  0,  90,  0],
        [0,   0,  90,  0,  90,  0],
    ]

    # 3) 손목 트위스트(마지막 6축 살짝) 
    twist = [
        [0, 0, 90, 0, 90,  30],
        [0, 0, 90, 0, 90, -30],
        [0, 0, 90, 0, 90,  20],
        [0, 0, 90, 0, 90, -20],
        [0, 0, 90, 0, 90,   0],
    ]

    # 안전하게 홈으로 한번 가고 시작
    movej(posj(*home), vel=10, acc=80)

    for _ in range(loops):
        # sway
        for j in sway:
            movej(posj(*j), vel=20, acc=120)

        # pump
        for j in pump:
            movej(posj(*j), vel=18, acc=140)

        # twist
        for j in twist:
            movej(posj(*j), vel=15, acc=100)

    # 엔딩 포즈
    ending = [0, -10, 95, 0, 90, 0]
    movej(posj(*ending), vel=10, acc=80)
    movej(posj(*home), vel=10, acc=80)


def main(args=None):
    rclpy.init(args=args)

    ROBOT_ID = "dsr01"
    ROBOT_MODEL = "m1013"

    DR_init.__dsr__id = ROBOT_ID
    DR_init.__dsr__model = ROBOT_MODEL

    node = rclpy.create_node("dance_node", namespace=ROBOT_ID)
    DR_init.__dsr__node = node

    from DSR_ROBOT2 import movej, posj, set_robot_mode, ROBOT_MODE_AUTONOMOUS
    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    dance(movej, posj, loops=3)

    print("Dance complete")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
