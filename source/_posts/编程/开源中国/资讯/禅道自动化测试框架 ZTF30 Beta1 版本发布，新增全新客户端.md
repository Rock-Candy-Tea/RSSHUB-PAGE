
---
title: '禅道自动化测试框架 ZTF3.0 Beta1 版本发布，新增全新客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ztf.im/file.php?f=202206/f_d624084bb79d08099d2cd28ca8680639&t=png&o=&s=&v=1632294574'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 14:24:00 GMT
thumbnail: 'https://ztf.im/file.php?f=202206/f_d624084bb79d08099d2cd28ca8680639&t=png&o=&s=&v=1632294574'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start">大家好，禅道自动化测试框架ZTF的3.0 Beta版发布。新版本增加了一个全新的客户端，命令行也依然可用。</p> 
<p style="text-align:start">ZTF是禅道团队自研的开源自动化测试框架，与禅道无缝集成，可将禅道用例和测试脚本进行同步，将执行结果自动提交到禅道并生成测试报告，执行失败的用例可通过命令在禅道中创建Bug。</p> 
<p style="text-align:start">ZTF命令行工具可以配合Jenkins、GitLab CI等持续集成工具使用。在流水线中，可以调用ZTF执行测试脚本，执行结束后，<span>ZTF负责</span>把单元或自动化测试的结果回传给禅道。二者合作打通了持续测试的一个闭环。</p> 
<div> 
 <p>欢迎大家下载使用，并提出宝贵建议。<span style="color:#337fe5"><span style="color:#e53333">由于使用了禅道的新版Rest API，请配合</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2Fdownload%2Fzentaopms16.0-80448.html" target="_blank"><span style="color:#337fe5">禅道16.0</span></a><span style="color:#e53333">及以后版本使用。</span></span></p> 
 <h3>一、更新记录</h3> 
 <ol> 
  <li>新增客户端工具；</li> 
  <li>使用禅道新版REST API接口；</li> 
  <li>修复了一些遗留的问题。</li> 
 </ol> 
 <h3>二、客户端下载地址</h3> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fwin64%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-win64-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fwin32%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-win32-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Flinux%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-linux-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fdarwin%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-mac-3.0_beta1.zip</span></a></li> 
 </ul> 
 <h3>二、命令行工具下载地址</h3> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fwin64%2Fztf-cmd.zip" target="_blank"><span style="color:#337fe5">ztf-win64-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fwin32%2Fztf-cmd.zip" target="_blank"><span style="color:#337fe5">ztf-win32-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Flinux%2Fztf-cmd.zip" target="_blank"><span style="color:#337fe5">ztf-linux-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.0.0_beta1%2Fdarwin%2Fztf-cmd.zip" target="_blank"><span style="color:#337fe5">ztf-mac-3.0_beta1.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf" target="_blank"><span style="color:#337fe5">开源项目代码</span></a></li> 
 </ul> 
 <ul> 
 </ul> 
 <h3>四、帮助文档</h3> 
 <ol> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Frun-in-jenkins-task-45.html" target="_blank"><span style="color:#337fe5">Jenkins持续集成文档</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fautoit-43.html" target="_blank"><span style="color:#337fe5">自动化测试文档</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fjunit-33.html" target="_blank"><span style="color:#337fe5">单元测试文档</span></a></li> 
 </ol> 
 <h3>五、优化功能展示</h3> 
 <p style="color:#333333"><strong>客户端查看和执行脚本</strong></p> 
 <p style="color:#333333"><img alt src="https://ztf.im/file.php?f=202206/f_d624084bb79d08099d2cd28ca8680639&t=png&o=&s=&v=1632294574" referrerpolicy="no-referrer"></p> 
 <p><strong>客户端查看测试结果</strong></p> 
 <p><img alt src="https://ztf.im/file.php?f=202206/f_29a44b3ab4ed5cce7126a0e912296ff1&t=png&o=&s=&v=1632294574" referrerpolicy="no-referrer"></p> 
 <h3><span style="color:#24292e">六、ZTF功能简介</span></h3> 
 <div> 
  <p>ZTF使用Go语言开发，真正做到了平台无依赖、部署无依赖，只需要一个可执行文件就可以运行，可以解决用例信息管理、测试脚本执行、测试结果比对、缺陷Bug提交等问题。</p> 
  <p><img alt src="https://ztf.im/file.php?f=202106/f_a1656bc6e7755e7574d088f1ce35220b&t=jpg&o=&s=&v=1623838494" referrerpolicy="no-referrer"></p> 
  <p>ZTF自动化测试框架对您现有的测试脚本资产没有侵入，可很好地驱动8种单元测试框架、5种自动化测试工具、9种脚本语言来执行测试，并把最终结果回传给禅道，进行统一的报告展示，打通项目管理和持续集成工具之间的沟壑。</p> 
  <p>相关代码可参考demo目录和<a href="https://gitee.com/organizations/ngtesting/projects" target="_blank"><span style="color:#337fe5">这里。</span></a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            