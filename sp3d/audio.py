from sp3d import *
from panda3d.core import *

class Audio():
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def play(self, loop=False):
        self.audio_node = AudioNode(self.audio_file)
        self.audio_node.loop(loop)
        self.audio_node.play()
    
    def stop(self):
        self.audio_node.stop()
