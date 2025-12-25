## to create env:-

python -m venv venv-fastapi

venv-fastapi\Scripts\activate

(update pip whenever you create a virtual env.)

## to download requirements

pip install -r requirements.txt

## to run

uvicorn main:app --reload --port 8080 (cant use in production better for development)

## to check api run fine --> swagger UI
http://localhost:8080/docs


## github commands
## first time

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git push -u origin main


## eevrytime after

git add .
git commit -m "Update"
git push

