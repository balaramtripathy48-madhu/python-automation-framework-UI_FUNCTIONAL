"""
Utility module for handling screenshots and HTML report generation
"""
import os
from pathlib import Path
from datetime import datetime
from logging_config import get_logger

logger = get_logger(__name__)


class ScreenshotManager:
    """Manages screenshot capture and storage for test reporting"""

    REPORTS_DIR = os.path.join(os.path.dirname(__file__), 'reports')

    @staticmethod
    def create_reports_dir():
        """Create reports directory if it doesn't exist"""
        os.makedirs(ScreenshotManager.REPORTS_DIR, exist_ok=True)
        logger.debug(f"Reports directory ensured at: {ScreenshotManager.REPORTS_DIR}")
        return ScreenshotManager.REPORTS_DIR

    @staticmethod
    def capture_screenshot(driver, screenshot_name=None):
        """
        Capture screenshot from WebDriver

        Args:
            driver: Selenium WebDriver instance
            screenshot_name: Optional custom screenshot name

        Returns:
            str: Path to captured screenshot
        """
        try:
            ScreenshotManager.create_reports_dir()

            if not screenshot_name:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
                screenshot_name = f"screenshot_{timestamp}.png"

            screenshot_path = os.path.join(ScreenshotManager.REPORTS_DIR, screenshot_name)
            driver.save_screenshot(screenshot_path)
            logger.debug(f"Screenshot captured: {screenshot_name}")

            return screenshot_path
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")
            return None

    @staticmethod
    def capture_screenshot_on_failure(driver, test_name):
        """
        Capture screenshot specifically for test failure

        Args:
            driver: Selenium WebDriver instance
            test_name: Name of the test

        Returns:
            str: Path to captured screenshot
        """
        try:
            ScreenshotManager.create_reports_dir()

            # Generate failure-specific screenshot name
            test_name_clean = test_name.replace('[', '_').replace(']', '_').replace(' ', '_')
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
            screenshot_name = f"FAILURE_{test_name_clean}_{timestamp}.png"

            screenshot_path = os.path.join(ScreenshotManager.REPORTS_DIR, screenshot_name)
            driver.save_screenshot(screenshot_path)
            logger.error(f"Failure screenshot captured: {screenshot_name}")

            return screenshot_path
        except Exception as e:
            logger.error(f"Failed to capture failure screenshot: {str(e)}")
            return None

    @staticmethod
    def get_relative_screenshot_path(screenshot_path):
        """
        Get relative path of screenshot for HTML report embedding

        Args:
            screenshot_path: Full path to screenshot

        Returns:
            str: Relative path to screenshot
        """
        try:
            return os.path.relpath(screenshot_path, ScreenshotManager.REPORTS_DIR)
        except Exception as e:
            logger.error(f"Failed to get relative path: {str(e)}")
            return screenshot_path


class ReportConfig:
    """Configuration for HTML report generation"""

    @staticmethod
    def get_report_path():
        """Get the full path where HTML report will be generated"""
        reports_dir = ScreenshotManager.create_reports_dir()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        return os.path.join(reports_dir, f'report_{timestamp}.html')

    @staticmethod
    def get_report_options():
        """
        Get pytest-html report options

        Returns:
            dict: Report generation options
        """
        return {
            'self_contained_html': True,
            'style': 'assets/style.css',
        }

