## application configuration file

# Flask configuration
DEBUG = True  # Set to False in production
SECRET_KEY = 'your-secret-key'  # Change this to a secure random string

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'  # SQLite database URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
