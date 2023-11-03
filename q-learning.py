import gym
import numpy as np
env = gym.make("MountainCar-v0",render_mode='human')
env.reset()
done = False
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_win_os_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

q_table = np.random.uniform(low=-2,high=0,size=(DISCRETE_OS_SIZE + [env.action_space.n]))
print(q_table.shape)
print(discrete_win_os_size)
# while not done:
#     action = 2 # 2 to move right 1 to move left 0 to do nothing
#     new_state, reward, done, truncated, info = env.step(action)
#     print(new_state,reward)
#     env.render() # to show the env
#
# env.close()