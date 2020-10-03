# BAKOD AI

BAKOD AI is a proof of concept machine learning project aimed towards creating an automated monitoring process of forests using 30-250 meter altitude satellite imagery from NASA and the United States Geological Survey Agency's Landsat. 

## What is BAKOD AI?

BAKOD AI was named after the Filipino word "*Bakod*," which roughly translates to the fence. However, in *Illongo*, the term is often used to distinguish one owner's land from another. This concept was adopted by the BAKOD AI team to create a project to monitor the land areas of forests, which has a significant role to play as a solution towards reducing massive emissions.

According to the United Nations Environment Programme (UNEP), it is impossible to limit the average global temperature increase to 1.5°C without forests reducing much of our society's emissions. Forests are also important ecosystems for the different animals on earth. Hence, the need to monitor our forest has been the primary focus of our project.

In monitoring forests through machine learning, the general public can monitor how much forests are being reduced or grown in their areas. It also allows potential areas of monitoring whereby satellite imagery can be monitored to identify which geolocations do deforestation occur more rapidly. Identifying these critical areas enables authorities to identify areas that can cause deforestation.

Doing this project allows the potential to create more robust models in identifying deforestation through satellite imagery and machine learning image processing. In doing so, the project can serve as a plug-and-play solution towards monitoring deforestation in any area worldwide.

Deforestation Activities that can be detected by our proof of concept are:

- Forest Combustion
- Agriculture
- Mining
- Weather (Hazy, Cloudy, Foggy, etc.)
- Logging
- Slash & Burn
*However, the model is yet to be trained towards identifying anthropogenic and non-anthropogenic causes of Deforestation.

## Development of BAKOD AI

Our team created this project based on how environmentalists protect wildlife in the Philippines, specifically our forests. Protecting the forests of our country is a life-threatening duty to most environmentalists. Some even lose their lives as they watch over these forests through physical monitoring of these landscapes. Our team knew that there has to be a safer way to protect our forests. Thus, we realized BAKOD AI as a safer alternative monitoring system for people in preserving the forests.

We believed that forests could be easily monitored by satellites as they are always under their field of vision. On top of that, an image classification machine learning model is integrated to identify a forest area's health. The team used a pre-trained PyTorch model named Resnet (specifically Resent18) and fed multiple satellite images of the Amazon rainforest to train the model to identify the Amazon rainforest landscape and look for deforestation activities.

The model was deployed using Django, a Python-based web framework, to give the team and future developers the ability to customize the whole web app into the needed parts for their specific needs. Django has allowed our team to separate each functionality into clearly defined apps that would enable people to make modular versions of our final product.