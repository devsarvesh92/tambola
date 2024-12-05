# Tambola Claim Validator

A Python implementation for validating Tambola game claims using the Strategy pattern.

## Prerequisites
- Python 3.10+
- [PDM](https://pdm.fming.dev/) for dependency management

## Installation
This project uses PDM for dependency management. First, make sure you have PDM installed:
```bash
pip install pdm
```

Then install project dependencies:
```bash
make install  # runs pdm install
```

## Development Commands
```bash
# Install dependencies
make install

# Format code (black + ruff)
make format

# Run tests
make test

# Run specific test
make run-test test=test_name

# Run demo
make run
```

## Project Structure
```
tambola/
├── src/
│   ├── domain/          # Domain models and enums
│   │   ├── ticket.py
│   │   └── claim_result.py
│   ├── strategies/      # Claim validation strategies
│   │   ├── base_claim_strategy.py
│   │   ├── top_line_claim_strategy.py
│   │   └── ...
│   ├── factory/        # Strategy creation
│   │   └── claim_strategy_factory.py
│   └── main.py        # Demo implementation
├── tests/             # Test suite
├── Makefile
├── pdm.lock          # PDM lock file
└── pyproject.toml    # Project dependencies and config
```

## Contributing
1. Install PDM if you haven't already:
```bash
pip install pdm
```

2. Install project dependencies:
```bash
make install
```

3. Format code:
```bash
make format
```

4. Run tests:
```bash
make test
```

---
> **Note**: The demo in main.py serves as a reference implementation only. For complete usage patterns, refer to the test suite.