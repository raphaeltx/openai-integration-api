# OpenAI API integration

Ask questions to OpenAI!

## Endpoint: It Grows

**Purpose:**  
This endpoint returns the response from OpenAI API based on the user prompt.

### **URL**

`POST /ask-question`

### **Body**

```
{
  "text": "value"
}
```

### Response example

```
{
    "data": "value"
}
```

## How to run locally

Make sure you have python3 installed. Create a Virtual Environment:

```
python -m venv venv
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the following command at the root of the project: 

```
fastapi dev main.py
```

You can also with docker compose. Make sure you have docker and docker compose installed.
Run the following command in the root directory:

```
    docker-compose up --build
```

### You can access the endpoint by the URL http://localhost:8000