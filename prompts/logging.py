# We are somewhat satisfied with current implementation.
# Only one root logger is allowed to write to stderr to avoid duplicate log messages.
# The user can add additional destinations for log messages, such as file etc.
# log messages should be pretty printed with rich. We like current format.
# Note the time format. We should allow user to use relative / absolute time format or allow customization.
# We should also install exception hook or other similar hooks to log exceptions with rich traceback in log.


# To avoid hard dependency on `liblaf.traceback`, we should provide an API to custom traceback formatting function, so that user can use `liblaf.traceback` or other traceback formatting libraries to format traceback in log messages. By default, we should use `liblaf.traceback` when it's available, otherwise use standard library `traceback` module.


# Usually each module has a logger. By default, modules from stable release should use WARNING level. While modules from pre-release version should use INFO level. dev version should use lowest level to print everything. Those levels should be customizable.


# This library should also provide an `ic()` like API for quick debug variables.
# `ic()` should default go into logging system instead of directly go to stderr.
# In addition to `ic()`, we should also allow user to custom print functions.
# If `liblaf.pprint` is available, we should use that.
