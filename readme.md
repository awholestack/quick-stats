# Quickstats

An example project to get started creating and testing a Click CLI. A detailed explanation is available at [A Whole Stack](https://awholestack.com/posts/building-a-python-cli/).

## Getting Started

### Installing

To perform an editable install within a virtual enviroment:

```
python -m venv env
source env/bin/activate
git clone https://github.com/awholestack/quick-stats.git
pip install -r requirements.txt
pip install --editable .
```

## Running the tests

```
pip install pytest
pytest
```

## Deployment

```bash
python setup.py sdist
pip install dist/quickstats-0.1.tar.gz
```

## Usage

```bash
$ quickstats
Usage: quickstats [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  memory  Show memory stats
```

## Built With

* [Click](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [psutil](https://maven.apache.org/) - Dependency Management
