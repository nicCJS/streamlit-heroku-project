import streamlit as st
from PIL import Image

# hidden div with anchor
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)   

im = Image.open("MMU_logo.png")
st.image(im, width=500)

st.title("TDS 3301 - Data Mining")
st.header("PROJECT: QUESTION 1")
st.subheader("Profiling Customers in a Self-Service Coin Laundry Shop")

st.markdown("**Group Members:**")
st.markdown("- Nicholas Chee Jian Shen 1171103441")
st.markdown("- Chan Jun Ting 1171103572")
st.markdown("- Tee Wai Bing 1171103537")

st.markdown("""---""")

chapter = st.selectbox('Jump to a chapter:', 
('Show All Chapters',
'Chapter 1: Exploratory Data Analysis and Data Pre-Processing', 
'Chapter 2: Feature Selection', 
'Chapter 3: Appropriate Machine Learning Techniques Used',
'Chapter 4: Deployment'))

if chapter == "Show All Chapters":
    st.subheader("Chapter 1: Exploratory Data Analysis and Data Pre-Processing")
    q1_1 = Image.open("0.png")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The data that we used has no outliers and is approximately symmetrically distributed.")
    st.write("- No significant strong correlations are found.")
    st.write("- The combination of the washer no.3 and dryer no.7 is most frequently used by the customers, with a total of 90 times.")
    st.write("- A linear decrease in the number of customers as their age decreases.")
    q1_2 = Image.open("1.png")
    q1_3 = Image.open("2.png")
    q1_4 = Image.open("3.png")
    q1_5 = Image.open("4.png")
    q1_6 = Image.open("5.png")
    st.image(q1_1, caption="Boxplot of Age_Range")
    st.image(q1_2, caption="Correlation between the attributes in the dataset")
    st.image(q1_3, caption="Bar chart of washer frequency")
    st.image(q1_4, caption="Bar chart of dryer frequency")
    st.image(q1_5, caption="Bar chart of washer and dryer combination")
    st.image(q1_6, caption="Bar chart of age range")
    st.markdown("""---""")

    st.subheader("Chapter 2: Feature Selection")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The top 5 features obtained are the same, with them being Washer_No, Time, Pants_Colour, Age_Range and Shirt_Colour.")
    st.write("- Washer_No, Time and Pants_Colour are the features we will be using in the upcoming models.")
    q2_1 = Image.open("6.png")
    q2_2 = Image.open("7.png")
    st.image(q2_1, caption="Boruta Feature Selection")
    st.image(q2_2, caption="RFE Feature Selection")
    st.markdown("""---""")

    st.subheader("Chapter 3: Appropriate Machine Learning Techniques Used")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The Decision Tree Classifier is good in classifying the customer’s gender based on the washer’s number, customer’s pants colour and time of service.")
    st.write("- The Random Forest Regression is good in classifying the customer gender based on the washer’s number, customer’s pants colour and time of service.")
    st.write("- A thing to note is even though the variance score and the R2 score of the Random Forest Regression is the highest among the models, it is still low comparatively to real world values.")
    st.write("- Only one rule is shown, which is between washer no.3 and dryer no.7.")
    st.write("- The support value of 0.112, the confidence value of 0.3947 and the lift of 1.3672 represents a strong association between washer no.3 and dryer no.7.")
    st.write("- This goes along with the high frequency of their combined use which means that customers tend to use these two machines together in particular.")
    st.write("- The clustering number is 5 based on the elbow method.")
    st.write("- The customers who wear black, blue_jeans, yellow, white, brown and grey pants mostly appear in the morning or during night hours.")
    st.write("- The customers who wear orange, blue, green, red, purple, pink pants mostly appear in the morning and in the afternoon.")
    st.write("- The customers with ages between 45 to 55 appear early in the morning.")
    st.write("- The customers with ages between 30 to 40 appear at night.")
    st.write("- The customers who wear blue, white, red, black, brown and yellow shirts will mostly appear during the afternoon hour.")
    st.write("- The customers who wear grey, orange, green, purple and pink shirts will mostly appear in the morning and during night hours.")
    q3_1 = Image.open("8.png")
    q3_2 = Image.open("9.png")
    q3_3 = Image.open("10.png")
    q3_4 = Image.open("11.png")
    st.image(q3_1, caption="Confusion Matrix for classifiers")
    st.image(q3_2, caption="ROC Curve for classifiers")
    st.image(q3_3, caption="Comparison of the predicted data and test set of the 4 models")
    st.image(q3_4, caption="Original Data Clustering")
    st.markdown("""---""")

    st.subheader("Chapter 4: Deployment")
    st.success("**From this chapter, we gathered that:**")
    st.write("- This very website is from the Python streamlit package deployed to Heroku for hosting!")
    # add the link at the bottom of each page
    st.markdown("<center><a href='#linkto_top'>Back to top</a></center>", unsafe_allow_html=True)

if chapter == "Chapter 1: Exploratory Data Analysis and Data Pre-Processing":
    st.subheader("Chapter 1: Exploratory Data Analysis and Data Pre-Processing")
    q1_1 = Image.open("0.png")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The data that we used has no outliers and is approximately symmetrically distributed.")
    st.write("- No significant strong correlations are found.")
    st.write("- The combination of the washer no.3 and dryer no.7 is most frequently used by the customers, with a total of 90 times.")
    st.write("- A linear decrease in the number of customers as their age decreases.")
    q1_2 = Image.open("1.png")
    q1_3 = Image.open("2.png")
    q1_4 = Image.open("3.png")
    q1_5 = Image.open("4.png")
    q1_6 = Image.open("5.png")
    st.image(q1_1, caption="Boxplot of Age_Range")
    st.image(q1_2, caption="Correlation between the attributes in the dataset")
    st.image(q1_3, caption="Bar chart of washer frequency")
    st.image(q1_4, caption="Bar chart of dryer frequency")
    st.image(q1_5, caption="Bar chart of washer and dryer combination")
    st.image(q1_6, caption="Bar chart of age range")
    st.markdown("""---""")
    # add the link at the bottom of each page
    st.markdown("<center><a href='#linkto_top'>Back to top</a></center>", unsafe_allow_html=True)

if chapter == "Chapter 2: Feature Selection":
    st.subheader("Chapter 2: Feature Selection")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The top 5 features obtained are the same, with them being Washer_No, Time, Pants_Colour, Age_Range and Shirt_Colour.")
    st.write("- Washer_No, Time and Pants_Colour are the features we will be using in the upcoming models.")
    q2_1 = Image.open("6.png")
    q2_2 = Image.open("7.png")
    st.image(q2_1, caption="Boruta Feature Selection")
    st.image(q2_2, caption="RFE Feature Selection")
    st.markdown("""---""")
    # add the link at the bottom of each page
    st.markdown("<center><a href='#linkto_top'>Back to top</a></center>", unsafe_allow_html=True)

if chapter == "Chapter 3: Appropriate Machine Learning Techniques Used":
    st.subheader("Chapter 3: Appropriate Machine Learning Techniques Used")
    st.success("**From this chapter, we gathered that:**")
    st.write("- The Decision Tree Classifier is good in classifying the customer’s gender based on the washer’s number, customer’s pants colour and time of service.")
    st.write("- The Random Forest Regression is good in classifying the customer gender based on the washer’s number, customer’s pants colour and time of service.")
    st.write("- A thing to note is even though the variance score and the R2 score of the Random Forest Regression is the highest among the models, it is still low comparatively to real world values.")
    st.write("- Only one rule is shown, which is between washer no.3 and dryer no.7.")
    st.write("- The support value of 0.112, the confidence value of 0.3947 and the lift of 1.3672 represents a strong association between washer no.3 and dryer no.7.")
    st.write("- This goes along with the high frequency of their combined use which means that customers tend to use these two machines together in particular.")
    st.write("- The clustering number is 5 based on the elbow method.")
    st.write("- The customers who wear black, blue_jeans, yellow, white, brown and grey pants mostly appear in the morning or during night hours.")
    st.write("- The customers who wear orange, blue, green, red, purple, pink pants mostly appear in the morning and in the afternoon.")
    st.write("- The customers with ages between 45 to 55 appear early in the morning.")
    st.write("- The customers with ages between 30 to 40 appear at night.")
    st.write("- The customers who wear blue, white, red, black, brown and yellow shirts will mostly appear during the afternoon hour.")
    st.write("- The customers who wear grey, orange, green, purple and pink shirts will mostly appear in the morning and during night hours.")
    q3_1 = Image.open("8.png")
    q3_2 = Image.open("9.png")
    q3_3 = Image.open("10.png")
    q3_4 = Image.open("11.png")
    st.image(q3_1, caption="Confusion Matrix for classifiers")
    st.image(q3_2, caption="ROC Curve for classifiers")
    st.image(q3_3, caption="Comparison of the predicted data and test set of the 4 models")
    st.image(q3_4, caption="Original Data Clustering")
    st.markdown("""---""")
    # add the link at the bottom of each page
    st.markdown("<center><a href='#linkto_top'>Back to top</a></center>", unsafe_allow_html=True)

if chapter == "Chapter 4: Deployment":
    st.subheader("Chapter 4: Deployment")
    st.success("**From this chapter, we gathered that:**")
    st.write("- This very website is from the Python streamlit package deployed to Heroku for hosting!")
    # add the link at the bottom of each page
    st.markdown("<center><a href='#linkto_top'>Back to top</a></center>", unsafe_allow_html=True)



