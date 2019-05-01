#!/usr/bin/bash
echo "content-type:text/html"
if [  "$QUERY_STRING" == "" ]
then
	rand=$(($RANDOM%5+1));
	echo "Set-Cookie: question=$rand"
fi
echo ""
echo "<html>"
echo "<head>"
echo "</head>"
echo "<body>"

if [  "$QUERY_STRING" != "" ]
then
	#echo $HTTP_COOKIE;
	#echo $QUERY_STRING;

	question=`echo $HTTP_COOKIE|cut -d ';' -f 1`;
	question=`echo $question|cut -d '=' -f 2`;
	#echo $question;
	
	ans=`echo $QUERY_STRING|cut -d '&' -f 1`;
	ans=`echo $ans|cut -d '=' -f 2`;
	#echo $ans;
	
	correct=`awk -F '|' 'NR=='$question'{  print $5}' quiz/quiz.txt`
		
	echo $correct
	if [ $ans == $correct ]
	then
		echo "Correct..!"
	else
		echo "Wrong..!"
	fi

else 
	echo "<div>"
	
	#echo $rand;
	question=`awk -F '|' 'NR=='$rand'{  print $1}' quiz/quiz.txt`
	option1=`awk -F '|' 'NR=='$rand'{  print $2}' quiz/quiz.txt`
	option2=`awk -F '|' 'NR=='$rand'{  print $3}' quiz/quiz.txt`
	option3=`awk -F '|' 'NR=='$rand'{  print $4}' quiz/quiz.txt`

	echo $question
	
	echo "<form method=\"GET\" action=\"\">"
	echo "<input type=radio name=\"ans\" value=\"1\" />"
	echo "<span>" $option1 "</span>" 
	echo "<input type=radio name=\"ans\"  value=\"2\"/>"
	echo "<span>" $option2 "</span>" 
	echo "<input type=radio name=\"ans\" value=\"3\" />"
	echo "<span>" $option3 "</span>" 
	echo "<button type=\"submit\">Submit </button>" 
	echo "</form>"

	echo "</div>"

fi

echo "</body>"
echo "</html>"


