from core.agent.neural_agent import NeuralAgent
from core.network.feed_forward_network import FeedForwardNetwork

class FFNAgent(NeuralAgent):
    def __init__(self):
        super().__init__()
        
    def add_brain(
        self,
        hidden_nodes: int = -1,
        inputs: int = -1,
        outputs: int = -1,
        bias: bool = True
    ) -> None:
        if hidden_nodes == -1:
            hidden_nodes = len(self.sensors)
        if inputs == -1:
            inputs = len(self.sensors)
        if outputs == -1:
            outputs = len(self.controls)
        
        self.brain = FeedForwardNetwork(inputs, outputs, hidden_nodes, bias=bias)
        self.brain.randomise()
        self._has_brain = True
    
    def brain_output(self):
        for i, sensor in enumerate(self.sensors.values()):
            self.brain.input_values[i] = sensor.output()
            i += 1
        self.brain.fire()
        return self.brain.output_values
    
    # TODO: define control method?
    # TODO: Serialise/deserialise?