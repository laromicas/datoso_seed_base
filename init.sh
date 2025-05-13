#!/usr/bin/bash
name=$1
if [ -z "$name" ]; then
    echo "Usage: init.sh <name>"
    exit 1
fi

cd ..
mkdir datoso_seed_${name}
cp -r datoso_seed_base/* datoso_seed_${name}/
cd datoso_seed_${name}

if [ -d ".git" ]; then
    echo "Deleting .git directory"
    rm -rf .git/
fi
if [ -d "src/datoso_seed_base.egg-info" ]; then
    echo "Deleting build directory"
    rm -rf src/datoso_seed_base.egg-info/
fi

echo "Initializing git repository"
git init

echo "Renaming base to ${name}"
sed -i "s/_base/_${name}/g" $(find . -type f)
mv src/datoso_seed_base src/datoso_seed_${name}
sed -i "s/Base/${name^}/g" $(find . -type f)

echo "Removing init.sh file"
rm init.sh
