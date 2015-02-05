from django.shortcuts import render,HttpResponse
<html>
<head>
<title> login page</title>
</head>
<body>
<form action="check_login" method="GET">
user name<input type='text' name='user'><br>
password<input type='password' name='pwd'><br>
<input type='submit' value='login'>
</form>
</body>
</html>
def check_login(request):
	return HttpResponse('welcome to baba')
# Create your views here.


print "This is Testing call"
