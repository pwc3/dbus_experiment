import dbus
import dbus.service
import time

class Time(dbus.service.Object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        name = dbus.service.BusName("com.paulcalnan.Time", bus=self.bus)
        super().__init__(name, "/Time")

    @dbus.service.method("com.paulcalnan.Time", out_signature="s")
    def current_time(self):
        formatter = "%Y-%m-%d %H:%M:%S"
        return time.strftime(formatter)

if __name__ == "__main__":
    import dbus.mainloop.glib
    from gi.repository import GLib

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    loop = GLib.MainLoop()
    object = Time()

    print("Started, press Ctrl-C to stop")
    loop.run()

