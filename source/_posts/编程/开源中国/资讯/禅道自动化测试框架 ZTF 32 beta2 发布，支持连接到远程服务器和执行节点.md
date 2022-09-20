
---
title: '禅道自动化测试框架 ZTF 3.2 beta2 发布，支持连接到远程服务器和执行节点'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ztf.im/file.php?f=202209/f_d396fd08430b0a6b9c95207e565da120&t=png&o=&s=&v=1662516436'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 15:57:00 GMT
thumbnail: 'https://ztf.im/file.php?f=202209/f_d396fd08430b0a6b9c95207e565da120&t=png&o=&s=&v=1662516436'
---

<div>   
<div class="content">
                                                                                            <p>大家好，禅道自动化测试框架ZTF 3.2 beta2发布了，新版本支持连接到远程ZTF服务器，可在远程代理节点上执行测试。</p> 
<p>ZTF是禅道团队自研的开源自动化测试框架，与禅道无缝集成，可将禅道用例和测试脚本进行同步，将执行结果自动提交到禅道并生成测试报告，执行失败的用例可通过命令在禅道中创建Bug。ZTF命令行工具可以配合Jenkins、GitLab CI等持续集成工具使用。在流水线中，可以调用ZTF执行测试脚本，执行结束后，ZTF负责把单元或自动化测试的结果回传给禅道。二者合作打通了持续测试的一个闭环。</p> 
<div> 
 <p>欢迎大家下载使用，并提出宝贵建议。<span style="color:#337fe5"><span style="color:#e53333">由于ZTF3.0开始使用了禅道的新版Rest API，请配合</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2Fdownload%2Fzentaopms17.0.beta1-80861.html" target="_blank"><span style="color:#e53333"><u>禅道17.0</u></span></a><span style="color:#337fe5"><span style="color:#e53333">及以后版本使用。</span></span>如需兼容此前版本的禅道，可以在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2Fextension-viewExt-186.html" target="_blank"><span style="color:#337fe5">这里</span></a>下载安装禅道插件。</p> 
 <h3>一、更新记录</h3> 
 <ol> 
  <li><span>支持切换到远程ZTF服务器</span>；</li> 
  <li>支持在远程代理节点上执行测试；</li> 
  <li>优化客户端界面，修复了一些遗留问题。</li> 
 </ol> 
 <h3>二、客户端下载地址</h3> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.2.0%2Fwin64%2Fztf.zip%3Ftm%3D1658472162" target="_blank"><span style="color:#337fe5">ztf-win64-3.2.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.2.0%2Fwin32%2Fztf.zip%3Ftm%3D1658472162" target="_blank"><span style="color:#337fe5">ztf-win32-3.2.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.2.0%2Flinux%2Fztf.zip%3Ftm%3D1658472162" target="_blank"><span style="color:#337fe5">ztf-linux-3.2.zip</span></a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fztf%2F3.2.0%2Fdarwin%2Fztf.zip%3Ftm%3D1658472162" target="_blank"><span style="color:#337fe5">ztf-mac-3.2.zip</span></a></li> 
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
 <p><strong>客户端配置多个服务器及执行节点</strong><img alt src="https://ztf.im/file.php?f=202209/f_d396fd08430b0a6b9c95207e565da120&t=png&o=&s=&v=1662516436" referrerpolicy="no-referrer"></p> 
 <p><strong>客户端查看和执行脚本</strong></p> 
 <img alt src="https://ztf.im/file.php?f=202209/f_666daeff0de63087c6dcaffee4a58f11&t=png&o=&s=&v=1662516436" referrerpolicy="no-referrer"> 
 <p><strong>客户端查看测试结果</strong></p> 
 <p><img alt src="https://ztf.im/file.php?f=202209/f_743901e45488588dc6fc851b404690fc&t=png&o=&s=&v=1662516436" referrerpolicy="no-referrer"></p> 
 <h3><span style="color:#24292e">六、ZTF功能简介</span></h3> 
 <div> 
  <p>ZTF使用Go语言开发，真正做到了平台无依赖、部署无依赖，只需要一个可执行文件就可以运行，可以解决用例信息管理、测试脚本执行、测试结果比对、缺陷Bug提交等问题。</p> 
  <div style="text-align:center">
   <img align alt="ZTF功能" height="865" src="https://ztf.im/file.php?f=202209/f_dba33cb7556bcea51c8bd75fd09e5060&t=jpg&o=&s=&v=1662511100" width="800" referrerpolicy="no-referrer">
  </div> 
  <p>ZTF自动化测试框架对您现有的测试脚本资产没有侵入，可很好地驱动9种脚本语言、10种单元测试框架、7种自动化测试工具来编写和执行脚本，并把最终结果回传给禅道，进行统一的报告展示，打通项目管理和持续集成工具之间的沟壑。</p> 
  <p>相关代码可参考demo目录和<a href="https://gitee.com/organizations/ngtesting/projects" target="_blank"><span style="color:#337fe5">这里。</span></a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            