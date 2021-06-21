
---
title: '禅道自动化测试框架 ZTF 发布 2.4 版本，增加测试步骤自动提取功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ztf.im/file.php?f=202106/f_1f0e3be8e529e4ef329b04f3fbb6cc23&t=png&o=&s=&v=1623838494'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 13:03:00 GMT
thumbnail: 'https://ztf.im/file.php?f=202106/f_1f0e3be8e529e4ef329b04f3fbb6cc23&t=png&o=&s=&v=1623838494'
---

<div>   
<div class="content">
                                                                    
                                                        <p>大家好，禅道自动化测试框架2.4版本发布，支持在脚本的任意地方编写测试步骤和期待结果，并提供了一个extract命令用于提取这些信息。</p> 
<p>ZTF是禅道团队自研的自动化测试框架，支持与禅道无缝集成，可将禅道用例和测试脚本进行同步，将执行结果自动提交到禅道并生成测试报告，执行失败的用例可通过命令在禅道中创建Bug。ZTF自动化测试框架实现了与Jenkins持续集成功能的打通。用户发起Jenkins构建后，通过ZTF调度执行测试脚本，结束后把单元和功能测试的结果回传给禅道，二者合作打通持续集成的闭环。</p> 
<p>欢迎大家下载试用，并提出宝贵建议。</p> 
<h3>一、更新记录</h3> 
<ol> 
 <li>支持在脚本的任意地方编写测试步骤和期待结果；</li> 
 <li>新增extract命令，用于提取测试步骤和期待结果；</li> 
 <li>修复了一些小的问题。</li> 
</ol> 
<h3>二、下载地址</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.4%2Fwin64%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-win64-2.4.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.4%2Fwin32%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-win32-2.4.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.4%2Flinux%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-linux-2.4.tar.gz</span></a></li> 
 <li><span style="background-color:#ffffff"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F2.4%2Fmac%2Fztf.zip%3Fr%3D210510" target="_blank"><span style="color:#337fe5">ztf-mac-2.4.zip</span></a></span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf%2Farchive%2Frefs%2Ftags%2F2.4.zip" target="_blank"><span style="color:#337fe5">项目源代码(zip)</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaoatf" target="_blank"><span style="color:#337fe5">GitHub项目首页</span></a></li> 
</ul> 
<h3>三、帮助文档</h3> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Frun-in-jenkins-task-45.html" target="_blank"><span style="color:#337fe5">Jenkins持续集成文档</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fautoit-43.html" target="_blank"><span style="color:#337fe5">自动化测试文档</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fztf.im%2Fbook%2Fztf-doc%2Fjunit-33.html" target="_blank"><span style="color:#337fe5">单元测试文档</span></a></li> 
</ol> 
<h3>四、新功能界面展示</h3> 
<p><strong>从代码中提取测试步骤：</strong></p> 
<p>1. 示例脚本<span style="background-color:#f5f5f5; color:#666666">demo\sample\8_extract_desc.php中</span>，注释包含了测试步骤和期待结果；</p> 
<p>2. 执行以下命令，提取分散在左侧文件代码中的步骤和期待结果；</p> 
<pre>ztf.exe extract demo\sample\8_extract_desc.php</pre> 
<p><img alt src="https://ztf.im/file.php?f=202106/f_1f0e3be8e529e4ef329b04f3fbb6cc23&t=png&o=&s=&v=1623838494" referrerpolicy="no-referrer"></p> 
<p>3. 获得右侧结果文件，在顶部注释中，新增了提取的用例步骤描述。</p> 
<p>具体语法如下：</p> 
<ul> 
 <li>group:开始一个分组，以2个中括号]]结尾；</li> 
 <li>step:开始一个步骤，单行的期待结果紧跟在>>后；</li> 
 <li>步骤的期待结果为多行时，使用2组>>符号括起来;</li> 
 <li>分组和多行期待结果的子项，前面用2个空格作为缩进，以保持同先前语法的兼容。</li> 
</ul> 
<p><strong>禅道自动化测试报告展示：</strong></p> 
<p><img alt src="https://ztf.im/file.php?f=202004/f_b8992ab0da2179c6c76ab1151899d75c&t=png&o=&s=&v=1576227565" referrerpolicy="no-referrer"></p> 
<h3><strong>五、ZTF功能简介</strong></h3> 
<div>
 ZTF使用Go语言开发，真正做到了平台无依赖、部署无依赖，只需要一个可执行文件就可以运行，可以解决用例信息管理、测试脚本执行、测试结果比对、缺陷Bug提交等问题。 
 <p>ZTF自动化测试框架对您现有的测试脚本资产没有侵入，可很好地驱动8种单元测试框架、5种自动化测试工具、9种脚本语言来执行测试，并把最终结果回传给禅道，进行统一的报告展示，打通项目管理和持续集成工具之间的沟壑。</p> 
 <p><span style="color:#24292e">相关代码可参考demo目录和</span><a href="https://gitee.com/organizations/ngtesting/projects" target="_blank"><span style="color:#337fe5">这里</span></a><span style="color:#24292e">。</span></p> 欢迎大家下载试用。
</div>
                                        </div>
                                      
</div>
            