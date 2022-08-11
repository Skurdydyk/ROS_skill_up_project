#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>


class MoveActionRobot{
    typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;
    public:
        // tell the action client that we want to spin a thread by default
        MoveActionRobot() : client("move_base", true){
            ROS_INFO("Waiting for action server to start.");
            client.waitForServer();
            ROS_INFO("Action server started, sending goal.");
        }

        int number_goal = 1;
        move_base_msgs::MoveBaseGoal goal;

        void send_goal(float position_x, float position_y, float orientation_z, float orientation_w){
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
            ROS_INFO("Finished goal %i", number_goal);

            number_goal += 1;
        }

   private:
     MoveBaseClient client;
};

int main(int argc, char** argv){
    ros::init(argc, argv, "simple_navigation_goals");
    MoveActionRobot robot;

//    robot.send_goal(3, -1, -0.03, 1);
//    robot.send_goal(7.4, -7.8, -0.11, 0.99);
    robot.send_goal(-0.46, 7.5, 1, 1);

    ROS_INFO("Finished sending goals!");

    return 0;
}