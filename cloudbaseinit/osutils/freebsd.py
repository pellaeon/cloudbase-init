from cloudbaseinit.osutils import base
import subprocess

class FreeBSDUtils(base.BaseOSUtils):
    def reboot(self):
        subprocess.check_output('reboot', shell=True)

    def user_exists(self, username):
        from pwd import getpwall
        return any(p.pw_name==usename for p in getpwall())

    # not completed
    def create_user(self, username, password, password_expires=False):
        adduser_cmd = "adduser -w yes -s tcsh" # it should be completed someday
        subprocess.check_output(adduser_cmd, shell=True)

    def set_host_name(self, new_host_name):
        # subprocess.check_output(["hostname", new_host_name]) # is it no use ?
        # using SED
        cmd_newhost = "[ -z `egrep '^hostname' /etc/rc.conf` ] && { echo 'hostname=\"%s\"' >> /etc/rc.conf } || { sed -e 's/^hostname=.*$/hostname=\"%s\"/' -I '' /etc/rc.conf }" % (new_host_name, new_host_name)
        subprocess.check_output(cmd_newhost, shell=True)

    def sanitize_shell_input(self, value):
        pass

    def set_user_password(self, username, password, password_expires=False):
        pass

    def add_user_to_local_group(self, username, groupname):
        pass

    def get_user_home(self, username):
        pass

    def get_network_adapters(self):
        pass

    def set_static_network_config(self, adapter_name, address, netmask,
                                  broadcast, gateway, dnsdomain,
                                  dnsnameservers):
        pass

    def set_config_value(self, name, value, section=None):
        pass

    def get_config_value(self, name, section=None):
        pass

    def wait_for_boot_completion(self):
        pass

    def terminate(self):
        pass

    def get_default_gateway(self):
        pass

    def check_static_route_exists(self, destination):
        pass

    def add_static_route(self, destination, mask, next_hop, interface_index,
                         metric):
        pass

    def get_os_version(self):
        pass

    def get_volume_label(self, drive):
        pass
