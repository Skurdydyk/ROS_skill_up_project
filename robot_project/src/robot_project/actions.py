import actionlib
import rospkg
import rospy

from gazebo_msgs.srv import DeleteModel, GetModelState, SpawnModel
from geometry_msgs.msg import Pose
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_srvs.srv import Empty, EmptyRequest


class Action(object):
    @staticmethod
    def feedback_callback(feedback):
        print("[Feedback] Going to Goal Pose...")

    def send_goal(self, pos_x, pos_y, pos_z, orient_w):
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
        client.send_goal(goal, feedback_cb=self.feedback_callback)

        rospy.logwarn("wait_for_result")
        client.wait_for_result()

        rospy.logwarn("[Result] State: %d" % (client.get_state()))

    @staticmethod
    def spawn_model(model_name, x, y, z):
        # set the position of the model
        initial_pose = Pose()
        initial_pose.position.x = x
        initial_pose.position.y = y
        initial_pose.position.z = z

        try:
            package_path = rospkg.RosPack().get_path("robot_project")
            with open(f'{package_path}/models/{model_name}/model.sdf', 'r') as xml_file:
                model_xml = xml_file.read().replace('\n', '')
        except EnvironmentError as e:
            rospy.logwarn(f'model.sdf file was not found: {e}')

        try:
            spawn_model_prox = rospy.ServiceProxy('gazebo/spawn_sdf_model', SpawnModel)
            spawn_model_prox(model_name, model_xml, '', initial_pose, 'world')
        except (rospy.ServiceException, rospy.ROSException) as e:
            rospy.logwarn(f'Spawn Model service call failed: {e}')

    @staticmethod
    def get_model_position(model_name):
        resp_coordinates = None

        try:
            model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            # get coordinates of the model
            resp_coordinates = model_coordinates(model_name, '')
        except (rospy.ServiceException, rospy.ROSException) as e:
            rospy.logwarn(f'Get Model State service call failed: {e}')

        return resp_coordinates

    @staticmethod
    def reset_world():
        rospy.init_node('reset_world_client')
        rospy.wait_for_service('/gazebo/reset_world')
        reset_world_service = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        srv_msg = EmptyRequest()
        reset_world_service(srv_msg)

    @staticmethod
    def delete_model(model_name):
        del_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
        rospy.wait_for_service('gazebo/delete_model')
        del_model_prox(model_name)
