





class Browser:
    def __init__(self, **kwargs):
        self.window_size =  kwargs['']
        self.binary_path =   kwargs['']
        self.driver_path =  kwargs['']
        self.browser_name = kwargs['']
        self.proxy =  kwargs['']         
        self.user_agent = kwargs['']                
        self.headless_mode = kwargs['']
        self.proxy_dir = kwargs['']     
        self.download_dir = kwargs['']      
        self.implicit_wait_time =

    def perform(self):
        self._manage_paths()
        self._initiate_browser()
        self._call_browser()
        self.implicit_wait()
        return self._add_2_stg()  # add this obj to settings (stg) to make it like a global variable


    def _initiate_browser(self) -> None:
        inputs = {"binary_path": self.binary_path,
                  "driver_path": self.driver_path,
                  "window_size": self.window_size,
                  "browser_name": self.browser_name,
                  "proxy": self.proxy,
                  "extension": self.extension,
                  "user_agent": self.user_agent,
                  "headless_mode": self.headless_mode,
                  "proxy_dir": self.proxy_dir,
                  "download_dir": self.download_dir}

        if self.browser_name in ('chromium', "google-chrome"):
            self.driver = Chrome(**inputs)
        elif self.browser_name == 'firefox':
            self.driver = Firefox(**inputs)
        elif self.browser_name == 'ie':
            pass
        elif self.browser_name == 'edge':
            pass

    def implicit_wait(self) -> None:
        if self.implicit_wait_time:
            self.driver.implicitly_wait(self.implicit_wait_time)

    def _call_browser(self) -> None:
        self.driver.perform()

    def save_screen(self, address_and_name: str = None) -> None:
        original_size = self.driver.get_window_size()
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth') + 100
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight') + 100
        try:
            self.driver.set_window_size(required_width, required_height)
            # driver.save_screenshot(path)  # has scrollbar
            self.driver.find_element(by='tag name', value='body').screenshot(address_and_name)  # avoids scrollbar
            if not path.getsize(address_and_name):
                remove(address_and_name)
                self.driver.save_screenshot(address_and_name)

        except Exception:
            self.driver.save_screenshot(address_and_name)

        finally:
            self.driver.set_window_size(original_size['width'], original_size['height'])

    def save_entire_dom(self, address_and_name: str = None) -> None:
        html = self.driver.page_source
        with open(address_and_name, "w") as f:
            f.write(html)

    def __del__(self):
        self._quit_browser()

    @manage_exceptions_decorator(report_traceback=False)
    def _quit_browser(self):
        self.driver.quit()

    @manage_exceptions_decorator()
    def _add_2_stg(self):
        STG.BROWSER_OBJ = self