# Pyramid Hello World

A simple Pyramid web application ready for cloud deployment.

## Local Development

1. Create virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run locally:
   ```
   python server.py
   ```

## Deployment

This app is configured for deployment to Render.com or AWS App Runner.

- **Render.com**: Connect repo and deploy as Python Web Service
- **AWS App Runner**: Connect repo and configure Python runtime

The `Procfile` defines the web process using gunicorn.
