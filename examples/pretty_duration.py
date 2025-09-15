import about_time
import rich
from rich.table import Table

from liblaf import grapes


def main() -> None:
    sec_list: list[float] = []
    for log10_sec in range(-12, 7):
        sec_list.append(0.9986 * 10**log10_sec)
        sec_list.append(10**log10_sec)
    sec_list.sort()
    table = Table("{sec:#.3g}", "liblaf.grapes", "about-time")
    for sec in sec_list:
        table.add_row(
            f"{sec:#.3g}",
            grapes.pretty_duration(sec),
            about_time.HumanDuration(sec).as_human(),
        )
    rich.print(table)


if __name__ == "__main__":
    main()
