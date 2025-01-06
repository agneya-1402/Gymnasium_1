import gymnasium as gym

# init env
env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset(seed=52) # reset env

for _ in range(5000):
    # random action
    action = env.action_space.sample()
    # step env
    observation, reward, terminated, truncated, info = env.step(action)
    # episode end?
    if terminated or truncated:
        observation, info = env.reset()

env.close()