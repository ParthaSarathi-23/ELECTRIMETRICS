import streamlit as st 

st.markdown("""
<head>
<style>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap">
*{
    margin: 0;
    padding: 0;
    font-family: 'poppins',sans-serif;
}
section{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100%;
    background: url('https://www.hotelmize.com/wp-content/webp-express/webp-images/uploads/2020/11/factors_of_demand_forecasting-01.jpg.webp')no-repeat;
    background-position: center;
    background-size: cover;
}
.form-box{
    position: relative;
    width: 400px;
    height: 450px;
    background: transparent;
    border: 2px solid rgba(255,255,255,0.5);
    border-radius: 20px;
    backdrop-filter: blur(15px);
    display: flex;
    justify-content: center;
    align-items: center;
}
h2{
    font-size: 2em;
    color: #000000;
    text-align: center;
}
.inputbox{
    position: relative;
    margin: 30px 0;
    width: 310px;
    border-bottom: 2px solid #fff;
}
.inputbox label{
    position: absolute;
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
    color: #000000;
    font-size: 1.3em;
    pointer-events: none;
    transition: .5s;
}
input:focus ~ label,
input:valid ~ label{
top: -5px;
}
.inputbox input {
    width: 100%;
    height: 50px;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1em;
    padding:0 35px 0 5px;
    color: #000000;
}
.inputbox ion-icon{
    position: absolute;
    right: 8px;
    color: #fff;
    font-size: 1.2em;
    top: 20px;
}
.forget{
    margin: -15px 0 15px ;
    font-size: .9em;
    color: #000000;
    display: flex;
    justify-content: space-between;  
}
.forget label input{
    margin-right: 3px;    
}
.forget label a{
    color: #000000;
    text-decoration: none;
    font-weight: 600;
}
.forget label a:hover{
    text-decoration: underline;
}
button{
    width: 100%;
    height: 40px;
    border-radius: 40px;
    background: #fff;
    border: none;
    outline: none;
    cursor: pointer;
    font-size: 1em;
    font-weight: 600;
}
.register{
    font-size: .9em;
    color: #000000;
    text-align: center;
    margin: 25px 0 10px;
}
.register p a{
    text-decoration: none;
    color: #000000;
    font-weight: 600;
}
.register p a:hover{
    text-decoration: underline;
}
</style>
  <title>HASH TECHIE OFFICIAL</title>
</head>
<body>
    <section>
        <div class="form-box">
            <div class="form-value">
                <form action="http://localhost:8501/",method = "get">
                    <h2>Login</h2>
                    <div class="inputbox">
                        <ion-icon name="mail-outline"></ion-icon>
                        <input type="email" id = "email"  required>
                        <label for="">Email</label>
                    </div>
                    <div class="inputbox">
                        <ion-icon name="lock-closed-outline"></ion-icon>
                        <input type="password" id = "password"  required>
                        <label for="">Password</label>
                    </div>
                    <div class="forget">
                        <label for=""><input type="checkbox">Remember Me  <a href="#">Forget Password</a></label> 
                    </div>
    <button class = "login-btn" onclick = "func()" type="submit">Log in</button>
                    <div class="register">
                        <p>Don't have a account <a href="http://localhost:8501/">Register</a></p>
                    </div>
                </form>
            </div>
        </div>
    </section>
    <script>
    function func(){
        var email = document.getElementById("email").value;
        var pass = document.getElementById("password").value;
        if(email == "jpk@gmail.com" && pass == "jpk@2023"){
            alert("success !")
            window.location.assign("http://localhost:8501/")
        }
        else{
            alert("Wrong entry")
        }
    }
    </script>
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</body>
</html>
""",unsafe_allow_html = True)