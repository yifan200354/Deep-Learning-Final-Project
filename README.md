# Deep-Learning-Final-Project

The repository consists of pre-processing code and data, as well as two colab notebooks with all codes and results (one is our implementation, one is original implementation). 

The folder image-caption data contains four files. We referred to HW5 when preprocessing our data to generate captions for input images. Our codes for data preprocessing and caption generation are in the file HW5.ipynb (modified from hw5, used for pre-processing), and preprocessing.py. The file classes.txt consists of the 58 classes for our image dataset. The file captions.txt consists of the filenames of all images along with their corresponding classes.

Our image dataset was too large to be uploaded to Github, so we uploaded the image dataset folder on Google Drive (linked below).
https://drive.google.com/drive/folders/19Cda5cHoQWQm0j4wnPiej4NzI_RdJiFO?usp=sharing

To run the notebooks, we need to upload both image dataset (the folder from Google Drive) and caption data ("image-caption data/captions.txt"), and then put the datasets and the notebooks in the same folder (mine is called CSCI 1470 Final Project) as the colab notebooks. When using Google Colab to run our notebook: final_results_5_12.ipynb, users can edit their own filepath to the above folder in the third code block, where image_path and caption_file are defined. To see the results, users could run everything and see the loss reports in the main function as well as the generated images. Users can also compare the results to the ones generated from the notebook: "original_implementation_+_our_dataset.ipynb", which contains the results from using the original model on our dataset.
