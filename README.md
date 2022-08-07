# ROS_skill_up_project

Tasks

1. Add your robot (the one with ROS (Robot Operating System)) to the simulation (Gazebo or Isaac Sim). Any open-source simulation world could be used, or you can create your own.
2. Add lidar to the robot in simulation. Any lidar can be used (RPLidar A1 is ok)
3. Move robot inside simulation using lidar for navigation
4. Create ROS node (C++) to move the robot inside the simulation using specified points in the environment and avoid obstacles (at least one obstacle)
5. Write test to test robot behavior in simulation, e.g. if robot can avoid obstacles.

# Build and run app with docker compose
1. Build docker image noetic_desktop with Dockerfile

2. Run docker compose command
- docker-compose -f docker-gmapping.yaml up (services: ros-master, gmapping, spawn_robot, amcl, flat_map)
- docker-compose -f docker-path-planning.yaml up (services: ros-master, spawn_robot, amcl_world_map)

# Run the following commands for a test control:
- roslaunch robot_project flat_map.launch (spawn the world)
- roslaunch robot_project spawn.launch (spawn the robot, run rviz)

# Run the following commands for a mapping:
- roslaunch robot_project gmapping.launch (spawn the world, run slam gmapping)
- roslaunch robot_project spawn.launch (spawn the robot, run rviz)

# Run the following commands for a localization and path planning run:
- roslaunch robot_project path_planning.launch (spawn the world, run path planning, amcl, map saver)
- roslaunch robot_project spawn.launch (spawn the robot, run rviz)

Git sources with packages for the project:
1) openslam_gmapping - https://github.com/ros-perception/openslam_gmapping.git
2) gmapping - https://github.com/ros-perception/slam_gmapping.git
3) amcl, map_saver, base_local_planner, dwa_local_planner, global_planner, carrot_planner, move_base, costmap_2d, voxel_grid, nav_core, navfn, rotate_recovery, clear_costmap_recovery - https://github.com/ros-planning/navigation.git
4) tf2_sensor_msgs - https://github.com/ros/geometry2.git
5) move_base_msgs - https://github.com/ros-planning/navigation_msgs.git