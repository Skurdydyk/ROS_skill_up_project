#ifndef MOVE_ACTION_ROBOT_H
#define MOVE_ACTION_ROBOT_H

#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>

class MoveActionRobot{
    typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;
    public:
        MoveActionRobot();
        static int number_goal;
        move_base_msgs::MoveBaseGoal goal;

        void send_goal(float position_x, float position_y, float orientation_z, float orientation_w);
   private:
     MoveBaseClient client;
};

#endif