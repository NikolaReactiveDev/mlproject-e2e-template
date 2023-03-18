# Template steps for conducting an End-To-End Machine learning Project

### Initially: Set up Project with Github
1.	Data Ingestion
2.	Data Transformation
3.	Model Trainer
4.	Model Evaluation
5.	Model Deployment

CI/CD Pipelines – Github Actions

Deployment – AWS

## Agenda (whenever working on ML project w/ team)
Before everything else:	Set up the Repository (Github) – deciding/establishing formal project structure
a)	Make New environment
b)	Setup.py
c)	Requirements.txt – build a package

* Step 1. Create New GitHub Repository named by the project (*-mlproject)
* Step 2. Create virtual environment with Conda in desired folder where project will reside.
Cmd: conda create -p venv python==3.8 -- to create venv and install python version we need 
	conda activate venv  -- to activate the virtual environment
* Step 3. Syncing with github repo we already made. We need to execute series of commands in terminal:
git init
git add README.md (need to create that file in your folder first!)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/NikolaReactiveDev/mlproject-e2e-template.git (git remote -v to confirm we synced with remote repository on github)
git push -u origin main
After these commands or before all create .gitignore directly on GitHub with template for python language and execute: git pull --to pull .gitignore file from repository

* Step 4. Create setup.py and requirement.txt files in root working project folder
Setup.py – would be responsible for setting up our project/ml application as package so it can be installed and used in another project. This file is called the Setup Script, the main purpose is to describe our module to the Distutils, so the various commands that operates on our module do the right thing. 
Create ./src folder and inside of it __init__.py file, so setup() from setuptools can find it upon execution and treat it as a package it needs to build.
