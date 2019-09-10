# API_prediccion

API_HTTP_presiccion in Docker container
1. Download and unzip this source repository, or clone it using Git:
  git clone https://github.com/DenysV/API_prediccion.git foldername_local

2. In foldername_local that Dockerfile run in terminal sudo docker build . -t user_name/prediccion.

3. Check that image was created successfully and see its ID, run sudo docker images | grep prediccion.

4. Start API-> run images: sudo docker run -p 5000:5001 ID_image.

5. Start in browser 0.0.0.0:5000

API_HTTP_presiccion in local

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
