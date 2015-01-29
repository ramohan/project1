from django.shortcuts import render
<html>
<head>
<title> login page</title>
</head>
<body>
<form action="check_login" method="GET">
user name<input type='text' name='user'>
password<input type='password' name='pwd'>
<input type='submit' value='login'>
</form>
</body>
</html>
# Create your views here.
