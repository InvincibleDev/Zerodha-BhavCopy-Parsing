from BhavCopy.settings.base import *

SECRET_KEY = 'django-insecure-%+^q4t^a3$+w*&li^l3q_-)nv58(#j2#_rdc4bcdd7$0_*y)_m'

DEBUG = False

ALLOWED_HOSTS = ["http://zerodha-bhav-copy.s3-website.ap-south-1.amazonaws.com",
"ec2-35-154-206-196.ap-south-1.compute.amazonaws.com"]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ["http://zerodha-bhav-copy.s3-website.ap-south-1.amazonaws.com"]

print("\n" + "-" * 60)
print("Running server with production settings..")
print("-" * 60, "\n")
