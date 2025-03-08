import logging
import time

import dbus
import dbus.service


class Time(dbus.service.Object):
    def __init__(self):
        self.log = logging.getLogger("dbus_experiment")
        self.bus = dbus.SessionBus()

        name = dbus.service.BusName("com.paulcalnan.Time", bus=self.bus)
        super().__init__(name, "/Time")

        self.log.info("Started time service")

    @dbus.service.method("com.paulcalnan.Time", out_signature="s")
    def current_time(self):
        self.log.info("Received current_time request")
        formatter = "%Y-%m-%d %H:%M:%S"

        response = time.strftime(formatter)
        self.log.info("Responding with %s", response)

        return response
