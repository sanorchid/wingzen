from fabric.api import local

def prepare_deploy():
	# '.\' is for windows powershell, should be './' in linux shell.
	local("git add -p && git commit")
	local("git push")


	