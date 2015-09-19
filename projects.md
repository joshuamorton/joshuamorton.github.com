---
layout: default
title: Projects
priority: 3
---

#Joshua Morton
####Projects

#####IARRC
IARRC, the International Autonomous Robot Racing Competition. This year The Agency, a club I run, was asked to assist with software development for the competition by Robojackets, a GT robotics organization. [Our code](https://github.com/RoboJackets/iarrc-software), written in C++ allowed us to place 4th overall at the competition. 

The system uses a reactive control driving scheme on the [ROS](http://www.ros.org/) platform. The readings from a lidar and camera were converted into a birds-eye view and then into OpenCV images. These images were then overlayed, and used to make steering decisions. In addition to architecting the system, I also implemented some of the ROS nodes, including one that [converts a pointcloud to an OpenCV imagemat](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/pointcloud_to_image/pointcloud_to_image.cpp) and the system that [combined the camera and lidar data](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/iarrc_world_model/world_model.cpp).

#####ClassRank
[ClassRank](https://github.com/joshuamorton/ClassRank) has been my pet project since my freshman summer. I started by [proving some facts about collaborative filtering](https://www.sharelatex.com/github/repos/joshuamorton/ClassRank/builds/c7ae4929b2575f232753d366ce574833a94864ee/raw/output.pdf) using that to build an application to help recommend classes for students to take. This project has developed into my [CS Capstone Project](https://github.com/classrank), that I'm developing with a few classmates. 

#####Snippets
My [tidbits](https://github.com/joshuamorton/tidbits) repository serves as a place to store things that don't belong anywhere else. It contains short projects that don't deserve their own place. Things like musings on python internals and thoughts that end up being blog posts. Some of the coolest pieces are a [collaborative filter implementation in scala](https://github.com/joshuamorton/tidbits/blob/master/CollabFilter.scala), an implementation of [an object system that supports inheritance](https://github.com/joshuamorton/tidbits/blob/master/objectModel.py), and a [short lisp interpreter](https://github.com/joshuamorton/tidbits/blob/master/lispy.py) written by a friend and I.

#####Serve
I attended [MHacks IV](http://mhacks-iv.devpost.com/) and while there developed [Serve](https://github.com/thepav/serve), an application to help hackathon-goers build super simple web applications more efficiently. By housing a simple single endpoint API in a docker instance, and providing a small database to back the system, we created a platform that would allow hackers to build tools without sweating how their system worked. It just would.

#####ABAGAIL
[ABAGAIL](https://github.com/joshuamorton/ABAGAIL) is the machine learning library used for CS4641 (Machine Learning) at Georgia Tech. I made some updates to the old java library that includes one of the only implementations of the MIMIC algorithm. These included improved documentation and some major improvements in the efficiency of the vector mathematics that are vital to neural networks and other common matrix-based algorithms. These led to a 3-4x increase in the speed of large matrix multiplies in the framework.

Additionally, I make use of the library in my [machine learning](https://github.com/joshuamorton/Machine-Learning) class, for which I published both my ABAGAIL code and the scikit-learn code, as well as supporting tools for data visualization through matplotlib.

#####Buzzmobile
[Buzzmobile](https://github.com/gtagency/buzzmobile) is the code repository for the Agency's large autonomous parade float project. This project has lasted several years, and for most of that time I served in an advisory role, though recently with my experience with IARRC, am expected to take a more leading role in development and project planning. In the past, I've both worked on documentation, as well as theoretical and abstract system design. Additionally, I implemented nodes, including one that honked the horn when the vehicle encountered an obstacle.
