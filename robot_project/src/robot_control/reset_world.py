#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest
from gazebo_msgs.srv import DeleteModel


def reset_world():
    rospy.init_node('reset_world_client')
    rospy.wait_for_service('/gazebo/reset_world')
    reset_world_service = rospy.ServiceProxy('/gazebo/reset_world', Empty)
    srv_msg = EmptyRequest()
    reset_world_service(srv_msg)


def delete_model(model_name):
    del_model_prox = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
    rospy.wait_for_service('gazebo/delete_model')
    del_model_prox(model_name)


reset_world()
delete_model('construction_barrel')
