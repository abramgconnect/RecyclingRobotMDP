# Reinforcement Learning: An Introduction
# Book by Andrew Barto and Richard S. Sutton
# Second Edition
# Chapter 3: Finite Markov Decision Processes
# Example 3.3 P74/548
import random


class Recycling_Robot_MDP():
    def __init__(self, initial_state):
        if initial_state == 'low' or initial_state == 'high':
            self.state = initial_state
            self.rewards = 0
        else:
            raise Exception("Invalid Initialization")

    def switch(self):
        if self.state == 'low':
            a = self.__RandomActionPolicy()
            if a == 0:
                prob = random.random()
                if prob < 0.5:  # beta
                    self.state = 'high'
                    self.rewards -= 3
                else:
                    self.state = 'low'
                    self.rewards += 5  # reward of searching
            elif a == 1:
                self.state == 'low'
                self.rewards += 1  # reward of waiting
            elif a == 2:
                self.state = 'high'
                self.rewards += 0

        elif self.state == 'high':
            a = self.__RandomActionPolicy()
            if a == 0:
                prob = random.random()
                if prob < 0.5:  # beta
                    self.state = 'high'
                    self.rewards += 5  # reward of searching
                else:
                    self.state = 'low'
                    self.rewards += 5  # reward of searching
            elif a == 1:
                self.state = 'high'
                self.rewards += 1

    def __RandomActionPolicy(self):
        if self.state == 'low':
            return random.randint(0, 2)  # 0=search 1=wait 2=recharge
        elif self.state == 'high':
            return random.randint(0, 1)  # 0=search 1=wait


if __name__ == '__main__':
    robot = Recycling_Robot_MDP('low')
    for i in range(0, 100):
        robot.switch()
        print(robot.state)
        print(robot.rewards)
