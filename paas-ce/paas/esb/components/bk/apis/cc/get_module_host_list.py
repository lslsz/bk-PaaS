# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa
from django import forms

from common.forms import BaseComponentForm
from common.constants import API_TYPE_Q
from components.component import Component
from .toolkit import tools, configs


class GetModuleHostList(Component):
    """
    apiLabel {{ _("查询模块主机列表") }}
    apiMethod GET

    ### {{ _("功能描述") }}

    {{ _("查询模块主机列表") }}

    ### {{ _("请求参数") }}

    {{ common_args_desc }}

    #### {{ _("接口参数") }}

    | {{ _("字段") }}      |  {{ _("类型") }}      | {{ _("必选") }}   |  {{ _("描述") }}      |
    |-----------|------------|--------|------------|
    | app_id |  string    | {{ _("是") }}     | {{ _("业务ID") }} |
    | module_id |  string    | {{ _("是") }}     | {{ _("模块ID") }} |

    ### {{ _("请求参数示例") }}

    ```python
    {
        "app_code": "esb_test",
        "app_secret": "xxx",
        "bk_token": "xxx",
        "app_id": "1",
        "module_id": "1"
    }
    ```

    ### {{ _("返回结果示例") }}

    ```python
    {
        "result": true,
        "code": "00",
        "message": "",
        "data": [
            {
                "ModuleName": "Test",
                "IdcName": "",
                "Source": "3",
                "ApplicationID": "1",
                "Status": "",
                "HardMemo": "",
                "Mem": "0",
                "HostName": "host",
                "DeviceClass": "",
                "SetID": "1",
                "ApplicationName": "Test",
                "HostID": "1",
                "BakOperator": "",
                "OuterIP": "",
                "Region": "test",
                "ModuleID": "1",
                "SetName": "",
                "AssetID": "test-1",
                "OSName": "",
                "Operator": "",
                "InnerIP": "10.0.0.1",
                "CreateTime": "2016-03-22 21:07:47"
            }
        ]
    }
    ```
    """
    sys_name = configs.SYSTEM_NAME
    api_type = API_TYPE_Q

    host = configs.host

    class Form(BaseComponentForm):
        app_id = forms.CharField(label='business ID', required=True)
        module_id = forms.CharField(label='module ID', required=True)

        def clean(self):
            data = self.cleaned_data
            return {
                'ApplicationID': data['app_id'],
                'ModuleID': data['module_id'],
            }

    def handle(self):
        client = tools.CCClient(self)
        self.response.payload = client.post_request(
            self.host,
            '/api/Host/getmodulehostlist',
            data=self.form_data,
        )
