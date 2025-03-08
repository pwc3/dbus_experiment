import logging

import dbus


def run_client():
    log = logging.getLogger("dbus_experiment")

    bus = dbus.SessionBus()
    time = bus.get_object("com.paulcalnan.Time", "/Time")

    log.info("Requesting current_time")
    curr = time.current_time()
    log.info("Received current time %s", curr)

    print("The current time is", curr)
