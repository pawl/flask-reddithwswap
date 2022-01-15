import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

bind = "0.0.0.0:80"

preload_app = True
max_requests = 5000
max_requests_jitter = 50

loglevel = "info"
