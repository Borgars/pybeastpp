from OpenGL.GL import *

from core.agent.agent import Agent
from core.utils import ColourPalette, ColourType as CT

MONITOR_BAR_HEIGHT = 25

class AgentPainter():
    def __init__(self, agents: list[Agent]):
        self.agents = agents
        self.visible: bool = True