# ROS_skill_up_project

Tasks

1. Add your robot (the one with ROS (Robot Operating System)) to the simulation (Gazebo or Isaac Sim). Any open-source simulation world could be used, or you can create your own.
2. Add lidar to the robot in simulation. Any lidar can be used (RPLidar A1 is ok)
3. Move robot inside simulation using lidar for navigation
4. Create ROS node (C++) to move the robot inside the simulation using specified points in the environment and avoid obstacles (at least one obstacle)
5. Write test to test robot behavior in simulation, e.g. if robot can avoid obstacles.

# Run the following commands for a test run:

- roslaunch robot_project flat_map.launch (spawn the world)
- roslaunch robot_project spawn.launch (spawn the robot)

Git sources with packages for the project:
1) openslam_gmapping - https://github.com/ros-perception/openslam_gmapping.git
2) gmapping - https://github.com/ros-perception/slam_gmapping.git