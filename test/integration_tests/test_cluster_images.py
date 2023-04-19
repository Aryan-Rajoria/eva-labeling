import unittest
import os

from evaml.cluster_images import EVAModel
from label_studio_ml.api import init_app

class TestClusterImages(unittest.TestCase):

    def test_server_running(self):
        app = init_app(
        model_class=EVAModel,
        # model_dir=os.environ.get("MODEL_DIR", args.model_dir),
        # redis_queue=os.environ.get("RQ_QUEUE_NAME", "default"),
        # redis_host=os.environ.get("REDIS_HOST", "localhost"),
        # redis_port=os.environ.get("REDIS_PORT", 6379),
        )
        with app.test_client() as client:
            # Make requests to app here
            reponse = client.get("/")
            print(reponse)
            assert reponse.status_code == 200, "The server did not start"

