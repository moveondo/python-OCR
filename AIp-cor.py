
import time
from aip import AipOcr


class Aiocr(object):

    def __init__(self, app_id, api_key, secret_key):
        self._app_id = app_id
        self._api_key = api_key
        self._secret_key = secret_key
        self._client = AipOcr(app_id, api_key, secret_key)

    def proc_form(self, image):
        image = self.get_file_content(image)
        return self._client.tableRecognitionAsync(image);

    def proc_from_res(self, req_id):
        options = {"result_type": "excel"}
        return self._client.getTableRecognitionResult(req_id, options)

    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':

    APP_ID = '11635479'
    API_KEY = 'y52YctCoPhY8KRwtzoFliKsU'
    SECRET_KEY = 'GawZoudCnmRhqq1lDbqkpgky3rpsmk8G'

    ai_ocr = Aiocr(APP_ID, API_KEY, SECRET_KEY)
    res = ai_ocr.proc_form('./image/1.jpg')
    for req in res['result']:
        resp = ai_ocr.proc_from_res(req['request_id'])
        while not ('error_code' in resp) and not resp['result']['ret_code'] == 3:
            time.sleep(10)
            resp = ai_ocr.proc_from_res(req['request_id'])
        print(resp)
