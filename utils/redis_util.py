from redis import Redis
import utils.args as args
import os
# SETTINGS_PARAMS_MAP = {
#     'REDIS_URL': 'url',
#     'REDIS_HOST': 'host',
#     'REDIS_PORT': 'port',
#     'REDIS_ENCODING': 'encoding',
# }
# allow test settings from environment
REDIS_HOST = os.environ.get('REDIST_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
ARG=args.argparsed

def update_email(email,password):
    pass
def add_contact(name, email, ):
    pass
def redis_pub(parser_of, new_cves, new_advisory, ver_affected, link):
    r = Redis(REDIS_HOST,REDIS_PORT,0)
    for index in range(0,len(new_cves)):
        message="New cve found in "+parser_of+"\n cve_id: "+new_cves[index]+"\n version_Affect: "+ver_affected[index]+"\n Advisory: "+new_advisory[index]+"\n link : "+link[0]
        r.publish(parser_of,message)


# todo we need to use a way to cnfig settings and also setting from  users
