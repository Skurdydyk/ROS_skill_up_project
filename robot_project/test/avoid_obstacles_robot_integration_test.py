#! /usr/bin/env python

import unittest
import rostest
import rospy

from helpers import send_goal, spawn_model, get_model_position

PKG = 'robot_project'
NAME = 'avoid_obstacle_robot_integration_test'


class TestRobotControl(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_node')

    def test_avoid_obstacle(self):
        # send the first move base goal to move
        send_goal(2, 0.0, 0.0, 0.2)
        # get coordinates of the robot before avoiding an obstacle
        coordinates_robot = get_model_position('my_robot')

        # check the position of the robot
        self.assertTrue(1.3 <= coordinates_robot.pose.position.x <= 1.6)
        self.assertTrue(-0.3 <= coordinates_robot.pose.position.y <= 0.3)

        # spawning an obstacle directly in front of the robot
        spawn_model('construction_barrel', 3, 0, 0.2)

        # send second move base goal
        send_goal(6, 0.0, 0.0, 0.2)

        # get coordinates robot and obstacle after avoiding obstacle
        coordinates_robot = get_model_position('my_robot')
        coordinates_obstacle = get_model_position('construction_barrel')

        self.assertTrue(5 <= coordinates_robot.pose.position.x <= 6)
        self.assertTrue(-0.3 <= coordinates_robot.pose.position.y <= 0.3)

        # check the position of the obstacle
        self.assertTrue(2.9 <= coordinates_obstacle.pose.position.x <= 3.1)
        self.assertTrue(-0.1 <= coordinates_obstacle.pose.position.y <= 0.1)


if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestRobotControl)
