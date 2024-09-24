assignment 4
1. HttpResponseRedirect() is a class in Django that is used to perform a manual redirect to a different URL. It takes a URL as an argument and sends a response telling the browser to navigate to that URL.

redirect() is a convenience function provided by Django that abstracts away the lower-level HttpResponseRedirect(). It can accept not only a URL string but also a view name or even an object, making it more flexible.

2. In Django, a foreign key relationship can link MoodEntry model and User model as so:
user = models.ForeignKey(User, on_delete=models.CASCADE)
This creates a relationship where each mmood entry is related to a specific user to retrieve all mood entries made by user.

3. Authentication: process of verifying who a user is
Authorization: process of determining what an authenticated user is allowed to do

4. Django stores data on the server and a session ID in a cookie on the user's browser. Every time the user makes a request, the session ID is sent along with it, allowing Django to recognize the user as logged in.

Other uses of cookies:
- Tracking user preferences: Cookies can be used to store user preferences, such as language settings or dark mode preferences.
- Cart functionality: In e-commerce sites, cookies can track the items added to a user's shopping cart.
- Analytics and tracking: Cookies are used for analytics purposes to track user behavior and activity on a website.

Not all cookies are safe, especially when dealing with sensitive information. 

5. First I implemented function and registration forms by adding the registration form and created the register mechanism. This is done by editing views.py and urls.py and creating register.html.

Next, I implemented a login function by importing authenticate, login and AuthenticationForm (built-in Django functions) in views.py and adding a login_user function to authenticate users to log in. Then, I created login.html and edited urls.py as needed.

After that, I implemented a logout function by editing and importing logout in views.py. I also implemented the logout mechanism by creating a logout_user function, then I edited main.html so that it would link to the URL based on app_name and name defined in urls.py. I then edited urls.py as needed

I also restricted access to the main page then used data from cookies by importing HttpResponseRedirect, reverse and datetime and modified a few functions in views.py

Finally, I connected ProductEntry model to the User model by linking each ProductEntry object created to the user who made it so that an authorized user only sees entries they created.



















assignment 3
1. Enables communication between different parts of the system and between platforms and users. It forms the backbone of communication in any platform, ensuring that information flows seamlessly across all components.

2. JSON is generally better for web applications because it is:
- simpler, more compact syntax compared to XML.
- easier and faster to parse, especially in JavaScript.
- JSON data is easy for both humans and machines to read.

XML may be better for complex documents and data interchange where the structure needs to be more rigorous:
- more flexible with its support for attributes and nested elements, making it useful for defining complex data structures.
- XML supports namespaces, which helps in differentiating similar data fields in large documents.

JSON is more popular than XML because:
- JSON is faster to parse and generate than XML.
- JSON's minimal syntax makes it easier to write, read, and debug. This is a key reason for its widespread adoption in modern APIs.
- JSON is directly compatible with JavaScript, the most widely used language for web development, making it a natural choice for web applications.
-  JSON is more concise, requiring fewer characters to represent data than XML

3. The is_valid() method in Django forms checks whether the form data is valid by:
- Validating Data: It runs through all field validators and ensures that the data conforms to the rules defined in the form’s fields (e.g., required fields, data types, and length constraints).
- Cleaning Data: After validation, the is_valid() method stores the cleaned data in form.cleaned_data for further processing (e.g., saving to the database).
- Returns a Boolean: If the data is valid, it returns True; otherwise, it returns False and stores error messages in form.errors.

Why Do We Need is_valid()?
- Error Handling: It prevents invalid or incomplete data from being processed and provides users with informative error messages to fix issues in form submission.
- Security: Validating data before processing ensures that only clean, expected data is accepted, reducing the risk of malicious input or data corruption.

4. - prevent attackers from submitting forms on behalf of users.
- avoid exploitation of authenticated user's session and take over sensitive operations

5. Compare them with tutorial 2 and implement them. First I implemented the Skeleton of a View, then changed the Primary Key from integer to UUID, then I created as form input data and displayed data on HTML. Next I returned data in both XML and JSON format and did it based on an ID, then I used Postman as a data viewer and deployed to PWS

![WhatsApp Image 2024-09-18 at 11 21 39_39d33e01](https://github.com/user-attachments/assets/0d7c5adb-a8ab-4c6a-a41e-a48a0ff8ca58)
![WhatsApp Image 2024-09-18 at 11 22 04_87fd11b8](https://github.com/user-attachments/assets/a1c0bdab-6607-4e32-8ac7-ff4706507863)
![WhatsApp Image 2024-09-18 at 11 22 45_e458d2f4](https://github.com/user-attachments/assets/7fcac5c7-78f9-4ca2-99db-c6fe57466c67)
![WhatsApp Image 2024-09-18 at 11 23 14_1c26978f](https://github.com/user-attachments/assets/c5ea2597-bafb-478f-970e-651ba471b8c8)






















assignment 2
1. First, I figured out to combine Tutorial 0 and 1 for this assignment, then after comparing the checklist and the tutorial, I simply followed the tutorials with the checklist as my guideline and made changes where necessary. I created a new repository for the new project and many folders and files inside folders as shown in the checklist, I then performed routing and created a model. I had to adjust here and for the function in views.py as well. I then created a routing in urls.py for the application main to map the function created in views.py then deployed to PWS.

2. <img width="286" alt="image" src="https://github.com/user-attachments/assets/c88d1e20-4970-46e5-bdc2-6fdececffa90">

   urls.py -> maps URLs to specific views (which view should handle that request)
   views.py -> contains the logic to execute request, communicates with models.py to fetch or update data from database, if necessary, it will pass data to HTML template for rendering
   models.py -> defines models (data structure), interacts with database
   HTML file -> view passes data to HTML file, dynamically generates a webpage using the provided data, and this page is then returned to the client as a response

4. Git can track changes made. Git keeps track of changes made so that developers can review or go back to the previous code when needed. Git can allow developers to collaborate as it allows merging without conflict and also branch so that if anything happens to one branch, the others will not be affected. Git can also back up data.
   
5. I find it seamless that it uses chunks of python and HTML so that we can learn something new and strengthen previous knowledge as well. Despite many new things to learn, I did not struggle as much as I had been familiar with Python.
  
6. It allows developers to interact with the database using Python objects rather than writing raw SQL queries. This way, it reduces errors in database interactions.

link:


