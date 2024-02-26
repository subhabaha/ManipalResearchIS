import requests
import streamlit as st



#API Key
api_key ='WaOd3n1r.JxLL0NgzS4McGj5xJ1PiumWoURsBP6cH'

headers = {
    'Content-Type': 'application/json',
    'Apikey': f'Api-Key {api_key}',
}

data = {
    "payload": notes
}

url = 'https://payload.vextapp.com/hook/T1NLTAMZVR/catch/$(manipal)'


def main():
    st.title("Manipal Research Information System")
    notes = st.text_area("Write down the query you want to ask:")
    if st.button("Generate Response"):
        with st.spinner("Generating Response ..."):
            response = requests.post(url, json = data, headers = headers)
        description = response
        st.subheader("Generated Response")
        st.write(description)


if __name__ == '__main__':
   main()
