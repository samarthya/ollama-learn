# 📜 Level 7 Grimoire: The Capsule (Containerization)

We have built a creature of logic (Python). Now we must build it a Spacesuit (Docker) so it can survive anywhere.

## 📦 Concept 1: The Dockerfile (The Recipe)

A `Dockerfile` tells a computer how to build your app from scratch.

- `FROM python:3.10`: Start with Linux + Python.
- `COPY . .`: Put our code inside.
- `RUN pip install`: Add dependencies.
- `CMD streamlit`: Run the app.

## 🐙 Concept 2: Compose (The Orchestra)

`docker-compose.yml` lets us run complex systems with one command: `docker-compose up`.

- It handles **Ports** (`8501:8501` means "Map my localhost 8501 to the container's 8501").
- It handles **Environment Variables**.

## 🕸️ Concept 3: Networking (The Bridge)

This is the hardest part.

- **Localhost inside Docker** != **Your Computer**.
- "Localhost" inside the container just means "The Container itself".
- To talk to your specific Windows Ollama, we pass `OLLAMA_HOST_IP` as an Environment Variable.

---

**THE FINAL ACT**

To run your creation (Docker):

```bash
docker-compose up --build
```

To run with **Podman** (Rootless):

1.  Ensure you have `podman-compose` or just use `podman compose` (newer versions).
2.  Run:
    ```bash
    podman-compose up --build
    ```

Open `http://localhost:8501`.
