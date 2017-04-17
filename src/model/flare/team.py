from src.model.flare.node import NodeInterface

class Team(NodeInterface):
    """Represents a Team Member and All associated MetaData"""
    def __init__(self,
                 name=None,
                 desc=None,
                 leaf=None,
                 children=None,
                 leader=None):

        self.leader = leader
        super().__init__(name, desc, leaf, children)
