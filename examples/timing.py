import time

from liblaf import grapes


@grapes.timer()
def func() -> None:
    time.sleep(0.1)


def main() -> None:
    grapes.init_logging()

    for _ in range(10):
        func()
    grapes.get_timer(func).finish()

    for _ in grapes.timer(range(10)):
        time.sleep(0.1)

    t: grapes.Timer = grapes.timer("With")
    for _ in range(10):
        with t:
            time.sleep(0.1)
    t.finish()

    t = grapes.timer("Start / Stop")
    for _ in range(10):
        t.start()
        time.sleep(0.1)
        t.stop()
    t.finish()

    with grapes.Progress() as progress:
        for _ in progress.track(range(10)):
            time.sleep(0.1)

    for _ in grapes.track(range(10)):
        time.sleep(0.1)


if __name__ == "__main__":
    main()
