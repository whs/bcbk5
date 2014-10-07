#!/bin/bash

set -e
cd `dirname $0`

git subtree split --prefix=frontend -b frontend
git checkout frontend
git push -u git@github.com:whs/bcbk5-front.git frontend:gh-pages
