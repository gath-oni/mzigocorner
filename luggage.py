import streamlit as st

st.title("Welcome to Mzigo Corner")

from PIL import Image
img = Image.open("Stow.jpg")
st.image(img,250)

st.text("Welcome to Mzigo Corner where your luggage is our concern.")

st.text("Dear Customer please select your Service")

service = st.radio("Select:",('Drop-off', 'Pick-up'))
if (service == 'Drop-off'):
    st.success("Drop-off")
    
if (service == 'Pick-up'):
    st.success("Pick-up")

if (service == 'Drop-off'):
    name = st.text_input("Enter your name:")
    bag = st.multiselect("Select your type of bags:",
                  ('Suitcase', 'Backpack', 'Duffel bag','Travel bag'))
    st.text("Please proceed to the counter for locker assignment, key and card collection.\nDrop off your luggage at the assigned locker.")
    
    
    selection = st.radio("Have you dropped off your luggage?",('Yes','No'))
    if (selection == 'Yes'):
        st.success("Luggage successfully dropped off")
        dt1=st.time_input("Enter your drop-off time:")
        if (st.button('Submit')):
            st.write("%s, your %s was dropped off at %s." % (name,bag,dt1))
            st.text("Thank you for trusting us with your luggage.")
    else:
        st.error("Try Again!")
        
if (service == 'Pick-up'):
    st.text("Proceed to the counter and produce your card.")
    
    dt2 = st.time_input("Enter your Pick-up time:")
    
    hours = st.number_input("Enter the number of hours your luggage has been in storage:")
    if (hours <= 1):
        payment = 50
        st.text("Your payment is %d" % payment)
        
    else:
        rate = 1.5 * 50
        extra_hours = hours - 1
        payment = 50 + rate + extra_hours
        st.text("Your payment is %d" % payment)
        
    mode_payment = st.selectbox("Kindly select a payment method: ",
                     ['Bank Transfer', 'M-Pesa'])
    if (mode_payment == 'Bank Transfer'):
        st.text("Kindly make a transfer to 12345678, KCB Bank")
    else:
        st.text("Kindly make a transfer to paybill number 368456, Mzigo Corner account")

    payment_status = st.radio ("Have you made the payment", ('Yes', 'No' )) 
    if (payment_status == 'Yes'):
        st.success("Payment made. Your luggage will be released ASAP") 
        st.text ("Please proceed to your assigned locker and collect your luggage")
        
        level = st.select_slider('How would you rate our services?', ['Bad', 'Fair', 'Very Satisfied'])
 
        st.text('Selected: {}'.format(level))

        if (level == 'Bad'):
            Feedback = st.text_input("Kindly tell us what you did not like:", "Type Here ...")
                                     
    else:
        st.error("Your luggage cannot be released until payment is made")  
        st.text("Please make a payment for your luggage to be released")
                                     
    st.text("Thank you for choosing Mzigo Corner, your satisfaction is our priority!")
    
    
    
    
hide_menu_style = """
             <style>
             #MainMenu{visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             """
st.markdown(hide_menu_style, unsafe_allow_html=True)
    
        
    
    
    
