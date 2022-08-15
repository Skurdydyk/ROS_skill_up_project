# ROS_skill_up_project

Tasks

1. Add your robot (the one with ROS (Robot Operating System)) to the simulation (Gazebo or Isaac Sim). Any open-source simulation world could be used, or you can create your own.
2. Add lidar to the robot in simulation. Any lidar can be used (RPLidar A1 is ok)
3. Move robot inside simulation using lidar for navigation
4. Create ROS node (C++) to move the robot inside the simulation using specified points in the environment and avoid obstacles (at least one obstacle)
5. Write test to test robot behavior in simulation, e.g. if robot can avoid obstacles.

# Build and run app with docker compose
1. Build docker image noetic_desktop with Dockerfile
2. Execute command "xhost +" in your local terminal for access control disabled clients can connect from any host
3. Run docker compose command
- docker-compose -f docker-gmapping.yaml up (services: ros-master, spawn, gmapping)
- docker-compose -f docker-localization.yaml up (services: ros-master, spawn, localization)
- docker-compose -f docker-path-planning.yaml up (services: ros-master, spawn, path_planning)

# Run the following commands for a test control:
- roslaunch robot_project flat_map.launch (spawn the world)
- roslaunch robot_project spawn.launch (spawn the robot)
- rosrun teleop_twist_keyboard teleop_twist_keyboard.py (control)

# Run the following commands for a mapping:
- roslaunch robot_project gmapping.launch (spawn the world, running gmapping and rviz)
- roslaunch robot_project spawn.launch (spawn the robot)
- rosrun teleop_twist_keyboard teleop_twist_keyboard.py (control)

# Run the following commands for a localization
- roslaunch robot_project localization.launch (spawn the world, running map server with map, amcl, rviz)
- roslaunch robot_project spawn.launch (spawn the robot)
- rosrun teleop_twist_keyboard teleop_twist_keyboard.py (control)

# Run the following commands for a path planning:
- roslaunch robot_project path_planning.launch (spawn the world, running map server with map, amcl, rviz, move base, ekf)
- roslaunch robot_project spawn.launch (spawn the robot)

# Run the following command for checking correct avoid obstacles
- rostest robot_control avoid_obstacles_robot_integration_test.test --reuse-master