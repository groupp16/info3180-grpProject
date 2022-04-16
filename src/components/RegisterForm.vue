<template>
    <h1>Register New User</h1>
    <form  id="register" name="register" method="POST" enctype="multipart/form-data" @submit.prevent="upload">
    
    <label>Name:</label>
    <input type="text" name="name" id="name" required/>

    <label>Username:</label>
    <input type="text" name="username" id="username" required/>

    <label>Password:</label>
    <input type="password" name="code" id="code" required/>

    <label>Email:</label>
    <input type="email" name="email" id="email" required/>

    <label>Location:</label>
    <input type="textarea" name="location" id="location" required/>

    <label>Biography:</label>
    <textarea name="biography" id="biography" required/>
      
    <label>Photo of yourself:</label>
    <input type="file" name="photo" id="photo" required/>

    <div class="send">
        <button>Register</button>
    </div>
    

    </form>
</template>

<script>
export default {
    data() {
        return{

        }
    },
    upload()
    {

    }
    
}
</script>

<style>
h1{
    text-align: center;
}
 form {
    max-width: 420px;
    margin: 30px auto;
    border: 2px black solid;
    background:white; 
    border-radius: 10px;
    text-align: left;
    padding: 40px;
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
input, textarea {

    width: 100%;
    display: block; 
    box-sizing: border-box; 
    border: none; 
    border-bottom: 1px solid;
    color: #555;
}
button {
    background: limegreen;
    border: 0;
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white; 
    border-radius: 20px;
    justify-content: center;
}
 .photo{
     padding: none;
 }
.send {
    text-align: center;
}
</style>