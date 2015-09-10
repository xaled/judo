#!/bin/bash
HOMEDIR=$1
echo "removing homedir: $1"
/bin/rm -Rf "$HOMEDIR"
echo "fin remove"
