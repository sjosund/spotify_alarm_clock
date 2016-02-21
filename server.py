from argparse import ArgumentParser
from datetime import datetime

from flask import Flask, request, render_template

from alarm import Alarm


app = Flask(__name__)
alarm = Alarm(alarm_t=datetime.now(), active=False)


@app.route('/')
def index():
    return render_template('index.html', status=alarm.status(), alarm_t=alarm.time())


@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    hour, minute = [int(n) for n in request.form['alarm_time'].split(':')]
    alarm.set_alarm(
        datetime(
            2000, 1, 1, hour, minute
        )
    )
    return render_template('index.html', status=alarm.status(), alarm_t=alarm.time())


@app.route('/deactivate')
def deactivate():
    alarm.deactivate()
    return 'deactivated'


@app.route('/activate')
def activate():
    alarm.activate()
    return 'activated'


@app.route('/status')
def status():
    return 'Status: {}, Time: {}'.format(alarm.status(), alarm.time())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host')
    parser.add_argument('--port')
    kwargs = vars(parser.parse_args())

    alarm.start()
    app.run(debug=True, **kwargs)
