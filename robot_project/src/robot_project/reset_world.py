#! /usr/bin/env python

from actions import Action

if __name__ == '__main__':
    action = Action()

    action.reset_world()
    action.delete_model('construction_barrel')
