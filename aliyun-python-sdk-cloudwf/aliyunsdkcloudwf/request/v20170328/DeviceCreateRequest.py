# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class DeviceCreateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloudwf', '2017-03-28', 'DeviceCreate','cloudwf')

	def get_DeviceNum(self):
		return self.get_query_params().get('DeviceNum')

	def set_DeviceNum(self,DeviceNum):
		self.add_query_param('DeviceNum',DeviceNum)

	def get_DevicePosition(self):
		return self.get_query_params().get('DevicePosition')

	def set_DevicePosition(self,DevicePosition):
		self.add_query_param('DevicePosition',DevicePosition)

	def get_DeviceName(self):
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self,DeviceName):
		self.add_query_param('DeviceName',DeviceName)

	def get_DeviceType(self):
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self,DeviceType):
		self.add_query_param('DeviceType',DeviceType)

	def get_Sid(self):
		return self.get_query_params().get('Sid')

	def set_Sid(self,Sid):
		self.add_query_param('Sid',Sid)