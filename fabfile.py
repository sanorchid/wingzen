from fabric.api import env, settings, run

env.user = 'newdust'
env.hosts = ['216.185.102.20']

def exists(path):
	with settings(warn_only=True):
		return run('test -e %s' % path)

def ls():
	run('ls')

def whoami():
	run('whoami')

def migrate():
	pass
def deploy():
	pass

