import argparse
import sys

import dbus.mainloop.glib
from gi.repository import GLib

from dbus_experiment._log import configure_module_logger
from dbus_experiment.client import run_client
from dbus_experiment.service import Time


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description="D-Bus experiment")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Subcommands"
    )

    subparsers.add_parser("run-service", help="Run the service")
    subparsers.add_parser("run-client", help="Run the client")
    options = parser.parse_args(argv)

    configure_module_logger()

    if options.command == "run-service":
        run_service()
    elif options.command == "run-client":
        run_client()


def run_service():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    _ = Time()
    print("Started, press Ctrl-C to stop")
    loop.run()


if __name__ == "__main__":
    sys.exit(main())
