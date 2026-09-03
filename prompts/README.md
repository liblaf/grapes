We are building a collection of Python projects.

The `.py` files in this directory are interface sketches, not executable
modules. They intentionally use placeholders and undefined example types while
the contracts are being designed.

- `liblaf.pprint` - to replace `wadler_lindig`, `rich.pretty`, `pprint`, `reprlib`, `rich.repr`, etc. We already have a draft `liblaf.pretty`.
- `liblaf.logging` - to setup logging. This should also replace `icecream`.
- `liblaf.traceback` - to replace standard `traceback`, `rich.traceback` with pretty traceback
- `liblaf.timeit` - timer API, like current `grapes.timer`. Info should be printed to log system instead of directly to stdout.
- `liblaf.progress` - to replace `tqdm`, `rich.progress`, etc. Progress should be printed to log system instead of directly to stdout.
- `liblaf.cache` - to replace `shelve`, `diskcache`.
- `liblaf.conf` - as we current implemented, used by other projects for config management

`liblaf.conf` is shared across our projects, so the other projects may depend on
it. The remaining projects should not hard-depend on one another. Keep their
integration seams replaceable, while allowing optional peers to improve the
default experience when installed.

"Replace" means covering the same daily workflows with a better liblaf-native
experience. It does not promise compatible imports, names, signatures, or
return types. Familiar vocabulary is useful only when it still describes the
best interface. For example, `liblaf.pprint` should expose one pretty
presentation that can render through Rich, produce deterministic text, or show
itself; it should not force those capabilities through `pformat()` or use
Rich's broad `RenderableType` as its own interface.
