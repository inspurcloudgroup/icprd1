#!/usr/bin/env python3

import os
import time
import random
import threading

N = 5 

philosophers = N
forks = N

class Philosopher(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = fork_list[self.index]
        self.right_fork = fork_list[(self.index + 1) % len(fork_list)]

    def eating(self):
        print('philosopher[{}] is eating'.format(self.index))
        # ����deadlockʱ�����߳�˯��ʱ���й�ϵ
        # ȥ�������sleep()�����׾ͷ�������
        time.sleep(random.uniform(1, 3) * 0.000001)

    def thinking(self):
        print('philosopher[{}] is thinking'.format(self.index))
        time.sleep(random.uniform(1, 3) * 0.000001)

    def run(self):
        while True:
            self.left_fork.pick_up()
            self.right_fork.pick_up()
            self.eating()
            self.left_fork.lay_down()
            self.right_fork.lay_down()
            self.thinking()


class Fork():
    def __init__(self):
        self.lock = threading.Lock()

    def pick_up(self):
        self.lock.acquire()

    def lay_down(self):
        self.lock.release()


if __name__ == '__main__':
    fork_list = [Fork() for i in range(forks)]
    philosopher_list = [Philosopher(i) for i in range(philosophers)]

    for philosopher in philosopher_list:
        philosopher.start()


# �������ٴ�ӡ��Ϣ����������������
# ��ʱ�������̶߳�ӵ����Դ��һ��fork��
# �����̶߳��ڵȴ���Դ����һ��fork��
