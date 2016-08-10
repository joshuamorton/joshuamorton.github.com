---
layout: subpage
title: IARRC
priority: 0
---

![the IARRC Vehicle](https://{{ site.url }}/assets/IARRC.jpg)

IARRC, the International Autonomous Robot Racing Competition. This year The
Agency, a club that has been building progressively more advanced autonomous
vehicles, was asked to assist with software development for the competition by
Robojackets, a GT robotics organization. [Our
code](https://github.com/RoboJackets/iarrc-software), written in C++ allowed us
to place 4th overall at the competition. 

The system uses a reactive-control driving scheme on the
[ROS](http://www.ros.org/) platform. The readings from a lidar and camera were
converted into a birds-eye view and then into OpenCV images. These images were
then overlayed and used to make steering decisions. In addition to architecting
the system, I also implemented some of the ROS nodes, including one that
[converts a pointcloud to an OpenCV
imagemat](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/pointcloud_to_image/pointcloud_to_image.cpp)
and the system that [combined the camera and lidar
data](https://github.com/RoboJackets/iarrc-software/blob/master/iarrc/src/iarrc_world_model/world_model.cpp).


