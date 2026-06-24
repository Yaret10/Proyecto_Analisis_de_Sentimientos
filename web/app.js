const API_URL = "";

const loginForm = document.getElementById("loginForm");
const loginMessage = document.getElementById("loginMessage");

const commentText = document.getElementById("commentText");
const resultDiv = document.getElementById("result");

const baseBtn = document.getElementById("baseBtn");
const finetunedBtn = document.getElementById("finetunedBtn");
const compareBtn = document.getElementById("compareBtn");
const logoutBtn = document.getElementById("logoutBtn");

function getToken() {
  return localStorage.getItem("token");
}

function saveToken(token) {
  localStorage.setItem("token", token);
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}

function checkAuth() {
  const isLogin = window.location.pathname.includes("login.html");
  const token = getToken();

  if (!isLogin && !token) {
    window.location.href = "login.html";
  }
}

checkAuth();

if (loginForm) {
  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
      });

      if (!response.ok) {
        throw new Error("Usuario o contraseña incorrectos");
      }

      const data = await response.json();
      saveToken(data.access_token);

      window.location.href = "index.html";
    } catch (error) {
      loginMessage.textContent = error.message;
    }
  });
}

async function predict(endpoint) {
  const text = commentText.value.trim();

  if (!text) {
    resultDiv.innerHTML = `<p class="error">Escribe un comentario.</p>`;
    return;
  }

  try {
    resultDiv.innerHTML = `<p>Analizando...</p>`;

    const response = await fetch(`${API_URL}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${getToken()}`
      },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      throw new Error("Error al consultar la API");
    }

    const data = await response.json();
    renderResult(data);
  } catch (error) {
    resultDiv.innerHTML = `<p class="error">${error.message}</p>`;
  }
}

function renderResult(data) {
  if (data.base_model && data.finetuned_model) {
    resultDiv.innerHTML = `
      <h2>Comparación</h2>

      <div class="result-box">
        <h3>Modelo base</h3>
        <p><strong>Categoría:</strong> ${data.base_model.label}</p>
        <p><strong>Confianza:</strong> ${data.base_model.score}</p>
      </div>

      <div class="result-box">
        <h3>Modelo fine-tuned</h3>
        <p><strong>Categoría:</strong> ${data.finetuned_model.label}</p>
        <p><strong>Confianza:</strong> ${data.finetuned_model.score}</p>
      </div>
    `;
  } else {
    resultDiv.innerHTML = `
      <h2>Resultado</h2>
      <div class="result-box">
        <p><strong>Modelo:</strong> ${data.model}</p>
        <p><strong>Categoría:</strong> ${data.label}</p>
        <p><strong>Confianza:</strong> ${data.score}</p>
      </div>
    `;
  }
}

if (baseBtn) {
  baseBtn.addEventListener("click", () => predict("/predict/base"));
}

if (finetunedBtn) {
  finetunedBtn.addEventListener("click", () => predict("/predict/finetuned"));
}

if (compareBtn) {
  compareBtn.addEventListener("click", () => predict("/predict/compare"));
}

if (logoutBtn) {
  logoutBtn.addEventListener("click", logout);
}
