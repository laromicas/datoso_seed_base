#!/usr/bin/bash
$name=$1
sed -i "s/_base/_${name}/g" $(find . -type f)
mv src/datoso_seed_base src/datoso_seed_${name}
rm rename.sh