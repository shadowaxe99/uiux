from src.agent_interaction import AgentInteraction
import sys

if __name__ == '__main__':
    try:
        ai = AgentInteraction()
        ai.initialize_project('Test Project', 'Test Objectives')
    except Exception as e:
        print('Error: ' + str(e))
        sys.exit(1)

print('Initialized project')