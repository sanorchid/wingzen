from fabric.api import *

def prepare_deploy():
	# '.\' is for windows powershell, should be './' in linux local
	local("git add -p")
	local("git commit -m 'test commit' ")
	local("git push")


	