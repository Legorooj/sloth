import os
env = os.environ

conf = '''[distutils]
index-servers =
    default

[default]
repository: {repo}
username: {uname}
password: {pswd}
'''

uname = env['TWINE_USERNAME']
pswd = env['TWINE_PASSWORD']
repo = env['UPLOAD_REPO']

conf = conf.format(uname=uname, pswd=pswd, repo=repo)

open('.pypirc', 'w').write(conf)
