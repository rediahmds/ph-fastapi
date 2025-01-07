# pH Susu Sapi API

This is an API for pH Susu Sapi. The data is collected from ESP32 that is connected with [PH Sensor Kit E-201C-Blue](https://digiwarestore.com/id/sensor-other/ph-sensor-kit-e-201c-blue.html) and sent to the server. The server will process the data and send it to the client.

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

![Espressif](https://img.shields.io/badge/espressif-E7352C.svg?style=for-the-badge&logo=espressif&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

</div>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher. You can download it [here](https://www.python.org/downloads/).
- SQLite3. You can download it [here](https://sqlitebrowser.org/dl/).

> [!TIP]
> It is recommended to use [Python 3.12.3](https://www.python.org/downloads/release/python-3123/) as it the version used in this project.

### Installing

#### 1. Clone the repository

Make sure you have git installed on your machine. You can download it [here](https://git-scm.com/downloads). Then, run the following command:

```bash
git clone https://github.com/rediahmds/ph-fastapi.git
```

After that, navigate to the project directory:

```bash
cd ph-fastapi
```

#### 2. Create and Activate Virtual Environment

Create a virtual environment using `venv` module.

- On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

- On macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Make sure you are in the project directory and the virtual environment is activated. You can see the `(venv)` prefix in your terminal. Below is an example of the terminal output:

![Virtual Environment successfully activated](/docs/assets/venv-success.png)

> [!NOTE]
> From here on, you have to make sure that the virtual environment is activated by checking the `(venv)` prefix in your terminal before running any command. If you close the terminal, you have to activate the virtual environment again.

#### 3. Install Dependencies

Install the dependencies using `pip`:

- On Windows:

```powershell
pip install -r requirements.txt
```

- On macOS and Linux:

```bash
pip3 install -r requirements.txt
```

#### 4. Run the Server

Run the server using the following command:

- On Windows:

```powershell
python .\src\main.py
```

- On macOS and Linux:

```bash
python3 ./src/main.py
```

If the server is running successfully, you will see the following output:

```bash
INFO:     Started server process [2700]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Now, you can access the server on [http://localhost](http://localhost) using a browser.

## API Documentation

To access the API documentation, you can go to [http://localhost/docs](http://localhost/docs) using a browser. You will see the following page:

![API Documentation](/docs/assets/api-docs.png)
