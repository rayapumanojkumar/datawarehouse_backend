# FastAPI Data Warehouse

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fastapi_data_warehouse.git
    cd fastapi_data_warehouse
    ```

2. Build the Docker image:
    ```sh
    docker build -t fastapi_data_warehouse .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 80:80 fastapi_data_warehouse
    ```

## API Documentation
   ```
    http//host:port/docs
   ```

### Endpoints

- `POST /webhook`: Receive data from a webhook
- `GET /data/customers`: Retrieve stored customer data with pagination
- `GET /data/campaigns`: Retrieve stored campaign data with pagination
- `GET /sync/{source}`: Trigger synchronization for a specific data source
- `GET /tasks`: List all running background tasks
- `POST /tasks/cancel`: Cancel a specific background task

### Usage of AI

In this project, Got help from AI in ensuring best practices in structuring the application and debugging 
few endpoints and the project requirements.
