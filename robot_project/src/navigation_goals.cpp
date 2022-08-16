#include <ros/ros.h>
#include "robot_project/move_robot.h"


int main(int argc, char** argv){
    ros::init(argc, argv, "navigation_goals");
    MoveActionRobot robot;

    robot.send_goal(3, -1, -0.03, 1);

    ros::Duration(0.5).sleep();
    robot.send_goal(7.4, -7.8, -0.5, 0.8);

    ros::Duration(0.5).sleep();
    robot.send_goal(5, 6.8, 0.97, 0.2);

    ROS_INFO("Finished sending goals!");

    return 0;
}