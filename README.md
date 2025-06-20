# tavern_automation

This repository shows how to test an API using [Tavern](https://tavern.dev/).
All test suites live in the `tests/` directory. The application under test is
expected to be running separately. See 

## Project layout

- `tests/` – Additional Tavern YAML tests and pytest fixtures.
- `config/` – YAML snippets included by the tests, such as the base URL.
- `data/` – Sample request bodies and expected responses.
- `plugins/` – Custom pytest hooks used during testing.

## Requirements

Install the required packages in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install pytest pytest-tavern
```

## Running the tests

Ensure the target API is reachable at the base URL configured in
`config/settings.yaml` (default: `http://localhost:5000`). Then execute all
tests using `pytest`:

```bash
pytest tests/quotes/ --junitxml=results.xml
```

A summary of the last run is written to `results.xml`.