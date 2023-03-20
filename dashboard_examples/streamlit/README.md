# Streamlit example app

The following example can be deployed via CDS dashboards on Nebari using the default dashboard environment that ships with Nebari.  

Make sure to do the following when you are setting up your dashboard:

1. Choose the nebari-git-dashboard environment. 
   
2. Point to  "dashboard_examples/streamlit/streamlit-image-comparison/app.py" in your jupyter tree. 
   
3. Choose "streamlit" as your framework.

Note:  If you do not see anything in the folder above, see the note below about initializing the submodule.

Alternatively, you can run the app by installing the environment outlined in the environment.yml file by following these few steps:


1. Create conda environment using environment.yml file.
   
    ```
    conda env create -f environment.yml
    conda activate streamlit-dashboard

    ```

2.  Run the app. 
   
   ```
   cd example-app-image-comparison
   streamlit run streamlit_app.py

   ```


Note: The code for this example app is found here: https://github.com/Quansight/streamlit-image-comparison.git.   It is set up as a submodule in the nebari-demo repo.  If you are not seeing anything listed in `dashboard_examples/streamlit/streamlit-image-comparison` you will need to run the following commands:

```
git submodule init
git submodule update

```

Every once in awhile, the submodules may be updated.  You will need to run the following command:

```
git submodule update --remote

```




