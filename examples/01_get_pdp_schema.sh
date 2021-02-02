# source: https://github.com/profusion/sgqlc#code-generator
python3 -m sgqlc.introspection \
     --exclude-deprecated \
     --exclude-description \
     -H "Authorization: Basic ${BASE64_AUTH_TOKEN}" \
     https://graphql-api.pdp.dev.srgssr.ch/graphql \
     pdp_schema.json
