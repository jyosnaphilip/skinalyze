document.addEventListener("DOMContentLoaded", () => {
  const loginText = document.querySelector(".title-text .login");
  const signupText = document.querySelector(".title-text .signup");
  const loginForm = document.querySelector("form.login");
  const signupForm = document.querySelector("form.signup");
  const loginBtn = document.querySelector("label.login");
  const signupBtn = document.querySelector("label.signup");

  // Show Login Form
  loginBtn.onclick = () => {
      loginForm.style.display = "block";
      signupForm.style.display = "none";
      loginText.style.display = "block";
      signupText.style.display = "none";
  };

  // Show Signup Form
  signupBtn.onclick = () => {
      signupForm.style.display = "block";
      loginForm.style.display = "none";
      signupText.style.display = "block";
      loginText.style.display = "none";
  };
});
