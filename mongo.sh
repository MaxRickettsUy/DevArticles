#!/bin/bash

if [ "$1" == "start" ]; then
	sudo service mongod start
fi

if [ "$1" == "stop" ]; then
	sudo service mongod stop
fi

service mongod status
