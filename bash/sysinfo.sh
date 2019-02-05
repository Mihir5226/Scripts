#!/bin/bash
#This script will email us our user,IP hostname,datetime,version of bash
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
emailaddress="patelm7@mail.uc.edu"
dt=$(date +"%d-%m-%Y")
printf -v content "User:\t%s\n IP:\t%s\n Hostname:\t%s\n Version:\t%s\n Date: \t%s\n" $USER $ip $HOSTNAME $BASH_VERSION $dt 
echo  $content
#echo Hostname: $HOSTNAME
#echo Version: $BASH_VERSION
#echo Date: $dt
mail -s "IT3038C Linux IP" $emailaddress <<< $content
