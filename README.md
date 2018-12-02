# Django_REST_API
REST API, PostgreSQL


<h1>Instruction for using API:</h1>


<h2>Create user:</h2>

http://127.0.0.1:8000/users/

body {
        "email": "your email",
	      "first_name": "your name",
	      "last_name": "your surname",
	      "password": "your password"
}

headers {
        "Content-Type": "application/json",
}


<h2>Get token:</h2>

http://127.0.0.1:8000/api-token-auth/

body {
        "email": "your email",
	      "password": "your password"
}

headers {
        "Content-Type": "application/json",
}


<h2>Add post:</h2>

http://127.0.0.1:8000/posts/

body {
        "email": "your email",
	      "first_name": "your name",
	      "last_name": "your surname",
	      "password": "your password"
}

headers {
        "Content-Type": "application/json",
        "Authorization": "JWT <token>"
}


<h2>Add like/unlike:</h2>

http://127.0.0.1:8000/posts/

body {
        "title": "title",
	      "like": "True or False"
}

headers {
        "Content-Type": "application/json",
        "Authorization": "JWT <token>"
}


<h2>Find post by title</h2>

http://127.0.0.1:8000/posts/?title=my first post

headers {
        "Content-Type": "application/json",
        "Authorization": "JWT <token>"
}

