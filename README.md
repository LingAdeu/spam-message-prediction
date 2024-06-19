![header here](header.png)

# Development and Evaluation of a Classification Model for Spam Detection

## Summary
This project attempts to build a classification model to predict spam messages (`1` for spam and `0` for ham/legitimate message) in a telecommunication company. Due to minimizing both false positives (type I errors) and false negatives (type II errors), F1 was chosen as the primary evaluation metric. Based on the results, the best model, namely logistic regression, achieved a high F1 score of 0.92 $\pm$ 0.01 across 10 folds. Furthermore, as the model can save financial cost of \$23K based on a simulation, the model can be used to minimize the impacts of spams on the users.

## Getting Started
To replicate my analysis or explore the data further, kindly follow the following steps:
1. Clone this repository to your local machine.
```bash
https://github.com/LingAdeu/spam-message-prediction.git
```
2. Ensure that all necessary dependencies are installed, especially Python and Jupyter Notebook. All libraries are specified on file requirements.txt.
3. Run my Jupyter Notebook file (`*.ipynb`) in [notebook](https://github.com/LingAdeu/spam-message-prediction/blob/main/report.ipynb) folder to reproduce the analysis. This notebook contains the detailed implementation of data preprocessing, model training, and evaluation. Alternatively, kindly check this Jupyter Notebook Viewer [URL](https://nbviewer.org/github/LingAdeu/spam-message-prediction/blob/main/report.ipynb) to see the notebook.

## Folder Organization
```
  .
  ├── README.md                           <- The top-level README for using this project
  ├── data
  │   └── spam.csv                        <- Dataset
  ├── header.png
  ├── model
  │   └── calibrated_best_model.joblib    <- Best model (calibrated logistic regression)
  ├── report.ipynb                        <- Jupyter Notebook file
  ├── requirements.txt                    <- The requirements file for reproducing the environment
  └── src
      └── app7.py                         <- Streamlit app for for model testing
```

## Feedback
If there are any questions or suggestions for improvements, feel free to contact me here:

<a href="https://www.linkedin.com/in/adelia-januarto/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"/>
  </a>
<a href="mailto:januartoadelia@gmail.com" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/gmail/default.svg"  width="52" height="40" alt="gmail logo"/>
  </a>
