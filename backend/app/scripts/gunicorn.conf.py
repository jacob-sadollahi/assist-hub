bind = '0.0.0.0:8000'
loglevel = 'error'
accesslog = '-'
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"
chdir = "/app"
worker_connections = 1000
workers = 1
threads = workers
reload = False
preload = True
