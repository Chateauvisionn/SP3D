from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, loadPrcFileData

class App(ShowBase):
    def __init__(self, **kwargs):
        ShowBase.__init__(self)
        self.props = WindowProperties() 

        if "title" in kwargs:
            self.props.setTitle(kwargs["title"])
        else:
            self.props.setTitle("SP3D")
        self.win.requestProperties(self.props)


        if "color" in kwargs:
            self.setBackgroundColor(*kwargs["color"])
        
        if "size" in kwargs:
            if isinstance(kwargs["size"], tuple):
                self.props.setSize(kwargs["size"][0], kwargs["size"][1]) 

                self.win.requestProperties(self.props) 

def run(app: ShowBase):
    print("starting application...")
    app.run()

if __name__ == "__main__":
    app = App()
    run(app)