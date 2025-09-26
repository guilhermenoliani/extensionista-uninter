# 🌡️ Projeto de Monitoramento com React + Flask

Este projeto é composto por **duas partes**:

- **Frontend:** Aplicação em **React (Vite + TailwindCSS)** para exibir os dados.  
- **Backend:** API em **Flask (Python)** que fornece os dados simulados do sensor (ou reais, se conectados).  

---

## 🚀 Tecnologias utilizadas

- **Frontend**
  - [React](https://react.dev/)
  - [Vite](https://vitejs.dev/)
  - [TailwindCSS](https://tailwindcss.com/)

- **Backend**
  - [Python 3.10+](https://www.python.org/)
  - [Flask](https://flask.palletsprojects.com/)
  - [Flask-CORS](https://flask-cors.readthedocs.io/)

---

## 📂 Estrutura do projeto

Projeto/
│── backend/ # API Flask
│ ├── app.py
│ ├── sensor.py
│ └── ...
│
│── frontend/ # Interface React + Vite
│ ├── src/
│ ├── package.json
│ └── ...
│
└── README.md


---

## ⚙️ Como rodar o Backend (Flask)

1. Entre na pasta `backend`:

   ```bash
   cd backend
Crie e ative um ambiente virtual:


python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
Instale as dependências:

pip install -r requirements.txt
Rode o servidor:


python app.py
🔗 O backend estará rodando em: http://localhost:5000

🎨 Como rodar o Frontend (Vite + React)
Entre na pasta frontend:


cd frontend
Instale as dependências:

npm install
Rode o servidor de desenvolvimento:


npm run dev
🔗 O frontend estará rodando em: http://localhost:5173

🔗 Integração Frontend ↔ Backend
O frontend faz requisições para:


http://localhost:5000/data
⚠️ Certifique-se de rodar primeiro o backend, depois o frontend.

📦 Build de Produção
Para gerar a versão final do frontend:


cd frontend
npm run build
Os arquivos otimizados ficarão na pasta frontend/dist/.

✅ Checklist de execução
Inicie o backend (python app.py) → Porta 5000.

Inicie o frontend (npm run dev) → Porta 5173.

Acesse no navegador: http://localhost:5173.