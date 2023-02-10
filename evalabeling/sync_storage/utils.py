import asyncio
import re
from eva.server.db_api import connect


def file_path_convert(data_path):
    where_upload_starts = re.search("^\/data\/local\-files\/\?d=", data_path)
    if where_upload_starts != None:
        start_pos = len("/data/local-files/?d=")
        data_path = data_path[start_pos:]
        data_path = "/" + data_path
    else:
        # TODO: Path needs to be verifies
        data_path = data_path.split("/data")[1]
        data_path = "/root/.local/share/label-studio/media/" + data_path
    return data_path


def add_to_eva(request_data):
    # TODO: Support formats other than 'image'
    for new_task in request_data["tasks"]:
        data_path = new_task["data"]["image"]
        data_path = file_path_convert(data_path)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        EVA_CURSOR = connect(host="127.0.0.1", port=5432).cursor()
        EVA_CURSOR.execute(
            f"LOAD IMAGE '{data_path}' INTO v{request_data['project']['id']}"
        )
        eva_result = EVA_CURSOR.fetch_all()
        print(eva_result)
        print("TaskID: ", new_task["id"], ", ProjectID: ", request_data['project']['id'], eva_result.status.value == 0)


def remove_from_eva(request_data):

    for new_task in request_data["tasks"]:
        data_path = new_task["data"]["image"]
        data_path = file_path_convert(data_path)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        EVA_CURSOR = connect(host="127.0.0.1", port=5432).cursor()
        EVA_CURSOR.execute(
            f"LOAD IMAGE '{data_path}' INTO v{request_data['project']['id']}"
        )
        eva_result = EVA_CURSOR.fetch_all()
        print(eva_result)
        print(new_task["id"], eva_result.status.value == 0)
