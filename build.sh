#!/bin/bash

set -e

BASE_VERSION=$(git describe --tags --match "v[0-9]*.[0-9]*.[0-9]*" --abbrev=0 2>/dev/null || echo "v0.0.0")
if git describe --exact-match --tags --match "v[0-9]*.[0-9]*.[0-9]*" HEAD >/dev/null 2>&1; then
  VERSION="$BASE_VERSION"
else
  VERSION="${BASE_VERSION}-dev"
fi

export VERSION

docker build . --build-arg APP_VERSION="$VERSION" -t project-hivebox:"$VERSION"