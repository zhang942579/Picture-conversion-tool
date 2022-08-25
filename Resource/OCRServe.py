from PyQt5.QtWidgets import QMessageBox
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
# 导入指定云服务的库 huaweicloudsdk{service}
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from huaweicloudsdkocr.v1 import *
import base64
from .Config import Config
import easyocr
"""
文字识别接口
"""


class OCRServe:
    def __init__(self):
        self.client = None
        self.credentials = None
        self.config = Config()
        self.ak = self.config.ak
        self.sk = self.config.sk

    def to_word(self, imagepath, is_internet):

        if(is_internet):
            return self.have_internet(imagepath)
        else:
           return self.no_internet(imagepath)


    def have_internet(self, imagepath):
        self.credentials = BasicCredentials(self.ak, self.sk)
        self.client = OcrClient.new_builder() \
            .with_credentials(self.credentials) \
            .with_region(OcrRegion.value_of("cn-north-4")) \
            .build()
        image_data = self.open_imgBS(imagepath)
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        try:
            request = RecognizeGeneralTextRequest()
            request.body = GeneralTextRequestBody(
                image=image_base64
            )
            response = self.client.recognize_general_text(request)
            result = []
            for i in response.result.words_block_list:
                result.append(i.words)
            return result
        except exceptions.ClientRequestException as e:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', e)
            msg_box.exec_()



    def no_internet(self, imagepath):
        reader = easyocr.Reader(['ch_sim', 'en'])  # this needs to run only once to load the model into memory
        result = reader.readtext(imagepath, detail=0)
        print(result)
        return result


    def open_imgBS(self, imagepath):
        with open(imagepath, "rb") as bin_data:
            image_data = bin_data.read()
        return image_data  # 使用图片的Base64编码

