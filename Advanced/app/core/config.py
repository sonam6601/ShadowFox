import os


class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")

    @property
    def upload_dir(self):
        return self.UPLOAD_DIR


settings = Settings()
