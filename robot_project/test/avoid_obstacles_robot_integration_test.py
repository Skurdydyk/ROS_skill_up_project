#! /usr/bin/env python

from gazebo_msgs.srv import GetModelState
from tf import TransformListener
import unittest
import rostest
import rospy

from helpers import send_goal

PKG = 'robot_project'
NAME = 'rotate_robot_integration_test'


class TestRobotControl(unittest.TestCase):

    def setUp(self):
        rospy.init_node('test_node')
        self.tf = TransformListener()
        self.current_orientation = dict()

    def test_move_rotation(self):
        resp_coordinates = None
        send_goal(2, 0.0, 0.0, 0.2)

        try:
            model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            resp_coordinates = model_coordinates('my_robot', '')
        except rospy.ServiceException as e:
            rospy.logwarn('Get Model State service call failed:  {0}'.format(e))

        self.assertTrue(1.3 <= resp_coordinates.pose.position.x <= 1.6)


if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestRobotControl)
