# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys

from cloudbaseinit.utils import classloader


class OSUtilsFactory(object):
    def get_os_utils(self):
        osutils_class_paths = {
            'windows': 'cloudbaseinit.osutils.windows.WindowsUtils', # not sure about windows yet
            'posix': 'cloudbaseinit.osutils.posix.PosixUtils',
	    'freebsd9': 'cloudbaseinit,osutils.freebsd.FreeBSDUtils'
        }

        cl = classloader.ClassLoader()
        return cl.load_class(osutils_class_paths[sys.platform])()
