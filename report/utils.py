from pathlib import Path
import pickle


# Root path of the project
ROOT_PATH = Path(__file__).resolve().parents[1]

# Path to the trained model
MODEL_PATH = ROOT_PATH / "assets" / "model.pkl"


def load_model():
    """
    Load and return the trained machine learning model.
    """
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model
