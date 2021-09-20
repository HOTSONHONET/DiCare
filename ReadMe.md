# DiCare

A web app backed by a predictive model which can distinguish patients at the time of admission whether they are going to be readmitted again to the hospital within a month. Here, the model is only responsible for diabetes patients and it will take some qualitative features to perform the task. By screening out more vulnerable patients, more attentive and qualitative treatment plans can be made..


# How to install dependecies ?

* Install [python 3.7+](https://www.python.org/downloads/release/python-378/)
* Open a terminal and type in the below command to install **virtualenv** module
~~~
pip install virtualenv
~~~

* Create a new folder and clone this repository *(Assuming you already have **git** installed)*
~~~
git clone https://github.com/HOTSONHONET/DiCare.git
~~~

* Use `Shift + rightclick` to open up a terminal in the folder
* Create a virtual environment and install all the dependecies from **requirements.txt**
~~~
virtualenv <name-of-env>
./<name-of-env>/Scripts/activate
pip install -r requirements.txt
~~~


# Folder Structure
* After downloading the weight file, make sure you have the same folder structure
* It may happen that you may see the *__pyache__* folder in your end but not listed here, it's completely fine 👌
~~~

│   config.py
│   install.sh
│   ReadMe.md
│   requirements.txt
│   run.sh
│   server_run.sh
│   sleep.sh
│   wsgi.py
│
├───src
    │   database.py
    │   routes.py
    │   __init__.py
    │
    ├───assets
    │       icon.ico
    │
    ├───Dash
    │      apis.py
    │      components.py
    │      dashapp.py
    │      __init__.py
    │   
    │   
    │
    ├───static
    │   ├───css
    │   │       main.css
    │   │
    │   └───imgs
    │           check.jpg
    │           diabetes.jpg
    │           enrollPatient.jpg
    │           icon.ico
    │
    ├───templates
    │       checkNow.html
    │       enroll.html
    │       index.html
    │       layout.html
    │
    ├───Uitls
         model.py
         reAdmissionDiabeticsModel.pkl
         StndSclr.sav

~~~


# How to run the application ?
* Open command prompt inside the clone folder using `Shift + rightclick`
* Type the below command <em>(use python3 instead of py, if you are on Ubuntu)</em>
~~~
py wsgi.py
~~~

# Installing in EC2 Instance
* Create an Ubuntu EC2 instance... 
* Clone the repository there... 
* Run `run.sh`, it will install all the required files and dependency automatically... 
* Just sit back and use the application 😁

# Sample Images 😉
<table>
  <tr>
    <td>Homepage</td>
     <td>Readmission Check</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56304060/114261767-13eb6600-99fa-11eb-99b0-c3eda4d3e447.png" width=500 height=200></td>
    <td><img src="https://user-images.githubusercontent.com/56304060/114261769-151c9300-99fa-11eb-82a6-0ada52ea4bf9.png" width=500 height=200></td>
  </tr>
  <tr>
    <td>Enroll</td>
    <td>Dashboard</td>     
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56304060/114261766-12ba3900-99fa-11eb-9549-da8f9cb2215d.png" width=500 height=200></td>
    <td><img src="https://user-images.githubusercontent.com/56304060/114261764-11890c00-99fa-11eb-87eb-b96f1da742d5.png" width=500 height=200></td>    
  </tr>
 </table>
