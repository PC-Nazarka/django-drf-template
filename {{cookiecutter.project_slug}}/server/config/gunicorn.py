from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
workers = cpu_count() * 2 + 1
logconfig_json = 'log_conf.json'
worker_class = 'uvicorn.workers.UvicornWorker'
