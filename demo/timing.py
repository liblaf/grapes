import time

from liblaf import grapes


@grapes.timer()
def func() -> None:
    time.sleep(0.1)


def main() -> None:
    grapes.init_logging()

    func()

    for _ in grapes.track(range(10)):
        time.sleep(0.1)

    with grapes.timer():
        time.sleep(0.1)

    t = grapes.timer()
    t.start()
    time.sleep(0.1)
    t.stop()


if __name__ == "__main__":
    main()
