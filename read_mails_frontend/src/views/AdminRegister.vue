<template>
  <div class="register">
    <div class="registerForm">
        <div v-if="errorMessage != ''" class="alert-danger">
      <div show class="d-flex justify-content-center">{{errorMessage}}</div>
    </div>
      <div v-if="errorMessage == ''" class="registerTitle">Welcome!</div>
      <div class="input-container ic1">
        <input
          id="firstname"
          class="input"
          type="text"
          placeholder=" "
          v-model="form.firstName"
        />
        <div class="cut"></div>
        <label for="firstname" class="placeholder">First name</label>
      </div>
      <div class="input-container ic2">
        <input
          id="lastname"
          class="input"
          type="text"
          placeholder=" "
          v-model="form.lastName"
        />
        <div class="cut"></div>
        <label for="lastname" class="placeholder">Last name</label>
      </div>
      <div class="input-container ic2">
        <input
          id="email"
          class="input"
          type="text"
          placeholder=" "
          v-model="form.email"
        />
        <div class="cut cut-short"></div>
        <label for="email" class="placeholder">Email</label>
      </div>
      <div class="input-container ic2">
        <input
          id="phoneNumber"
          class="input"
          type="text"
          placeholder=" "
          v-model="form.phoneNumber"
        />
        <div class="cut cut-short"></div>
        <label for="phoneNumber" class="placeholder">Phone number</label>
      </div>
      <div class="input-container ic2">
        <input
          id="password"
          class="input"
          type="password"
          placeholder=" "
          v-model="form.password"
        />
        <div class="cut cut-short"></div>
        <label for="password" class="placeholder">Password</label>
      </div>
      <div class="input-container ic2">
        <input
          id="confirmPassword"
          class="input"
          type="password"
          placeholder=" "
          v-model="form.confirmPassword"
        />
        <div class="cut cut-short"></div>
        <label for="confirmPassword" class="placeholder"
          >Confirm password</label
        >
      </div>
      <button type="text" class="submit" @click="register()">Register</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      form: {
        firstName: "",
        lastName: "",
        email: "",
        phoneNumber: "",
        password: "",
        confirmPassword: "",
      },
      errorMessage: ""
    };
  },
  methods: {
    register() {
      console.log("registracija");
      if (this.form.password === this.form.confirmPassword) {
        axios({
          method: "post",
          url: "api/register/admin",
          data: {
            firstName: this.form.firstName,
            lastName: this.form.lastName,
            email: this.form.email,
            phoneNumber: this.form.phoneNumber,
            password: this.form.password,
            is_superuser: true
          },
        }).then((response) => {
            if(response.status == 200) {
                this.$router.replace("/");
            } else {
              this.errorMessage = "Error occured while registering!"
          }
        }).catch(error => {
            console.log(error);
            this.errorMessage = "Error occured while registering!";
        });
      } else {
        this.errorMessage = "Passwords are not matching!"
      }
    },
  },
};
</script>

<style>
/* body {
  align-items: center;
  background-color: #000;
  display: flex;
  justify-content: center;
  height: 100vh;
} */

.register {
  width: 100%;
  height: 100vh;
  display: flex;
  margin: 30px;
  /* align-items: center; */
  justify-content: center;
}

.registerForm {
  background-color: rgb(8, 8, 41);
  /* border-radius: 20px; */
  box-sizing: border-box;
  height: 630px;
  padding: 20px;
  width: 380px;
}

.registerTitle {
  color: #eee;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 30px;
  font-weight: 600;
}

.registerSubtitle {
  color: #eee;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-top: 10px;
}

.input-container {
  height: 50px;
  position: relative;
  width: 100%;
}

.ic1 {
  margin-top: 25px;
}

.ic2 {
  margin-top: 25px;
}

.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 16px;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 100%;
}

.cut {
  background-color: rgb(8, 8, 41);
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 76px;
}

.cut-short {
  width: 50px;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
}

.placeholder {
  color: #65657b;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  left: 20px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #dc2f55;
}

.submit {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #297b99;
  /* border-radius: 12px; */
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  margin-top: 30px;
  text-align: center;
  width: 100%;
}

.submit:active {
  background-color: #06b;
}
</style>