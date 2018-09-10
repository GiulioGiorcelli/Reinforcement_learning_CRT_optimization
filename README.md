# Reinforcement learning for CRT optimization
Working in online marketing and lead gen, I naturally eneded up trying to solve the multi-armed bandit dilemma in the best and most profitable way possible. Reinforcement learning is one of the most fascinating branches of AI and, based on my research, it appears to provide the optimal solution to this issue.

# What you'll find in this repository
In the repo you will find my own implementations of RL algorithms tailored to solve CRT optimization for online advertising. The Thompson Sampling algorithm is what I worked on for now. You will also find lucko515's implementation of the TS algorithm so that you can compare it against mine on the same dataset and draw you own conclusion. More on this below.

# Inspiration and credits
My work has been inspired by this GitHub repo: https://github.com/lucko515/ads-strategy-reinforcement-learning although I found lucko515's implementation to be too greedy for the my own applications. More specifically, lucko515's AI arrives to the same optimal solution as mine but it does so without exploring all possible options. This is not a matter of which one is the best, it a matter of what implementation is optimal for one's own use case. In my use case, exploring all ads is a business requirement.

Regardless, I will clearly flag lucko515's code. No matter which version you like the most, his work has been instumental to the creation of this software. Kudos to this guy: https://github.com/lucko515

# License
This entire repo is under MIT license.



