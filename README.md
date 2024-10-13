## API tests

## Environment Setup
1. In case of running tests on user machine:
- Install Python 3.12.0

## Usage

### Run tests on local machine
1. Install requirements: `pip install -r requirements.txt`
2. Run command under the `petSore` directory : `pytest -s -v -n 2 --reruns 1 --reruns-delay 5 --html=reports/pet_report.html --self-contained-html`
