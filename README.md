# cookiecutter-mlflow-mlproject
Cookie cutter template to create containerized MLflow Projects for production

## Quick Start

### Prerequisites

- Python 3.11+
- Poetry
- Docker

### Setup

Install dependencies:

```bash
poetry install
```

Activate the virtual environment:

```bash
poetry shell
# or
poetry env activate
```

### Generate a New Model

```bash
cookiecutter https://github.com/kagankalafat/cookiecutter-mlflow-mlproject
```

- Enter the model name when prompted, then press Enter.
- Copy `.env.example` to `.env` in your new model repository and fill in the required values.