from node import NodeInterface


class Team(NodeInterface):

    def __init__(self,
                 name=None,
                 desc=None,
                 leaf=None,
                 children=None,
                 leader=None):

        self.leader = leader
        super().__init__(name, desc, leaf, children)
