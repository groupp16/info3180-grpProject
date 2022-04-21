

<template>
    <div class="container">
      <div class="info">
        <h1>Buy and Sell Cars Online</h1>
      <p>United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
        Find a Great Price on the Vehicle You Want.
      </p>
      <div class="btnpos">
        <a href="http://localhost:3000/register"><button  class="button register">Register</button> </a> 
        <a href="http://localhost:3000/login"> <button  class="button login">Login</button></a>
      </div>
     
      </div>
    
      <div class="photo">
        <img alt="Sample car" class="logo" src="@/assets/car.jpg" width=115% />
      </div>

    </div> 
  
     
</template>
<script>
export default {
    data() {
        return {};
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
    border: 0;
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white; 
    border-radius: 20px;
    justify-content: center;
    margin:4px;
}
.info{
  text-align: center;
}
.btnpos{
  text-align: center;
}

.register{
    background:skyblue;
}
</style>