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
* It may happen that you may see the *__pyache__* folder in your end but not listed here, it's completely fine π
~~~

β   config.py
β   install.sh
β   ReadMe.md
β   requirements.txt
β   run.sh
β   server_run.sh
β   sleep.sh
β   wsgi.py
β
ββββsrc
    β   database.py
    β   routes.py
    β   __init__.py
    β
    ββββassets
    β       icon.ico
    β
    ββββDash
    β      apis.py
    β      components.py
    β      dashapp.py
    β      __init__.py
    β   
    β   
    β
    ββββstatic
    β   ββββcss
    β   β       main.css
    β   β
    β   ββββimgs
    β           check.jpg
    β           diabetes.jpg
    β           enrollPatient.jpg
    β           icon.ico
    β
    ββββtemplates
    β       checkNow.html
    β       enroll.html
    β       index.html
    β       layout.html
    β
    ββββUitls
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
* Just sit back and use the application π

# WorkFlow 
![Template builder (1)](https://user-images.githubusercontent.com/56304060/134165318-055a288b-f524-436d-938b-d452919f005b.png)

# Sample Images π
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
