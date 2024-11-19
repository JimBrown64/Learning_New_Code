"""AI used to make selection of ships"""
import random
# import pickle


def selection(request,answers):
    """placeholder function to assist in gathering thoughts"""
    choice = random.choice(answers)
    return str(request) + str(choice)

# Define the environment
def environment(input_ship):
    """Environment for testing"""
    print("selected ship: ", input_ship)
    return_value = 0
    valid_response = False
    while valid_response is False:
        answer = input("Is this acceptable?(Y/N)")
        if answer.upper() == "Y":
            valid_response = True
            return_value = 1
        elif answer.upper() == "N":
            valid_response = True
        else: valid_response = False
    return return_value

# Define the Q-learning agent
class QLearningAgent:
    """learning agent used for making selections"""
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=0.9):
        self.q_values = {}  # Q-values dictionary
        self.epsilon = epsilon  # Exploration-exploitation trade-off
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.actions = {}

    def recall_q_value(self):
        file = globals()["file"]
        result = file.read()

    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        current_q_value = self.get_q_value(state, action)
       #print(current_q_value)
        best_next_action = max((self.get_q_value(next_state, next_action), next_action) \
                                for next_action in self.actions)[1]
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * self.get_q_value(next_state, best_next_action) - current_q_value)
        self.q_values[(state, action)] = new_q_value

    def choose_action(self, state): #1 in 10 chance to choose a random answer, 9 in 10 chance to utilize pre-existing data
        if random.random() < self.epsilon:
            return random.choice(self.actions)  # Explore: choose random action
        else:
            return max((self.get_q_value(state, action), action) for action in self.actions)[1]  # Exploit: choose action with max Q-value

# Training the Q-learning agent
agent = QLearningAgent()
file = open('storedQValues.txt','r')
# agent.recall_q_value()
file.close()
# Training loop
for episode in range(100):
    state = random.choice(agent.actions)  # Random initial state
    for _ in range(10):  # Maximum steps per episode
        action = agent.choose_action(state)
        reward = environment(state)
        next_state = random.choice(agent.actions)  # Random next state
        agent.update_q_value(state, action, reward, next_state)
        state = next_state

# Testing the agent
test_names = ["James", "John", "Robert", "Michael", "William", "plbtbabieie"]
for name in test_names:
    action = agent.choose_action(name)
    if action == 0:
        print(f"{name} is classified as not a valid name.")
    else:
        print(f"{name} is classified as a valid name.")
file = open('storedQValues.txt','w')
file.write(agent.q_values)
file.close()
