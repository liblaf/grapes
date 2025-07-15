import time

from liblaf import grapes

N_ITER: int = 3
TIMEDELTA_SEC: float = 0.1


@grapes.timer()
def func() -> None:
    time.sleep(TIMEDELTA_SEC)


class A:
    @grapes.timer()
    def method(self) -> None:
        time.sleep(TIMEDELTA_SEC)


def main() -> None:
    grapes.logging.init()

    for _ in range(N_ITER):
        func()
    grapes.get_timer(func).finish()

    a = A()
    for _ in range(N_ITER):
        a.method()
    grapes.get_timer(a.method).finish()

    for _ in grapes.timer(range(N_ITER)):
        time.sleep(TIMEDELTA_SEC)

    t: grapes.Timer = grapes.timer("With")
    for _ in range(N_ITER):
        with t:
            time.sleep(TIMEDELTA_SEC)
    t.finish()

    t = grapes.timer("Manual")
    for _ in range(N_ITER):
        t.start()
        time.sleep(TIMEDELTA_SEC)
        t.stop()
    t.finish()

    with grapes.Progress() as progress:
        for _ in progress.track(range(N_ITER), description="Progress"):
            time.sleep(TIMEDELTA_SEC)

    for _ in grapes.track(range(N_ITER), description="Track"):
        time.sleep(TIMEDELTA_SEC)


if __name__ == "__main__":
    main()
