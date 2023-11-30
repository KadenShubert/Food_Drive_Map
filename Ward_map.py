import streamlit as st

def main():
    st.title('Interactive map of location information from Food Drive Data')
    st.write('Food Drive LDS Stake + Ward Map:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1xych3q6SLdy5f2WdPC0GIQrU-hA9wk8&ehbc=2E312F&noprof=1" width="640" height="480"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

