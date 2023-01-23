<!-- for i in requirements.in requirements-test.in requirements-dev.in ; do pip-compile --generate-hashes --upgrade "${i}" ; done -->

./helpers/run-pip-compile.sh
./helpers/run-pip-sync.sh --dry-run
