The code for example apps is found here: https://github.com/plotly/dash-sample-apps

In order to run the apps in each folder, you will need to go to a specific example and install the dependencies in requirements.txt.  For example,

```
    pip install -r requirements.txt

    or

    conda install -n plotly-dashboard requirements.txt
```

However, if you want to create a conda environment that can run an interesting example of our choosing, you can do the following:

1. Create conda environment using environment.yml file.
   
    ```
    conda env create -f environment.yml
    conda activate plotly-dashboard

    ```

2.  Run the app. 
   
   ```
   python run dash-opioid-epidemic/app.py

   ```

## Run apps on CDS Dashboards

To deploy on Nebari with CDS Dashboards: 

1. Choose the nebari-git-dashboard environment 
2. Point to  "dashboard_examples/plotly-dash/dash-sample-apps/apps/dash-opioid-epidemic/app.py" in your jupyter tree. 
3. Choose "plotlydash" as your framework.