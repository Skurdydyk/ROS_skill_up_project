import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib


def feedback_callback(feedback):
    print("[Feedback] Going to Goal Pose...")


def send_goal(pos_x, pos_y, pos_z, orient_w):
    # create the connection to the action server
    client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
    rospy.logwarn('wait_for_server "move_base"')
    client.wait_for_server()

    # creates a goal to send to the action server
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.pose.position.x = pos_x
    goal.target_pose.pose.position.y = pos_y
    goal.target_pose.pose.position.z = pos_z
    goal.target_pose.pose.orientation.w = orient_w

    # sends the goal to the action server, specifying which feedback function
    # to call when feedback received
    rospy.logwarn("send_goal")
    client.send_goal(goal, feedback_cb=feedback_callback)

    rospy.logwarn("wait_for_result")
    client.wait_for_result()

    rospy.logwarn("[Result] State: %d" % (client.get_state()))
