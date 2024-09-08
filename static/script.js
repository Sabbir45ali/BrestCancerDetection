// Login and Signup page
const container=document.getElementById("container");
const registerbtn=document.getElementById("register");
const loginbtn=document.getElementById("login");

registerbtn.addEventListener("click",()=>{
    container.classList.add("active");
});

loginbtn.addEventListener("click",()=>{
    container.classList.remove("active");
});

// Profile page
function openModal() {
    document.getElementById('profileModal').style.display = 'block';
  }

  function closeModal() {
    document.getElementById('profileModal').style.display = 'none';
  }

  function updateProfile(event) {
    event.preventDefault();

    document.getElementById('name').innerText = document.getElementById('nameInput').value;
    document.getElementById('email').innerText = document.getElementById('emailInput').value;
    document.getElementById('phone').innerText = document.getElementById('phoneInput').value;
    document.getElementById('gender').innerText = document.getElementById('genderInput').value;
    document.getElementById('blood').innerText = document.getElementById('bloodInput').value;

    closeModal();
  }

  function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        document.getElementById('profileImage').src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }

//   form logic
function submitForm(event) {
    event.preventDefault();
    // Handle form submission here
    alert('Form submitted!');
  }