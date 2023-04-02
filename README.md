# eva-labeling
## What is EVA Labeling?

The EVA Labeling is a wrapper to enable you to run EVA alongside [Label-Studio](!https://labelstud.io/) It lets you connect to Label Studio server to do the following:

- Annotate your dataset more quickly and easily by allowing you to label them in bulk.
- Dynamically pre-annotate data based on model inference results.
- Retrain or fine-tune a model based on recently annotated data.

## Video

<video height="500" controls>
  <source src="assets\bulk-prop-demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## How it works

1. This application helps fetch data from Label Studio server and add it to EVA.
2. Then you use Label Studio ML Backend to run `EVA Query` Statements on you data. (e.g. Clustering, Object detection, Object Tracking)
3. Returns the desired output to Label Studio


## Quickstart

1. Clone this repository
    ```bash
    git clone https://github.com/georgia-tech-db/eva-labeling.git
    ```

2. Setup Environment  
    It is highly recommended to use `venv` python environments. You can use the same environment as Label Studio. [Read more](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) about creating virtual environments via `venv`.
   ```bash
   cd eva-labeling
   
   # Install eva-labeling
   pip install -e .
   ```

3. Start eva-labeling server
    > Note: this will also start the `evadb` server.
    ```bash
    evalabeling start ./evaml -eu <eva-server-url> -ep  <eva-server-port> -k <apikey> -ls <label-studio-url>
    ```

4. Add Image Clustering Interface
    ```html
    <View>
    <Image name="image" value="$image"/>
    <RectangleLabels name="label" toName="image">
      
    </RectangleLabels>
    <TextArea name="cluster" toName="image"
              rows="1" editable="true" />
    </View>
    ```

5. Start and Register EVA ML Backend to Label Studio.
    > Following [Label Studio ML documentation](https://github.com/heartexlabs/label-studio-ml-backend)  
    <img title="Webhook Registering" alt="Webhook Registering with EVA" src="assets/model_registering.png" width="500">
    <img title="Webhook Registering" alt="Webhook Registering with EVA" src="assets/model_registered.png" width="500">


<!-- EVA ML 
<img title="EVA Label Studio Integration" alt="Pipeline" src="assets/pipeline_screenshot.png" width="500"> -->