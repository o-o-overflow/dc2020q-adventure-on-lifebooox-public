#!/bin/bash -e

echo "NOTE: This will only work if your repository shares history with the template"
echo "      If not, you may have to cherry-pick (or just ask me to fix it for you)"

git remote add template 'git@github.com:o-o-overflow/dc2020q-template.git' 2>/dev/null || true
git fetch template
git rebase --stat template/master
