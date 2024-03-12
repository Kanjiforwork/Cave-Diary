# CAVE DIARY - CS50 Final Project
#### Demonstation on Youtube:  <URL HERE>
#### Description:
Welcome to Cave Diary. This is the final project for my cs50 course.
Essentially, this website allows you to write your diary whenever you want. What's more, the background is a cartoonish picture of a cave which moves around whenever you scroll down. You can either write and review your diaries or perhaps mess around with the parallax effect of the background for fun.
## Technologies used:
1. Python
2. Html
3. Sqlite3
4. Css
5. Flask framework
6. Figma


## How to use it?
1. Login with your username and password.
2. Then you will have access to a private space.
3. Ckick "Write here" to get started, fill in the form and hit submit to store your diary.
4. Scroll below to review the diaries you have written and click on them to read them again.

# Files and Structure:

## Templates
#### 1. login.html
- Here you can log in to your account via your username and password.
#### 2. register.html
- A space to make a new account, here you are asked for a new username, a password and a confirmation for said password.
#### 3. main.html
- This is the main space. On top of the page is the header that displays the name of the page, the name of the user and a "log out" button
- The selling point of the page is the parallax image whose components move around when you scroll down.
- The page includes a "Write here" button which opens a form in which you can go about writing your diary.
- After submitting a diary, you can access it at the bottom of the file.
- Each submitted diary encompasses a title, a content and the date it is written.
- Once clicked, each diary will enlarge, providing you with a better view of the content.
#### 4. layout.html
- This html serves as a layout for the aforementioned sites

## Static
#### 1. style.css
- Manage the style of login.html and register.html.
#### 2. parallax.css
- Manage the style of main.html.
#### 3. Others
- Mostly pictures and PNG components for the parallax effect in main.html.
- The mentioned components are rated from a picture using Figma as the main tool.

## Final.db
- Includes 2 tables:
+ users: username, hash. (Here is basically where your username and the hash of your password is stored)
+ diaries: time, username, topic and content. (Here is the place that stores your diary)

## app.py
- Manage the logic and overall flow of the website.
- For login.html and register.html: check for valid username and password.
- For main.html: store and load the diary of the user based on their username.

