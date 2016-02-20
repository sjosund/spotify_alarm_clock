from datetime import datetime
from subprocess import Popen, call
from threading import Thread
from time import sleep


class Alarm(Thread):
    def __init__(self, alarm_t=None, active=False):
        Thread.__init__(self)
        self.alarm_t = alarm_t
        self.active = active
        self._alarm_on = False

    def set_alarm(self, alarm_t):
        self.alarm_t = alarm_t
        self.active = True

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def run(self):
        while True:
            if self.active:
                if not self._alarm_on:
                    t = datetime.now()
                    if t.hour == self.alarm_t.hour and \
                       t.minute == self.alarm_t.minute:
                        play_spotify()
                        self._alarm_on = True
            else:
                if self._alarm_on:
                    stop_spotify()
                    self._alarm_on = False
            sleep(1)


playlists = {
    'morning': 'spotify:user:1146628823:playlist:14FRsyt8MBES8xcNgSOdhy'
}


def start_spotify():
    p = Popen(['spotify'])
    if p.poll() is None:
        p.wait()


def play_spotify():
    playlist = playlists['morning']
    call(
        [
            'spotify-remote', 'play',
            playlist
        ],
    )


def stop_spotify():
    call(['spotify-remote', 'pause'])
