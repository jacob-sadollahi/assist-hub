from fastapi import FastAPI, Depends
from faster_whisper import WhisperModel

from functools import lru_cache

from config import AppConfig


class FasterWhisperModelManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("First time")
            cls._instance = super().__new__(cls)
            cls._instance.model = cls._load_model()
        else:
            print("Already exists model.")
        return cls._instance

    @classmethod
    def _load_model(cls) -> WhisperModel:
        return WhisperModel(
            model_size_or_path="base"
        )

    def get_model(self):
        """
        Returns the loaded model
        """
        return self.model


@lru_cache(maxsize=1)
def get_model_manager():
    return FasterWhisperModelManager()


app = FastAPI()


@app.on_event("startup")
async def startup_event(
        model_manager: FasterWhisperModelManager = Depends(get_model_manager)
):
    # This ensures the model is loaded during application startup
    print("Application starting up, loading model...")


# @app.on_event("startup")
# async def initialize_config():
#     app.state.config = AppConfig()
#     app.state.faster_whisper_model = app.state.config.load_whisper_model()


@app.get("/")
def read_root(
        model_manager: FasterWhisperModelManager = Depends(get_model_manager)
):
    model = model_manager.get_model()
    return {"Hello": "World"}
