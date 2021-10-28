<template>
  <div class="login">
    <div class="loginForm">
      <div class="loginTitle">Login</div>
      <div class="input-container ic1">
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
      <button type="text" class="submit" @click="proba()">Proba</button>
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
    };
  },
  methods: {
    async login() {
      var email = this.form.email;
      var password = this.form.password;

           var headers = new Headers();

  headers.append('Content-Type', 'application/json');
  headers.append('Accept', 'application/json');

  headers.append('Access-Control-Allow-Origin', 'http://localhost:8000');
  headers.append('Access-Control-Allow-Credentials', 'true');

  headers.append('GET', 'POST', 'OPTIONS');

  console.log("HEADERS ", headers)

      await fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        // headers: { "Content-Type": "application/json", "Accept": "application/json", "Access-Control-Allow-Origin": "http://localhost:8000", "Access-Control-Allow-Credentials": "true" },
        // headers: headers,
        headers: { "Content-Type" : "application/json" },
        credentials: "include",
        body: JSON.stringify({
          email,
          password,
        }),
      }).then((response) => {
        console.log(response);
        // axios
        //   .get("api/user", { withCredentials: true })
        //   .then(function (response) {
        //     const content = response.data;
        //     history.replace("/");
        //     props.setId(content.id);
        //     props.setName(content.name);
        //   })
        //   .catch(function (error) {
        //     console.log(error);
        //     if (error.status === 403) {
        //       setErrorMessage("You have entered wrong credentials!");
        //     } else {
        //       setErrorMessage("Error occured while signing in!");
        //     }
        //   });
      });
    },

    proba() {
      // axios({
      //   method: "post",
      //   url: "api/registerr",
      // }).then((response) => {
      //   console.log("Registerr response");
      //   console.log(response);
      //   console.log(response.data);
      // });

      axios({
        method: "post",
        url: "api/login",
        credentials: "include",
        data: {
          email: this.form.email,
          password: this.form.password
        }
      }).then((response) => {
        console.log(response);
        console.log(response.data);
      });
    },
  },
};
</script>

<style>
/* .login {
  background-color: rgb(245, 245, 245);
  border-radius: 6px;
  width: 80%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  margin-left: auto;
  margin-right: auto;
  margin-top: auto;
  margin-bottom: auto;
} */

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
  background-color: #11bfeb;
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