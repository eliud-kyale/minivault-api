# MiniVault API
This is a lightweight REST API that recieves a prompt and returns an generated response.

The response is from a local large language model(LLM) 'llama3'.

## Notes

The application is written Python and makes use of 2 python libraries:
+ [FastAPI](https://fastapi.tiangolo.com/): A web framework that makes writing REST API handlers easy
+ [Ollama Python](https://github.com/ollama/ollama-python): A wrapper library for send REST requests to a local Ollama server

Both the Ollama server and my application are running in Docker containers. This helps simplify the dependancies on the host machine. No complicated python virtual enviroments or installations.

In the future, I’d like to incorporate model management into the API. Currently, the LLM is hardcoded to use 'llama3'.

Additionally, a nice enhancement would be to allow users to load multiple models and generate side-by-side responses from the different LLMs.

## Prerequisites

+ [Install *Docker*](https://docs.docker.com/get-started/get-docker/):
  Container Runtime
  ```
  docker -v
  ```
  ```
  Docker version 28.3.0, build 38b7060
  ```

+ [Install Postman CLI](https://learning.postman.com/docs/postman-cli/postman-cli-installation/): (***Optional***)
  For running postman collections to test REST API
  ```
  postman --version
  ```
  ```
  1.17.0
  ```
## Usage

### Clone the GitHub Repository

```
git clone https://github.com/eliud-kyale/minivault-api.git
```
### Run the Ollama server in a Docker Container

```
docker run \
-d -v ollama:/root/.ollama \
-p 11434:11434 --name ollama \
--add-host=host.docker.internal:host-gateway  \
ollama/ollama

curl http://localhost:11434
```
```
Ollama is running
```

### Pull the ***llama3*** model

```
docker exec ollama ollama pull llama3
docker exec ollama ollama list
```
```
  NAME             ID              SIZE      MODIFIED
  llama3:latest    365c0bd3c000    4.7 GB    3 minutes ago
```

### If the ollama pull fails - download a huggingface equivalent

```
docker exec ollama ollama pull hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:Q4_K_M
docker exec ollama ollama cp hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:Q4_K_M llama3
docker exec ollama ollama list
docker exec ollama ollama show llama3
```
Send a Curl prompt to verify the model is working
```
docker exec ollama ollama run llama3 "Marco?"
It seems like we just started! How can I assist you today? Do you want to talk about Marco, or is there something else on your mind?
```
### Run application in Docker Container

A [run.sh](https://github.com/eliud-kyale/minivault-api/blob/master/run.sh) utility will
build and run the application in a docker container.
```
./run.sh
```

### Verify both containers are running
```
docker ps
```
```
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                                             NAMES
3249e4f64d1f   eliudkyale/minivault-api   "fastapi dev --host …"   58 seconds ago   Up 56 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp       gallant_rubin
1c81d9b09950   ollama/ollama              "/bin/ollama serve"      22 minutes ago   Up 22 minutes   0.0.0.0:11434->11434/tcp, [::]:11434->11434/tcp   ollama
```

### Test REST api using Curl

GET '/' Request (Welcome Page)
```
curl http://localhost:8000
```
```
    <html>
        <head>
            <title>Written by Eliud Kyale</title>
        </head>
        <body>
            <h1>MiniVault API using 'llama3' LLM local instance</h1>
        </body>
    </html>
    %
```

POST '/generate' Request
```
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt":"Marco ?"}'
```
```
{"response":"Polo!"}%
```

### Run Postman CLI to test REST API (Optional)

A sample [postman collection](https://github.com/eliud-kyale/minivault-api/blob/master/minivault_generate.postman_collection.json) is provided to test the REST API
In a separate terminal
```
cd minivault-api
postman collection run ./minivault_generate.postman_collection.json
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/eliud-kyale/minivault-api/blob/master/LICENSE) file for details.

## System Considerations

LLMs in general require sizable GPU and RAM to run. Some prompts could take upto 2 mins to run

For context, I ran this project on:

+ OS: macOS 15.5 24F74 arm64
+ Host: MacBookPro17,1
+ Kernel: 24.5.0
+ CPU: Apple M1
+ GPU: Apple M1
+ Memory: 16384MiB
