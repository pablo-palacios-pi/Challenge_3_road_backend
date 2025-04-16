# 🚀 Challenge 3 - Backend API

Repositorio que resuelve el **Challenge 3**.

📄 **Challenge original**: `Challenge 3.docx`

---

## 📦 Preparación del entorno

Primero, generá un entorno virtual con el nombre `.venv`:

### Usando virtualenv 
```bash
virtualenv .venv
```
### Con venv de Python
```bash
python3 -m venv .venv
```

### Luego activalo

#### En Windows:
```bash
.venv\Scripts\activate
```

#### En macOS/Linux:

```bash
source .venv/bin/activate
```


## 🚀 Correr la API
Ejecutá el siguiente comando para levantar el servidor:

```bash
uvicorn app:main --host 0.0.0.0 --port 8000 --reload
```
Esto iniciará la API en http://localhost:8000

