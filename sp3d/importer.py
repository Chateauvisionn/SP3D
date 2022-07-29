from sp3d import *

def load_model(model_path):
    """
    Load a model from a file.
    """
    try:
        m = loader.loadModel(model_path)
        return m
    except Exception as e:
        print("Error:", e)
        return None

# def load_texture(texture_path):
#     """
#     Load a texture from a file.
#     """
#     try:
#         t = loader.loadTexture(texture_path)
#         return t
#     except Exception as e:
#         print("Error:", e)
#         return None