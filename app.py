from flask import Flask
from config import Configuration

# В данном случае __name__ это имя текущего файла, а именно app.py
app=Flask(__name__)
app.config.from_object(Configuration)
