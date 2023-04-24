# Fake-News-Image-Recognition

**Team:** 
- Abdullah Kamal
- Zaid Jamal
- Brian Robinson
- Gabriel Rosales
- Zachary Sotny

## Description
Grover is a neural network that is able to classify text as machine written or human-written. Grover can not determine if the text is fake or real.
Our goal is to provide a way for users to verify if an image of an article is fake or real. Currently, only images from New York Times can be verified.
Our project uses Google Cloud Vision API and New York Times API to verify images of New York Times articles found on social media. Users can find an image of an article and upload it
using the front end. The backend takes this image and uses Google Cloud Vision to detect text. The New York Times API is then used to query this text and to
see if articles with that text exist in the New York Times database. A link to the article will be provided if the text is found in the article. If no link is found,
the image is considered fake news.

## How to Run This On Your Machine

### Environment Setup 
* Clone this repository onto your computer.
* Ensure that Python is installed on your system. (https://www.python.org/downloads/)
* Install Flask using ```pip install flask```
* Install support for .env files using ```pip install python-dotenv```
* Install Requests using ```pip install requests```
* Install Google Cloud Vision using ```pip install google-cloud-vision``` 

### Google Cloud Vision API Setup
* Go to https://cloud.google.com/vision/docs/setup and follow the steps to create a Google Cloud account, create a project, setup billing (there is a generous free trial), and enable the API. (Note: You do NOT need to install Google Cloud CLI)
* For authentication with Google Cloud Vision, you can either use OAuth 2.0 or a service account. API keys will not work.
* This project has been setup to work with a service account. To create one:
 * Go to the dashboard for the Google Cloud project you created and go to **APIs & Services** -> **Credentials**
 * Under **+Create Credentials** click **Service account** and enter a name and ID.
 * When granting the service account access to the project, make sure to specify the role of owner.
 * Once the service account is created, click on it and go to **Keys** -> **Add Key**. 
 * Select JSON as the format and save the generated file in the project directory on your machine.
 * On Line 13 of backend.py, replace ```fake-article-detect-15937-caffac9b5baf.json``` with the name of your JSON file. 

### New York Times API Setup
* Go to https://developer.nytimes.com/get-started and follow the steps to create an account and get an API key.
* Inside the project directory, create a file called .env and add the following line: ```NYT_API_KEY = 'YOUR_API_KEY'```

### Running and Testing 
* In your terminal, use ```python backend.py``` to run the code. 
* Click on the http://127.0.0.1:5000 link generated to view the website. 
* On the website's main page, scroll down to **Input Image of Article for News Verification:** and upload an image of an article (accepted file types are png, jpg, jpeg, and gif). Test samples of real and fake articles have been provided in the articles folder. 
* Upon clicking **Submit** the website will reload and under **Is This News Real or Not?** an link to the New York Times article will be provided if the article is real, or the website will let you know it is fake. 

### Limitations 
* The NYT API has a limit on the number of calls that can be made every minute so allow a few moments between testing different images. If too many calls are made, you will recieve a 500 error. Simply restart the website and wait a few moments before submitting another image. 
* This code will only work for articles that are from the New York Times. APIs for other news sites could be added in the future. 
* If the image of the article has miscellaneous information at the bottom, it may cause issues for the NYT API.

### Proposal
We detailed our solution in a short research proposal utilizing IEEE's conference paper format. Included in it are the reasons for developing our solution as well as a quick rundown of the various components included in our project. 

*Paper URL*: https://drive.google.com/file/d/1WGj14UHhiYGJuBa-X4Rx2_p8-n5vZvIo/view?usp=sharing
