#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include "robot_project/move_robot.h"

MoveActionRobot::MoveActionRobot() : client("move_base", true){
    ROS_INFO("Waiting for action server to start.");
    client.waitForServer();
    ROS_INFO("Action server started, sending goal.");
}

int MoveActionRobot::number_goal = 1;

void MoveActionRobot::send_goal(float position_x, float position_y, float orientation_z, float orientation_w){
    // setting params for the goal
    goal.target_pose.header.frame_id = "map";
    goal.target_pose.pose.position.x = position_x;
    goal.target_pose.pose.position.y = position_y;
    goal.target_pose.pose.orientation.z = orientation_z;
    goal.target_pose.pose.orientation.w = orientation_w;

    ROS_INFO("Sending goal %i", number_goal);
    // send the goal with params
    client.sendGoal(goal);
    // waiting for the robot to reach the goal
    ROS_INFO("Waiting for result");
    client.waitForResult();

    if(client.getState() == actionlib::SimpleClientGoalState::SUCCEEDED){
        ROS_INFO("Finished goal %i!", number_goal);
    }
    else{
        ROS_INFO("Something went wrong!");
    }

    number_goal += 1;
}


int main(int argc, char** argv){
    return 0;
}