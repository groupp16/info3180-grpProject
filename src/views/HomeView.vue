

<template>
    <div class="container">
      <div class="info">
        <h1>Buy and Sell Cars Online</h1>
      <p>United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
        Find a Great Price on the Vehicle You Want.
      </p>
      <button @click="register" id="register">Register</button> 
      <button @click="login" id="login">Login</button>
      </div>
    
      <div class="photo">
        <img alt="Sample car" class="logo" src="@/assets/car.jpg" width=115%/>
      </div>

    </div> 
  
     
</template>
<script>
export default {
    data() {
        return {};
    },
    methods:{
       register(){
   this.$router.push('/register'); 
      },
      login(){
   this.$router.push('/login'); 
      }
    }
}
</script>
<style>
.container{
  display: grid;
  grid-template-columns: 1fr 2fr;
  align-items: center;
}
p{
  margin: 4px;
}
button{
  margin:4px;
}
</style>