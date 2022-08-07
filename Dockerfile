FROM osrf/ros:noetic-desktop-full

ENV DISPLAY=:1 \
    XAUTHORITY="/tmp/.docker.xauth" \
    net=host

RUN  apt-get update && echo y|apt-get install libsdl-image1.2-dev && apt-get install libsdl-dev

RUN /bin/bash -c 'source ros_entrypoint.sh; \
    mkdir -p catkin_ws; \
    cd catkin_ws; \
    mkdir src; \
    catkin_make;'

COPY robot_project /catkin_ws/src/robot_project/
COPY amcl /catkin_ws/src/amcl/
COPY openslam_gmapping /catkin_ws/src/openslam_gmapping/
COPY gmapping /catkin_ws/src/gmapping/
COPY roslib /catkin_ws/src/roslib/
COPY map_server /catkin_ws/src/map_server/
COPY move_base /catkin_ws/src/move_base/
COPY teleop_twist_keyboard /catkin_ws/src/teleop_twist_keyboard/

COPY base_local_planner /catkin_ws/src/base_local_planner/
COPY global_planner /catkin_ws/src/global_planner/
COPY dwa_local_planner /catkin_ws/src/dwa_local_planner/
COPY carrot_planner /catkin_ws/src/carrot_planner/

#COPY teb_local_planner /catkin_ws/src/teb_local_planner/
#COPY mbf_msgs /catkin_ws/src/mbf_msgs/
#COPY mbf_utility /catkin_ws/src/mbf_utility/
#COPY mbf_abstract_core /catkin_ws/src/mbf_abstract_core/
#COPY mbf_costmap_core /catkin_ws/src/mbf_costmap_core/
#COPY costmap_converter /catkin_ws/src/costmap_converter/

COPY costmap_2d /catkin_ws/src/costmap_2d/
COPY tf2_sensor_msgs /catkin_ws/src/tf2_sensor_msgs/
COPY voxel_grid /catkin_ws/src/voxel_grid/
COPY nav_core /catkin_ws/src/nav_core/
COPY navfn /catkin_ws/src/navfn/
COPY clear_costmap_recovery /catkin_ws/src/clear_costmap_recovery/
COPY rotate_recovery /catkin_ws/src/rotate_recovery/
COPY move_base_msgs /catkin_ws/src/move_base_msgs/


RUN /bin/bash -c 'source ros_entrypoint.sh;  \
    cd catkin_ws;  \
    catkin_make;\
    source devel/setup.bash;'
