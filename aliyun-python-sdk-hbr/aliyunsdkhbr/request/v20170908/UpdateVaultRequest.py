# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateVaultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hbr', '2017-09-08', 'UpdateVault','hbr')
		self.set_protocol_type('https')

	def get_VaultId(self):
		return self.get_query_params().get('VaultId')

	def set_VaultId(self,VaultId):
		self.add_query_param('VaultId',VaultId)

	def get_SearchEnabled(self):
		return self.get_query_params().get('SearchEnabled')

	def set_SearchEnabled(self,SearchEnabled):
		self.add_query_param('SearchEnabled',SearchEnabled)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_VaultName(self):
		return self.get_query_params().get('VaultName')

	def set_VaultName(self,VaultName):
		self.add_query_param('VaultName',VaultName)