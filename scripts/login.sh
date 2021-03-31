FILE_PATH="~/.ssh/id_rsa"
FILE_PATH2="~/.ssh/id_rsa.pub"

if [ -f "$FILE_PATH" ] ; then
    echo $FILE_PATH "is aleady file exist" 
else 
    echo "file not exist" 
fi

if [ -f "$FILE_PATH2" ] ; then
    echo $FILE_PATH2 "is aleady file exist" 
else 
    echo "file not exist" 
fi

ssh-keygen
