import dbus

bus = dbus.SessionBus()
time = bus.get_object("com.paulcalnan.Time", "/Time")

curr = time.current_time()
print("The current time is", curr)

