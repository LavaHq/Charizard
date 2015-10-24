"""Abstract Base Class For Flare Entities"""

class NodeInterface:

    def __init__(self, name=None, desc=None, leaf=None, children=None):
        """ """
        self.name = name
        self.desc = desc
        self.leaf = leaf
        self.children = children

    def methodx(self):
        """ sdkagfjhds """
        raise NotImplemented
