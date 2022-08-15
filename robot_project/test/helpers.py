import rospy
import rospkg
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from gazebo_msgs.srv import GetModelState, SpawnModel
from geometry_msgs.msg import Pose


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


def spawn_model(model_name):
    try:
        initial_pose = Pose()
        initial_pose.position.x = 3
        initial_pose.position.y = 0
        initial_pose.position.z = 0.2

        package_path = rospkg.RosPack().get_path("robot_project")

        with open(f'{package_path}/models/{model_name}/model.sdf', 'r') as xml_file:
            model_xml = xml_file.read().replace('\n', '')

        spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
        spawn_model_prox(model_name, model_xml, '', initial_pose, 'world')
    except rospy.ServiceException as e:
        rospy.logwarn('Spawn Model service call failed: {0}'.format(e))


def get_model_position(model_name):
    resp_coordinates = None

    try:
        model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp_coordinates = model_coordinates(model_name, '')
    except rospy.ServiceException as e:
        rospy.logwarn('Get Model State service call failed: {0}'.format(e))

    return resp_coordinates
