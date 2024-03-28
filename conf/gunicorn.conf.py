"""
    Configuration for Gunicorn
"""
import multiprocessing


bind = '127.0.0.1:__PORT__'

# https://docs.gunicorn.org/en/latest/settings.html#workers
workers = multiprocessing.cpu_count() * 2 + 1

# https://docs.gunicorn.org/en/latest/settings.html#logging
loglevel = 'info'

# https://docs.gunicorn.org/en/latest/settings.html#logging
accesslog = '/var/log/__APP__/__APP__.log'
errorlog = '/var/log/__APP__/__APP__.log'

# https://docs.gunicorn.org/en/latest/settings.html#pidfile
pidfile = '__INSTALL_DIR__/app/gunicorn.pid'
