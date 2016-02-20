from argparse import ArgumentParser
from datetime import datetime

from flask import Flask, request

from alarm import Alarm


app = Flask(__name__)
alarm = Alarm(alarm_t=datetime.now(), active=False)


@app.route('/set_alarm')
def set_alarm():
    hour = int(request.args['hour'])
    minute = int(request.args['minute'])
    alarm.set_alarm(
        datetime(
            2000, 1, 1, hour, minute
        )
    )
    return 'Alarm set to {}:{}'.format(
        str(alarm.alarm_t.hour).zfill(2),
        str(alarm.alarm_t.minute).zfill(2)
    )


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
    return 'Active: {}, Time: {}:{}'.format(
        alarm.active,
        str(alarm.alarm_t.hour).zfill(2),
        str(alarm.alarm_t.minute).zfill(2)
    )


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--host')
    parser.add_argument('--port')
    kwargs = vars(parser.parse_args())

    alarm.start()
    app.run(**kwargs)
