#!/usr/bin/bash
name=$1
if [ -z "$name" ]; then
    echo "Usage: rename.sh <name>"
    exit 1
fi
sed -i "s/_base/_${name}/g" $(find . -type f)
mv src/datoso_seed_base src/datoso_seed_${name}
rm rename.sh