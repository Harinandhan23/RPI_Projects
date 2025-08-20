import threading

class TimerIRQ:
    def __init__(self, interval, callback_function):
        self.interval = interval
        self.callback_function = callback_function
        self.timer = None
        self.running = False

    def _run(self):
        self.running = False
        self.start()
        self.callback_function()

    def start(self):
        if not self.running:
            self.timer = threading.Timer(self.interval, self._run)
            self.timer.start()
            self.running = True

    def stop(self):
        if self.timer:
            self.timer.cancel()
        self.running = False