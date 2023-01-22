pytest -v -m"regression" -capture=tee-sys --alluredir="C:\Users\nagav\PycharmProjects\pythonHybridFW\AllureReports\reports" TestCases\ --browser chrome

REM pytest -v -m"sanity" -capture=tee-sys --alluredir="C:\Users\nagav\PycharmProjects\pythonHybridFW\AllureReports\reports1" TestCases\ --browser chrome
REM pytest -v -m"sanity or regression" -capture=tee-sys --alluredir="C:\Users\nagav\PycharmProjects\pythonHybridFW\AllureReports\reports1" TestCases\ --browser chrome