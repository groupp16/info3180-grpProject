<template>
    <h1>Login</h1>
    <form  id="register" name="register" method="POST" @submit.prevent="login">
        <label>Username:</label>
        <input type="text" name="username" id="username" required/>

        <label>Password:</label>
        <input type="password" name="code" id="code" required/>
        <div class="btnpos">
            <button class="button loginbtn">Login</button>
        </div>
        
       
    </form>

    
</template>

<script>
export default {
    data() {
        return{

        }
    },
    method:{
        login()
    {
        let LoginForm=document.getElementById('LoginForm');
        let formdata= new FormData(LoginForm);
        fetch("/api/auth/login",{
            method:'POST',
            body:formdata,
            headers:{
                  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
                }
        })
        .then(function (response) 
        {
            return response.json();
        })
        .then(function (data)
         {
         // display a success message
            console.log(data);
        })
        .catch(function (error) 
        {
            console.log(error);
        });
    },

    }
}
</script>


<style>
h1{
    text-align: center;
    padding-top: 10px;
}
 form {
    max-width: 420px;
    margin: 10px auto;
    border: 2px lightgray solid;
    background:white; 
    border-radius: 10px;
    text-align: left;
    padding: 20px;
}

label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}

button {
    border: 0;
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white; 
    border-radius: 20px;
    justify-content: center;
}
.loginbtn{
       background-color:  rgb(0, 184, 245);
}
</style>