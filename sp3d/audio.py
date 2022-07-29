from sp3d import *

class Audio():
    def __init__(self, audio_file, volume=1.0):
        self.audio_file = audio_file
        self.audio_node = loader.loadSfx(self.audio_file)
        self._volume = volume
        self.audio_node.setVolume(self._volume)

    def play(self, loop=False):
        self.audio_node.setLoop(loop)
        if self.audio_node.status == self.audio_node.READY:
            self.audio_node.play()
    
    def stop(self):
        if self.audio_node.status() == self.audio_node.PLAYING:
            self.audio_node.stop()

    def get_audio_length(self):
        return self.audio_node.length()