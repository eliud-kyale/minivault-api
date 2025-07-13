# MiniVault API
This is a lightweight REST API that recieves a prompt and returns an generated response. 

The response is from a local large language model(LLM) 'llama3'.

## Prerequisites

+ [Install *Docker*](https://docs.docker.com/get-started/get-docker/): Container Runtime 
  ```
  ❯ docker -v
  Docker version 28.3.0, build 38b7060
  ```

+ [Install *Python*](https://www.python.org/downloads/): Ensure you have Python 3.12 or later installed on your system.
  ```
  ❯ python --version
  Python 3.12.11
  ```

+ [Install *Ollama*](https://github.com/ollama/ollama/blob/main/docs/README.md): Locally deployed AI model runner

+ In a separate terminal window. Start Ollama. *Ctrl+C* to stop 
  ```
  ❯ ollama serve 
  ```

+ Verify Ollama is running. Either issuing a curl command or by web browser. [link](http://localhost:11434) 
  ```
  ❯ curl http://localhost:11434
  Ollama is running
  ```
+ Pull the ***llama3*** model 
  ```
  ❯ ollama pull llama3
  ❯ ollama list
  NAME             ID              SIZE      MODIFIED
  llama3:latest    365c0bd3c000    4.7 GB    ...
  ```

+ [Install uv](https://github.com/astral-sh/uv): Python Package and Project Manager 

+ [Install Postman CLI](https://learning.postman.com/docs/postman-cli/postman-cli-installation/): For running postman collections to test REST API
  ```
  ❯ postman --version
  1.17.0
  ```
## Usage

### Clone the GitHub Repository

  ```
  ❯ git clone https://github.com/eliud-kyale/minivault-api.git
  ```

<table>
<tr>
<td> <h3>Docker Container</h3> </td> <td>  <h3>Python Virtual Environment</h3> </td>
</tr>
<tr>
<td style="vertical-align: top;>
Running app in docker container ***Simplest Way***

+ A run.sh utility is provided for quickly 
building the image and starting the container.
  ```
  ❯ ./run.sh
  ```

</td>
<td>
Running app manually in python virtual environment

+ Setup Virtual Environment
  ```
  ❯ cd minivault-api
  ❯ uv .venv --python 3.12
  ❯ source .venv/bin/activate
  ```

+ Install python package dependancies in virtual environment
  ```
  ❯ uv sync
  ```

+ Start the application
  ```
  ❯ uv run fastapi dev app.py
  ```

</td>
</tr>
</table>

### Run Postman CLI to test REST API (Optional)

In a separate terminal
```
❯ cd minivault-api
❯ postman collection run ./minivault_generate.postman_collection.json
```
## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.

## System Considerations 

LLMs in general require sizable GPU and RAM to run 

For context, I ran this project on:

+ OS: macOS 15.5 24F74 arm64
+ Host: MacBookPro17,1
+ Kernel: 24.5.0
+ CPU: Apple M1
+ GPU: Apple M1
+ Memory: 16384MiB