---
layout: default
title: Projects
---

#Joshua Morton
#####Projects

######IARRC
IARRC, the International Autonomous Robot Racing Competition. This year The Agency, a club I run, was asked to assist with software development for the competition by Robojackets, a GT robotics organization. [Our code](https://github.com/RoboJackets/iarrc-software), written in C++ allowed us to place 4th overall at the competition. 

The system uses a reactive control driving scheme on the [ROS](http://www.ros.org/) platform. The readings from a lidar and camera were converted into a birds-eye view and then into OpenCV images. These images were then overlayed, and used to make steering decisions. In addition to architecting the system, I also implemented some of the ROS nodes, including one that [converts a pointcloud to an OpenCV imagemat](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/pointcloud_to_image/pointcloud_to_image.cpp) and the system that [combined the camera and lidar data](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/iarrc_world_model/world_model.cpp).

######ClassRank
[ClassRank](https://github.com/joshuamorton/ClassRank) has been my pet project since my freshman summer. I started by [proving some facts about collaborative filtering](https://www.sharelatex.com/github/repos/joshuamorton/ClassRank/builds/c7ae4929b2575f232753d366ce574833a94864ee/raw/output.pdf) using that to build an application to help recommend classes for students to take. This project has developed into my [CS Capstone Project](https://github.com/classrank), that I'm developing with a few classmates. 

######Snippets

######Serve
I attended [MHacks IV](http://mhacks-iv.devpost.com/) and while there developed [Serve](https://github.com/thepav/serve), an application to help hackathon-goers build super simple web applications more efficiently.

######ABAGAIL

######Elanor

