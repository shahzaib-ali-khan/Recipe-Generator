# Recipe Generator (FastAPI)

Smart Recipe Generator using LLMs. This is FastAPI backend for generating recipes using LLMs. The service exposes endpoints to:

- Return supported LLM models
- Accept ingredient inputs + chosen model, and produce a recipe

It’s designed to be used via a bot (Telegram, etc.), frontend, or other client layers. A bot is already developed [here](https://github.com/shahzaib-ali-khan/Recipe-Generator-Client).

## ✅ Features

- List supported LLMs `GET /api/v1/supported_llms`
- Recipe generation via `POST /api/v1/recipes`
- Input validation, error handling
- Modular / multi-layer architecture (client layer, service, LLM integration)
- Docker‑friendly & environment‑driven configuration
- Logging for diagnostics


## ⚙️ Requirements & Setup

- Python 3.11+
- Poetry for dependency management
- An API key / credentials for your LLM provider (e.g. OpenAI)
- Docker & Docker Compose (for containerized setup)

## 🧩 Configuration & Environment Variables

Set the following env variables in settings file

```dotenv
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_openai_api_key
```

## 🏃 Running Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/shahzaib-ali-khan/Recipe-Generator.git
   cd Recipe-Generator
   ```

2. Install dependencies with Poetry:

   ```bash
   poetry install
   ```

3. Run the app:

   ```bash
   poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. API docs will be available at:

   - Swagger UI: `http://localhost:8000/docs`
   - Redoc: `http://localhost:8000/redoc`

## 🐋 Docker & Deployment

Create `compose.yml` in the root directory and paste below content:


```yaml
services:
  server:
    container_name: recipe-generator
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=your_openai_api_key
      - GEMINI_API_KEY=your_openai_api_key
```

then run `docker compose up -d`. Once container is running, access the API at `http://localhost:8000`.

