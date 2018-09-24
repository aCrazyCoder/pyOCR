from API import Client


class ocr:
    """
    ocr识别
    """

    def __init__(self):
        self._appid = ''
        self._secret_id = ''
        self._secret_key = ''
        self._bucket = ''
        self._time = 30
        self.client = Client(self._appid, self._secret_id, self._secret_key, self._bucket)
        self.client.use_http()
        self.client.set_timeout(self._time)

    def setappid(self, appid):
        """
        设置APPID
        :param appid: 字符串形式
        :return: null
        """
        if isinstance(appid, str):
            self._appid = appid
            self.client.setattr(appid=self._appid, sid=self._secret_id, skey=self._secret_key, bucket=self._bucket)
        else:
            raise TypeError

    def setsecretid(self, secretid):
        """
        设置secretID
        :param secretid: 字符串形式
        :return: null
        """
        if isinstance(secretid, str):
            self._secret_id = secretid
            self.client.setattr(appid=self._appid, sid=self._secret_id, skey=self._secret_key, bucket=self._bucket)
        else:
            raise TypeError

    def setsecretkey(self, secretkey):
        """
        设置secretkey
        :param secretkey: 字符串形式
        :return: null
        """
        if isinstance(secretkey, str):
            self._secret_key = secretkey
            self.client.setattr(appid=self._appid, sid=self._secret_id, skey=self._secret_key, bucket=self._bucket)
        else:
            raise TypeError

    def setbucket(self, bucket):
        """
        设置bucket
        :param bucket: 字符串形式
        :return: null
        """
        if isinstance(bucket, str):
            self._bucket = bucket
            self.client.setattr(appid=self._appid, sid=self._secret_id, skey=self._secret_key, bucket=self._bucket)
        else:
            raise TypeError

    def settemeout(self, time):
        """
        设置识别时间界限
        :param time: 整数形式
        :return: null
        """
        if isinstance(time, int):
            self._time = time
            self.client.set_timeout(self._time)
        else:
            raise TypeError
