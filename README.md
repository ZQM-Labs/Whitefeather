# Whitefeather

Whitefeather operational tooling.

## About

`Whitefeather` is part of the ZQM operational brand toolchain. It provides capabilities for [specific purpose extracted from repo tooling].

## Installation

```bash
pip install -e .
```

Requires Python 3.11+.

## Usage

```bash
# CLI entry point
whitefeather --help
```

## Features

- Operational workflow automation
- Fleet attestation integration via zqm-intel-platforms
- Evidence packaging and provenance tracking
- Configurable report generation
- CI-validated codebase with ruff/mypy

## CI

[![CI](https://github.com/ZQM-Labs/Whitefeather/actions/workflows/ci.yml/badge.svg)](https://github.com/ZQM-Labs/Whitefeather/actions)
[![Ruff](https://img.shields.io/badge/lint-ruff-blue)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/typecheck-mypy-blue)](https://github.com/python/mypy)

## Integration: zqm-intel-platforms

`Whitefeather` declares `zqm-intel-platforms>=0.1.0` and participates in the fleet attestation mesh.

- Hub role: operational data collection and routing
- Downstream: zqm-attestation-toolkit, zqm-sword

## License

MIT — see LICENSE file.

## Contact

Alex Zelenski — zqmcomputing@gmail.com
Brand: ZQM Computing / ZQM-Labs
