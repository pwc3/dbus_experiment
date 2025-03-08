# Writing a Simple D-Bus Service in Python

Implements a D-Bus service for getting the current time. Code taken from ["Writing a Simple D-Bus Service in Python" by Gokberk Yaltirakli](https://www.gkbrk.com/2018/02/simple-dbus-service-in-python/).

Requires some packages, installed via `sudo apt install`:
- `libcairo2-dev`
- `libdbus-1-dev`
- `libgirepository1.0-dev`

Also requires [Poetry](https://python-poetry.org/).

Run `poetry install` to install dependencies in the local virtual environment.

## Running the project

```bash
poetry install
poetry run python3 src/dbus_experiment run-service &
poetry run python3 src/dbus_experiment run-client
```
