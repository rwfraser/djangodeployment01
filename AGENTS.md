# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a **Pyramid** web application (not Django, despite the repo name). It serves a simple "Hello World" response at the root route.

## Commands

### Local Development
```powershell
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server (port 8000)
python server.py

# Run with custom port
$env:PORT=3000; python server.py
```

### Production (gunicorn)
```bash
gunicorn server:app --bind 0.0.0.0:$PORT
```

## Architecture

### Entry Point
- `server.py` - Single-file application containing all routing and views
  - `create_app()` - Application factory that returns WSGI app
  - `app` - Module-level WSGI object used by gunicorn
  - `hello_world()` - View function for the root route (`/`)

### Deployment
- `Procfile` - Defines web process for Render.com/App Runner
- Cloud platforms inject `PORT` environment variable; app defaults to 8000 locally

## Dependencies
- `pyramid` - Web framework
- `gunicorn` - Production WSGI server
