#!/bin/bash

cd ../pyrewallui
pnpx openapi-zod-client http://127.0.0.1:5050/openapi/openapi.json -o src/api.ts --export-types --with-description --with-docs --group-strategy tag --template ../scripts/api_client_template.hbs