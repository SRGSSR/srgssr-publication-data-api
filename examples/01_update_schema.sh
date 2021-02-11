#!/bin/bash

# check if environment variables are defined
if [ -z "$USER_NAME" ] || [ -z "$USER_PASSWORD" ] || [ -z "$PDP_API" ]; then
    echo "ERROR - One or more variables of [ USER_NAME, USER_PASSWORD, PDP_API ] were not found!"
    echo "Please export your .env credentials as outlined in README before running the script"
    exit 1
fi

echo "INFO - Starting schema update from ${PDP_API}"

# compute the basic authentication token
BASE64_AUTH_TOKEN=$(echo -n "${USER_NAME}:${USER_PASSWORD}" |  base64)

# Introspection call to retrieve JSON schema from GraphQL Endpoint
# source: https://github.com/profusion/sgqlc#code-generator
python3 -m sgqlc.introspection \
     --exclude-deprecated \
     --exclude-description \
     -H "Authorization=Basic ${BASE64_AUTH_TOKEN}" \
     "${PDP_API}" \
     pdp_schema.json || exit 1

echo "INFO - Successfully downloaded pdp_schema.json"

# source: https://github.com/profusion/sgqlc#code-generator
sgqlc-codegen schema pdp_schema.json pdp_schema.py && echo "INFO - Successfully updated pdp_schema.py"
