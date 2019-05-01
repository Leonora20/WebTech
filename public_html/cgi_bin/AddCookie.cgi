#!/usr/bin/bash
echo "content-type:text/html";

n=5;
if [  "$QUERY_STRING" != " " ]
then
	val1=`echo $QUERY_STRING|cut -d '&' -f 1`;
	num=`echo $val1|cut -d '=' -f 2`;

	val3=`echo $HTTP_COOKIE|cut -d ';' -f 1`;
	sum=`echo $val3|cut -d '=' -f 2`;
	sum=`expr $sum + $num`;

	val2=`echo $HTTP_COOKIE|cut -d ';' -f 2`;
	i=`echo $val2|cut -d '=' -f 2`;
	echo "Set-Cookie: sum=$sum";
	i=`expr $i + 1`;
	echo "Set-Cookie: i=$i";

else
	sum=0;
	i=0;
fi
echo "";
echo "<html>";
echo "<head>";
echo "</head>";
echo "<body>";
echo "$HTTP_COOKIE";
if [ $i -lt $n ]
then
	
	echo "<form action='AddCookie.cgi' method='GET'>";
	echo "Enter a number";
	echo "<input type='text' name='num'>";
	echo "<input type='submit' value='add'>";
	echo "</form>";
else 
	echo "<div> sum is $sum </div>";
fi	
echo "</body>";

echo "</html>";




