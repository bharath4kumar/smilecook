class Config:
    """Enabled debugging for diagnostic purposes"""
    DEBUG = True
    """Path of the database"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bharath:Ashy459@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
