![image-recognition-microservice](./assets/logo.png)

# Image Recognition Microsevice

This is a standalone microservice for `image recognition` and question answering. It can analyze an image and respond to specific questions about its content. The server is built using `Python` and `moondream` (a small vision language model designed to run efficiently on edge devices, ([more on huggingface](https://huggingface.co/vikhyatk/moondream2)) for image recognition and question answering.

## Features

- Recognizes objects and scenes in images.
- Answers questions related to the image's content.
- Simple REST API for integration.

## Brief Example

![image-example](./assets/example.png)

### Describe this image (default question)

> The image depicts the animated character Homer Simpson in a room, pointing to a drawing of a car on a whiteboard.

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/ -H "Authorization: Bearer 123" -F "image=@./assets/example.png"
```

**Response:**

```json
{
  "answer": "The image depicts the animated character Homer Simpson in a room, pointing to a drawing of a car on a whiteboard.",
  "question": "Describe this image"
}
```

### Describe in detail this image

> The image depicts a scene from the animated television series "The Simpsons". The central figure is Homer Simpson, a renowned character known for his love of cars. He is standing in front of a whiteboard, which displays a drawing of a car. Homer is pointing towards the drawing, suggesting he is explaining or admiring it. The background is a vibrant purple color, providing a contrast to the whiteboard and the yellow figure of Homer.

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/ -H "Authorization: Bearer 123" -F "image=@./assets/example.png" -F "question=Describe in detail this image"
```

**Response:**

```json
{
  "answer": "The image depicts a scene from the animated television series \"The Simpsons\". The central figure is Homer Simpson, a renowned character known for his love of cars. He is standing in front of a whiteboard, which displays a drawing of a car. Homer is pointing towards the drawing, suggesting he is explaining or admiring it. The background is a vibrant purple color, providing a contrast to the whiteboard and the yellow figure of Homer.",
  "question": "Describe in detail this image"
}
```

### What color is the skin?

> The color of skin in the image is yellow.

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/ -H "Authorization: Bearer 123" -F "image=@./assets/example.png" -F "question=What color is the skin?"
```

**Response:**

```json
{
  "answer": "The color of skin in the image is yellow.",
  "question": "What the color of skin?"
}
```

## Table of Contents

- [Image Recognition Microsevice](#image-recognition-microsevice)
  - [Features](#features)
  - [Brief Example](#brief-example)
    - [Describe this image (default question)](#describe-this-image-default-question)
    - [Describe in detail this image](#describe-in-detail-this-image)
    - [What color is the skin?](#what-color-is-the-skin)
  - [Table of Contents](#table-of-contents)
  - [Server](#server)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Configuration](#configuration)
    - [Start the server](#start-the-server)
    - [Dependencies](#dependencies)
  - [API Usage](#api-usage)
    - [Endpoint](#endpoint)
    - [Headers](#headers)
    - [Form Data](#form-data)
    - [Example Request](#example-request)
    - [Example Response](#example-response)
    - [Example Response with Error](#example-response-with-error)
  - [Node.js Image Recognition Client](#nodejs-image-recognition-client)
    - [Installation](#installation-1)
    - [Usage](#usage)
    - [API](#api)
    - [Notes](#notes)
  - [Project Structure](#project-structure)
  - [License](#license)
  - [Contributing](#contributing)
  - [Support](#support)
  - [Created by](#created-by)


## Server

### Prerequisites

1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).
2. Prepare an `.env` file for API token configuration.

### Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Edit `.env` file and set the `API_TOKEN`:
   ```plaintext
   API_TOKEN=your_secret_token
   ```

3. Build and run the service using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. The API will be available at `http://127.0.0.1:5000/`.

### Configuration

Set the `API_TOKEN` in the `.env` file to secure the API. Example:
```plaintext
API_TOKEN=your_secret_token
```

### Start the server

To start the server, run the following command:

```bash
sudo docker compose build
sudo docker compose up
```

After running the command, wait for the following message to appear in the terminal:

```plaintext
api-1  |  * Serving Flask app 'server'
api-1  |  * Debug mode: off
api-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
api-1  |  * Running on all addresses (0.0.0.0)
api-1  |  * Running on http://127.0.0.1:5000
api-1  |  * Running on http://172.21.0.2:5000
api-1  | Press CTRL+C to quit
```

The server will be available at `http://localhost:5000/`.

### Dependencies

- Python 3.10
- Flask
- PyTorch
- Pillow
- Transformers
- Einops

## API Usage

### Endpoint

**POST /**

### Headers

- `Authorization: Bearer <your_secret_token>`

### Form Data

- `image`: The image file to be analyzed (e.g., `.jpg`, `.png`).
- `question`: A string containing the question about the image. Optional, default value is `Describe this image.`.

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/ \
-H "Authorization: Bearer your_secret_token" \
-F "image=@./assets/example.png" \
-F "question=Describe this image."
```

### Example Response

```json
{
  "question":"Describe this image.",
  "answer":"A close-up image of a pile of ripe, red strawberries with green leaves."
}
```

### Example Response with Error

```json
{
  "question":"Describe this image.",
  "error":"Invalid image format."
}
```

## Node.js Image Recognition Client

This client provides a simple interface to interact with the Image Recognition. It allows you to easily recognize objects and scenes in images and ask questions about them.

See [Server](#server) section to set up the server.

### Installation

To install the image recognition client, use npm:

```bash
npm i -S image-recognition-microservice
```

### Usage

Here's a basic example of how to use the image recognition client:

```typescript
import ImageRecogniton from 'image-recognition-microservice';

// Initialize the client with the server URL
const imageRecognition = new ImageRecogniton('http://localhost:3000');

const imageBuffer = await readFile('path/to/your/image.jpg');
const image = new File([imageBuffer], 'image.jpg', { type: 'image/jpeg' });

// Check the file
const result = await imageRecognition.recognize(image, 'Describe this image.');

// Log the result
console.log(result);
```

In this example, we're reading an image file from disk, creating a `File` object, and passing it to the `recognize` method along with a question. The method returns a promise that resolves to an object with the answer to the question.

### API

The `ImageRecogniton` class provides the following method:

- `recognize(file: File | Blob, question: string): Promise<{ question: string, answer?: string, error?: string }>`
  
  Scans the provided file for viruses. Returns a promise that resolves to an object with:
  - `answer`: a string with the answer to the question asked about the image.
  - `error`: a string with error message if the file is not recognized.
  - `question`: the question that was asked.

### Notes

- Make sure the (Image Recognition Server)[#server] is running and accessible at the URL you provide when initializing the `ImageRecogniton` client.
- The client works with both `File` and `Blob` objects, making it flexible for various use cases.
- Error handling is built into the client. If there's an error communicating with the server, the `recognize` method will return `{ error: 'Error message', question: 'The question asked' }`.

For more information on setting up and using the server, refer to the [Image Recognition Server](#image-recognition-microservice-server) documentation above.

## Project Structure

- `Dockerfile`: Docker configuration for the service.
- `docker-compose.yaml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.
- `src/server.py`: Server implementation.
- `src/client.js`: Node.js client.
- `.env.example`: Example of environment variables.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support

If you encounter any problems or have questions, please open an issue in the project repository.

## Created by

Dimitry Ivanov <2@ivanoff.org.ua> # curl -A cv ivanoff.org.ua

