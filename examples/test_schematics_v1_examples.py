# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for SchematicsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import io
import os
import pytest
from ibm_cloud.schematics_v1 import *

#
# This file provides an example of how to use the schematics service.
#
# The following configuration properties are assumed to be defined:
# SCHEMATICS_URL=<service base url>
# SCHEMATICS_AUTH_TYPE=iam
# SCHEMATICS_APIKEY=<IAM apikey>
# SCHEMATICS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'schematics_v1.env'

schematics_service = None

config = None


##############################################################################
# Start of Examples for Service: SchematicsV1
##############################################################################
# region
class TestSchematicsV1Examples:
    """
    Example Test Class for SchematicsV1
    """

    @classmethod
    def setup_class(cls):
        global schematics_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            schematics_service = SchematicsV1.new_instance(
            )

            # end-common
            assert schematics_service is not None

            # Load the configuration
            global config
            config = read_external_sources(SchematicsV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_locations_example(self):
        """
        list_locations request example
        """
        try:
            print('\nlist_locations() result:')

            # begin-list_locations

            response = schematics_service.list_locations()
            schematics_locations_list = response.get_result()

            print(json.dumps(schematics_locations_list, indent=2))

            # end-list_locations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_group_example(self):
        """
        list_resource_group request example
        """
        try:
            print('\nlist_resource_group() result:')

            # begin-list_resource_group

            response = schematics_service.list_resource_group()
            list_resource_group_response = response.get_result()

            print(json.dumps(list_resource_group_response, indent=2))

            # end-list_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_schematics_version_example(self):
        """
        get_schematics_version request example
        """
        try:
            print('\nget_schematics_version() result:')

            # begin-get_schematics_version

            response = schematics_service.get_schematics_version()
            version_response = response.get_result()

            print(json.dumps(version_response, indent=2))

            # end-get_schematics_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_process_template_meta_data_example(self):
        """
        process_template_meta_data request example
        """
        try:
            print('\nprocess_template_meta_data() result:')

            # begin-ProcessTemplateMetaData

            git_source_model = {
                'computed_git_repo_url': 'https://github.com/IBM-Cloud/terraform-provider-ibm/tree/master/examples/ibm-vsi',
                'git_repo_url': 'https://github.com/IBM-Cloud/terraform-provider-ibm',
                'git_repo_folder': 'examples/ibm-vsi',
                'git_release': 'v1.0.0',
                'git_branch': 'master',
            }

            external_source_model = {
                'source_type': 'git_hub',
                'git': git_source_model,
            }

            response = schematics_service.process_template_meta_data(
                template_type='terraform_v1_0',
                source=external_source_model,
            )
            template_meta_data_response = response.get_result()

            print(json.dumps(template_meta_data_response, indent=2))

            # end-ProcessTemplateMetaData

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_resources_v2_example(self):
        """
        get_workspace_resources_v2 request example
        """
        try:
            print('\nget_workspace_resources_v2() result:')

            # begin-get_workspace_resources_v2

            response = schematics_service.get_workspace_resources_v2(
                w_id='testString',
            )
            template_resources_object = response.get_result()

            print(json.dumps(template_resources_object, indent=2))

            # end-get_workspace_resources_v2

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_outputs_v2_example(self):
        """
        get_workspace_outputs_v2 request example
        """
        try:
            print('\nget_workspace_outputs_v2() result:')

            # begin-get_workspace_outputs_v2

            response = schematics_service.get_workspace_outputs_v2(
                w_id='testString',
            )
            output_values_object = response.get_result()

            print(json.dumps(output_values_object, indent=2))

            # end-get_workspace_outputs_v2

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_input_metadata_v2_example(self):
        """
        get_workspace_input_metadata_v2 request example
        """
        try:
            print('\nget_workspace_input_metadata_v2() result:')

            # begin-get_workspace_input_metadata_v2

            response = schematics_service.get_workspace_input_metadata_v2(
                w_id='testString',
                t_id='testString',
            )
            template_values_meta_data = response.get_result()

            print(json.dumps(template_values_meta_data, indent=2))

            # end-get_workspace_input_metadata_v2

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_workspaces_example(self):
        """
        list_workspaces request example
        """
        try:
            print('\nlist_workspaces() result:')

            # begin-list_workspaces

            response = schematics_service.list_workspaces()
            workspace_response_list = response.get_result()

            print(json.dumps(workspace_response_list, indent=2))

            # end-list_workspaces

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_workspace_example(self):
        """
        create_workspace request example
        """
        try:
            print('\ncreate_workspace() result:')

            # begin-create_workspace

            workspace_variable_request_model = {
                'name': 'region',
                'type': 'string',
                'value': 'us-south',
            }

            template_source_data_request_model = {
                'type': 'terraform_v1.9',
                'variablestore': [workspace_variable_request_model],
            }

            template_repo_request_model = {
                'url': 'https://github.com/ptaube/tf_cloudless_sleepy',
            }

            response = schematics_service.create_workspace(
                description='Workspace to provision infrastructure',
                location='us-east',
                name='my-terraform-workspace',
                resource_group='Default',
                tags=['env:dev', 'project:demo'],
                template_data=[template_source_data_request_model],
                template_repo=template_repo_request_model,
                type=['terraform_v1.9'],
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-create_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_example(self):
        """
        get_workspace request example
        """
        try:
            print('\nget_workspace() result:')

            # begin-get_workspace

            response = schematics_service.get_workspace(
                w_id='testString',
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-get_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_workspace_example(self):
        """
        update_workspace request example
        """
        try:
            print('\nupdate_workspace() result:')

            # begin-update_workspace

            workspace_status_update_request_model = {
                'frozen': False,
            }

            response = schematics_service.update_workspace(
                w_id='testString',
                description='Updated workspace description',
                name='my-workspace-updated',
                tags=['env:production', 'team:devops'],
                workspace_status=workspace_status_update_request_model,
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-update_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_workspace_example(self):
        """
        replace_workspace request example
        """
        try:
            print('\nreplace_workspace() result:')

            # begin-replace_workspace

            workspace_variable_request_model = {
                'description': 'Description of sample_var',
                'name': 'sample_var',
                'secure': False,
                'value': 'THIS IS IBM CLOUD TERRAFORM CLI DEMO',
            }

            template_source_data_request_model = {
                'folder': '.',
                'type': 'terraform_v1.0',
                'variablestore': [workspace_variable_request_model],
            }

            template_repo_update_request_model = {
                'url': 'https://github.com/ptaube/tf_cloudless_sleepy',
            }

            workspace_status_update_request_model = {
                'frozen': True,
            }

            response = schematics_service.replace_workspace(
                w_id='testString',
                description='terraform workspace updated',
                name='testWorkspaceApi',
                tags=['department:HR', 'application:compensation', 'environment:staging'],
                template_data=[template_source_data_request_model],
                template_repo=template_repo_update_request_model,
                type=['terraform_v1.0'],
                workspace_status=workspace_status_update_request_model,
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-replace_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_readme_example(self):
        """
        get_workspace_readme request example
        """
        try:
            print('\nget_workspace_readme() result:')

            # begin-get_workspace_readme

            response = schematics_service.get_workspace_readme(
                w_id='testString',
            )
            template_readme = response.get_result()

            print(json.dumps(template_readme, indent=2))

            # end-get_workspace_readme

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_template_repo_upload_example(self):
        """
        template_repo_upload request example
        """
        try:
            print('\ntemplate_repo_upload() result:')

            # begin-template_repo_upload

            response = schematics_service.template_repo_upload(
                w_id='testString',
                t_id='testString',
            )
            template_repo_tar_upload_response = response.get_result()

            print(json.dumps(template_repo_tar_upload_response, indent=2))

            # end-template_repo_upload

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_inputs_example(self):
        """
        get_workspace_inputs request example
        """
        try:
            print('\nget_workspace_inputs() result:')

            # begin-get_workspace_inputs

            response = schematics_service.get_workspace_inputs(
                w_id='testString',
                t_id='testString',
            )
            template_values = response.get_result()

            print(json.dumps(template_values, indent=2))

            # end-get_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_workspace_inputs_example(self):
        """
        replace_workspace_inputs request example
        """
        try:
            print('\nreplace_workspace_inputs() result:')

            # begin-replace_workspace_inputs

            workspace_variable_request_model = {
                'description': 'IBM Cloud region',
                'name': 'region',
                'secure': False,
                'type': 'string',
                'value': 'us-south',
            }

            response = schematics_service.replace_workspace_inputs(
                w_id='testString',
                t_id='testString',
                env_values=[{'name': 'env_variable_name', 'value': 'env_variable_value'}],
                values='string',
                variablestore=[workspace_variable_request_model],
            )
            user_values = response.get_result()

            print(json.dumps(user_values, indent=2))

            # end-replace_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_all_workspace_inputs_example(self):
        """
        get_all_workspace_inputs request example
        """
        try:
            print('\nget_all_workspace_inputs() result:')

            # begin-get_all_workspace_inputs

            response = schematics_service.get_all_workspace_inputs(
                w_id='testString',
            )
            workspace_template_values_response = response.get_result()

            print(json.dumps(workspace_template_values_response, indent=2))

            # end-get_all_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_input_metadata_example(self):
        """
        get_workspace_input_metadata request example
        """
        try:
            print('\nget_workspace_input_metadata() result:')

            # begin-get_workspace_input_metadata

            response = schematics_service.get_workspace_input_metadata(
                w_id='testString',
                t_id='testString',
            )
            template_metadata = response.get_result()

            print(json.dumps(template_metadata, indent=2))

            # end-get_workspace_input_metadata

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_outputs_example(self):
        """
        get_workspace_outputs request example
        """
        try:
            print('\nget_workspace_outputs() result:')

            # begin-get_workspace_outputs

            response = schematics_service.get_workspace_outputs(
                w_id='testString',
            )
            list_output_values_inner = response.get_result()

            print(json.dumps(list_output_values_inner, indent=2))

            # end-get_workspace_outputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_resources_example(self):
        """
        get_workspace_resources request example
        """
        try:
            print('\nget_workspace_resources() result:')

            # begin-get_workspace_resources

            response = schematics_service.get_workspace_resources(
                w_id='testString',
            )
            list_template_resources = response.get_result()

            print(json.dumps(list_template_resources, indent=2))

            # end-get_workspace_resources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_state_example(self):
        """
        get_workspace_state request example
        """
        try:
            print('\nget_workspace_state() result:')

            # begin-get_workspace_state

            response = schematics_service.get_workspace_state(
                w_id='testString',
            )
            state_store_response_list = response.get_result()

            print(json.dumps(state_store_response_list, indent=2))

            # end-get_workspace_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_template_state_example(self):
        """
        get_workspace_template_state request example
        """
        try:
            print('\nget_workspace_template_state() result:')

            # begin-get_workspace_template_state

            response = schematics_service.get_workspace_template_state(
                w_id='testString',
                t_id='testString',
            )
            template_state_store = response.get_result()

            print(json.dumps(template_state_store, indent=2))

            # end-get_workspace_template_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_activity_logs_example(self):
        """
        get_workspace_activity_logs request example
        """
        try:
            print('\nget_workspace_activity_logs() result:')

            # begin-get_workspace_activity_logs

            response = schematics_service.get_workspace_activity_logs(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity_logs = response.get_result()

            print(json.dumps(workspace_activity_logs, indent=2))

            # end-get_workspace_activity_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_log_urls_example(self):
        """
        get_workspace_log_urls request example
        """
        try:
            print('\nget_workspace_log_urls() result:')

            # begin-get_workspace_log_urls

            response = schematics_service.get_workspace_log_urls(
                w_id='testString',
            )
            log_store_response_list = response.get_result()

            print(json.dumps(log_store_response_list, indent=2))

            # end-get_workspace_log_urls

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_logs_example(self):
        """
        get_template_logs request example
        """
        try:
            print('\nget_template_logs() result:')

            # begin-get_template_logs

            response = schematics_service.get_template_logs(
                w_id='testString',
                t_id='testString',
            )
            template_log_store_string = response.get_result()

            print(json.dumps(template_log_store_string, indent=2))

            # end-get_template_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_activity_log_example(self):
        """
        get_template_activity_log request example
        """
        try:
            print('\nget_template_activity_log() result:')

            # begin-get_template_activity_log

            response = schematics_service.get_template_activity_log(
                w_id='testString',
                t_id='testString',
                activity_id='testString',
            )
            workspace_activity_template_log_string = response.get_result()

            print(json.dumps(workspace_activity_template_log_string, indent=2))

            # end-get_template_activity_log

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_actions_example(self):
        """
        list_actions request example
        """
        try:
            print('\nlist_actions() result:')

            # begin-list_actions

            response = schematics_service.list_actions()
            action_list = response.get_result()

            print(json.dumps(action_list, indent=2))

            # end-list_actions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_action_example(self):
        """
        create_action request example
        """
        try:
            print('\ncreate_action() result:')

            # begin-create_action

            git_source_model = {
                'git_repo_url': 'https://github.com/Cloud-Schematics/ansible-is-instance-actions',
            }

            external_source_model = {
                'source_type': 'git',
                'git': git_source_model,
            }

            response = schematics_service.create_action(
                name='Example-12ab1334',
                description='action_description',
                location='us-south',
                resource_group='test',
                tags=['department:HR', 'application:compensation', 'environment:staging', 'env:dev', 'k8s'],
                source=external_source_model,
            )
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-create_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_action_example(self):
        """
        get_action request example
        """
        try:
            print('\nget_action() result:')

            # begin-get_action

            response = schematics_service.get_action(
                action_id='testString',
            )
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-get_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_action_example(self):
        """
        update_action request example
        """
        try:
            print('\nupdate_action() result:')

            # begin-update_action

            git_source_model = {
                'git_repo_url': 'https://github.com/Cloud-Schematics/ansible-lamp-stack',
                'git_branch': 'v2.0',
            }

            external_source_model = {
                'source_type': 'git_hub',
                'git': git_source_model,
            }

            variable_metadata_model = {
                'type': 'string',
                'secure': True,
            }

            variable_data_model = {
                'name': 'db_password',
                'value': 'NewSecurePassword456',
                'metadata': variable_metadata_model,
            }

            response = schematics_service.update_action(
                action_id='testString',
                name='Deploy LAMP Stack - Updated',
                description='Updated action to deploy LAMP stack with new configuration',
                tags=['env:production', 'app:lamp', 'version:2.0'],
                source=external_source_model,
                command_parameter='site-v2.yml',
                inputs=[variable_data_model],
            )
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-update_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upload_template_tar_action_example(self):
        """
        upload_template_tar_action request example
        """
        try:
            print('\nupload_template_tar_action() result:')

            # begin-upload_template_tar_action

            response = schematics_service.upload_template_tar_action(
                action_id='testString',
            )
            template_repo_tar_upload_response = response.get_result()

            print(json.dumps(template_repo_tar_upload_response, indent=2))

            # end-upload_template_tar_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_workspace_activities_example(self):
        """
        list_workspace_activities request example
        """
        try:
            print('\nlist_workspace_activities() result:')

            # begin-list_workspace_activities

            response = schematics_service.list_workspace_activities(
                w_id='testString',
            )
            workspace_activities = response.get_result()

            print(json.dumps(workspace_activities, indent=2))

            # end-list_workspace_activities

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_activity_example(self):
        """
        get_workspace_activity request example
        """
        try:
            print('\nget_workspace_activity() result:')

            # begin-get_workspace_activity

            response = schematics_service.get_workspace_activity(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity = response.get_result()

            print(json.dumps(workspace_activity, indent=2))

            # end-get_workspace_activity

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_run_workspace_commands_example(self):
        """
        run_workspace_commands request example
        """
        try:
            print('\nrun_workspace_commands() result:')

            # begin-run_workspace_commands

            response = schematics_service.run_workspace_commands(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_command_result = response.get_result()

            print(json.dumps(workspace_activity_command_result, indent=2))

            # end-run_workspace_commands

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_apply_workspace_command_example(self):
        """
        apply_workspace_command request example
        """
        try:
            print('\napply_workspace_command() result:')

            # begin-apply_workspace_command

            response = schematics_service.apply_workspace_command(
                refresh_token='testString',
                w_id='testString',
            )
            workspace_activity_apply_result = response.get_result()

            print(json.dumps(workspace_activity_apply_result, indent=2))

            # end-apply_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_destroy_workspace_command_example(self):
        """
        destroy_workspace_command request example
        """
        try:
            print('\ndestroy_workspace_command() result:')

            # begin-destroy_workspace_command

            response = schematics_service.destroy_workspace_command(
                refresh_token='testString',
                w_id='testString',
            )
            workspace_activity_destroy_result = response.get_result()

            print(json.dumps(workspace_activity_destroy_result, indent=2))

            # end-destroy_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_plan_workspace_command_example(self):
        """
        plan_workspace_command request example
        """
        try:
            print('\nplan_workspace_command() result:')

            # begin-plan_workspace_command

            response = schematics_service.plan_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_plan_result = response.get_result()

            print(json.dumps(workspace_activity_plan_result, indent=2))

            # end-plan_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_refresh_workspace_command_example(self):
        """
        refresh_workspace_command request example
        """
        try:
            print('\nrefresh_workspace_command() result:')

            # begin-refresh_workspace_command

            response = schematics_service.refresh_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_refresh_result = response.get_result()

            print(json.dumps(workspace_activity_refresh_result, indent=2))

            # end-refresh_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_jobs_example(self):
        """
        list_jobs request example
        """
        try:
            print('\nlist_jobs() result:')

            # begin-list_jobs

            response = schematics_service.list_jobs()
            job_list = response.get_result()

            print(json.dumps(job_list, indent=2))

            # end-list_jobs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_job_example(self):
        """
        create_job request example
        """
        try:
            print('\ncreate_job() result:')

            # begin-create_job

            response = schematics_service.create_job(
                refresh_token='testString',
                command_object='action',
                command_object_id='us-east.ACTION.Example-12a1b212.3287dc42',
                command_name='ansible_playbook_run',
                command_parameter='site.yml',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-create_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_example(self):
        """
        get_job request example
        """
        try:
            print('\nget_job() result:')

            # begin-get_job

            response = schematics_service.get_job(
                job_id='testString',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-get_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_job_example(self):
        """
        update_job request example
        """
        try:
            print('\nupdate_job() result:')

            # begin-update_job

            response = schematics_service.update_job(
                job_id='testString',
                refresh_token='testString',
                command_object='action',
                command_object_id='us-east.ACTION.Example-12a1b212.3287dc42',
                command_name='ansible_playbook_run',
                command_parameter='site.yml',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-update_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_job_logs_example(self):
        """
        list_job_logs request example
        """
        try:
            print('\nlist_job_logs() result:')

            # begin-list_job_logs

            response = schematics_service.list_job_logs(
                job_id='testString',
            )
            job_log = response.get_result()

            print(json.dumps(job_log, indent=2))

            # end-list_job_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_files_example(self):
        """
        get_job_files request example
        """
        try:
            print('\nget_job_files() result:')

            # begin-get_job_files

            response = schematics_service.get_job_files(
                job_id='testString',
                file_type='template_repo',
            )
            job_file_data = response.get_result()

            print(json.dumps(job_file_data, indent=2))

            # end-get_job_files

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_workspace_deletion_job_example(self):
        """
        create_workspace_deletion_job request example
        """
        try:
            print('\ncreate_workspace_deletion_job() result:')

            # begin-create_workspace_deletion_job

            response = schematics_service.create_workspace_deletion_job(
                refresh_token='testString',
                job='delete',
                workspaces=['us-south.workspace.testWorkspace.a6010c37', 'us-south.workspace.teraformNewupdatedone.72011986', 'us-south.workspace.readterraform.400b427c', 'us-south.workspace.myworkspacesink.49745827', 'us-south.workspace.ReadTerraformTemp.c98c9774', 'us-south.workspace.SampleTest1.2a51c3a1'],
            )
            workspace_bulk_delete_response = response.get_result()

            print(json.dumps(workspace_bulk_delete_response, indent=2))

            # end-create_workspace_deletion_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_deletion_job_status_example(self):
        """
        get_workspace_deletion_job_status request example
        """
        try:
            print('\nget_workspace_deletion_job_status() result:')

            # begin-get_workspace_deletion_job_status

            response = schematics_service.get_workspace_deletion_job_status(
                wj_id='testString',
            )
            workspace_job_response = response.get_result()

            print(json.dumps(workspace_job_response, indent=2))

            # end-get_workspace_deletion_job_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_inventories_example(self):
        """
        list_inventories request example
        """
        try:
            print('\nlist_inventories() result:')

            # begin-list_inventories

            response = schematics_service.list_inventories()
            inventory_resource_record_list = response.get_result()

            print(json.dumps(inventory_resource_record_list, indent=2))

            # end-list_inventories

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_inventory_example(self):
        """
        create_inventory request example
        """
        try:
            print('\ncreate_inventory() result:')

            # begin-create_inventory

            response = schematics_service.create_inventory(
                name='dev-inventoryapidocexample',
                description='My cloud linux inventory',
                location='us-east',
                resource_group='Default',
                inventories_ini='[windows]\n158.177.7.181',
            )
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-create_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_inventory_example(self):
        """
        get_inventory request example
        """
        try:
            print('\nget_inventory() result:')

            # begin-get_inventory

            response = schematics_service.get_inventory(
                inventory_id='testString',
            )
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-get_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_inventory_example(self):
        """
        replace_inventory request example
        """
        try:
            print('\nreplace_inventory() result:')

            # begin-replace_inventory

            credential_variable_metadata_model = {
            }

            credential_variable_data_model = {
                'metadata': credential_variable_metadata_model,
            }

            host_model = {
                'name': '158.177.7.182',
                'credential': credential_variable_data_model,
            }

            group_model = {
                'name': 'windows',
                'credentials': credential_variable_data_model,
                'hosts': [host_model],
            }

            inventory_view_model = {
                'groups': [group_model],
            }

            response = schematics_service.replace_inventory(
                inventory_id='testString',
                name='dev-inventoryapidocexample',
                description='My cloud linux inventory',
                location='us-east',
                resource_group='Default',
                connection_type='ssh',
                inventories_ini='[windows]\n158.177.7.182',
                inventory_view=inventory_view_model,
            )
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-replace_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_query_example(self):
        """
        list_resource_query request example
        """
        try:
            print('\nlist_resource_query() result:')

            # begin-list_resource_query

            response = schematics_service.list_resource_query()
            resource_query_record_list = response.get_result()

            print(json.dumps(resource_query_record_list, indent=2))

            # end-list_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_query_example(self):
        """
        create_resource_query request example
        """
        try:
            print('\ncreate_resource_query() result:')

            # begin-create_resource_query

            resource_query_param_model = {
                'name': 'workspace-id',
                'value': 'us-east.ACTION.kubectlWorkshop.1010101',
                'description': 'string',
            }

            resource_query_model = {
                'query_type': 'workspaces',
                'query_condition': [resource_query_param_model],
            }

            response = schematics_service.create_resource_query(
                type='workspace_resource',
                name='hello',
                queries=[resource_query_model],
            )
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-create_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resources_query_example(self):
        """
        get_resources_query request example
        """
        try:
            print('\nget_resources_query() result:')

            # begin-get_resources_query

            response = schematics_service.get_resources_query(
                query_id='testString',
            )
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-get_resources_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_execute_resource_query_example(self):
        """
        execute_resource_query request example
        """
        try:
            print('\nexecute_resource_query() result:')

            # begin-execute_resource_query

            response = schematics_service.execute_resource_query(
                query_id='testString',
            )
            resource_query_response_record = response.get_result()

            print(json.dumps(resource_query_response_record, indent=2))

            # end-execute_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_resources_query_example(self):
        """
        replace_resources_query request example
        """
        try:
            print('\nreplace_resources_query() result:')

            # begin-replace_resources_query

            resource_query_param_model = {
                'name': 'workspace-id',
                'value': 'us-east.ACTION.kubectlWorkshop.1010101',
                'description': 'string',
            }

            resource_query_model = {
                'query_type': 'workspaces',
                'query_condition': [resource_query_param_model],
            }

            response = schematics_service.replace_resources_query(
                query_id='testString',
                type='workspace_resource',
                name='hello my world',
                queries=[resource_query_model],
            )
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-replace_resources_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_agent_data_example(self):
        """
        list_agent_data request example
        """
        try:
            print('\nlist_agent_data() result:')

            # begin-list_agent_data

            response = schematics_service.list_agent_data()
            agent_data_list = response.get_result()

            print(json.dumps(agent_data_list, indent=2))

            # end-list_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_agent_data_example(self):
        """
        create_agent_data request example
        """
        try:
            print('\ncreate_agent_data() result:')

            # begin-create_agent_data

            agent_infrastructure_model = {
                'infra_type': 'ibm_kubernetes',
                'cluster_id': 'cluster_id',
                'cluster_resource_group': 'Default',
                'cos_instance_name': 'blueprint_basic',
                'cos_bucket_name': 'sample_bucket_name',
                'cos_bucket_region': 'us-east',
            }

            variable_metadata_model = {
                'secure': True,
            }

            variable_data_model = {
                'name': 'ibmcloud_api_key',
                'value': '<api_key of the account where cluster and cos are present>',
                'metadata': variable_metadata_model,
            }

            agent_user_state_model = {
                'state': 'enable',
            }

            response = schematics_service.create_agent_data(
                name='AgentName',
                resource_group='Default',
                version='v1.0.0',
                schematics_location='us-south',
                agent_location='us-south',
                agent_infrastructure=agent_infrastructure_model,
                description='Create Agent',
                tags=['tag1', 'tag2'],
                agent_inputs=[variable_data_model],
                user_state=agent_user_state_model,
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-create_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_agent_data_example(self):
        """
        get_agent_data request example
        """
        try:
            print('\nget_agent_data() result:')

            # begin-get_agent_data

            response = schematics_service.get_agent_data(
                agent_id='testString',
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-get_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_agent_data_example(self):
        """
        update_agent_data request example
        """
        try:
            print('\nupdate_agent_data() result:')

            # begin-update_agent_data

            agent_infrastructure_model = {
                'infra_type': 'ibm_kubernetes',
                'cluster_id': 'cluster_id',
                'cluster_resource_group': 'Default',
                'cos_instance_name': 'blueprint_basic',
                'cos_bucket_name': 'sample_bucket_name',
                'cos_bucket_region': 'us-east',
            }

            variable_metadata_model = {
                'secure': True,
            }

            variable_data_model = {
                'name': 'ibmcloud_api_key',
                'value': '<api_key of the account where cluster and cos are present>',
                'metadata': variable_metadata_model,
            }

            agent_user_state_model = {
                'state': 'enable',
            }

            response = schematics_service.update_agent_data(
                agent_id='testString',
                name='AgentName',
                resource_group='Default',
                version='v1.0.0',
                schematics_location='us-south',
                agent_location='us-south',
                agent_infrastructure=agent_infrastructure_model,
                description='New Description',
                tags=['tag1', 'tag2'],
                agent_inputs=[variable_data_model],
                user_state=agent_user_state_model,
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-update_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_agent_versions_example(self):
        """
        get_agent_versions request example
        """
        try:
            print('\nget_agent_versions() result:')

            # begin-get_agent_versions

            response = schematics_service.get_agent_versions()
            agent_versions = response.get_result()

            print(json.dumps(agent_versions, indent=2))

            # end-get_agent_versions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_prs_agent_job_example(self):
        """
        prs_agent_job request example
        """
        try:
            print('\nprs_agent_job() result:')

            # begin-prs_agent_job

            response = schematics_service.prs_agent_job(
                agent_id='testString',
            )
            agent_prs_job = response.get_result()

            print(json.dumps(agent_prs_job, indent=2))

            # end-prs_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_health_check_agent_job_example(self):
        """
        health_check_agent_job request example
        """
        try:
            print('\nhealth_check_agent_job() result:')

            # begin-health_check_agent_job

            response = schematics_service.health_check_agent_job(
                agent_id='testString',
            )
            agent_health_job = response.get_result()

            print(json.dumps(agent_health_job, indent=2))

            # end-health_check_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_deploy_agent_job_example(self):
        """
        deploy_agent_job request example
        """
        try:
            print('\ndeploy_agent_job() result:')

            # begin-deploy_agent_job

            response = schematics_service.deploy_agent_job(
                agent_id='testString',
            )
            agent_deploy_job = response.get_result()

            print(json.dumps(agent_deploy_job, indent=2))

            # end-deploy_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_kms_settings_example(self):
        """
        get_kms_settings request example
        """
        try:
            print('\nget_kms_settings() result:')

            # begin-get_kms_settings

            response = schematics_service.get_kms_settings(
                location='testString',
            )
            kms_settings = response.get_result()

            print(json.dumps(kms_settings, indent=2))

            # end-get_kms_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_kms_settings_example(self):
        """
        update_kms_settings request example
        """
        try:
            print('\nupdate_kms_settings() result:')

            # begin-update_kms_settings

            kms_settings_primary_crk_model = {
                'kms_name': 'Key Protect-xxx',
                'kms_private_endpoint': 'https://private.us-south.kms.cloud.ibm.com',
                'key_crn': 'crn:v1:public:kms:us-south:a/010101010:key:3a14ceaf-c679-455d-10101010',
            }

            response = schematics_service.update_kms_settings(
                location='US',
                encryption_scheme='byok',
                resource_group='Default',
                primary_crk=kms_settings_primary_crk_model,
            )
            kms_settings = response.get_result()

            print(json.dumps(kms_settings, indent=2))

            # end-update_kms_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_kms_example(self):
        """
        list_kms request example
        """
        try:
            print('\nlist_kms() result:')

            # begin-list_kms

            response = schematics_service.list_kms(
                encryption_scheme='testString',
                location='testString',
            )
            kms_discovery = response.get_result()

            print(json.dumps(kms_discovery, indent=2))

            # end-list_kms

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policy_example(self):
        """
        list_policy request example
        """
        try:
            print('\nlist_policy() result:')

            # begin-list_policy

            response = schematics_service.list_policy()
            policy_list = response.get_result()

            print(json.dumps(policy_list, indent=2))

            # end-list_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_policy_example(self):
        """
        create_policy request example
        """
        try:
            print('\ncreate_policy() result:')

            # begin-create_policy

            response = schematics_service.create_policy(
                kind='agent_assignment_policy',
                name='new-policy-dev',
                description='Policy for job execution of secured workspaces on agent1',
                resource_group='Default',
                tags=['policy:secured-job'],
                location='us-south',
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-create_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            print('\nget_policy() result:')

            # begin-get_policy

            response = schematics_service.get_policy(
                policy_id='testString',
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-get_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_example(self):
        """
        update_policy request example
        """
        try:
            print('\nupdate_policy() result:')

            # begin-update_policy

            response = schematics_service.update_policy(
                policy_id='testString',
                kind='agent_assignment_policy',
                name='new-policy-dev',
                description='Policy for job execution of secured workspaces on agent1 updated',
                resource_group='Default',
                tags=['policy:secured-job'],
                location='us-south',
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-update_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_workspace_example(self):
        """
        delete_workspace request example
        """
        try:
            print('\ndelete_workspace() result:')

            # begin-delete_workspace

            response = schematics_service.delete_workspace(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_delete_response = response.get_result()

            print(json.dumps(workspace_delete_response, indent=2))

            # end-delete_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_action_example(self):
        """
        delete_action request example
        """
        try:
            # begin-delete_action

            response = schematics_service.delete_action(
                action_id='testString',
            )

            # end-delete_action
            print('\ndelete_action() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_workspace_activity_example(self):
        """
        delete_workspace_activity request example
        """
        try:
            print('\ndelete_workspace_activity() result:')

            # begin-delete_workspace_activity

            response = schematics_service.delete_workspace_activity(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity_apply_result = response.get_result()

            print(json.dumps(workspace_activity_apply_result, indent=2))

            # end-delete_workspace_activity

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_job_example(self):
        """
        delete_job request example
        """
        try:
            # begin-delete_job

            response = schematics_service.delete_job(
                job_id='testString',
                refresh_token='testString',
            )

            # end-delete_job
            print('\ndelete_job() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_inventory_example(self):
        """
        delete_inventory request example
        """
        try:
            # begin-delete_inventory

            response = schematics_service.delete_inventory(
                inventory_id='testString',
            )

            # end-delete_inventory
            print('\ndelete_inventory() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resources_query_example(self):
        """
        delete_resources_query request example
        """
        try:
            # begin-delete_resources_query

            response = schematics_service.delete_resources_query(
                query_id='testString',
            )

            # end-delete_resources_query
            print('\ndelete_resources_query() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_agent_data_example(self):
        """
        delete_agent_data request example
        """
        try:
            # begin-delete_agent_data

            response = schematics_service.delete_agent_data(
                agent_id='testString',
            )

            # end-delete_agent_data
            print('\ndelete_agent_data() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_agent_resources_example(self):
        """
        delete_agent_resources request example
        """
        try:
            print('\ndelete_agent_resources() result:')

            # begin-delete_agent_resources

            response = schematics_service.delete_agent_resources(
                agent_id='testString',
                refresh_token='testString',
            )
            delete_agent_resources202_response = response.get_result()

            print(json.dumps(delete_agent_resources202_response, indent=2))

            # end-delete_agent_resources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_policy_example(self):
        """
        delete_policy request example
        """
        try:
            # begin-delete_policy

            response = schematics_service.delete_policy(
                policy_id='testString',
            )

            # end-delete_policy
            print('\ndelete_policy() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SchematicsV1
##############################################################################
