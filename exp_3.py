import gym

# CartPole environment
env = gym.make('CartPole-v0', render_mode="human")
num_episodes = 30

for episode in range(num_episodes):
    # Reset env
    state = env.reset()
    done = False
    step_count = 0

    while not done:
        # random action
        action = env.action_space.sample()
        # Step the env with action
        next_state, reward, done, truncated, info = env.step(action)
        # epsode ended?
        done = done or truncated
        # Inc step 
        step_count += 1

    print(f"Episode {episode + 1} finished after {step_count} steps.")

env.close()
