"""Example flows."""
import time

from prefect import flow


@flow(log_prints=True)
def hello_world():  # noqa
    print("OK")


@flow(log_prints=True)
def long_time(counter: int = 10):  # noqa
    print("Start")
    time.sleep(counter)
    print("Finished")
