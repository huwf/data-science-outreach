import os
import sys

c = get_config()

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# c.DockerSpawner.container_image = "jupyter/scipy-notebook"
c.DockerSpawner.container_image = "jupyterhub/singleuser"
here = os.path.dirname(__file__)
# c.DockerSpawner.args = ['-it', '-v', '%s/nbgrader/assignments:/home/jovyan/assignments' % here]
c.DockerSpawner.volumes = {'%s/assignments/outreach' % here: '/home/jovyan/work'}
c.DockerSpawner.debug = True
#c.DockerSpawner.container_ip = '0.0.0.0'
c.DockerSpawner.remove_containers = True
c.Spawner.debug = True
#c.DockerSpawner.hub_ip_connect = '152.78.64.211'
#c.JupyterHub.hub_ip = '152.78.64.211'

c.DockerSpawner.hub_ip_connect = '172.17.0.1'
c.JupyterHub.hub_ip = '172.17.0.1'

c.JupyterHub.port = 8000

c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.create_system_users = False

join = os.path.join


# root = os.environ.get('OAUTHENTICATOR_DIR', here)
sys.path.insert(0, here)

# ssl config
ssl = join(here, 'ssl')

keyfile = join(ssl, 'key.pem')
certfile = join(ssl, 'cert.pem')
if os.path.exists(keyfile):
    c.JupyterHub.ssl_key = keyfile
if os.path.exists(certfile):
    c.JupyterHub.ssl_cert = certfile

