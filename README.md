# Clippy UI Project

This project is a user interface for interacting with an AI agent named Clippy. The project is built with Python and uses a modular architecture for easy expansion and maintenance.

## Getting Started

To get started with this project, clone the repository and navigate into the project directory. Run the `main.py` file to start the application.

## Architecture

The project is structured into three main components:

- **Agent Management**: Handles the creation and management of AI agents. This is done through the `agent_management_tab.py` file.

- **Chat Interface**: Provides a user interface for interacting with the AI agents. This is done through the `agent_interaction.py` file.

- **Visual Cues**: Provides visual feedback based on the agent's activities. This is done through the `timeline.py` file.

Each component is implemented as a Python class in its own file. The `AgentInteraction` class in the `agent_interaction.py` file serves as the main entry point for the application.

## Dependencies

The following dependencies are required to run this project:

- gitpython
- flask
- flask-cors
- jsonschema
- pyyaml
- matplotlib
- pandas
- seaborn

Please make sure to install these dependencies before running the application.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.