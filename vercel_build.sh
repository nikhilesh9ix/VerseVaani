#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
