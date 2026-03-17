import streamlit as st
from datetime import date
import time

if "form_data" not in st.session_state:
    st.session_state["form_data"]=False
if "alive" not in st.session_state:
    st.session_state["alive"]=0

st.title("Would You Survive ?")

def titanic_boading_form():
    def check_form():
        if first_name and last_name:
            return True
        else:
            st.error(f"unfilled input **'Fist name'** or **'last name'**")
            return False
    with st.form("details"):
        col = st.columns(2)
        first_name = col[0].text_input("Name",placeholder="First Name")
        last_name = col[1].text_input("",placeholder="Last Name")

        dob = col[0].date_input("DOB",value="2020-01-01",max_value="today",min_value="1990-01-01")
        gender = col[1].radio("Gender",options=["male","female"],horizontal=True)

        fare = col[0].number_input("fare",min_value=10.20,max_value=512.66)
        sibling = col[1].number_input("any sibling",min_value=0,max_value=10,step=1)
        
        embark_town=col[0].selectbox("embark_town",options=['Southampton', 'Cherbourg', 'Queenstown'])
        parents = col[1].number_input("any parents",min_value=0,max_value=10,step=1)
        form_data = st.form_submit_button("Board The titanic")
    
    if form_data and check_form():
        today=date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        st.success(dob)
        st.success(age)

        st.session_state["form_data"]={
            "first_name":first_name,
            "last_name":last_name,
            "age":age,
            "gender":gender,
            "fare":fare,
            "sibling":sibling,
            "embark_town":embark_town,
            "parents":parents
        }
        st.rerun()


def prediction_models():
    import skops.io as sio
    import pandas as pd
    def update_form_data():
        st.session_state["form_data"]=False
        st.session_state["alive"]=0
    def display_result(result,column):
        if result==1:
            column.success("You are save!")
            st.session_state["alive"]+=1
        else:
            column.error("You are dead!")
    def making_prediction_data():
        encoder = sio.load("encoder_transformer.skops")
        if st.session_state["form_data"]["fare"]<167:
            pclass=3
            word_class="Third"
        elif 334>st.session_state["form_data"]["fare"]>167:
            pclass=2
            word_class="First"
        else:
            pclass=1
            word_class="Second"
        predict_data =pd.DataFrame({
            "pclass":pclass,
            "sex":st.session_state["form_data"]["gender"],
            "age":st.session_state["form_data"]["age"],
            "sibsp":st.session_state["form_data"]["sibling"],
            "parch":st.session_state["form_data"]["parents"],
            "fare":st.session_state["form_data"]["fare"],
            "embarked":st.session_state["form_data"]["embark_town"][0],
            "class":word_class,
            "embark_town":st.session_state["form_data"]["embark_town"]
        },index=[0])
        predict_data = encoder.transform(predict_data)
        return predict_data

    col = st.columns(3,border=True,gap="xxsmall",vertical_alignment="bottom")
    def display_model():
        col[0].subheader("Naive Bayes",text_alignment="center")
        col[0].image("Mails-Filter-768x719.png")
        col[1].subheader("SVM model",text_alignment="center")
        col[1].image("SVG.jpg")
        col[2].subheader("Random Forest",text_alignment="center")
        col[2].image("RFC.jpg")


    @st.fragment
    def NB_column():

        nb_progress = col[0].progress(20,"processing...")
        time.sleep(1)
        Naive_bayes = sio.load("naive_bayes-82.skops")

        nb_progress.progress(40,"processing...")
        time.sleep(1)

        ans = Naive_bayes.predict(making_prediction_data())

        nb_progress.progress(100,"processing...")
        time.sleep(1)
        display_result(ans[0],col[0])

    @st.fragment
    def SVM_column():

        nb_progress = col[1].progress(20,"processing...")
        time.sleep(1)
        SVM = sio.load("SVM-87.skops")

        nb_progress.progress(40,"processing...")
        time.sleep(1)

        ans1 = SVM.predict(making_prediction_data())

        nb_progress.progress(100,"processing...")
        time.sleep(1)
        display_result(ans1[0],col[1])
    
    @st.fragment
    def rfc_column():

        nb_progress = col[2].progress(20,"processing...")
        time.sleep(1)
        rfc = sio.load("Rfc_model_compress.skops")

        nb_progress.progress(40,"processing...")
        time.sleep(1)

        ans2 = rfc.predict(making_prediction_data())

        nb_progress.progress(100,"processing...")
        time.sleep(1)
        display_result(ans2[0],col[2])

    display_model()
    NB_column()
    SVM_column()
    rfc_column()
    if st.session_state["alive"]>=2:
        st.success(f"Consequently, based on the majority agreement, the passenger {st.session_state["form_data"]["first_name"]} {st.session_state["form_data"]["last_name"]} is classified as 'Alive'.")
    else:
        st.error(f"Consequently, based on the majority agreement, the passenger {st.session_state["form_data"]["first_name"]} {st.session_state["form_data"]["last_name"]} is classified as 'Dead'.")
    st.caption("The final prediction was determined using a Majority Voting Ensemble approach, leveraging the consensus of three independent models—Random Forest, SVG, and Naive Bayes to improve classification robustness.")
    st.button("Retry",on_click=update_form_data())


if not st.session_state["form_data"]:
    titanic_boading_form()
else:
    prediction_models()