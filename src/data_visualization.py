import matplotlib.pyplot as plt
from collections import Counter

# Assuming agentUsageData is a list of agent names used for each project
agentUsageData = []

def visualizeData(agentUsageData):
    agent_counts = Counter(agentUsageData)
    agents = list(agent_counts.keys())
    usage_counts = list(agent_counts.values())

    plt.bar(agents, usage_counts)
    plt.xlabel('Agents')
    plt.ylabel('Usage Count')
    plt.title('Agent Usage Data')
    plt.show()

visualizeData(agentUsageData)