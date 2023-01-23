#!/usr/bin/env bash
set -eux -o pipefail

MY_ROOT="$( cd "$( dirname "${0}" )" && pwd )"

if [ "${#}" -eq 0 ] ; then

    check_secrets_ready_py="$( cat <<EOF
from mm.lib.sm import aws_sm_get_secret_string
from mm.dev.aws_test_utils import aws_sm_test_client
SECRET_NAME = "_MM_DEV_LOCALSTACK_READY_AT"
secret = aws_sm_get_secret_string(aws_sm_test_client(), SECRET_NAME)
print(f"{SECRET_NAME}: {secret}")
EOF
    )"

    check_cognito_jwks_available_py="$( cat <<EOF
from mm.lib.sm import aws_sm_get_secret_string
from mm.dev.aws_test_utils import aws_sm_test_client
from jwt import PyJWKClient
SECRET_NAME = "MM_COGNITO_JWKS_URI"
secret = aws_sm_get_secret_string(aws_sm_test_client(), SECRET_NAME)
jwks_client = PyJWKClient(secret)
jwks_client.get_signing_keys()
EOF
    )"

    for n in {1..60} ; do
        if python 2>/dev/null -c "${check_secrets_ready_py}" && python 2>/dev/null -c "${check_cognito_jwks_available_py}"  ; then
            break
        fi

        sleep 5
    done

    python -c "${check_secrets_ready_py}"

    python_args=(
        "${MY_ROOT}/manage.py" runserver
        "0.0.0.0:${APP_PORT:-8000}"
    )

    if [ -n "${DEBUGPY_PORT:+x}" ] || [ -n "${DEBUGPY_WAIT:+x}" ] ; then
        python_args=(
            -m debugpy
            --listen "0.0.0.0:${DEBUGPY_PORT:-5678}"
            ${DEBUGPY_WAIT:+--wait-for-client}
            "${python_args[@]}"
        )
    fi

    export DJANGO_SETTINGS_MODULE=mm.dev.iam_dev_settings
    export DJANGO_CONFIGURATION=DevRuntimeConfiguration
    python "${MY_ROOT}/manage.py" migrate
    exec python "${python_args[@]}"
else
    exec "${@}"
fi
