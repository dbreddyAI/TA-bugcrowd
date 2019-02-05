import ta_bugcrowd_declare

import os
import sys
import time
import datetime
import json

import modinput_wrapper.base_modinput
from solnlib.packages.splunklib import modularinput as smi



import input_module_bugcrowd_api as input_module

bin_dir = os.path.basename(__file__)

'''
    Do not edit this file!!!
    This file is generated by Add-on builder automatically.
    Add your modular input logic to file input_module_bugcrowd_api.py
'''
class ModInputbugcrowd_api(modinput_wrapper.base_modinput.BaseModInput):

    def __init__(self):
        if 'use_single_instance_mode' in dir(input_module):
            use_single_instance = input_module.use_single_instance_mode()
        else:
            use_single_instance = False
        super(ModInputbugcrowd_api, self).__init__("ta_bugcrowd", "bugcrowd_api", use_single_instance)
        self.global_checkbox_fields = None

    def get_scheme(self):
        """overloaded splunklib modularinput method"""
        scheme = super(ModInputbugcrowd_api, self).get_scheme()
        scheme.title = ("Bugcrowd API")
        scheme.description = ("Go to the add-on\'s configuration UI and configure modular inputs under the Inputs menu.")
        scheme.use_external_validation = True
        scheme.streaming_mode_xml = True

        scheme.add_argument(smi.Argument("name", title="Name",
                                         description="",
                                         required_on_create=True))

        """
        For customized inputs, hard code the arguments here to hide argument detail from users.
        For other input types, arguments should be get from input_module. Defining new input types could be easier.
        """
        scheme.add_argument(smi.Argument("api_key", title="API Key",
                                         description="Your HTTP Authorization Header. E.g. abcdefg:AB1cdef2G-A3bc3deFG_AB_CDe-fg",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("starting_from", title="Pull submissions starting from",
                                         description="New submissions to your programs will have state \"new\". This includes duplicates and non-applicable. Usually only submissions validated by Bugcrowd staff and set to state \"triaged\" are relevant to you",
                                         required_on_create=True,
                                         required_on_edit=False))
        scheme.add_argument(smi.Argument("track_states", title="Track submission state",
                                         description="Whether or not to create a new Splunk event if a submission\'s state is changed on the CrowdControl platform",
                                         required_on_create=True,
                                         required_on_edit=False))
        return scheme

    def get_app_name(self):
        return "TA-bugcrowd"

    def validate_input(self, definition):
        """validate the input stanza"""
        input_module.validate_input(self, definition)

    def collect_events(self, ew):
        """write out the events"""
        input_module.collect_events(self, ew)

    def get_account_fields(self):
        account_fields = []
        return account_fields

    def get_checkbox_fields(self):
        checkbox_fields = []
        return checkbox_fields

    def get_global_checkbox_fields(self):
        if self.global_checkbox_fields is None:
            checkbox_name_file = os.path.join(bin_dir, 'global_checkbox_param.json')
            try:
                if os.path.isfile(checkbox_name_file):
                    with open(checkbox_name_file, 'r') as fp:
                        self.global_checkbox_fields = json.load(fp)
                else:
                    self.global_checkbox_fields = []
            except Exception as e:
                self.log_error('Get exception when loading global checkbox parameter names. ' + str(e))
                self.global_checkbox_fields = []
        return self.global_checkbox_fields

if __name__ == "__main__":
    exitcode = ModInputbugcrowd_api().run(sys.argv)
    sys.exit(exitcode)