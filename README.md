# Assignment-Tasks

Deployment Instructions For AWS Lambda Functions
Create a Lambda Function:

1. Go to the AWS Lambda console.
2. Create a new function, choosing "Author from scratch."
3. Use Python as the runtime.
4. Add the Function Code:
5. Copy and paste the code into the code editor.
6. Test the Function:
7. Create a test event in the AWS Lambda console with the following JSON:
{
  "num1": 5,
  "num2": 10
}
8. Run the test to verify that the function returns the sum.


Deployment Instructions For Django Chat App

1. Install Python and ensure it's accessible via python or python3.
2. Navigate to the Django project directory.
3. Create a virtual environment: python -m venv env.
4. Activate the virtual environment:
    Windows: .\env\Scripts\activate
    macOS/Linux: source env/bin/activate
5. Install project dependencies: pip install -r requirements.txt.
6. Apply database migrations: python manage.py migrate.
7. Create a superuser (optional): python manage.py createsuperuser.
8. Run the development server: python manage.py runserver.
9. Access the app in a browser: Navigate to http://127.0.0.1:8000.
10.Test functionalities to ensure proper setup.

I tried to host on PythonAnywhere but it was showing error saying Something Went Wrong. I have attached a screenshot of it.
![image](https://github.com/user-attachments/assets/4dcdccc3-0307-4c7b-8a77-541c02f09fc9)


Deployment of Front-End Project
1. Open a folder in VS code.
2. Create the files name
   index.html
   styles.css
   scripts.js
3. Right click on screen in index.html file
4. Now open the index.html file "Open with live server" option.
