<template>
    <h1>Login</h1>
    <form  id="login" name="login" method="post" @submit.prevent="login">
        <label>Username:</label>
        <input type="text" name="username" id="username" required/>

        <label>Password:</label>
        <input type="password" name="password" id="password" required/>
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

</style>