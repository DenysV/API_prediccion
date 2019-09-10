# API_prediccion
API HTTP presiccion

1. Download and unzip this source repository, or clone it using Git:
  git clone https://github.com/DenysV/API_prediccion.git foldername_local

2. Create virtualenv
This is required once before installing dependencies

Windows
  virtualenv.exe -p python2.exe venv

UNIX
  virtualenv -p python2.7 venv

3. Activate virtualenv
This is required before installing dependencies or running the project.

Windows
  venv\Scripts\activate

UNIX
  source venv/bin/activate

4. Once virtualenv is activated, your prompt will change. To deactivate it, run
deactivate

5. Install dependencies
With virtualenv enabled, run
  pip install -r requirements.txt

6. Run the Project
With virtualenv enabled, run
  python main.py
