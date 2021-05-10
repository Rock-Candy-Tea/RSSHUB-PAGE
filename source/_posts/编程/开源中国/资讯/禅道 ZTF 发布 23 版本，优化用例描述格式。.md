
---
title: '禅道 ZTF 发布 2.3 版本，优化用例描述格式。'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ztf.im/file.php?f=202004/f_0d3a6224560588af327855ffdc3df276&t=png&o=&s=&v=1576227565'
author: 开源中国
comments: false
date: Mon, 10 May 2021 14:48:00 GMT
thumbnail: 'https://ztf.im/file.php?f=202004/f_0d3a6224560588af327855ffdc3df276&t=png&o=&s=&v=1576227565'
---

<div>   
<div class="content">
                                                                    
                                                        <p>2019年11月发布2.0版本之后，ZTF受到了禅道新老用户以及自动化测试人员的广泛关注。近年来，持续集成和DevOps在行业中的运用越发广泛，二者在缩短测试周期、提高测试效率和产品发布质量方面，起到了日益重要的作用。</p> 
<p>为了更好地服务于用户，我们在2.2版本中，支持了单元、自动化测试有关框架和工具；这次发布2.3版本，主要优化了用例描述的格式，修复了一些小的问题。</p> 
<p>ZTF支持与禅道无缝集成，可将禅道用例和测试脚本进行同步，执行结果可自动提交到禅道并生成测试报告，执行失败的用例可通过命令在禅道中创建Bug。ZTF自动化测试框架实现了与Jenkins持续集成功能的打通。用户发起Jenkins构建后，通过ZTF调度执行测试脚本，结束后把单元和功能测试的结果回传给禅道，二者合作打通了持续集成的闭环。</p> 
<p>欢迎大家下载试用，并提出宝贵建议。</p> 
<h4>一、2.3版本更新记录：</h4> 
<ol> 
 <li>更好支持主流的AutoIT、Selenium、Appium、RobotFramework和Cypress自动化测试工具，轻松完成自动化测试执行调度，并将结果和缺陷提交到禅道；</li> 
 <li>支持 JUnit, TestNG, PHPUnit, PyTest, Jest, CppUnit, GTest, QTest 8种单元测试框架，ZTF执行单元测试、解析测试输出、提交到禅道生成测试报告和缺陷；</li> 
 <li>优化用例描述格式，用户编写测试用例的步骤和期待结果时更为方便；</li> 
 <li>新增expect命令，用于执行测试、生成独立的测试结果.exp文件；</li> 
 <li>修复了一些小的问题。</li> 
</ol> 
<h4>二、下载地址：</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.3%2Fwin64%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-win64-2.3.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.3%2Fwin32%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-win32-2.3.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.3%2Flinux%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-linux-2.3.tar.gz</span></a></li> 
 <li><span style="background-color:#ffffff"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.3%2Fmac%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-mac-2.3.zip</span></a></span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf%2Farchive%2F2.3.zip" target="_blank"><span style="color:#337fe5">项目源代码(zip)</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf" target="_blank"><span style="color:#337fe5">GitHub项目首页</span></a></li> 
</ul> 
<h4>三、帮助文档</h4> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Frun-in-jenkins-task-45.html" target="_blank"><span style="color:#337fe5">Jenkins持续集成文档</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fautoit-43.html" target="_blank"><span style="color:#337fe5">自动化测试文档</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fjunit-33.html" target="_blank"><span style="color:#337fe5">单元测试文档</span></a></li> 
</ol> 
<h4>四、界面展示</h4> 
<p><strong>Jenkins集成配置：</strong></p> 
<p><img alt src="https://ztf.im/file.php?f=202004/f_0d3a6224560588af327855ffdc3df276&t=png&o=&s=&v=1576227565" referrerpolicy="no-referrer"></p> 
<p>注：第1-4行，根据禅道传过来的参数，签出对应tag或revision的代码。具体请参考<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2Fbook%2Fzentaopmshelp%2F393.html" target="_blank">禅道集成版本库和Jenkins进行构建</a></u>；第5行，为使用ZTF执行JUnit单元测试的样例，更多测试框架的调用方法，请参考<u><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.ztesting.net%2Fbook%2Fztf-doc%2Fautoit-43.html" target="_blank">本手册5.9 - 5.10小节</a></u>。</p> 
<p><strong>Jenkins自动化测试结果：</strong></p> 
<p><img alt src="https://ztf.im/file.php?f=202004/f_099aa6f600dc93d55f7af4429ac91d11&t=png&o=&s=&v=1576227565" referrerpolicy="no-referrer"></p> 
<p><strong>禅道自动化测试报告展示：</strong><img alt src="https://ztf.im/file.php?f=202004/f_b8992ab0da2179c6c76ab1151899d75c&t=png&o=&s=&v=1576227565" referrerpolicy="no-referrer"></p> 
<p><strong><strong>支持</strong><span style="background-color:#ffffff; color:#24292e">AutoIT、Selenium、Appium、RobotFramework和Cypress</span>自动化测试，内嵌PHP运行时和Selenium Driver。</strong><strong>相关代码可参考demo目录和</strong><a href="https://gitee.com/organizations/ngtesting/projects" target="_blank"><span style="color:#337fe5">这里</span></a><strong>。</strong></p> 
<p><img alt src="https://ztf.im/file.php?f=202004/f_7244187ccc0027a1c2f3de0cc950046f&t=png&o=&s=&v=1576227565" referrerpolicy="no-referrer"></p> 
<p><strong>Selenium自动化测试样例：</strong></p> 
<pre>#!/usr/bin/env php
<?php
/**

title=use ztf to run selenium test
cid=0
pid=0

1. check webpage title >> 禅道_百度搜索

*/

namespace Facebook\WebDriver;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Chrome\ChromeOptions;
include 'vendor/autoload.php';

// launch build-in selenium driver to test
if (isWindows())
&#123;
$command = 'start ' . dirname(__FILE__, 3) . '\runtime\selenium\chrome80.exe >log.txt 2>&1';
    //exec("CHCP 936");
&#125; else // for no-windows system, pls download chrome driver from https://chromedriver.storage.googleapis.com/index.html
&#123;
    $command = 'nohup ' . dirname(__FILE__, 3) . '/runtime/selenium/chrome80 >log.txt 2>&1 &';
&#125;
pclose(popen($command, 'r'));


$host = 'http://127.0.0.1:9515';

$options = new ChromeOptions();
$options->addArguments(['--no-sandbox']); // ['--headless', '--no-sandbox']
$desiredCapabilities = DesiredCapabilities::chrome();
$desiredCapabilities->setCapability(ChromeOptions::CAPABILITY, $options);

$driver = RemoteWebDriver::create($host, $desiredCapabilities);
$driver->get("https://www.baidu.com");
$html= $driver->getPageSource();
// print_r("$html \n");

$keywordsInput = $driver->findElement(WebDriverBy::id('kw'));
$keywordsInput->clear();
$keywordsInput->sendKeys("禅道");

$submitButton = $driver->findElement(WebDriverBy::id('su'));
$submitButton->click();

$driver-> wait(10, 500)-> until(WebDriverExpectedCondition::titleContains('禅道'));

$title = $driver->getTitle();
//if (isWindows()) $title = iconv("UTF-8","GB2312", $title);
print("$title\n");

$driver->close();

if (isWindows())
&#123;
    exec('taskkill /F /im chrome80.exe');
&#125; else
&#123;
    exec('ps -ef | grep chrome80 | grep -v grep | xargs kill -9 2>/dev/null');
&#125;

function  isWindows()
&#123;
    return strtoupper(substr(PHP_OS, 0, 3)) === 'WIN';
&#125;
</pre>
                                        </div>
                                      
</div>
            