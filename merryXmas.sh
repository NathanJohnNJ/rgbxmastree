#!/bin/bash
ip=$(hostname -I | awk '{print $1}'| sed -e 's/\ *$//g')
model=$(tr -d '\0' < /proc/device-tree/model)

curl --request POST \
        --silent \
        --output /dev/null \
        --url https://api.telegram.org/<INSERT TELEGRAM BOT ID HERE>/sendMessage \
        --header 'Accept: application/json' \
        --header 'Content-Type: application/json' \
        --data "
{
        \"text\": \"<b><u>Merry Christmas!</u></b>\\nEnjoy the light show and remember to have the best Christmas ever!!\\n\\n<i>${model%????????} - (${ip})</i>\",
        \"chat_id\": \"<INSERT TELEGRAM CHAT ID HERE>\",
        \"parse_mode\": \"html\"
}
"