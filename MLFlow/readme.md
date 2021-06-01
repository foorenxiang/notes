# mlFlow

Reference: [Getting Started with mlFLow](https://towardsdatascience.com/getting-started-with-mlflow-52eff8c09c61)

# What is mlFlow?

mlFlow is a framework that supports the machine learning lifecycle.

- Monitor model during training and running
- Store models and load models in production code
- Create experiment pipeline

The framework introduces 3 distinct features each with it’s own capabilities.

1. MlFlow Tracking

   - Logging framework around models. Define custom metrics for comparisons between runs

2. MlFlow Projects

   - Create a pipeline if required. This feature uses its own template to define how to run the model on a cloud environment. As most companies have a way to run code in production this feature may not be required.

3. MlFlow Models

   - An mlFlow Model is a standard format for packaging machine learning models
