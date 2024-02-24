#!/bin/bash 

if [[ $1 = "" ]]
then
    echo Missing: Имя файла
    exit
fi

echo Вы собираетесь удалить $1

if test -f  $1 
then
    echo Подтвердить действие? [y/n]
    read answer
        if [[ $answer = "y" ]] || [[ $answer = "Y" ]]
        then
            rm $1
            echo $1 удален
        else
            echo Действие отменено
        fi
    else
    echo $1 не является файлом
fi