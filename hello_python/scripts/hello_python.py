#!/usr/bin/env python
"""
    Hello Python!
"""
import rospy
from hello_python.hello import HelloPython

if __name__== "__main__":
    rospy.init_node('hello_python') # Resgistering node in ros master
        
    hp = HelloPython()
    rospy.spin()
