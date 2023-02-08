# 🔭 Example app image comparison

This code is found here: https://github.com/fcakyon/streamlit-image-comparison

It is added as a submodule to this repo.  The easiest way to run it is to do the following.

1. Initiate the submodule:
    ```
    git submodule init
    git submodule update
    ```

2. Create conda environment. 
   
    ```
    conda env create -f environment.yml
    conda activate streamlit-dashboard

    ```

3. Run the app.
   ```
   cd example-app-image-comparison
   streamlit run streamlit_app.py

   ```

## Deploy app on CDS Dashboards

To deploy on Nebari with CDS Dashboards:

1. Choose nebari-git-dashboard environment.
2. Point to  "dashboard_examples/streamlit/streamlit-image-comparison/app.py" in your jupyter tree.
3. Choose "streamlit" as your framework.