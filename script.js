// script.js

document.getElementById('uploadForm').onsubmit = async function (e) {
  e.preventDefault();

  const formData = new FormData(this);

  const response = await fetch('http://localhost:5000/upload', {
    method: 'POST',
    body: formData
  });

  const data = await response.json();
  alert(data.message || 'Upload completed');
};
