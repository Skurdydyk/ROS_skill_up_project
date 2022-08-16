#include <ros/ros.h>
#include <gtest/gtest.h>
#include "robot_project/move_robot.h"
#include <gazebo_msgs/GetModelState.h>

TEST(TestSuite, test_move_robot){
    float position_x;
    float position_y;

    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");

    gazebo_msgs::GetModelState gms;
    gms.request.model_name = "my_robot";

    MoveActionRobot robot;
    robot.send_goal(1, 0, 0, 0.2);

    ros::service::waitForService("/gazebo/get_model_state");

    if (client.call(gms)){
        position_x = gms.response.pose.position.x;
        position_y = gms.response.pose.position.y;

        ROS_INFO("x = %f ;", position_x);
        ROS_INFO("y = %f ;", position_y);
    }
    else{
        ROS_ERROR("Failed to call service /gazebo/get_model_state");
    }

    ASSERT_TRUE((0.5 <= position_x) && (position_x <= 0.6));
    ASSERT_TRUE((-0.05 <= position_y) && (position_y <= 0.05));
}


int main(int argc, char **argv){
    testing::InitGoogleTest(&argc, argv);
    ros::init(argc, argv, "navigation_goals");

    return RUN_ALL_TESTS();
}