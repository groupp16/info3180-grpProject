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
            return {
                 csrf_token: '' 
            }  
            }, 
        created() {     
                this.getCsrfToken(); 
            },
            
            methods: { 
               
                login() {  
                    let loginform = document.getElementById('login'); 
                    let form_data = new FormData(loginform);
                    fetch("/api/auth/login", {     
                        method: 'POST', 
                        body: form_data,         
                        headers: { 
                            'X-CSRFToken': this.csrf_token         
                            } 
                        })     
                        .then(function (response) {    
                        return response.json();     
                        })     
                        .then(function (data) {         
                            // display a success message         
                            console.log(data);    
                             })     
                            .catch(function (error) {         
                                console.log(error);     
                                });
                },
                getCsrfToken() {     
                    let self = this;     
                    fetch('/api/csrf-token')       
                    .then((response) => response.json())      
                     .then((data) => {         
                         console.log(data);         
                         self.csrf_token = data.csrf_token;   
                        })   
                } 
            }
};
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