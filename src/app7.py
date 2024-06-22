# import streamlit as st
# import joblib
# import pandas as pd
# import re
# from sklearn.base import BaseEstimator, TransformerMixin
# from lime.lime_text import LimeTextExplainer
# import matplotlib.pyplot as plt

# # create the TextCleaner class
# class TextCleaner(BaseEstimator, TransformerMixin):
#     def __init__(self):
#         pass

#     def fit(self, X, y=None):
#         return self

#     def transform(self, X):
#         if isinstance(X, list):
#             return [self.clean_text(text) for text in X]
#         elif isinstance(X, pd.Series):
#             return X.apply(self.clean_text)
#         elif isinstance(X, str):
#             return self.clean_text(X)
#         else:
#             raise ValueError("Unsupported input!")

#     def clean_text(self, text):
#         text = text.lower()
#         text = re.sub(r'\d+', '', text)
#         text = re.sub(r'\b\d+\b', '', text)
#         text = re.sub(r'http\S+|www\S+', '', text)
#         text = re.sub(r'[^a-zA-Z\s]', '', text)
#         text = re.sub(r'\s+', ' ', text).strip()
#         return text

# # load the model using joblib
# model_path = 'model/calibrated_best_model.joblib'
# model = joblib.load(model_path)

# # create function to predict
# def predict(input_text):
#     cleaner = TextCleaner()
#     cleaned_text = cleaner.transform(input_text)
#     data = pd.Series([cleaned_text])
#     prediction = model.predict(data)
#     probability = model.predict_proba(data)
#     return prediction, probability

# # create function to generate LIME explanation
# def lime_explanation(text, seed=42):
#     explainer = LimeTextExplainer(class_names=['Not Spam', 'Spam'], random_state=seed)
#     exp = explainer.explain_instance(text, model.predict_proba, num_features=10)
#     return exp

# # build streamlit app
# def main():
#     # add title & description
#     st.title("Spam Detection Model")
#     st.write("This app predicts whether an SMS is spam or not.")
#     # request user input
#     text = st.text_area("Enter your message:")
#     # execute if "Predict" button is pressed
#     if st.button("Predict"):
#         prediction, probability = predict(text)
        
#         prob_spam = probability[0][1]
#         prob_not_spam = probability[0][0]
        
#         if prediction[0] == 1:
#             st.markdown(f"There is a {prob_spam * 100:.2f}% chance this message is <span style='color:red;font-weight:bold'>SPAM</span>.", 
#                         unsafe_allow_html=True)
#         else:
#             st.markdown(f"There is a {prob_not_spam * 100:.2f}% chance this message is <span style='color:green;font-weight:bold'>NOT SPAM</span>.", 
#                         unsafe_allow_html=True)
        
#         st.markdown("""
#             ##### Explanation on the Prediction
#             The following plot helps us understand why the model made its prediction. 
#             It does this by changing parts of the message and seeing how it affects the result. 
#             The plot below shows the important words that influenced the model's decision to classify the message. 

#             - <span style='color:red;font-weight:bold'>Red bars</span> mean the word makes it more likely to be spam.
#             - <span style='color:green;font-weight:bold'>Green bars</span> mean the word makes it less likely to be spam.
#             """, 
#             unsafe_allow_html=True)

        
#         # generate and display LIME explanation
#         exp = lime_explanation(text)
#         fig, ax = plt.subplots()
#         exp_list = exp.as_list()
#         feature_names, scores = zip(*exp_list)
#         colors = ['green' if score < 0 else 'red' for score in scores]
#         bars = ax.barh(range(len(scores)), scores, align='center', color=colors)
#         ax.set_yticks(range(len(scores)))
#         ax.set_yticklabels(feature_names)
#         ax.invert_yaxis()  
#         ax.set_xlabel('Score')
#         ax.set_title('Word Influence Score')

#         st.pyplot(fig)

# if __name__ == "__main__":
#     main()

import streamlit as st
import joblib
import pandas as pd
import re
from sklearn.base import BaseEstimator, TransformerMixin
from lime.lime_text import LimeTextExplainer
import matplotlib.pyplot as plt

# set page title
st.set_page_config(page_title='SMS Spam Detection')

# create TextCleaner class (copy-pasting from report.ipynb)
class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if isinstance(X, list):
            return [self.clean_text(text) for text in X]
        elif isinstance(X, pd.Series):
            return X.apply(self.clean_text)
        elif isinstance(X, str):
            return self.clean_text(X)
        else:
            raise ValueError("Unsupported input!")

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'\b\d+\b', '', text)
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

# load model
model_path = 'model/calibrated_best_model.joblib'
model = joblib.load(model_path)

# create function to predict
def predict(input_text):
    cleaner = TextCleaner()
    cleaned_text = cleaner.transform(input_text)  
    data = pd.Series([cleaned_text])
    prediction = model.predict(data)
    probability = model.predict_proba(data)
    return prediction, probability, cleaned_text

# create function to generate explanation
def lime_explanation(text, seed=42):
    explainer = LimeTextExplainer(class_names=['Not Spam', 'Spam'], random_state=seed)
    exp = explainer.explain_instance(text, model.predict_proba, num_features=10)
    return exp

# build app
def main():
    st.markdown("<h1 style='text-align: left; color: black;'>Spam Detection Model</h1>", 
                unsafe_allow_html=True)
    st.write("This app predicts whether an SMS is spam or not.")

    text = st.text_area("Enter your message here:")

    if st.button("Predict"):
        if not text:
            st.error("Please enter a message.")
        else:
            prediction, probability, cleaned_text = predict(text)
            
            prob_spam = probability[0][1]
            prob_not_spam = probability[0][0]
            
            if prediction[0] == 1:
                st.markdown(f"There is a {prob_spam * 100:.2f}% chance this message is <span style='color:red;font-weight:bold'>SPAM</span>.", 
                            unsafe_allow_html=True)
            else:
                st.markdown(f"There is a {prob_not_spam * 100:.2f}% chance this message is <span style='color:green;font-weight:bold'>NOT SPAM</span>.", 
                            unsafe_allow_html=True)

            # separate sections
            st.markdown("---")
            st.markdown("#### Explanation on the Prediction")
            st.markdown("""
                The following plot helps us understand why the model made its prediction. 
                It does this by changing parts of the message and seeing how it affects the result. 
                The plot below shows the important words that influenced the model's decision to classify the message. 

                - <span style='color:red;font-weight:bold'>Red bar</span> means the word makes it more likely to be spam.
                - <span style='color:green;font-weight:bold'>Green bar</span> means the word makes it less likely to be spam.
                """, 
                unsafe_allow_html=True)

            # generate and display explanation
            exp = lime_explanation(cleaned_text)
            fig, ax = plt.subplots()
            exp_list = exp.as_list()
            feature_names, scores = zip(*exp_list)
            colors = ['green' if score < 0 else 'red' for score in scores]
            bars = ax.barh(range(len(scores)), scores, align='center', color=colors)
            ax.set_yticks(range(len(scores)))
            ax.set_yticklabels(feature_names)
            ax.invert_yaxis()  
            ax.set_xlabel('Score')
            ax.set_title('Word Influence Score')

            st.pyplot(fig)

    st.markdown("<h7 style='text-align: center; color: grey;'>Developed by LingAdeu</h7>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()