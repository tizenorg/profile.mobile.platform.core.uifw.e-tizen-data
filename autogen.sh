#!/bin/sh

rm -rf autom4te.cache
rm -f aclocal.m4

echo "Running aclocal..." ; aclocal || exit 1
echo "Running autoconf..." ; autoconf || exit 1
echo "Running automake..." ; automake --add-missing --copy --gnu || exit 1
