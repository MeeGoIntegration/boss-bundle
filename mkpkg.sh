#!/bin/bash
PROJECT=$1
PACKAGE=$2

bundle install --path=vendor/bundle
bundle pack --all
rm -f *gem *tar.bz2
here=$(pwd)
> Source.new
c=3
for src in $(find vendor/cache/  -mindepth 1 -maxdepth 1 -type d); do
   tar cfj $here/$(basename $src).tar.bz2 $src;
   echo Source$((c++)): $(basename $src).tar.bz2 >> $here/Source.new
done
cd $here
for g in vendor/cache/*gem; do echo Source$((c++)): $(basename $g) >>$here/Source.new ; done; 
sed -i '/^Source2:/,/# SourceEnd/ {//!d}; /^Source2:/r Source.new' boss-bundle.spec
rm Source.new
osc co $1 $2
cp boss-bundle.spec boss-bundle.changes boss-bundle.rpmlintrc Gemfile Gemfile.lock $1/$2/
mv *.tar.bz2 $1/$2
mv vendor/cache/*gem $1/$2/
pushd $1/$2/
osc ar
osc ci
popd
