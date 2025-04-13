from behave import then
from pandas.core.common import not_none

from environment import take_screenshot
from pages.navigate_each_page import Navigation


@then('Navigate to Each Page "{testcase}"')
def navigate_each_page_fun(context,testcase):
    page_name_list = context.tc_lhn_list[testcase]
    print(page_name_list)
    for page_name in page_name_list:
        navigation = Navigation(context.browser)
        if "Maintenance"!=page_name:
            status = navigation.navigate_each_page(str(page_name))
            take_screenshot(context)