import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'my-secret-key'
    API_KEY = os.getenv('API_KEY')