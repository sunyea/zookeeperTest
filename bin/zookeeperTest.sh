#!/bin/bash

RESTART=0555
NAME=zookeeperTest
PROGRAME=$NAME.py

while :
do
        NOW=`date +%H%M`
        PID=`ps -ef|grep $PROGRAME|grep -v $0|grep -v grep|awk '{print $2}'`

        if [ $RESTART = $NOW ];
        then
                sleep 40
                kill -9 $PID
                sleep 10
                nohup python3 $PROGRAME > $NAME.o 2>&1 &
                echo "restart $PROGRAME at $NOW"
                sleep 10
        elif [ -z "$PID" ];
        then
                nohup python3 $PROGRAME > $NAME.o 2>&1 &
        else
                sleep 10
        fi
done