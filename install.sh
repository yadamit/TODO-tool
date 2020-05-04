#!/bin/bash
filename=`pwd`'/todo'
chmod 777 $filename
ln -s $filename /usr/local/bin/todo
echo "Done!"