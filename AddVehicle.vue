<template>
  <H1>Add New Car</H1>

  <form id="add_car" name="add_car" method="POST" enctype="multipart/form-data" @submit.prevent="addcar" >
    <label> Make </label>
    <input type="text" name="make" id="make" required />

    <label> Model</label>
    <input type="text" name="model" id="model" required />

    <label>Colour</label>
    <input type="text" name="colour" id="colour" required />

    <label>Year</label>
    <input type="text" name="year" id="year" required />

    <label>Price</label>
    <input type="text" name="price" id="price" required />

    <div class="form-group">
      <label for="transmission">Transmission</label>
      <select name="transmission" id="transmission">
        <option value="Automatic">Automatic</option>
        <option value="Manual">Manual</option>
    </select>
    </div>

    <div class="form-group">
      <label for="cartype">Car Type</label>
      <select name="cartype" id="cartype">
        <option value="SUV">SUV</option>
        <option value="Sedan">Sedan</option>
        <option value="Coupe">Coupe</option>
        <option value="HatchBack">HatchBack</option>
        <option value="Wagon">Wagon</option>
    </select>
    </div>

    <label>Description</label>
    <textarea name="description" id="description" required />

    <label>Upload Photo</label>
    <input type="file" name="photo" id="photo" required />

    <div class="btnpos">
      <button class="button send">Save</button>
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
               
                addcar() {  
                    let addcarform = document.getElementById('add_car'); 
                    let form_data = new FormData(addcarform);
                    var myCookie = this.getCookie('token');
                    fetch("/api/cars", {     
                        method: 'POST', 
                        body: form_data,         
                        headers: { 

                           'Authorization': `Bearer ${myCookie}`,
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
                },
                getCookie(cname) {
                    let name = cname + "=";
                    let decodedCookie = decodeURIComponent(document.cookie);
                    let ca = decodedCookie.split(';');
                    for(let i = 0; i <ca.length; i++) {
                      let c = ca[i];
                      while (c.charAt(0) == ' ') {
                        c = c.substring(1);
                      }
                      if (c.indexOf(name) == 0) {
                        return c.substring(name.length, c.length);
                      }
                    }
                    return "";
              } 
            }
};
</script>


<style>
h1 {
  text-align: center;
}
form {
  max-width: 420px;
  margin: 30px auto;
  border: 2px black solid;
  background: white;
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
input,
textarea {
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
.send {
  text-align: center;
  background: rgb(53, 128, 53);
}
</style>