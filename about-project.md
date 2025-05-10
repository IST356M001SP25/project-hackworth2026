# About My Project

Student Name:  Hiram Hackworth
Student Email:  ahhackwo@syr.edu 

### What it does

My project creates a data pipeline that extracts, transforms, and analyzes superhero data from the Marvel and DC universes. It uses Python scripts to fetch and clean data, and then loads it into a Streamlit dashboard for interactive visual exploration. Users can filter by publisher, view charts of character stats, compare heroes, and see demographic breakdowns like gender distribution. The dashboard also highlights top heroes by individual power attributes such as strength, intelligence, and speed. I did want to add in some superhero imagery to make the visualiaztion more fashionable, but that task proved to be a bit out of my depth. In its stead I ensured that atleast a color scheme is assiocated to the seperate comic enities. 

### How you run my project

1. Clone the GitHub repository and install the required libraries using "pip install -r requirements.txt."

**IMPORTANT INFORMATION**
2. To ensure the full function of the data pipeline:
    2a. First, you must run the python in "code/extract.py", there you'll fetch the raw data.
    2b. Next, you will need to run the python in "code/transform.py", here you'll be able to clean and structure the data.
    3b. Then, by running the python in "code/load.py", this will load the clean data into the final file; "code/app.py". 

3. Launch the Streamlit dashboard with: "streamlit run code/app.py" or depending on your previous preperations you can use the "streamlit" run button on your tab when accesing the file "code/app.py".

4. Once your arrived in the streamlit app, you will now be able to use the sidebar to filter by publisher and explore the visual analytics provided.

### Other things you need to know

- The project is modular: each stage of the pipeline is in a separate Python script to ensure clean code organization.

- Logos for Marvel and DC should be placed in the cache/ folder as marvel_logo.png and dc_logo.png to display them in the UI.

- Test files are included in the tests/ folder to verify key functions for extraction, transformation, and data loading.

- The data source is a public superhero API: https://akabab.github.io/superhero-api.

- You can extend the project by integrating location data, adding maps, or comparing other stats like alignment or race.