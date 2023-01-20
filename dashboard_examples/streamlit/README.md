# 🔭 Example app image comparison

This code is found here: https://github.com/streamlit/example-app-image-comparison/

It is added as a submodule to this repo.  The easiest way to run it is to do the follow.

1. Initiate the submodule:
    ```
    git submodule init
    git submodule update
    ```

2. Create conda environment.  Note: it seemed to be taking a long time to create the environment from the environment.yml file.  It is faster to create an environment and then pip install the 2 dependencies.
   
    ```
    conda create --name streamlit-dashboard
    conda activate streamlit-dashboard

    pip install streamlit
    pip install streamlit-image-comparison

    ```
