from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

class DragDropPage(BasePage):

    frame = (By.CLASS_NAME, "demo-frame")   # We are switching to iframe as page contains a frame

    source = (By.ID, "draggable")
    target = (By.ID, "droppable")

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_drag_frame(self):     # This is a method to move to frame. This will be executed first then the drag and drop will be performed

        self.switch_to_frame(self.frame)

    def perform_drag_drop(self):
        self.drag_and_drop(self.source, self.target)

# COMPLETE JOURNEY FOR DRAG AND DROP
#         pytest
#         ↓
#         open drag drop page
#         ↓
#         switch to iframe
#         ↓
#         DragDropPage(driver)
#         ↓
#         perform_drag_drop()
#         ↓
#         BasePage.drag_and_drop()
#         ↓
#         find draggable element
#         ↓
#         find droppable element
#         ↓
#         ActionChains.drag_and_drop()
#         ↓
#         drag operations happen here
#