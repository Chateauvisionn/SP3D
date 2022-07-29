from sp3d import *
from panda3d.core import NodePath

class Entity(NodePath):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = None
        self._parent = render

        for k in ('model', '_parent', 'color'):
            if k in kwargs:
                setattr(self, k, kwargs[k])
                if k == 'position':
                    self.SetPos(kwargs[k])
                del kwargs[k]
        
        if 'scale' in kwargs:
            if isinstance(kwargs['scale'], int):
                self.setScale(self._parent, *kwargs['scale'])
                
        
        if self.model:
            self.model.reparentTo(self._parent)
