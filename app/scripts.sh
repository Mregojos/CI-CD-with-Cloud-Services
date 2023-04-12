# To build and run stremlit 
docker build -t streamlit-app .
docker run --name streamlit-app -d -p 8501:80 -v $(pwd):/app streamlit-app

# docker ps
# docker rm -f streamlit-app
