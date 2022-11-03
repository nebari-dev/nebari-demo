<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/nebari-dev/nebari-design/main/logo-mark/horizontal/Nebari-Logo-Horizontal-Lockup.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nebari-dev/nebari-design/main/logo-mark/horizontal/Nebari-Logo-Horizontal-Lockup-White-text.svg">
    <img alt="Nebari logo mark - text will be black in light color mode and white in dark color mode." width="50%"/>
  </picture>
</p>

---

# Nebari demo

> This material was presented at PyDataNYC 2022 🗽

This repo contains a walkthrough of many of Nebari's high-level features including Jupyter, Dask, conda-store, etc.


## Get started

To follow along with the material covered in this presentation, navigate to [demo.nebari.dev](https://demo.nebari.dev).


### Login for the first time

To login for the first time, follow these instructions:

1. Click on the `Sign in with Keycloak` button.

<img src="./assets/keycloak-sign-in.png" alt="">

2. Click `Register` at the bottom of the sign in prompt.

<img src="./assets/keycloak-register.png" alt="">

3. Fill out the short form to register as a new user.

<img src="./assets/keycloak-register-form.png" alt="">

> Your user account will promptly be deleted after the conclusion of the tutorial.

> The email address will serve as your username. We are not storing your email address and it will never be shared with anyone. You can also use a fake address here.

4. In the Hub page that opens automatically, click on the "Start My Server" button.

<img src="./assets/start-server.png" alt="">


5. For `Server Options`, select `Small instance` and then click `Start`.

<img src="./assets/server-options.png" alt="">

> If your server doesn't launch within 30 seconds, this means the cluster is in the process of auto-scaling to meet the new demand. Please be patient, this might take up to several minutes.

5. From here, you can clone this repo in two ways, from the Jupyter terminal or from the JupyterLab git extention.
    - Clone this repo from the Jupyter Terminal:

    ```
    git clone https://github.com/nebari-dev/nebari-demo
    ```

    - Clone this repo using JupyterLab git extention

    ![Image of the JupyterLab git extension](./assets/jupyterlab-git-extension.png)

6. Finally, open the `00_overview.ipynb` notebook to follow along.

## Deploy your own Nebari cluster

If you were not in attendance at the live PyDataNYC tutorial, you can deploy your own Nebari cluster and clone this repo to walk through the several of the high-level features.

To deploy your own Nebari cluster, please visit [github.com/nebari-dev/nebari](https://github.com/nebari-dev/nebari).

> Please note that the material presented in this repo need to be run on a live Nebari deployment. Many of the features highlighed in this repo are not available in basic JupyterHub deployments.


## More resources
* Get help:
* Nebari documentation:


## Acknowledgements
TBD
