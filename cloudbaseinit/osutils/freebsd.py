from cloudbaseinit.osutils import base
import subprocess

class FreeBSDUtils(base.BaseOSUtils):
	def reboot(self):
		if ( os.system('reboot') != 0 ):
			raise Exception('Reboot failed')

	def user_exists(self, username):
		try:
			subprocess.check_output(["id", username])
		except CalledProcessError:
			return False
		return True

	# not completed
	def create_user(self, username, password, password_expires=False):
		try:
			subprocess.check_output(["adduser", "-w", "yes", "-s", "tcsh"])
		except CalledProcessError:
			raise Exception(CalledProcessError.output)

	def set_host_name(self, new_host_name):
		try:
			subprocess.checkoutput(["hostname", new_host_name])
		except CalledProcessError:
			raise Exception(CalledProcessError.output)
