#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:21:12 2018

@author: osboxes
"""

class Robot:
    """Represents a robot, with a name."""
    # a class variable, containing the number of robots
    population = 0
    def __init__(self, name):
        self.name = name
        print("(Initializing {} ...)".format(self.name))
        # when this person is created, the robot adds to the population
        Robot.population += 1
    def die(self):
        """I am dying."""
        print("{} is destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working...".format(Robot.population))
    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))
    @classmethod  # this is a decorator or a rapper function
    def how_many(cls):
        """Prints the current population."""
        print("We've {:d} robots.".format(cls.population))
droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So, let's destroy them.\n")
droid1.die()
droid2.die()
Robot.how_many()
