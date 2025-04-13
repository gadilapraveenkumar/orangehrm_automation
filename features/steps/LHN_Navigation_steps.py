import time

from behave import then
from pages.lhn_name_list import LHN_name_list

@then('Get The all LHN Menu "{testcase}"')
def get_lhn_details(context, testcase):
    context.lhn_list = LHN_name_list(context.browser)
    time.sleep(5)
    lhn_list = context.lhn_list.get_all_lhn_menu_list(testcase)
    context.tc_lhn_list = {testcase: lhn_list}
    print(context.tc_lhn_list)
