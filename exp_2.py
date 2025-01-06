import gym

# MountainCar env
env = gym.make('MountainCar-v0', render_mode="human")
num_episodes = 50

for episode in range(num_episodes):
    # Reset env 
    state = env.reset()
    done = False
    step_count = 0

    while not done:
        # render env
        env.render()
        # random action 
        action = env.action_space.sample() # left, right, nthg
        # Step env
        next_state, reward, done, truncated, info = env.step(action)
        # episode end?
        done = done or truncated
        # Inc step 
        step_count += 1

    print(f"Episode {episode + 1} finished after {step_count} steps.")

env.close()
