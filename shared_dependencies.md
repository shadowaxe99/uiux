Shared Dependencies:

Exported Variables:
- "activeProjects": List of all active Clippy projects
- "projectStatus": Status of each project (in progress, completed, etc.)
- "agentActivities": Record of agent activities for each project
- "generatedCode": Code generated by Clippy for each project
- "projectFeedback": User feedback tagged to specific projects/times
- "agentConfig": Configuration of agents used for projects
- "projectChat": Chat history for each project
- "testOutputs": Outputs from testing Clippy-generated code
- "searchResults": Results from searching across all feedback and guidance
- "agentUsageData": Data on agent usage and performance
- "ideIntegrations": Integrations with IDEs like VSCode
- "clippyAvatar": Clippy avatar/assistant settings

Data Schemas:
- "ProjectSchema": Schema for Clippy projects
- "AgentActivitySchema": Schema for agent activities
- "CodeSchema": Schema for Clippy-generated code
- "FeedbackSchema": Schema for user feedback
- "AgentConfigSchema": Schema for agent configurations
- "ChatSchema": Schema for project chat history
- "TestOutputSchema": Schema for test outputs
- "SearchResultSchema": Schema for search results
- "AgentUsageDataSchema": Schema for agent usage data
- "IntegrationSchema": Schema for IDE integrations
- "AvatarSchema": Schema for Clippy avatar/assistant

DOM Element IDs:
- "projectDashboard"
- "projectTimeline"
- "codeEditor"
- "feedbackTab"
- "agentManagement"
- "chatInterface"
- "testingInterface"
- "searchBar"
- "dataVisualization"
- "ideIntegration"
- "clippyAvatar"

Message Names:
- "ProjectUpdate"
- "AgentActivityUpdate"
- "CodeUpdate"
- "FeedbackUpdate"
- "AgentConfigUpdate"
- "ChatUpdate"
- "TestOutputUpdate"
- "SearchResultUpdate"
- "AgentUsageDataUpdate"
- "IntegrationUpdate"
- "AvatarUpdate"

Function Names:
- "initializeProject"
- "monitorAgentActivity"
- "provideFeedback"
- "reviewCode"
- "manageAgents"
- "initiateChat"
- "runTest"
- "searchFeedback"
- "visualizeData"
- "integrateIDE"
- "interactWithAvatar"