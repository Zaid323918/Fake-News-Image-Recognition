# Fake-News-Image-Recognition

**Team:** 
- Abdullah Kamal
- Zaid Jamal
- Brian Robinson
- Gabriel Rosales
- Zachary Sotny

Our project focuses on optimizing the training model of the already developed NLP network, Grover, to increase its accuracy in recognizing examples of fake news in the hopes of preventing the widespread transmission of fallacious news content.

To approach this, we propose manipulating the coefficients of the connecting edges of the hidden layers to better calibrate the network for any commonalities between human written facts to machine written fake news. With our limited resources, we are hoping to test our model on generated articles from other AI models like ChatGPT and Rytr.

**Next Steps:**

We will utilize a web scraper to locate and collect a large number of articles from reputable sources. We will also generate an equal number of fake articles from various AI models and train the above CNN on the data. 

- In the *Web Scraper* folder in the *Article Dataset* folder, there is code for scraping the BBC website for articles. This can be modified for other news outlets and will be needed for a diverse dataset.
- The idea is to write all the necessary data to a csv that can be passed to the neural network for training.
