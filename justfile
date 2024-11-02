oapi_url := "https://api.ibkr.com/gw/api/v3/api-docs"

gen:
    openapi-python-client generate --url {{oapi_url}} --output-path ibkr-web-oapi --overwrite --config=config.yml

