# How to set-up New Python Project
https://www.youtube.com/watch?v=GeYis4ZuluY

## Set up virtualenv and pip


- Virtual File Creation
```
python3 -m venv venv
```
- Accessing Virutal Environment
```
source venv/bin/activate
```
- Deactivating Virutal Environment
```
deactivate
```

- https://pyscaffold.org/en/stable/usage.html

- pip install pyscaffold


```
pip install --upgrade pip
pip install -r requirements.txt

- to add
pylint
pytest
black
pytest-cov


pip freeze
```
<!--
## pyscaffold
```pip install --upgrade pyscaffold[all]
putup lease_allocation_rebalance
cd Lease_Allocation_Rebalance -->

```
https://www.youtube.com/watch?v=-mdv2wf8yQ8
## Makefile
```
touch Makefile

install:
pip install --upgrade pip &&\ pip install -r requirements.txt

format:
black*.py

lint:
pylint --disable=R,C {fileName.py}

test:
python3 -m pytest -vv {fileName.py}

```

make format
<!--
##  How to
from setuptools import setup, find_packages

setup(
    name="Lease Allocation Rebalance Project",
    version="1.1",
    author="Stephen Choung",
    description="Lease Rebalance Algorithm and Api",
    test_suite="tests
    packages = find_packages(exclude={'tests','tests.*'})
)

python setup.py develop -->

## Running Tests -> pytest tests/{filename.py}
- the -vv adds extra information in addition to the test passing or failing
```
pytest tests/active_and_rolling_oz_finder_test.py -vv
pytest tests/concurrent_lease_finder_test.py -vv
pytest tests/function_test.py -vv
pytest tests/lease_with_date_modifiction_test.py -vv
pytest tests/users_in_and_out_of_lease_test.py -vv

- will add more as needed
pytest tests/
```

## Useful Commands:

### You can list all the packages installed in your virtualenv by running the following command from within the environment:
```
pip list --local
```
