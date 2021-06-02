# PDCT-backend
Backend of the PDCT Melanoma project
The backend holds the model and expose an API route to predict if the sent image is a malignant melanoma or a benin one.

If the result is equal to `"0"` the mole is classified as a benin melanoma.

If the result is equal to `"1"` the mole is classified as a malignant melanoma.

# Disclaimer
We are not responsible of the given result and you may in any case see a doctor if you have any doubt about any of your moles.

# API
## How to run the API

```sh
cd API
docker build -t api .
docker run -p '10000:10000' api
```

## Test API on Postman

<img src="./readme-img/postman-request.png" />

# Training of models
The training of the models is first done though "Classification melanoma (from scratch).ipynb" which traines models from scratch. Random search is used to test different hyperparameter settings.
The second step of training is training a model through "Classification melanoma (transfer learning fine tuning).ipynb". Here transfer learning and fine tuning is used together with different hyperparameter settings for the classification layer (random search is used). Two models in the base model is here tested, VGG16 and InceptionV3, where the latter is favoured based on evaluation metrics.

# Evaluation of models
To evaluate the models created, the result from each training is written to a local database. Another script is used to generate graphs ("trainingResults/Show training graphs.ipynb"), that is stored in the same folder as .png-files.
In the training notebooks there are also code showing evaluation metrics as accuracy on held-out testset, confusion matrix etc.

# Contibutors

- SPANIER Nathan
- RIVET Baptiste
- PETTERSSON Kristoffer
