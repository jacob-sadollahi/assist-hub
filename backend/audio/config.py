from pydantic_settings import BaseSettings
from faster_whisper import WhisperModel


class AppConfig(BaseSettings):
    faster_whisper_model_name: str = 'base'

    def load_whisper_model(self) -> WhisperModel:
        return WhisperModel(
            model_size_or_path=self.faster_whisper_model_name
        )
