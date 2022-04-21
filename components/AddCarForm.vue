<template>
  <H1>Add New Car</H1>

  <form
    id=" addcar"
    name="addcar"
    method="POST"
    enctype="multipart/form-data"
    @submit.prevent="addcar"
  >
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
      {{ form.transmission((class_ = "form-control")) }}
    </div>

    <div class="form-group">
      <label for="cartype">Car Type</label>
      {{ form.cartype((class_ = "form-control")) }}
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
import { defineComponent } from "@vue/composition-api";

export default {
  data() {
    return {};
  },
  method: {
    addcar() {
      let AddCarForm = document.getElementById("AddCarForm");
      let formdata = new FormData(AddCarForm);
      fetch("/api/cars", {
        method: "POST",
        body: formdata,
        headers: {
          "X-CSRFToken": this.csrf_token,
        },
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
      fetch("/api/csrf-token")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        });
    },

    created() {
      this.getCsrfToken();
    },
  },
};
</script>
}

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
