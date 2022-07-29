from sp3d import *

app = App(color=(0,20,255), size=(800,600), title="Game")

e = Entity(model=load_model("sp3d/models/capsule.obj"))

run(app)