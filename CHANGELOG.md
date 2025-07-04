# Changelog

## [0.3.4](https://github.com/liblaf/grapes/compare/v0.3.3..v0.3.4) - 2025-07-04

### 📝 Documentation

- update commit hash in copier answers and correct readthedocs JavaScript path - ([a33f1fc](https://github.com/liblaf/grapes/commit/a33f1fc3431a79a284d4df161b7bec99a24f6aba))
- disable privacy plugin in mkdocs - ([9b2289d](https://github.com/liblaf/grapes/commit/9b2289d41c6ad1bb739a3cc0248a7b36c24f3acb))

### ❤️ New Contributors

- [@liblaf](https://github.com/liblaf) made their first contribution

## [0.3.3](https://github.com/liblaf/grapes/compare/v0.3.2..v0.3.3) - 2025-07-04

### ✨ Features

- **functools:** add cache utilities and platformdirs integration - ([8f73830](https://github.com/liblaf/grapes/commit/8f738306e19e01577dfea8824118e322d17ebea0))

## [0.3.2](https://github.com/liblaf/grapes/compare/v0.3.1..v0.3.2) - 2025-07-01

### ✨ Features

- **config:** add centralized configuration system - ([7eeae03](https://github.com/liblaf/grapes/commit/7eeae0304ba1fe40eb997353e39df4530179243b))

## [0.3.1](https://github.com/liblaf/grapes/compare/v0.3.0..v0.3.1) - 2025-06-23

### ⬆️ Dependencies

- **deps:** standardize lazy-loader version pin - ([690f814](https://github.com/liblaf/grapes/commit/690f81482ee73543b168f08fa3200ae98792f697))
- **deps:** pin dependency versions - ([514cd3b](https://github.com/liblaf/grapes/commit/514cd3b47c63010e9e5e5f67c258ce97d60700b8))
- **deps:** remove version constraints from dependencies - ([5500a05](https://github.com/liblaf/grapes/commit/5500a050976da7f6640334ec932dc29597ae08fb))

## [0.3.0](https://github.com/liblaf/grapes/compare/v0.2.3..v0.3.0) - 2025-06-23

### 💥 BREAKING CHANGES

- **timing:** restructure timing module and add depth tracking - ([1d160d8](https://github.com/liblaf/grapes/commit/1d160d87c5281d4dfa4bef1aff196e35dcc765f7))

### ♻ Code Refactoring

- **logging:** split depth tracker into context manager and tracker - ([2b77ae0](https://github.com/liblaf/grapes/commit/2b77ae0f4280dfb65be5468c83886fe482c586ae))
- clean up timing module and build config - ([3973878](https://github.com/liblaf/grapes/commit/39738789aa1c26d166bb8b84f4caeb220b766197))

## [0.2.3](https://github.com/liblaf/grapes/compare/v0.2.2..v0.2.3) - 2025-06-22

### ✨ Features

- **error:** add DispatchLookupError class - ([0efbe4f](https://github.com/liblaf/grapes/commit/0efbe4f68d26e5b0860463415ba6a6db73770fb2))

### 🐛 Bug Fixes

- **logging:** improve traceback formatting and add ANSI support - ([52940fb](https://github.com/liblaf/grapes/commit/52940fbdec25cff392e573d5562d1dd3bb827e7e))

### ♻ Code Refactoring

- **logging:** simplify filter dispatch - ([fbe4bf6](https://github.com/liblaf/grapes/commit/fbe4bf6921b3f15adb724a14eee37cb6a767a2ac))

## [0.2.2](https://github.com/liblaf/grapes/compare/v0.2.1..v0.2.2) - 2025-06-11

### ✨ Features

- **functools:** add clone_signature utility - ([4caccca](https://github.com/liblaf/grapes/commit/4caccca48893ed9beca43386ff1e826615b69fd5))

## [0.2.1](https://github.com/liblaf/grapes/compare/v0.2.0..v0.2.1) - 2025-06-09

### 🐛 Bug Fixes

- **logging:** properly register loguru levels with logging module - ([94b008e](https://github.com/liblaf/grapes/commit/94b008e8c561706098e963636b58bd32ea5f3051))

### ♻ Code Refactoring

- **logging:** move LogLevel to logging module - ([cfb0272](https://github.com/liblaf/grapes/commit/cfb027298b22fd75cc9c943662381f1a12b2d526))

## [0.2.0](https://github.com/liblaf/grapes/compare/v0.1.35..v0.2.0) - 2025-06-05

### 💥 BREAKING CHANGES

- reorganize utilities and clean up deprecated code - ([f9858c2](https://github.com/liblaf/grapes/commit/f9858c2b99deb4822fc996a7ecba19cc0ca704e4))

### ♻ Code Refactoring

- **functools:** improve ConditionalDispatcher implementation - ([6b49bef](https://github.com/liblaf/grapes/commit/6b49beffd6da362598f4f8a74a796b4349ec2aa9))

## [0.1.35](https://github.com/liblaf/grapes/compare/v0.1.34..v0.1.35) - 2025-06-03

### ✨ Features

- **error:** add MatchError class - ([cd9319d](https://github.com/liblaf/grapes/commit/cd9319d6db49da32fdc9e14e5b837768b3fbe4bc))

## [0.1.34](https://github.com/liblaf/grapes/compare/v0.1.33..v0.1.34) - 2025-06-03

### ✨ Features

- **tqdm:** add type overloads for parallel function - ([9cbd71f](https://github.com/liblaf/grapes/commit/9cbd71f60f6024bed707c67bc2ea4ccb6a14d119))

### 🐛 Bug Fixes

- **logging:** add null checks for logger instances - ([146c58f](https://github.com/liblaf/grapes/commit/146c58fe6714897425dc2710671639fe4709d5ee))
- **tqdm:** use direct local imports for joblib utilities - ([36f5e07](https://github.com/liblaf/grapes/commit/36f5e07afe0945097ec5f71451d101042ae0b9ba))

## [0.1.33](https://github.com/liblaf/grapes/compare/v0.1.32..v0.1.33) - 2025-06-02

### ✨ Features

- **logging:** handle unraisable exceptions - ([19b137f](https://github.com/liblaf/grapes/commit/19b137ff6eb1f036874161ac050fcc7c68b5d86c))

## [0.1.32](https://github.com/liblaf/grapes/compare/v0.1.31..v0.1.32) - 2025-05-31

### 🐛 Bug Fixes

- **logging:** properly handle ANSI escape sequences in messages - ([7b771ed](https://github.com/liblaf/grapes/commit/7b771edd16805aa8db4a927acdafa1655fac52d6))

## [0.1.31](https://github.com/liblaf/grapes/compare/v0.1.30..v0.1.31) - 2025-05-28

### ✨ Features

- **tqdm:** set timer name from progress description - ([f243bea](https://github.com/liblaf/grapes/commit/f243bea321cf612ae32ccd735bfc6d2d9c1fdb05))

## [0.1.30](https://github.com/liblaf/grapes/compare/v0.1.29..v0.1.30) - 2025-05-27

### 🐛 Bug Fixes

- **serde:** handle file extension stripping consistently - ([f75c986](https://github.com/liblaf/grapes/commit/f75c9868b324820337c1447228fcefdedd728408))

## [0.1.29](https://github.com/liblaf/grapes/compare/v0.1.28..v0.1.29) - 2025-05-26

### 🐛 Bug Fixes

- **pretty:** handle wrapped functions in pretty printing - ([3e42a50](https://github.com/liblaf/grapes/commit/3e42a502421bfd2ed9a6c85786d93ae7675d6a93))

### ♻ Code Refactoring

- **pretty:** improve function pretty printing robustness - ([09b6f87](https://github.com/liblaf/grapes/commit/09b6f8731e18b7ac4fc8ee503abca86ae3b4739d))

### 🔧 Continuous Integration

- update MegaLinter workflow to use head ref - ([4f57647](https://github.com/liblaf/grapes/commit/4f57647f9d1fadeaa593997cbf5f06d22e231b07))
- reorder workflow steps and update linter configuration - ([4844ce1](https://github.com/liblaf/grapes/commit/4844ce195885b7afddfbba214371093304053acd))

## [0.1.28](https://github.com/liblaf/grapes/compare/v0.1.27..v0.1.28) - 2025-05-25

### ✨ Features

- **timing:** add threshold parameter to skip logging fast operations - ([a233683](https://github.com/liblaf/grapes/commit/a233683a98c1cd808b3183d36929d49d7c1a8b54))

### 👷 Build System

- migrate from mise to direnv for Python environment management - ([dea6790](https://github.com/liblaf/grapes/commit/dea67905419cb82cac356bbc00e2b515c8ba65f3))

## [0.1.27](https://github.com/liblaf/grapes/compare/v0.1.26..v0.1.27) - 2025-05-24

### ✨ Features

- **docs:** switch from mike to mkdocs for documentation - ([51a836a](https://github.com/liblaf/grapes/commit/51a836a5913b6f53fe460a56967b51bcbc634423))

### 🐛 Bug Fixes

- update project dependencies - ([eb01ec6](https://github.com/liblaf/grapes/commit/eb01ec6f8608b05d8ea7599746aaacb08209a83c))

### 📝 Documentation

- update copier configuration files - ([1ac9813](https://github.com/liblaf/grapes/commit/1ac9813c7b7b763269e8f837fcc20d84ea8b45cc))

### 🔧 Continuous Integration

- update ReadTheDocs configuration to use asdf and uv - ([8fbcc4a](https://github.com/liblaf/grapes/commit/8fbcc4a5380a9b1ab864e9f353e33a84ae3490e5))
- add Read the Docs configuration file - ([7215139](https://github.com/liblaf/grapes/commit/72151396a3ed1befb60721ca8ff2ec3ce56e61fc))

## [0.1.26](https://github.com/liblaf/grapes/compare/v0.1.25..v0.1.26) - 2025-05-24

### ✨ Features

- **logging:** add enable_link parameter to control rich handler links - ([e6b606a](https://github.com/liblaf/grapes/commit/e6b606abdfeac325d0b433e663f1c004055eb0e3))
- **timing:** refactor timer implementation and add parallel processing - ([2a13037](https://github.com/liblaf/grapes/commit/2a1303744a397e5939d714a4a715fe85821815f2))

## [0.1.25](https://github.com/liblaf/grapes/compare/v0.1.24..v0.1.25) - 2025-05-22

### 🐛 Bug Fixes

- **logging:** improve rich console output handling - ([083778d](https://github.com/liblaf/grapes/commit/083778def714fb9907ea274024beb7f9204cdb8d))

### 👷 Build System

- migrate from pixi to uv package manager - ([86d8b6c](https://github.com/liblaf/grapes/commit/86d8b6cc0b46d053b4269e473e6ad216ec51619f))
- migrate from pixi to uv for package management - ([f9028e7](https://github.com/liblaf/grapes/commit/f9028e7eb996fd8355ec2bee19c6a21df98d76e2))

## [0.1.24](https://github.com/liblaf/grapes/compare/v0.1.23..v0.1.24) - 2025-05-22

### ✨ Features

- **serde:** replace tomlkit and ruamel.yaml with msgspec - ([5b0c626](https://github.com/liblaf/grapes/commit/5b0c626633401da14588032b72cc4d03f5057c42))

### ♻ Code Refactoring

- **logging:** restructure rich logging handler with column-based approach - ([8cdf600](https://github.com/liblaf/grapes/commit/8cdf600387b915f14d7d185a2b525bdf130f9ba4))

## [0.1.23](https://github.com/liblaf/grapes/compare/v0.1.22..v0.1.23) - 2025-05-09

### ✨ Features

- **grapes:** reorganize modules and improve logging - ([ef28cd1](https://github.com/liblaf/grapes/commit/ef28cd103f43f4423a2884dbb3cf2a358269fc9a))
- **timing:** add timer support and improve logging defaults - ([69f55d4](https://github.com/liblaf/grapes/commit/69f55d4fb6987038f2875d5bcdba9152517f77d9))

### ♻ Code Refactoring

- **timing:** simplify timer implementation and callback handling - ([3eaaa2a](https://github.com/liblaf/grapes/commit/3eaaa2a60079efe99981105a73d72f26441972a2))

## [0.1.22](https://github.com/liblaf/grapes/compare/v0.1.21..v0.1.22) - 2025-05-07

### 🐛 Bug Fixes

- **logging:** simplify rich handler and location formatting - ([47e46d0](https://github.com/liblaf/grapes/commit/47e46d06e2c06652d9c0cdc5cbdcc78efaf940da))

## [0.1.21](https://github.com/liblaf/grapes/compare/v0.1.20..v0.1.21) - 2025-05-05

### 🐛 Bug Fixes

- **logging:** replace default_filter with make_filter - ([a5d5e5b](https://github.com/liblaf/grapes/commit/a5d5e5b542495b0c9224ecb0e37f4e366b55b540))

## [0.1.20](https://github.com/liblaf/grapes/compare/v0.1.19..v0.1.20) - 2025-04-25

### ♻ Code Refactoring

- simplify logging benchmarks and environment variables - ([97b79d3](https://github.com/liblaf/grapes/commit/97b79d3db0c246eb3752845d4d9fd945c8e6a706))

## [0.1.19](https://github.com/liblaf/grapes/compare/v0.1.18..v0.1.19) - 2025-04-23

### ✨ Features

- **path:** replace find_project_dir with project_root and resolve_project_path - ([9a3f474](https://github.com/liblaf/grapes/commit/9a3f47451f6b1357fbaef2562c2104a0df0d406a))

### ♻ Code Refactoring

- **logging:** simplify logging configuration and remove deprecated features - ([c7b05bc](https://github.com/liblaf/grapes/commit/c7b05bce014ef623f0bdd002bc44b0c06f4e3543))
- **logging:** reorganize logging module structure and improve functionality - ([09c09da](https://github.com/liblaf/grapes/commit/09c09daab6245985701edff50cdcfa03c2294acf))

## [0.1.18](https://github.com/liblaf/grapes/compare/v0.1.17..v0.1.18) - 2025-04-06

### ♻ Code Refactoring

- **typed:** rename StrPath to PathLike for clarity - ([cdb4f96](https://github.com/liblaf/grapes/commit/cdb4f968398db334adf5f3333d129dd494b9415e))

## [0.1.17](https://github.com/liblaf/grapes/compare/v0.1.16..v0.1.17) - 2025-03-31

### 🐛 Bug Fixes

- **path:** correct project directory path resolution - ([b808842](https://github.com/liblaf/grapes/commit/b808842ca50e4033ec0d40bac0f2354f26391056))

## [0.1.16](https://github.com/liblaf/grapes/compare/v0.1.15..v0.1.16) - 2025-03-31

### 🐛 Bug Fixes

- **timing:** set `slots=False` for `TimedFunction` to support `functools.update_wrapper` - ([aebf7e2](https://github.com/liblaf/grapes/commit/aebf7e27637faa7f65ebf7fb78a4482745eb3fce))

## [0.1.15](https://github.com/liblaf/grapes/compare/v0.1.14..v0.1.15) - 2025-03-31

### 🐛 Bug Fixes

- **timing:** make wrapped objects immutable and update function wrapper - ([72d6440](https://github.com/liblaf/grapes/commit/72d64404cf6d04d5b71951b989b2dc7627c0663e))

### ♻ Code Refactoring

- **pretty:** reorganize pretty module and add find_project_dir - ([68b67dc](https://github.com/liblaf/grapes/commit/68b67dccf7445e256c6d0684c0c4913b73b36c4f))

## [0.1.14](https://github.com/liblaf/grapes/compare/v0.1.13..v0.1.14) - 2025-03-31

### ✨ Features

- **functools:** add decorator with optional arguments support - ([c0b86a0](https://github.com/liblaf/grapes/commit/c0b86a03bb9ddabaedf3ea82294fe8fd156f15fd))

### ⬆️ Dependencies

- **deps:** update dependency rich to v14 (#34) - ([e3e1e09](https://github.com/liblaf/grapes/commit/e3e1e09bdbd5fce6e9020cbd29ed256058780ea9))

## [0.1.13](https://github.com/liblaf/grapes/compare/v0.1.12..v0.1.13) - 2025-03-29

### ✨ Features

- **logging:** add default log format to file handler - ([257f508](https://github.com/liblaf/grapes/commit/257f508f79e0a85914cef0272421465feb2db66b))

### ♻ Code Refactoring

- **logging:** reorganize logging module structure and improve functionality - ([a680077](https://github.com/liblaf/grapes/commit/a6800778a4ada4213e9ca2198d7163d589926a97))

## [0.1.12](https://github.com/liblaf/grapes/compare/v0.1.11..v0.1.12) - 2025-03-28

### ✨ Features

- **logging:** add clear_handlers function and integrate with loguru - ([a4f2954](https://github.com/liblaf/grapes/commit/a4f2954dde68dd69e6892a4afec7fbb21683609a))
- enhance testing and benchmarking capabilities - ([c1c4eae](https://github.com/liblaf/grapes/commit/c1c4eae12c43fd6365cc08260a257cbfb484d2dd))

### 📝 Documentation

- update README with project description and features - ([6cdd39f](https://github.com/liblaf/grapes/commit/6cdd39fec0cb888dd63e0974508c6f52007263db))
- update README.md and mkdocs.yaml for improved formatting and clarity - ([49d6e20](https://github.com/liblaf/grapes/commit/49d6e20a3f48cc30b14d4c55414ab2de3c79fa14))

### ♻ Code Refactoring

- **timing:** restructure timer implementation and add protocol support - ([34e0b84](https://github.com/liblaf/grapes/commit/34e0b8418bd180cd6444d1badf2f9d16296a5e31))

### 🔧 Continuous Integration

- rename workflow from 'Test' to 'Bench' - ([228bfb3](https://github.com/liblaf/grapes/commit/228bfb3b83022fec0ebe4449e67b9434c8795c53))
- restructure workflows and add benchmark support - ([7e2e3a5](https://github.com/liblaf/grapes/commit/7e2e3a5e636ae3ac315d86a6cfb9e70acdb2b4ee))
- update GitHub Pages token configuration and repository references - ([679759f](https://github.com/liblaf/grapes/commit/679759f2eca7eaea5d8f1947af5919e24b5ddcfb))
- add GitHub Pages write permissions and setup action - ([bd19931](https://github.com/liblaf/grapes/commit/bd1993141a9852aacf0d5b30a5d012c8bca178c4))
- refactor GitHub Actions workflows for docs - ([eaec10d](https://github.com/liblaf/grapes/commit/eaec10d0700a9e15c7af47983fe7b770ac8175bb))
- conditionally run docs workflow on version tags - ([e0c2aec](https://github.com/liblaf/grapes/commit/e0c2aecd233210509188b80227337a6224d7b216))
- add GitHub workflows for docs deployment and testing - ([74b1906](https://github.com/liblaf/grapes/commit/74b190662918bf6c4ace03677c958731c147f3cb))

## [0.1.11](https://github.com/liblaf/grapes/compare/v0.1.10..v0.1.11) - 2025-03-23

### ♻ Code Refactoring

- **environ:** modify `init_env` to accept a path parameter - ([c35581a](https://github.com/liblaf/grapes/commit/c35581a400d16dfcf25e83d594766b70abb1de30))

## [0.1.10](https://github.com/liblaf/grapes/compare/v0.1.9..v0.1.10) - 2025-03-19

### 🐛 Bug Fixes

- **serde:** replace `warnings.deprecated` with `typing_extensions.deprecated` - ([ad88773](https://github.com/liblaf/grapes/commit/ad8877387f608e3c0382d9006c82054966a81dfe))

### ♻ Code Refactoring

- **logging:** replace DEFAULT_FILTER with default_filter function - ([33c7ad3](https://github.com/liblaf/grapes/commit/33c7ad3e78432231d8c117c05e2bf747e1ba69f0))

### 🔧 Continuous Integration

- update release-please config and manifest file paths - ([5a278e8](https://github.com/liblaf/grapes/commit/5a278e82c88a29422343194d41674c923c9fb315))

## [0.1.9](https://github.com/liblaf/grapes/compare/v0.1.8..v0.1.9) - 2025-03-18

### ✨ Features

- update package metadata and add type hints support - ([f561c77](https://github.com/liblaf/grapes/commit/f561c77bee9c1ace68bb0ab0d279f8a50aa52fc6))

## [0.1.8](https://github.com/liblaf/grapes/compare/v0.1.7..v0.1.8) - 2025-03-18

### ✨ Features

- **logging:** enhance loguru configuration with default level and improved filter_once - ([1e72e8e](https://github.com/liblaf/grapes/commit/1e72e8e5c242a0d2259dc989fce3f85848801741))
- **logging:** add conditional dispatcher and enhance loguru filters - ([db8f046](https://github.com/liblaf/grapes/commit/db8f046765da4509cc2ee25906ff90c3d5946b65))

### ♻ Code Refactoring

- **logging:** reorganize imports and rename filter types module - ([9e2aa67](https://github.com/liblaf/grapes/commit/9e2aa6753822f74a5d8c564f34b7494763d5e07d))

## [0.1.7](https://github.com/liblaf/grapes/compare/v0.1.6..v0.1.7) - 2025-03-11

### ✨ Features

- **logging:** refactor loguru module and add JSONL logging support - ([1bcfc19](https://github.com/liblaf/grapes/commit/1bcfc19a2b47f2fd782ee1ee94a8a8c55d6c460e))
- **serde:** add AutoSerializer to public API - ([8152e80](https://github.com/liblaf/grapes/commit/8152e80b0b82df425e1b9798d0bac030961a7c84))

## [0.1.6](https://github.com/liblaf/grapes/compare/v0.1.5..v0.1.6) - 2025-03-10

### ✨ Features

- **serde:** add dump/load functions and deprecate serialize/deserialize - ([0bc118f](https://github.com/liblaf/grapes/commit/0bc118f3415863412f4eff67d1418a44debecd96))

### ♻ Code Refactoring

- **serde:** rename dump/dumps methods to save/saves for clarity - ([a8feb62](https://github.com/liblaf/grapes/commit/a8feb621087bbb2f734b87950ba05523d0cb4224))

## [0.1.5](https://github.com/liblaf/grapes/compare/v0.1.4..v0.1.5) - 2025-03-09

### ✨ Features

- **git:** add GitInfo and info function for parsing git repository URLs - ([7699aab](https://github.com/liblaf/grapes/commit/7699aab9b86dabda009e2888878bf6d328865c3b))

### ♻ Code Refactoring

- **serde:** introduce AbstractSerializer for JSON, TOML, and YAML - ([83860b1](https://github.com/liblaf/grapes/commit/83860b1131391d3847f3b040fcefe1013caf924e))

## [0.1.4](https://github.com/liblaf/grapes/compare/v0.1.3..v0.1.4) - 2025-03-08

### ♻ Code Refactoring

- **serde:** replace autoregistry with plain dict for READERS and WRITERS - ([10a33f2](https://github.com/liblaf/grapes/commit/10a33f25d747e3e988be52815251d4a2c4adb4a4))

## [0.1.3](https://github.com/liblaf/grapes/compare/v0.1.2..v0.1.3) - 2025-03-08

### ✨ Features

- **git:** add git root detection utilities - ([6034ef0](https://github.com/liblaf/grapes/commit/6034ef071776a9acc5ad960158c9c23fa649e3c1))

### ✅ Tests

- add sample test and configure pytest options - ([0c3a082](https://github.com/liblaf/grapes/commit/0c3a082b4334db7aa80ebfb0a62054c16f44652a))

## [0.1.2](https://github.com/liblaf/grapes/compare/v0.1.1..v0.1.2) - 2025-02-23

### ♻ Code Refactoring

- add default value to `row` method - ([641858a](https://github.com/liblaf/grapes/commit/641858ab0827e010d4b88d3118905478a9053298))

## [0.1.1](https://github.com/liblaf/grapes/compare/v0.1.0..v0.1.1) - 2025-02-17

### ✅ Tests

- configure pytest options in pyproject.toml - ([56defba](https://github.com/liblaf/grapes/commit/56defba01241189b074eab59ae9df528e4c8bcbb))
- Add pytest configuration and enhance timing module - ([ab798a8](https://github.com/liblaf/grapes/commit/ab798a843e7ef72016150c50b9c72489a2656470))

## [0.1.0](https://github.com/liblaf/grapes/compare/v0.0.5..v0.1.0) - 2025-02-16

### ♻ Code Refactoring

- replace numpy with standard library for timing calculations - ([fa8a985](https://github.com/liblaf/grapes/commit/fa8a985c2561b8f9346b22214ba7df9c7a75b00d))

## [0.0.5](https://github.com/liblaf/grapes/compare/v0.0.4..v0.0.5) - 2025-02-14

### ✨ Features

- **logging:** add `warning_once` function to logging utilities - ([a7e64ce](https://github.com/liblaf/grapes/commit/a7e64ce033f246837d57b17dd3645aa466eea148))

### 👷 Build System

- update project configuration and dependencies - ([94683e5](https://github.com/liblaf/grapes/commit/94683e588f423b0df3103905a45199a9561d753c))

## [0.0.4](https://github.com/liblaf/grapes/compare/v0.0.3..v0.0.4) - 2025-02-09

### ✨ Features

- add path utilities and update type hints - ([b66c1bd](https://github.com/liblaf/grapes/commit/b66c1bd4f4ad3abb56de4d5268fa7be98e98f68a))
- add itertools module and logging once functions - ([10ad9cf](https://github.com/liblaf/grapes/commit/10ad9cfc1ace865296c1c380445750d0ca988187))

### ⬆️ Dependencies

- **deps:** update dependency boltons to v25 (#11) - ([cae7976](https://github.com/liblaf/grapes/commit/cae797647886d4fd8c2a2ae4d469ba4b3910f7fc))

### 📝 Documentation

- add line breaks for readability in serde docs - ([74f6f2c](https://github.com/liblaf/grapes/commit/74f6f2cf4843f13b3394cf9e47eeb30841ec28c2))
- add and update module docstrings - ([4740926](https://github.com/liblaf/grapes/commit/4740926faaebf47554065524d246b2c66fc64dd6))
- update and correct inventory URLs - ([45c6835](https://github.com/liblaf/grapes/commit/45c6835f732df6f35d979b439cf181b2dbb1e2f2))
- update and enhance documentation setup - ([39b1dad](https://github.com/liblaf/grapes/commit/39b1dada99ca91812cdc69483a9d7fcfbc3b9b49))
- add markdown support in HTML for README - ([eaafe22](https://github.com/liblaf/grapes/commit/eaafe22ac26e833788da5e9e7bde38b02e6d3713))

### ♻ Code Refactoring

- **docs:** replace Python asset download script with shell script - ([4fe1869](https://github.com/liblaf/grapes/commit/4fe1869a0f76ffd45d18f74bfa971c3a1bc7f01c))
- **timer:** simplify time counter logic and improve TimerRecords class - ([b40c2c3](https://github.com/liblaf/grapes/commit/b40c2c37fc5dd5c2afdf23727e355db4a8c38800))
- remove unused dependencies and update imports - ([69bfcf4](https://github.com/liblaf/grapes/commit/69bfcf45474d3a7dd5dae6abff8ea92c302d1e20))
- reorganize timer and optional imports modules - ([a362ce5](https://github.com/liblaf/grapes/commit/a362ce55e4979c94601bb192c75bb5ac2869faa2))

### 🔧 Continuous Integration

- remove redundant docs workflow - ([fad79ce](https://github.com/liblaf/grapes/commit/fad79cebc04e47a35fbf1de9ccfaa13aa863a86a))

## [0.0.3](https://github.com/liblaf/grapes/compare/v0.0.2..v0.0.3) - 2025-02-02

### ♻ Code Refactoring

- **grapes:** rename progress to progress_bar and enhance timer reporting - ([870b497](https://github.com/liblaf/grapes/commit/870b497df9f11eb3465d2de5da6bcd29c9f07f59))

### ❤️ New Contributors

- [@renovate[bot]](https://github.com/apps/renovate) made their first contribution in [#9](https://github.com/liblaf/grapes/pull/9)

## [0.0.1](https://github.com/liblaf/grapes/compare/v0.0.0..v0.0.1) - 2025-01-20

### ✨ Features

- add documentation workflow and assets - ([daca118](https://github.com/liblaf/grapes/commit/daca1183a8f7685a35be4a61ce3d8833f7f6c593))
- add MkDocs documentation setup and configuration - ([4830aee](https://github.com/liblaf/grapes/commit/4830aee1fbedc0c1321597bbeb1fc6ba56828aee))

### 🐛 Bug Fixes

- correct logo asset format from SVG to PNG - ([ae3c6a6](https://github.com/liblaf/grapes/commit/ae3c6a6b55bc00f9ab0c706cfde7d5893d51ebad))

### ♻ Code Refactoring

- improve code reference generation and documentation setup - ([9911c42](https://github.com/liblaf/grapes/commit/9911c4229e79b0228505a6bb0af255c063e5a187))

### 🔧 Continuous Integration

- update docs workflow and bump numpy version - ([6d3417e](https://github.com/liblaf/grapes/commit/6d3417ea9a5152e6015c7b0542095cf7e5d7a202))
- improve GitHub Actions workflow and asset download script - ([9f9323e](https://github.com/liblaf/grapes/commit/9f9323e97353f3af04a0121a0baf51b6ce213da0))

### ❤️ New Contributors

- [@liblaf-bot[bot]](https://github.com/apps/liblaf-bot) made their first contribution

## [0.0.0] - 2025-01-16

### ✨ Features

- **human:** add human_duration_series function and numpy dependency - ([f896854](https://github.com/liblaf/grapes/commit/f89685440683d5ff49fca0bb04a93cde66411381))
- **human:** add human-readable formatting for counts, durations, and throughput - ([7ab9ba7](https://github.com/liblaf/grapes/commit/7ab9ba7c0ca089f187cf32f5e8b82be43961fcfe))
- **serde:** add serialization/deserialization utilities - ([ba4cb55](https://github.com/liblaf/grapes/commit/ba4cb5506ff89af6859b635c84eae6b9a0bc61ea))
- **text:** add `strip_comments` utility for text processing - ([2144402](https://github.com/liblaf/grapes/commit/2144402c77b7a264e6ed1fbb2c3324b9c02b07a2))
- **timer:** enhance timer functionality and integrate with progress tracking - ([71c624d](https://github.com/liblaf/grapes/commit/71c624df066e54372251938b595dd1a4fcaa6dee))
- **timer:** enhance timer functionality and improve logging - ([7e3bcd3](https://github.com/liblaf/grapes/commit/7e3bcd312bbe657c9faa1184a5d578e5ef1a064f))
- **timer:** add TimerRecords class for tracking and reporting timing data - ([b73560e](https://github.com/liblaf/grapes/commit/b73560e6922eb38f82214932a248ebb4c2c47edb))
- add progress tracking and improve logging initialization - ([9a9764f](https://github.com/liblaf/grapes/commit/9a9764f1a15d3dd98db0615d1d9dd8723d65bd1b))
- add initial project structure and core functionality - ([03b5855](https://github.com/liblaf/grapes/commit/03b5855a860f269a10ebc471206979230fba5a13))

### ♻ Code Refactoring

- **logging:** extract caller location and function name utilities - ([a46420e](https://github.com/liblaf/grapes/commit/a46420e8c075282c1fd6577e42f65d92968080b2))

### 👷 Build System

- add twine check to build process and update dependencies - ([a07cce2](https://github.com/liblaf/grapes/commit/a07cce284b00e7ad178dc53cdf300636164d3c1a))
- add build task and update dependencies - ([d7557c7](https://github.com/liblaf/grapes/commit/d7557c73178492bde5e51270a8a0b3756ed82d6d))
- restructure project and update dependencies - ([8788a7c](https://github.com/liblaf/grapes/commit/8788a7c99b02aac2bcd6183c2bd7484a58fdf4b2))

### ❤️ New Contributors

- [@release-please[bot]](https://github.com/apps/release-please) made their first contribution in [#4](https://github.com/liblaf/grapes/pull/4)
- [@liblaf](https://github.com/liblaf) made their first contribution
