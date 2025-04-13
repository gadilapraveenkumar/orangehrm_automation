from utils.browser_manager import BrowserManager
import os
from behave.runner import Context
from behave import __version__ as behave_version
from utils.config_reader import ConfigReader

def before_all(context):
    print("before all ")

def before_scenario(context: Context, scenario):
    print(f"Starting scenario: {scenario.name}")
    config = ConfigReader()
    if config._config is None:
        print("Error: Configuration could not be loaded. Skipping browser initialization.")
        context.browser = None
        return
    try:
        context.browser = BrowserManager.get_browser()
    except Exception as e:
        print(f"Error initializing browser: {e}")
        context.browser = None

def after_scenario(context: Context, scenario):
    status = scenario.status.name
    print(f"Finished scenario: {scenario.name} - Status: {status.upper()}")
    if context.browser:
        if status == "failed":
            scenario_name = scenario.name.replace(" ", "_")
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{scenario_name}_failed.png")
            try:
                context.browser.save_screenshot(screenshot_path)
                print(f"Screenshot saved to: {screenshot_path}")
            except Exception as e:
                print(f"Error saving screenshot: {e}")
        try:
            BrowserManager.close_browser()
        except Exception as e:
            print(f"Error closing browser: {e}")
    else:
        print("Browser was not initialized, skipping browser cleanup.")

def after_all(context):
    print("All scenarios completed.")