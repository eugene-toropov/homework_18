class Config(object):
    """
    Класс конфигурации.

    Указываем место хранения ДБ. Статус дебагера и прочие настройки.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
