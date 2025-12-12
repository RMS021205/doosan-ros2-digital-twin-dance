## 프로젝트명
**ROS2 기반 두산 로봇팔 디지털 트윈(RViz)–실로봇 연동 제어**

## 프로젝트 설명
RViz2에서 두산 로봇팔 모델을 시각화하고, 동일한 ROS2(Humble) 환경에서 Doosan DSR API(`posj`, `movej`)를 사용해 **실제 두산 로봇팔**에 관절 기반 동작(댄스 시퀀스)을 전송·실행하는 디지털 트윈 연동 제어 프로젝트입니다.

## 기술 스택
- **OS**: Ubuntu 22.04
- **Middleware**: ROS2 Humble
- **Language**: Python (`rclpy`)
- **Robot SDK/Packages**: Doosan ROS2 (`doosan-robot2`, DSR API)
- **Visualization**: RViz2
- **Simulation (Virtual Mode)**: Docker Emulator
