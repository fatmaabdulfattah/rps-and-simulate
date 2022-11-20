#simulating a random walk

#to plot the graph
import matplotlib.pyplot as plt 
from random import choice

#use the next line if u run it in jupyter notebook
#%matplotlib inline

#size of the graph
plt.rc('figure',figsize=(12,6)) 

#create function to list a random walk
def rand_walk(step_num):
    walk = []
    step_choice = choice([1,-1])
    walk.append(step_choice)

    for i in range(1,step_num):
        step_choice_2 = choice([1,-1])
        next_step = walk[i-1] + step_choice_2
        walk.append(next_step)

    return walk

step_number=int(input('Enter number of steps: '))

random_walk=rand_walk(step_number)

#label the x and y axis and add a title and show our graph
def plot_walk(walk):
    plt.plot(walk)
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.title("Our Random walk")
    plt.show()
    
plot_walk(random_walk)
