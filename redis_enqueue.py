from rq import Queue
from redis import Redis
from tasks import call_predict_api
from flask import Flask, request

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def redis_worker_predict():
    file_data = request.data

    job = q.enqueue(call_predict_api, file_data)
    while(True):
        if job.result is not None:
            job_result = job.result
            break

    return job_result

if __name__ == '__main__':
    app.run(port=5001)