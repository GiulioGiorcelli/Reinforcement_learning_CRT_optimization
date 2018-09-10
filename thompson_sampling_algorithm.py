# Reinforcement learning for CTR optimization - Thompson Sampling
import numpy as np
import random


# this is an implementation of the Thompson Sampling algorithm that I found on GitHub. I don't think this implementation is correct
# as it is very greedy and it does not seem to explore as much as it should
def thompson_sampling(data):

	N = data.shape[0]
	d = data.shape[1]

	N1_n = {} 
	N0_n = {}

	for i in range(d):
		N1_n[i] = 0
		N0_n[i] = 0

	total_score = 0
	iter_object_selected = []


	for sample in range(N):
		
		object_results_from_distribution = []

		for object_ in range(d):
			if data[sample, object_] == 1:
				N1_n[object_] += 1
			elif data[sample, object_] == 0:
				N0_n[object_] += 1
			else:
				continue
			object_results_from_distribution.append(random.betavariate(N1_n[object_]+1, N0_n[object_]+1))
			

		iter_object_selected.append(np.argmax(object_results_from_distribution))
		reward = data[sample, np.argmax(object_results_from_distribution)]
		total_score += reward

	return iter_object_selected, total_score
	
	
	

# this is my own implementation of the TS algo. This implementation appears to explore as I would expect
def thompson_sampling_2(data):

	N = data.shape[0]
	d = data.shape[1] 

	ads_selected = []
	total_reward = 0
	
	N1_n = {} 
	N0_n = {} 

	for i in range(d):
		N1_n[i] = 0
		N0_n[i] = 0

	for n in range(N):
	
		ad = 0
		max_random = 0
		
		for i in range(d):

			random_beta = random.betavariate(N1_n[i]+1, N0_n[i]+1)

			if (random_beta > max_random):
				max_random = random_beta
				ad = i
				
		ads_selected.append(ad)
		reward = data[n, ad]
		
		if (reward == 1):
			N1_n[ad] = N1_n[ad] + 1
		else:
			N0_n[ad] = N0_n[ad] + 1

		total_reward += reward
		
	return ads_selected, total_reward