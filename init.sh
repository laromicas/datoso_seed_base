#!/usr/bin/bash
name=$1
if [ -z "$name" ]; then
    echo "Usage: rename.sh <name>"
    exit 1
fi
if [ -d ".git" ]; then
    echo "Deleting .git directory"
    rm -rf .git
fi

echo "Initializing git repository"
git init

echo "Renaming base to $name"
sed -i "s/_base/_${name}/g" $(find . -type f)
mv src/datoso_seed_base src/datoso_seed_${name}

echo "Removing init.sh file"
rm init.sh