import pytest
import time
import os
from pathlib import Path
from datetime import datetime
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from logging_config import setup_logging, get_logger
from reporting_utils import ScreenshotManager, ReportConfig

# Setup logging at module level
setup_logging()
logger = get_logger(__name__)


def pytest_configure(config):
    """
    Pytest hook: Configure HTML report generation and create reports directory
    Runs at the start of test session
    """
    # Create reports directory
    reports_dir = ScreenshotManager.create_reports_dir()
    
    # Configure HTML report path with timestamp
    report_path = ReportConfig.get_report_path()
    if hasattr(config.option, 'htmlpath'):
        config.option.htmlpath = report_path
    
    logger.info(f"Pytest HTML reporting configured")
    logger.info(f"Reports will be saved to: {reports_dir}")
    logger.info(f"HTML report path: {report_path}")


@pytest.fixture
def driver(request):
    """
    Pytest fixture that provides a Selenium WebDriver instance
    Stores the driver in request for access in hooks
    """
    logger.info("Initializing WebDriver")
    options = Options()
    options.add_argument("--headless")  # important for Docker
    driver = webdriver.Firefox(options=options)
    logger.debug(f"WebDriver initialized successfully")
    
    # Store driver reference for screenshot capture on failure
    request.driver = driver
    
    yield driver
    
    logger.info("Closing WebDriver")
    driver.quit()
    logger.debug("WebDriver closed successfully")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook: Capture screenshot on test failure and attach to HTML report
    Runs after each test case
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Capture screenshot on test failure (during call phase)
    if rep.failed and call.when == "call":
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Capture screenshot
                screenshot_path = ScreenshotManager.capture_screenshot_on_failure(
                    driver, 
                    item.name
                )
                
                if screenshot_path:
                    # Get relative path for HTML report
                    rel_path = os.path.basename(screenshot_path)
                    
                    # Attach screenshot to HTML report as extra content
                    if not hasattr(rep, 'extra'):
                        rep.extra = []
                    
                    # Add screenshot link to report
                    html_content = f'<a href="{rel_path}"><img src="{rel_path}" width="800px" style="border: 1px solid #ddd; padding: 5px;"/></a>'
                    rep.sections.append(('Screenshot on Failure', html_content))
                    
                    logger.info(f"Screenshot attached to HTML report: {rel_path}")
                
            except Exception as e:
                logger.error(f"Failed to capture screenshot for report: {str(e)}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    """
    Pytest hook: Log test execution details before and after test run
    """
    logger.info(f"{'='*70}")
    logger.info(f"Starting test: {item.name}")
    logger.info(f"Test file: {item.fspath}")
    logger.info(f"{'='*70}")
    
    start_time = datetime.now()
    outcome = yield
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds()
    
    # Log test result
    if outcome.excinfo:
        logger.error(f"Test {item.name} FAILED")
        logger.error(f"Execution time: {execution_time:.2f}s")
    else:
        logger.info(f"Test {item.name} PASSED")
        logger.info(f"Execution time: {execution_time:.2f}s")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Pytest hook: Log session summary after all tests complete
    """
    logger.info(f"{'='*70}")
    logger.info("Test Session Summary")
    logger.info(f"{'='*70}")
    
    # Get report statistics
    if hasattr(session, 'config') and hasattr(session.config.option, 'htmlpath'):
        report_path = session.config.option.htmlpath
        if os.path.exists(report_path):
            logger.info(f"HTML Report generated at: {report_path}")
    
    logger.info(f"Exit status: {exitstatus}")

