from src.dashboard import ProjectDashboard
from src.timeline import ProjectTimeline
from src.code_editor import CodeEditor
from src.feedback import FeedbackTab
from src.agent_management import AgentManagementTab
from src.chat_interface import ChatInterface
from src.testing_interface import TestingInterface
from src.search import SearchFeature
from src.data_visualization import DataVisualization
from src.integrations import IDEIntegration
from src.clippy_avatar import ClippyAvatar

class DesignGuidelines:
    def __init__(self):
        self.project_dashboard = ProjectDashboard()
        self.project_timeline = ProjectTimeline()
        self.code_editor = CodeEditor()
        self.feedback_tab = FeedbackTab()
        self.agent_management_tab = AgentManagementTab()
        self.chat_interface = ChatInterface()
        self.testing_interface = TestingInterface()
        self.search_feature = SearchFeature()
        self.data_visualization = DataVisualization()
        self.ide_integration = IDEIntegration()
        self.clippy_avatar = ClippyAvatar()

    def apply_design_guidelines(self):
        self.project_dashboard.apply_simple_design()
        self.project_timeline.apply_intuitive_design()
        self.code_editor.apply_responsive_design()
        self.feedback_tab.apply_unified_design()
        self.agent_management_tab.apply_visual_cues()
        self.chat_interface.apply_simple_design()
        self.testing_interface.apply_intuitive_design()
        self.search_feature.apply_responsive_design()
        self.data_visualization.apply_unified_design()
        self.ide_integration.apply_visual_cues()
        self.clippy_avatar.apply_avatar_design()

    def apply_navigation_guidelines(self):
        self.project_dashboard.enable_navigation()
        self.project_timeline.enable_navigation()
        self.code_editor.enable_navigation()
        self.feedback_tab.enable_navigation()
        self.agent_management_tab.enable_navigation()
        self.chat_interface.enable_navigation()
        self.testing_interface.enable_navigation()
        self.search_feature.enable_navigation()
        self.data_visualization.enable_navigation()
        self.ide_integration.enable_navigation()
        self.clippy_avatar.enable_navigation()

    def apply_mobile_support(self):
        self.project_dashboard.enable_mobile_support()
        self.project_timeline.enable_mobile_support()
        self.code_editor.enable_mobile_support()
        self.feedback_tab.enable_mobile_support()
        self.agent_management_tab.enable_mobile_support()
        self.chat_interface.enable_mobile_support()
        self.testing_interface.enable_mobile_support()
        self.search_feature.enable_mobile_support()
        self.data_visualization.enable_mobile_support()
        self.ide_integration.enable_mobile_support()
        self.clippy_avatar.enable_mobile_support()