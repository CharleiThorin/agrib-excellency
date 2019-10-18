import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thorin of oakenshield cant be guessed'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    AGRIB_MAIL_SUBJECT_PREFIX = '[Agrib Excellecy Limited]'
    AGRIB_MAIL_SENDER = 'Agrib Google Admin <agrib.excellency@gmail.com>'
    AGRIB_MAIL_RECEIVER = 'Agrib Admin <infor@agrib-excellency.com>'
    AGRIB_ADMIN = os.environ.get('AGRIB_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    print("its working")


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
