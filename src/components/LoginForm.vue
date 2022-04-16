<template>
    <h1>Login</h1>
    <form  id="register" name="register" method="POST" @submit.prevent="login">
        <label>Username:</label>
        <input type="text" name="username" id="username" required/>

        <label>Password:</label>
        <input type="password" name="code" id="code" required/>
        <div class="send">
            <button>Login</button>
        </div>
    </form>

    
</template>






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
    background:  rgb(0, 184, 245);
    border: 0;
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white; 
    border-radius: 20px;
    justify-content: center;
}
</style>