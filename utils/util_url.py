import os


def get_root_url(object_name):
    curPath = os.path.abspath(os.path.dirname(__file__))
    root_path = curPath[:curPath.find(object_name) + len(object_name)]  # 获取myProject，也就是项目的根路径
    return root_path


ROOT = get_root_url("wisdom_classroom")
