import sentry_sdk
sentry_sdk.init("https://3e2601d3b77c45158bf16d7638dbe3c3@sentry.io/1479026",release="python1");
#sentry_sdk.init("http://9c4bc5eadc0f4deb811dd6ff93979c76@127.0.0.1:9000/5")


from sentry_sdk import capture_exception

try:
    1/0
except Exception as e:
    capture_exception(e)

#from sentry_sdk import capture_message
#capture_message('Zhouyuan went wrong')
