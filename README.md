# Python Web Services
This is an amazing project were I develop a system that updates an information catalog with data provided by 'suppliers.' The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images are converted to smaller jpeg images and the text is turned into an HTML file that shows the image and the product description. The contents of the HTML file are then uploaded to a web service that is already running using Django. I then gather the name and weight of all fruits from the .txt files and use a Python request to upload it to a Django server.

I also created a Python script that processes the images and descriptions and then updates the company's online website to add the new products.

Once the task is complete, the supplier are notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should has a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, I check the health of the system and send an email if something goes wrong.
