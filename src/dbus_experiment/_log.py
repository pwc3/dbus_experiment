import logging


def configure_module_logger(level=logging.DEBUG):
    logger = logging.getLogger("dbus_experiment")
    logger.setLevel(level)

    fmt = logging.Formatter("%(name)s: %(levelname)s - %(message)s")

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)
