# Plotly-Dash example app

The following example can be deployed via CDS dashboards on Nebari using the default dashboard environment that ships with Nebari.  

Make sure to do the following when you are setting up your dashboard:

1. Choose the nebari-git-dashboard environment. 
2. Point to  "dashboard_examples/plotly-dash/dash-sample-apps/apps/dash-opioid-epidemic/app.py" in your jupyter tree. 
3. Choose "plotlydash" as your framework.

Note:  If you do not see anything in the folder above, see the note below about initializing the submodule.

Alternatively, you can run the app by installing the environment outlined in the environment.yml file by following these few steps:


1. Create conda environment using environment.yml file.
   
    ```
    conda env create -f environment.yml
    conda activate plotly-dashboard

    ```

2.  Run the app. 
   
   ```
   python run dash-opioid-epidemic/app.py

   ```


In order to run the apps in any other folder, you will need to go to a specific example and install the dependencies in requirements.txt.  For example,

```
    pip install -r requirements.txt

    or

    conda install -n plotly-dashboard requirements.txt

    python run <name of app>/app.py
```


Note: The code for this example app is found here: https://github.com/plotly/dash-sample-apps.   It is set up as a submodule in the nebari-demo repo.  If you are not seeing anything listed in `nebari-demo/dashboard_examples/plotly-dash/dash-sample-apps` you will need to run the following commands:

```
git submodule init
git submodule update

```

Every once in awhile, the submodules may be updated.  You will need to run the following command:

```
git submodule update --remote

```