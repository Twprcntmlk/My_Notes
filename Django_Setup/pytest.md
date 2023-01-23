./helpers/run-pytest.sh

./helpers/run-pytest.sh -s -vv -m require_django_settings_module --ds mm.iam.settings


# Running Pytest
./helpers/run-pytest.sh --ds mm.iam.settings py/mm/iam

local
DEBUGPY_PORT=5678 ./helpers/run-pytest.sh --ds mm.iam.settings py/mm/iam
