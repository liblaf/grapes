from __future__ import annotations

from typing import TYPE_CHECKING, Any

import attrs

from liblaf.grapes import deps

if TYPE_CHECKING:
    from matplotlib.figure import Figure


@attrs.define
class BenchResults:
    results: dict[str, Any]
    sizes: list[float]
    timings: dict[str, list[float]]

    def plot(
        self,
        *,
        relative_to: str | None = None,
        title: str = "Benchmark Results",
        xlabel: str = "Size",
        xscale: str = "log",
        ylabel: str = "Time (sec)",
        yscale: str = "log",
    ) -> Figure:
        with deps.optional_deps("liblaf-grapes", "bench"):
            import matplotlib.pyplot as plt
        fig: Figure = plt.figure()
        for label, timings in self.timings.items():
            if relative_to is not None:
                base: list[float] = self.timings[relative_to]
                relative: list[float] = [
                    t / b for t, b in zip(timings, base, strict=True)
                ]
                plt.plot(self.sizes, relative, label=label)
            else:
                plt.plot(self.sizes, timings, label=label)
        plt.grid(which="both", linestyle="--")
        plt.legend()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.xscale(xscale)
        plt.ylabel(ylabel)
        plt.yscale(yscale)
        return fig
