from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FORM</title>
    <link rel="stylesheet" href="style for form.css">

    <style>
        

    input:hover{
    background-color: lightsalmon;}

    input{
        border-radius: 10px;
     
    }

.heading{
    background-color: lightsalmon;
}
.subhead{
    background-color: lightsalmon;
}
    </style>
</head>

<div class="menu">
    
</div>
<body style="font-size: larger; background-color: beige;text-align: center;">
   
    
    <h1 class="heading"
    style="text-align: center ; font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; text-decoration: wavy;">
    REGISTER</h1>
    <form method="get">


        <input type="text" name="name" required minlength="3" maxlength="30" placeholder="Fullname"> <br> <br>

        <input type="number" name="phone" required minlength="10" placeholder="Mobile Number"><br><br>
        <input type="text" name="email" id="email" pattern="[a-zA-Z0-9._]+@[a-zA-Z0-9_\-.]+\.[a-z]{2,4}$"
            placeholder="Email address"><br><br>
        <input type="text" name="username" minlength="5" placeholder="username"> <br> <br>
        <input type="password" name="pass" required pattern="[?=.*\d][?=.*a-z][?=.*A-Z]"
            placeholder="Enter password"><br><br>

        <br>Enter Date of Birth <br>
        <input type="date" name="dob" placeholder="Enter Date of Birth(dd/mm/yyyy)"><br>
        <h3>Gender: </h3>
        <input type="radio" name="g" value="M" style="accent-color: blue ;">MAlE <br>
        <input type="radio" name="g" value="F" style="accent-color: deeppink;">Female <br>

        <h3>Your Interests: </h3>
        <input type="checkbox" name="Interests" value="M">Movies
        <input type="checkbox" name="Interests" value="MU">Music
        <input type="checkbox" name="Interests" value="G">Gaming
        <input type="checkbox" name="Interests" value="O">Others<br>
        Type your interests here:<br>
        <textarea name="otherInterests" cols="20" rows="1"></textarea>

        <h3>Select platform:</h3>
        <select name="platform" multiple>
            <option value="none">------SElect Platform--------</option>
            <option value="Insta">INSTAGRAM</option>
            <option value="Reddit">REDDIT</option>
            <option value="YT">YouTube</option>
        </select><br>

        <h3>Select your device:</h3>
        <select name="device">
            <option value="android">ANDROID PHONE</option>
            <option value="IOS">IOS</option>
            <option value="WIN">WINDOWS</option>
            <option value="MAC">MAC OS</option>


        </select><br><br>

        <textarea name="bio" placeholder="Your BIO" cols="30" rows="10"></textarea> <br><br>Upload your profile
        picture:<br>
        <input type="file" name="profile"> <br><br>

        <input type="submit" value="SAVE CHANGES" style="font-size: small; text-align: end; ">






    </form>

</body>

</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()