<template>
  <div class="login">
    <div class="loginForm">
      <div v-if="errorMessage != ''" class="alert-danger">
        <div show class="d-flex justify-content-center">{{ errorMessage }}</div>
      </div>
      <div v-if="errorMessage == ''" class="loginTitle">Login</div>
      <div class="input-container ic1">
        <input
          id="email"
          class="input"
          type="email"
          placeholder=" "
          v-model="form.email"
        />
        <div class="cut cut-short"></div>
        <label for="email" class="placeholder">Email</label>
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
      <button type="text" class="submit" @click="login()">Login</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async login() {
      var email = this.form.email;
      var password = this.form.password;
      try {
        await fetch("http://127.0.0.1:8000/api/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",
          body: JSON.stringify({
            email,
            password,
          }),
        }).then((response) => {
            if (response.status === 200) {
              this.$store.dispatch("setAuth", true);
              this.$router.replace("/leads");
              return;
            } 
            this.$store.dispatch("setAuth", false);
            this.errorMessage = "Wrong credentials!";
          })
          .catch((error) => {
            console.log(error);
            this.errorMessage = error;
          });
      } catch (e) {
        await this.$store.dispatch("setAuth", false);
      }
    },

    async test() {
      // const response = await fetch("http://127.0.0.1:8000/api/test", {
      //   method: "GET",
      //   headers: { "Content-Type": "application/json" },
      //   credentials: "include",
      // })
      //   console.log(response);
      //   console.log(response.data);
      //   const content = await response.json();
      // console.log(content);
      // console.log("IDE CONTENT", content);

      axios({
        method: "GET",
        headers: { "Content-Type": "application/json" },
        withCredentials: true,
        url: "api/test",
      }).then((response) => {
        console.log(response.data);
      });
    },
  },
};
</script>

<style>
.login {
  width: 100%;
  display: flex;
  margin: 30px;
  /* align-items: center; */
  justify-content: center;
}

.loginForm {
  background-color: rgb(8, 8, 41);
  /* border-radius: 20px; */
  box-sizing: border-box;
  height: 330px;
  padding: 20px;
  width: 380px;
  border-radius: 30px;
}

.loginTitle {
  color: #eee;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 30px;
  font-weight: 600;
}

.loginSubtitle {
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
  border-radius: 20px;
}

.submit:active {
  background-color: #06b;
}

.alert-danger {
  padding: 15px;
  /* margin: 5px; */
  margin-bottom: 5px;
  border: 1px solid transparent;
  border-radius: 4px;
  display: inline-block;
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
</style>