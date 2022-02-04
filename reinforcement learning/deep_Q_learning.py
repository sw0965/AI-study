import gym

import random
import math
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import deque

import matplotlib.pyplot as plt


# 파라미터 정의
EPISODES = 1000   # 에피소드 반복횟수
EPS_START = 0.9 # 학습 시작시 에이전트가 무작위로 행동할 확률
# 0.5 면 50% 절반의 확률로 무작위 행동
EPS_END = 0.05  # 학습 막바지에 에이전트가 무작위로 행동할 확률

EPS_DECAY = 200 # 학습 진행시 에이전트가 무작위로 행동할 확률을 감소시키는 값
GAMMA = 0.8 # 할인계수 : 에이전트가 현제 reward를 미래 reward보다 얼마나 더 가치있게 여기는 지에 대해 일종의 할인율

LR = 0.001  # 학습률
BATCH_SIZE = 64 # 배치크기


class DQNAgent:
    def __init__(self):
        self.model = nn.Sequential(
            nn.Linear(4, 256),
            nn.ReLU(),
            nn.Linear(256, 2)
            )
        self.optimizer = optim.Adam(self.model.parameters(), LR)
        self.steps_done = 0
        self.memory = deque(maxlen=10000)

    def memorize(self, state, action, reward, next_state):
        self.memory.append((state,
                            action,
                            torch.FloatTensor([reward]),
                            torch.FloatTensor([next_state])))

    def act(self, state):
        print('act 시작')
        print('EPS_END: ',EPS_END)
        print('(EPS_START - EPS_END): ', (EPS_START - EPS_END))
        print('self.steps_done: ', self.steps_done)
        print('EPS_DECAY: ', EPS_DECAY)

        eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1. * self.steps_done / EPS_DECAY)

        print('eps_threshold', eps_threshold)

        self.steps_done += 1

        if random.random() > eps_threshold:
            return self.model(state).data.max(1)[1].view(1, 1)
        else:
            return torch.LongTensor([[random.randrange(2)]])

    def learn(self):
        if len(self.memory) < BATCH_SIZE:
            return

        batch = random.sample(self.memory, BATCH_SIZE)
        states, actions, rewards, next_states = zip(*batch)

        states = torch.cat(states)
        actions = torch.cat(actions)
        rewards = torch.cat(rewards)
        next_states = torch.cat(next_states)

        current_q = self.model(states).gather(1, actions)

        max_next_q = self.model(next_states).detach().max(1)[0]
        expected_q = rewards + (GAMMA * max_next_q)

        loss = F.mse_loss(current_q.squeeze(), expected_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


env = gym.make('CartPole-v0')
agent = DQNAgent()
score_history = []

for e in range(1, EPISODES+1): # 50번의 플레이
    state = env.reset()
    steps = 0
    while True:
        print('1')
        env.render()
        state = torch.FloatTensor([state])

        action = agent.act(state)

        next_state, reward, done, _ = env.step(action.item())

        if done:
            reward = -1

        agent.memorize(state, action, reward, next_state)
        agent.learn()

        state = next_state
        steps += 1

        if done:
            print("에피소드:{0} 점수: {1}".format(e, steps))
            score_history.append(steps)
            break

    plt.plot(score_history)
    plt.ylabel('score')
    plt.xlabel('episode')
    plt.show(block=False)
    plt.pause(1)
    plt.close()