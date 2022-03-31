# Operationalizing Machine Learning

## Project Overview
In this project, we will work with the Bank Marketing dataset. We will use Azure to configure a cloud-based machine learning production model, deploy it, and consume it. We will also create, publish, and consume a pipeline.

In this project, we will following the below steps:

- Authentication
- Automated ML Experiment
- Deploy the best model
- Enable logging
- Swagger Documentation
- Consume model endpoints
- Create and publish a pipeline
- Documentation

## Architectural Diagram
The following diagram is an image that helps visualize the flow of operations from start to finish. An architectual diagram of the project :

![Info](screenshot/Info.JPG)

## Key Steps

### Step 1: Authentication

In this step, we will install the Azure Machine Learning Extension which allows you to interact with Azure Machine Learning Studio, part of the az command. After having the Azure machine Learning Extension, we will create a Service Principal account and associate it with our specific workspace.

### Step 2: Automated ML Experiment

At this point, security is enabled and authentication is completed. In this step, we will create an experiment using Automated ML, configure a compute cluster, and use that cluster to run the experiment. We will upload the bankmarketing_train.csv to Azure Machine Learning Studio so that it can be used when training the model. Data link to download : https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv

Screenshot : Registered dataset

![Registered_dataset](screenshot/Registered_dataset.JPG)

Screenshot : AutoML completed

![AutoML_Complete](screenshot/AutoML_Complete.JPG)

Screenshot : Experiment AutoML completed

![Experiment_completed](screenshot/Experiment_completed.JPG)

### Step 3: Deploy the Best Model

After the experiment run completes, a summary of all the models and their metrics are shown, including explanations. The Best Model will be shown in the Details tab. In the Models tab, it will come up first (at the top). Select the best model for deployment. Deploying the Best Model will allow to interact with the HTTP API service and interact with the model by sending data over POST requests.

Screenshot : AutoML Best model

![Best_model](screenshot/Best_model.JPG)

### Step 4: Enable Application Insights

Now that the Best Model is deployed, enable Application Insights and retrieve logs. Although this is configurable at deploy time with a check-box, it is useful to be able to run code that will enable it.

Screenshot : Application insights

![Application_Insights](screenshot/Application_Insights.JPG)

Screenshot : Logs

![logs](screenshot/logs.JPG)

### Step 5: Swagger Documentation

In this step, we will consume the deployed model using Swagger. Azure provides a Swagger JSON file for deployed models. Head to the Endpoints section, and find deployed model there, it should be the first one on the list.

Screenshot : Swagger documentation

![swagger_documentation](screenshot/swagger_documentation.JPG)

Screenshot : Swagger get responses

![swagger_get_responses](screenshot/swagger_get_responses.JPG)

Screenshot : Swagger post responses

![swagger_post_responses](screenshot/swagger_post_responses.JPG)

### Step 6: Consume Model Endpoints

Once the model is deployed, use the endpoint.py script to interact with the trained model. In this step, we need to run the script, modifying both the scoring_uri and the key to match the key for service and the URI that was generated after deployment. This URI can be found in the Details tab, above the Swagger URI.

Screenshot : Endpoint output

![endpoint_output](screenshot/endpoint_output.JPG)

### Step 7: Create, Publish and Consume a Pipeline

For this part of the project, we will use the Jupyter Notebook. We must make sure to update the notebook to have the same keys, URI, dataset, cluster, and model names already created.

Screenshot : Pipeline runs

![Pipeline_Runs](screenshot/Pipeline_Runs.JPG)

Screenshot : Pipeline run overview

![Pipeline_Completed](screenshot/Pipeline_Completed.JPG)

Screenshot : Pipeline endpoint

![Pipeline_Endpoint1](screenshot/Pipeline_Endpoint1.JPG)

Screenshot : Pipeline run details

![Pipeline_Consume_RunDetails](screenshot/Pipeline_Consume_RunDetails.JPG)

Screenshot : Published Pipeline overview

![Pipeline_Endpoint](screenshot/Pipeline_Endpoint.JPG)

Screenshot : Pipeline consume

![Pipeline_Submitted_Run](screenshot/Pipeline_Submitted_Run.JPG)

Screenshot : Published Pipeline overview

![Pipeline_Endpoint](screenshot/Pipeline_Endpoint.JPG)

Screenshot : All experiments

![All_Experiments](screenshot/All_Experiments.JPG)

Screenshot : Experiments completed

![Experiments_Completed](screenshot/Experiments_Completed.JPG)

## Screen Recording

Link to a screen recording of the project in action : https://youtu.be/3Yh48B21VeI

The screencast demonstrate:

- Working deployed ML model endpoint
- Deployed Pipeline
- Available AutoML Model
- Successful API requests to the endpoint with a JSON payload

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
