import streamlit as st


# Page Configuration
st.set_page_config(page_title="baag.ai", page_icon=":rocket:", layout="wide")

# Header
st.title("Welcome to baag.ai!")
st.subheader("Revolutionizing RFP Processes for Businesses")

# Introduction
st.markdown(
    """
    **baag.ai** is designed to simplify and streamline the process of filling out Requests for Proposals (RFPs). 
    Our tool uses AI to reduce the friction and pain points typically associated with RFPs, helping companies save time and resources.
"""
)

# Features
st.header("Features")
st.markdown(
    """
- **AI-Powered Assistance**: Leverage advanced AI to quickly fill out RFPs.
- **Template Library**: Access a wide range of customizable RFP templates.
- **Collaboration Tools**: Collaborate seamlessly with your team.
- **Analytics and Insights**: Gain insights to improve your RFP responses.
"""
)

# Testimonials (if available)
st.header("What Our Users Say")
st.info("User testimonials and feedback can be showcased here.")

# Call to Action
st.header("Get Started with baag.ai")
st.markdown(
    """
Interested in transforming your RFP process? 
[Sign up now](#) for early access or [contact us](#) for more information.
"""
)

# Footer
st.markdown("---")
st.markdown("© 2023 baag.ai | A Tool for Streamlining RFP Processes")
