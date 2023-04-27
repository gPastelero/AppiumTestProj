<h1>Appium Test Project</h1>
<hr>
<h3>This project is just a small demonstration of code that runs two tests on a test apk by Code2Lead.
All in a POM format, along with reports and screenshots.
<br><br>
The desired capabilities may be changed to suit your machine's needs, or to change the port the driver runs on. By default, it is
4723. This can be found in AppiumFramework/base/DriverClass.py</h3>
<hr>
<h1>Requirements</h1>
<hr>
<p>All requirements are in the resources folder.<br>Testing was done on an Android 13 Pixel 3a XL virtual machine using Android Studio,
along with Appium Server.
<br>Python packages required:</p>
<ul>
    <li>selenium</li>
    <li>pytest</li>
    <li>pytest-ordering</li>
    <li>allure-pytest</li>
</ul>
<hr>
<h1>Usage</h1>
<hr>
<p>To use, navigate to this folder's root directory and run the following commands:</p>
<ul>
  <li>py.test -v -s .\AppiumFramework\tests\TestSuite.py --alluredir='AppiumFramework/reports/allurereports'
  <br>This is used to run the tests.</li>
  <li>allure serve AppiumFramework\reports\allurereports
  <br>This is used to open the allure reports page on your browser.</li>
</ul>
