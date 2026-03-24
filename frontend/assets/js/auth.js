function login() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  const token = btoa(user + ":" + pass);
  localStorage.setItem("auth", token);

  fetch("http://localhost:8000/login", {
    headers: {
      "Authorization": "Basic " + token
    }
  })
  .then(res => {
    if (res.status === 200) {
      window.location.href = "dashboard.html";
    } else {
      document.getElementById("error").innerText = "Invalid credentials";
    }
  });
}

function getAuthHeader() {
  return {
    "Authorization": "Basic " + localStorage.getItem("auth"),
    "Content-Type": "application/json"
  };
}