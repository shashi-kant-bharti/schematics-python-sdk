#!/bin/bash
set -e

print_usage () {
    echo "
usage:
   ./prepare_project.sh [-n SDK_PACKAGE_NAME] [-d \"Project Description\"] [-g GIT_URL] [-s SDK_NAME] [-a AUTHOR_EMAIL] [-c SERVICE_CATEGORY] [-h]
where:
   -n: specify the project's main package directory name (e.g. ibm_platform_services)
   -d: specify project description string (e.g. \"IBM Cloud Platform Services Python SDK\")
   -g: specify the git url (e.g. https://github.com/IBM/platform-services-python-sdk)
   -s: specify sdk name string (e.g. \"Platform Services\")
   -a: specify the author's email address (e.g. email@ibm.com)
   -c: specify the service category (e.g. platform-services)
   -h: view usage instructions
"
}

# Parse flags and arguments
while getopts 'n:d:g:s:a:c:h' flag; do
  case "${flag}" in
    n) SDK_PACKAGE_NAME=${OPTARG} ;;
    d) PROJECT_DESCRIPTION=${OPTARG} ;;
    g) PROJECT_GIT_URL=${OPTARG} ;;
    s) SDK_NAME=${OPTARG} ;;
    a) AUTHOR_EMAIL=${OPTARG} ;;
    c) SERVICE_CATEGORY=${OPTARG} ;;
    *) print_usage
        exit 1 ;;
  esac
done

if [[ -z "$SERVICE_CATEGORY" ]]; then
    SERVICE_CATEGORY=$(basename $PWD | sed 's/-/_/g' | sed 's/_python_sdk//')
fi

if [[ -z "$SDK_NAME" ]]; then
    SDK_NAME=$(echo $SERVICE_CATEGORY | tr '_' ' ' |  awk '{for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)} 1')
fi

if [[ -z "$SDK_PACKAGE_NAME" ]]; then
    SDK_PACKAGE_NAME=ibm_$SERVICE_CATEGORY
fi

if [[ -z "$PROJECT_DESCRIPTION" ]]; then
    PROJECT_DESCRIPTION="Python SDK for IBM Cloud ${SDK_NAME} services"
fi

if [[ -z "$AUTHOR_EMAIL" ]]; then
    AUTHOR_EMAIL=$(git config --get user.email)
fi

if [[ -z "$PROJECT_GIT_URL" ]]; then
    url=$(git config --get remote.origin.url | sed 's/git@//' | sed 's/com:/com\//' | sed 's/.git$//')
    PROJECT_GIT_URL=${url}
fi

printf "\n>>>>> Project Initialization In Progress...\n\t SDK_PACKAGE_NAME: ${SDK_PACKAGE_NAME}\n\t PROJECT_DESCRIPTION: ${PROJECT_DESCRIPTION}\n\t PROJECT_GIT_URL: ${PROJECT_GIT_URL}\n\t SDK_NAME: ${SDK_NAME}\n\t AUTHOR_EMAIL: ${AUTHOR_EMAIL}\n\t SERVICE_CATEGORY: ${SERVICE_CATEGORY}\n"

# Remove sample files
rm examples/test_example_service_v1_examples.py
rm test/integration/test_example_service_v1.py
rm test/unit/test_example_service_v1.py
rm mysdk/example_service_v1.py
rm example_service_v1.env.hide
printf "\n>>>>> Example Service files removed."

# Update directory name
if [[ $SDK_PACKAGE_NAME != "mysdk" ]]; then
    mv mysdk $SDK_PACKAGE_NAME
    printf "\n>>>>> Directory structure updated."
fi

# Update gitignore
sed -i.bak 's/^example-service/# example-service/' .gitignore
rm .gitignore.bak
printf "\n>>>>> .gitignore updated."

# Update GitHub Actions workflows
rm ./.github/workflows/build.yaml
mv ./.github/workflows/build.yaml.sdk ./.github/workflows/build.yaml
mv ./.github/workflows/publish.yaml.sdk ./.github/workflows/publish.yaml
printf ">>>>> GitHub Action workflows updated.\n"

# Update supplemental files
sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' Makefile
rm Makefile.bak
printf "\n>>>>> Makefile updated."

sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' .bumpversion.toml
rm .bumpversion.toml.bak
printf "\n>>>>> .bumpversion.toml updated."

sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' $SDK_PACKAGE_NAME/version.py
rm $SDK_PACKAGE_NAME/version.py.bak
printf "\n>>>>> ${SDK_PACKAGE_NAME}/version.py updated."

# Update python initialization files
SDK_AGENT="$( sed 's~.*/.*/~~' <<< "$PROJECT_GIT_URL" )"
sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' $SDK_PACKAGE_NAME/common.py
sed -i.bak 's/my-python-sdk/'${SDK_AGENT}'/' $SDK_PACKAGE_NAME/common.py
rm $SDK_PACKAGE_NAME/common.py.bak
printf "\n>>>>> ${SDK_PACKAGE_NAME}/common.py updated."

sed -i.bak 's/my-python-sdk/'${SDK_AGENT}'/' test/unit/test_common.py
sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' test/unit/test_common.py
rm test/unit/test_common.py.bak
printf "\n>>>>> test/unit/test_common.py updated."

sed -i.bak "s/Python client library for the IBM Cloud MySDK Services/${PROJECT_DESCRIPTION}/" $SDK_PACKAGE_NAME/__init__.py
sed -i.bak "s/from .example_service_v1 import ExampleServiceV1/# from .example_service_v1 import ExampleServiceV1/" $SDK_PACKAGE_NAME/__init__.py
rm $SDK_PACKAGE_NAME/__init__.py.bak
printf "\n>>>>> ${SDK_PACKAGE_NAME}/__init__.py updated."

sed -i.bak "s~https://github.ibm.com/CloudEngineering/python-sdk-template~${PROJECT_GIT_URL}~" pyproject.toml
sed -i.bak 's/mysdk/'${SDK_PACKAGE_NAME}'/' pyproject.toml
sed -i.bak "s/Python client library for IBM Cloud MYSDK Services/${PROJECT_DESCRIPTION}/" pyproject.toml
sed -i.bak 's/devxsdk@us.ibm.com/'${AUTHOR_EMAIL}'/' pyproject.toml
rm pyproject.toml.bak
printf "\n>>>>> pyproject.toml updated."

# Update documentation
sed -i.bak "s/^# .*/# ${PROJECT_DESCRIPTION}/" README.md
sed -i.bak "s/github.ibm.com/github.com/" README.md
sed -i.bak "s/MySDK Service/${SDK_NAME}/" README.md
sed -i.bak "s/MySDK/${SDK_NAME}/" README.md
PYPI_NAME="$( sed 's~_~-~g' <<< "$SDK_PACKAGE_NAME" )"
sed -i.bak "s/mysdk/${PYPI_NAME}/" README.md
sed -i.bak "s/<service-category>/${SERVICE_CATEGORY}/" README.md
sed -i.bak "s~<github-repo-url>~${PROJECT_GIT_URL}~" README.md
sed -i.bak "s~https://github.ibm.com/CloudEngineering/python-sdk-template~${PROJECT_GIT_URL}~" README.md
sed -i.bak "s~^\[Example Service\].*~<!-- [Example Service](https://cloud.ibm.com/apidocs/example-service) | example_service_v1 | ExampleServiceV1 -->~" README.md
GH_SLUG="$( sed 's~.*.com/~~' <<< "$PROJECT_GIT_URL" )"
sed -i.bak "s~CloudEngineering/python-sdk-template~${GH_SLUG}~g" README.md

rm README.md.bak
printf "\n>>>>> README.md updated."

sed -i.bak "s~<github-repo-url>~${PROJECT_GIT_URL}~" CONTRIBUTING.md
rm CONTRIBUTING.md.bak
printf "\n>>>>> CONTRIBUTING.md updated."

printf "\n>>>>> Project Initialized Successfully!\n"
