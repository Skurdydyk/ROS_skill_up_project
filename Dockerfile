FROM osrf/ros:noetic-desktop-full

ENV DISPLAY=:1 \
    XAUTHORITY="/tmp/.docker.xauth" \
    net=host

RUN apt-get update &&  \
    apt-get install -y libsdl-image1.2-dev &&  \
    apt-get install libsdl-dev &&  \
    apt-get install -y git

RUN /bin/bash -c 'source ros_entrypoint.sh; \
    mkdir -p catkin_ws; \
    cd catkin_ws; \
    mkdir src; \
    catkin_make;'

RUN cd catkin_ws/src &&  \
    git clone https://github.com/Skurdydyk/teleop_twist_keyboard.git && \
    git clone https://github.com/Skurdydyk/navigation.git && \
    git clone https://github.com/Skurdydyk/slam_gmapping.git && \
    git clone https://github.com/Skurdydyk/openslam_gmapping.git && \
    git clone https://github.com/Skurdydyk/geometry2.git && \
    git clone https://github.com/Skurdydyk/navigation_msgs.git

COPY robot_project /catkin_ws/src/robot_project/

RUN /bin/bash -c 'source ros_entrypoint.sh;  \
    cd catkin_ws;  \
    catkin_make;\
    source devel/setup.bash;'