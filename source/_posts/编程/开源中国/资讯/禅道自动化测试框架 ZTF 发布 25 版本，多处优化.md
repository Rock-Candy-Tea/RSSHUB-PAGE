
---
title: '禅道自动化测试框架 ZTF 发布 2.5 版本，多处优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ztf.im/file.php?f=202112/f_e1a33158ed4d8c9dabd8c14d7974b605&t=png&o=&s=&v=1632294574'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 17:09:00 GMT
thumbnail: 'https://ztf.im/file.php?f=202112/f_e1a33158ed4d8c9dabd8c14d7974b605&t=png&o=&s=&v=1632294574'
---

<div>   
<div class="content">
                                                                                            <p><span>大家好，禅道自动化测试框架2.5版本发布，做了多处优化，并修复了一些小问题。</span><br> ZTF是禅道团队自研的自动化测试框架，支持与禅道无缝集成，可将禅道用例和测试脚本进行同步，将执行结果自动提交到禅道并生成测试报告，执行失败的用例可通过命令在禅道中创建Bug。ZTF自动化测试框架实现了与Jenkins持续集成功能的打通。用户发起Jenkins构建后，通过ZTF调度执行测试脚本，结束后把单元和功能测试的结果回传给禅道，二者合作打通持续集成的闭环。</p> 
<div> 
 <p>欢迎大家下载试用，提出您的宝贵建议。</p> 
 <h3>一、更新记录</h3> 
 <ol> 
  <li>优化了步骤和期待结果的描述格式；</li> 
  <li>设置空白的预期结果默认为"pass"；</li> 
  <li>修复禅道新版本的登录问题；</li> 
  <li>修复提交多余结果的问题；</li> 
  <li>优化控制台输出信息；</li> 
  <li>修复了一些其它的小问题。</li> 
 </ol> 
 <h3>二、下载地址</h3> 
 <ul> 
  <li><span style="color:#337fe5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.5%2Fwin64%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-win64</span><span style="color:#337fe5">-2.5.zip</span></a></span></li> 
  <li><span><span><span style="color:#337fe5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.5%2Fwin32%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-win32-2.5.zip</span></a></span></span></span></li> 
  <li><span><span style="color:#337fe5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.5%2Flinux%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-linux-2.5.zip</span></a></span></span></li> 
  <li><span style="background-color:#ffffff"><span style="color:#337fe5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.5%2Fmac%2Fztf.zip" target="_blank"><span style="color:#337fe5">ztf-mac-2.5.zip</span></a></span></span></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf" target="_blank"><span style="color:#337fe5">项目源代码</span></a></li> 
 </ul> 
 <h3>三、帮助文档</h3> 
 <ol> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Frun-in-jenkins-task-45.html" target="_blank"><span style="color:#337fe5">Jenkins持续集成文档</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fautoit-43.html" target="_blank"><span style="color:#337fe5">自动化测试文档</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fjunit-33.html" target="_blank"><span style="color:#337fe5">单元测试文档</span></a></li> 
 </ol> 
 <h3>四、优化功能展示</h3> 
 <p><strong>设置空白的预期结果默认为"pass"</strong></p> 
 <p><img alt src="https://ztf.im/file.php?f=202112/f_e1a33158ed4d8c9dabd8c14d7974b605&t=png&o=&s=&v=1632294574" referrerpolicy="no-referrer"></p> 
 <p><strong><strong>优化提取步骤和期望结果：</strong></strong></p> 
 <p><span><span><span>1. 示例脚本demo\sample\8_extract_desc.php中，注释包含了测试步骤和期待结果；</span></span></span></p> 
 <p><span><span><span>2. 执行以下命令，提取分散在左侧文件代码中的步骤和期待结果；</span></span></span></p> 
 <p> </p> 
 <pre>ztf.exe extract demo\sample\8_extract_desc.php</pre> 
 <p><strong><img alt src="https://ztf.im/file.php?f=202112/f_3d5fa0b6098ede14fd96251dbe65147f&t=png&o=&s=&v=1632294574" referrerpolicy="no-referrer"></strong></p> 
 <p>具体优化如下：</p> 
 <ul> 
  <li> 
   <div>
    支持多种注释，如“//”、“#”、“/*/”；
   </div> </li> 
  <li> <p>支持函数输入输出，单双引号皆可识别。</p> </li> 
 </ul> 
 <h3><span>五、ZTF功能简介</span></h3> 
 <div> 
  <p>ZTF使用Go语言开发，真正做到了平台无依赖、部署无依赖，只需要一个可执行文件就可以运行，可以解决用例信息管理、测试脚本执行、测试结果比对、缺陷Bug提交等问题。</p> 
  <p><img alt src="https://ztf.im/file.php?f=202106/f_a1656bc6e7755e7574d088f1ce35220b&t=jpg&o=&s=&v=1623838494" referrerpolicy="no-referrer"></p> 
  <p>ZTF自动化测试框架对您现有的测试脚本资产没有侵入，可很好地驱动8种单元测试框架、5种自动化测试工具、9种脚本语言来执行测试，并把最终结果回传给禅道，进行统一的报告展示，打通项目管理和持续集成工具之间的沟壑。</p> 
  <p><span style="color:#24292e">相关代码可参考demo目录和</span><a href="https://gitee.com/organizations/ngtesting/projects" target="_blank"><span style="color:#337fe5">这里</span></a><span style="color:#24292e">。</span></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            