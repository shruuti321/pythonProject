
import streamlit as st
from streamlit_chat import message
from bardapi import Bard


token='YAgcDLrT6r3ty7h4Xa2ne2FbRKYAZvaBKS4eYmww_hJITUcLkxbnitBOGdxH-Oeb5uY_Uw.'

#url='https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1213&q=80'
#data-testid="stAppViewContainer"
changes='''
<style>
[data-testid="stAppViewContainer"]
{
background-image:url('https://images.unsplash.com/photo-1479267658415-ff274a213280?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80');

background-size:cover;
.st-bx {
    background-color: rgba(255, 255, 255, 0.05);
    }
    
    /* .css-1hynsf2 .esravye2 */
    
    html {
    background: transparent;
    }
    div.esravye2 > iframe {
        background-color: transparent;
    }
}
</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

def get_text():
    input_text=st.text_input("CN Bot:","Hey bot!",key='input')
    return input_text
st.title('Personal Tutoring Bot!')

user_input=get_text()
if user_input:
    output=generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
         message(st.session_state['generated'][i],key=str(i))

         message(st.session_state['past'][i],key="user_"+str(i),is_user=True)
