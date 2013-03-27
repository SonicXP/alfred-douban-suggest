#!/bin/bash

result=`curl 'www.ip138.com/ips138.asp?ip={query}' | iconv -f gbk -t utf-8 | grep "<ul class=\"ul1\"><li>" | awk -F"<li>" '{for (i=2; i<=NF; ++i){ print $i }}' | awk -F"</li>" '{print $1}'`
echo '<?xml version="1.0"?>'
echo '<items>'
echo -e "$result" | awk -F'：' '{print "<item uid=\""$0"\" arg=\""$2"\" valid=\"YES\"><title>"$2"</title><subtitle>"$1"</subtitle><icon>icon.png</icon></item>"}'
echo '</items>'
