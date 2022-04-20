<template>
    <h1>Register New User</h1>
    <form  id="register" name="register" method="POST" enctype="multipart/form-data" @submit.prevent="register">

    <label>Username</label>
    <input type="text" name="username" id="username" required/>

    <label>Password</label>
    <input type="text" name="password" id="password" required/>

    <label>Fullname</label>
    <input type="text" name="fullname" id="name" required/>


    <label>Email</label>
    <input type="email" name="email" id="email" required/>

    <label>Location</label>
    <input type="textarea" name="location" id="location" required/>

    <label>Biography</label>
    <textarea name="biography" id="biography" required/>
      
    <label>Upload Photo</label>
    <input type="file" name="photo" id="photo" required/>
    
    <div class="btnpos">
         <button class="button send">Register</button>
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
               
                register() {  
                    let registerform = document.getElementById('register'); 
                    let form_data = new FormData(registerform);
                    fetch("/api/register", {     
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