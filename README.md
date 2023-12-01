# Live Bitcoin Price Dashboard

## Project Overview

This Django project features a live dashboard that displays real-time Bitcoin prices. It utilizes Django Channels and WebSockets for real-time data streaming, and fetches Bitcoin price data from the CoinGecko API. The project is configured to use Redis as the channel layer for handling WebSocket connections.

## Setup and Installation

### Prerequisites

-   Python 3.6 or higher
-   Redis server (Local or Cloud-based)

### Project Setup

1. **Create Django Project**

    ```bash
    django-admin startproject project
    cd project
    ```

2. **Create Django App**

    ```bash
    python manage.py startapp live_dashboard
    ```

3. **Install Dependencies**

    Install the required Python packages using pip:

    ```bash
    pip install django
    pip install python-decouple
    pip install channels channels_redis
    ```

### Configuration

1. **.env File**

    Create a `.env` file in the root of your Django project and add the following (replace with your actual Redis credentials):

    ```
    REDIS_HOST=your_redis_host
    REDIS_PORT=your_redis_port
    REDIS_PASSWORD=your_redis_password
    ```

### Run the Application

Start the Django application using Uvicorn:

```bash
uvicorn project.asgi:application --port 8000
```

### Access the Dashboard

Open a web browser and navigate to:

```
http://127.0.0.1:8000/dashboard/
```

### External Services

-   **Redis**: Set up a Redis instance. For a cloud-based setup, visit [Redis Labs](https://app.redislabs.com).
-   **Bitcoin Price API**: The application fetches data from [CoinGecko's Bitcoin Price API](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd).
