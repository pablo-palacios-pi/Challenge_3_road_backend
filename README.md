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


## 🐬 MySQL con XAMPP o Docker (uso local)

Si necesitás una base de datos local, podés levantar fácilmente un servidor MySQL local.

---

### 🧰 Requisitos

- **Tener [XAMPP](https://www.apachefriends.org/es/index.html) o MySQL instalado localmente**  
  _O bien usar Docker para levantar un contenedor MySQL._

---

### ⚙️ Configuración por defecto (local)

Por defecto, se espera que MySQL esté corriendo con los siguientes datos:

- **Host:** `127.0.0.1`
- **Usuario:** `root`
- **Contraseña:** _(vacía)_
- **Base de datos:** `test`

---

### 📦 Levantar MySQL con Docker (opcional)

Si preferís usar Docker:

```bash
docker run --name mysql-local -e MYSQL_ROOT_PASSWORD= -e MYSQL_DATABASE=test -p 3306:3306 -d mysql:latest
```

Verificá que esté corriendo:

```bash
docker ps
```



## 🚀 Correr la API
Ejecutá el siguiente comando para levantar el servidor:

```bash
uvicorn main:app --reload
```
Esto iniciará la API en http://localhost:8000
