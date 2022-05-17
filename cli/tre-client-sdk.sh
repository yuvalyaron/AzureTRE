cd /home/joalmeid/tre-cli/AzureTRE/cli
export PATH=$PATH:~/bin/openapitools/

# OpenAPI-CLI
mkdir -p ~/bin/openapitools
curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh > ~/bin/openapitools/openapi-generator-cli
chmod u+x ~/bin/openapitools/openapi-generator-cli
export PATH=$PATH:~/bin/openapitools/

## Execute latest released openapi-generator-cli
openapi-generator-cli version

## Validate python client
openapi-generator-cli validate \
  -i $MY_OPENAPI_GENERATOR_SPEC \
  --recommend

## Generate python client
export OPENAPI_GENERATOR_VERSION=5.4.0
export OPENAPI_GENERATOR_NAME=csharp-netcore
export OPENAPI_GENERATOR_SPEC="https://ocwtre32.northeurope.cloudapp.azure.com/api/openapi.json"
export LOCAL_OPENAPI_GENERATOR_SPEC="./tre-spec.yaml"
export OPENAPI_GENERATOR_OUTPUT=./client-csharp-2
export TRE_SDK_VERSION=0.0.1
rm ./client-csharp/* -fdR && openapi-generator-cli generate \
  -i $OPENAPI_GENERATOR_SPEC \
  -g $OPENAPI_GENERATOR_NAME \
  -o $OPENAPI_GENERATOR_OUTPUT \
  -c ./config.dotnet.json \
  --additional-properties=packageVersion=$TRE_SDK_VERSION \
  --release-note "tre dotnet sdk $EASYPAY_SDK_VERSION" \
  --log-to-stderr 
  # --global-property debugModels \
  # --dry-run

