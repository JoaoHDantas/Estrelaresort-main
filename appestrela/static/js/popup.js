
  document.addEventListener("DOMContentLoaded", function() {
    const checkbox = document.querySelector(".checkbox");
    const body = document.body;
  
    checkbox.addEventListener("change", function() {
      if (this.checked) {
        body.classList.add("dark");
        localStorage.setItem("darkMode", "enabled");
      } else {
        body.classList.remove("dark");
        localStorage.setItem("darkMode", null);
      }
    });
  
    const darkMode = localStorage.getItem("darkMode");
  
    if (darkMode === "enabled") {
      body.classList.add("dark");
      checkbox.checked = true;
    }
  });