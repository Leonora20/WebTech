#!/usr/bin/bash

echo "content-type:text/html";
echo "";
echo "<html>";
echo "<head>";
echo "</head>";
echo "<body>";
n=5;
if [ $QUERY_STRING != " " ]
then
	val1=`echo $QUERY_STRING|cut -d '&' -f 1`;
	num=`echo $val1|cut -d '=' -f 2`;

	val2=`echo $QUERY_STRING|cut -d '&' -f 2`;
	i=`echo $val2|cut -d '=' -f 2`;

	val3=`echo $QUERY_STRING|cut -d '&' -f 3`;
	sum=`echo $val3|cut -d '=' -f 2`;

	sum=`expr $sum + $num`;
	i=`expr $i + 1`;
else
	sum=0;
	i=0;
fi

if [ $i -lt $n ]
then
	echo "<form action='adding_5_nos.cgi' method='GET'>";
	echo "Enter a number";
	echo "<input type='text' name='num'>";
	
	echo "<input type='hidden' name='i' value='$i'>";
	echo "<input type='hidden' name='sum' value='$sum'>";
	echo "<input type='submit' value='add'>";
	echo "</form>";
else 
	echo "<div> sum is $sum </div>";	
fi	

echo "</body>";

echo "</html>";
