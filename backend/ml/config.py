import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARTIFACTS_PATH = os.path.join(BASE_DIR, "artifacts")

def get_model_path(filename):
    return os.path.join(ARTIFACTS_PATH, filename)