# Django-Sweet-Alert
This is a simple project on how to send your django messages to the frontend using sweetalert.js

First, you import the django messages module in your views.py file like this:

![image](https://user-images.githubusercontent.com/93172841/224373416-ae43a5fc-c9a3-4bce-a28d-411657c85186.png)

After that, in your view, you specify the kind of message you want to send. The method takes two arguments, request and the message.

![image](https://user-images.githubusercontent.com/93172841/224373773-0fe91f22-1102-4c65-a1f2-062f5416f697.png)

You can also specify the type of message you want, whether it's info, message, warning, error, etc. You could look through the messages docs for more using this link:
https://docs.djangoproject.com/en/4.1/ref/contrib/messages/

Now, to display the message, we need to first add the sweetalert.js CDN(Content Delivery Network) url to our template using the script tag like this:
![image](https://user-images.githubusercontent.com/93172841/224374643-c71c639a-23b8-4881-ac55-b6451b47470d.png)
This CDN is going to help us with the pop up messages. 

After this, we can then write a for loop in the template to loop through the message, we then add the "swal" function inside a script tag inside our for loop like this:
![image](https://user-images.githubusercontent.com/93172841/224375061-6617efe6-6e97-4f22-a68f-2fe8ca765dbd.png)

The first argument in the function is the title of the message, the second argument is the actual message and the final argument is the type of icon we want our
popup to display. The last argument can always be removed.
In my case, I passed my message tag there cause my message is tagged as a success message

This is what you should see in the end:

![image](https://user-images.githubusercontent.com/93172841/224375719-f64327c4-fec3-4954-8260-63fb6aa6c634.png)
