#!/bin/bash
HOMEDIR=$1
PROFILEDIR=$2
echo "init homedir: $1 for profile: $2"
/bin/rm -Rf "$HOMEDIR"
/bin/cp -R "$PROFILEDIR" "$HOMEDIR"
#/bin/chmod o-x  $HOMEDIR
echo "fin init"
