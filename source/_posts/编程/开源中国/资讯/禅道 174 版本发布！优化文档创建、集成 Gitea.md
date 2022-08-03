
---
title: '禅道 17.4 版本发布！优化文档创建、集成 Gitea'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://blog.easycorp.cn/file.php?f=easycorp/202208/f_01f64e22f517634c246b1acc15ee061a&t=png&o=&s=&v=1659317226'
author: 开源中国
comments: false
date: Wed, 03 Aug 2022 09:36:00 GMT
thumbnail: 'https://blog.easycorp.cn/file.php?f=easycorp/202208/f_01f64e22f517634c246b1acc15ee061a&t=png&o=&s=&v=1659317226'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">禅道项目管理软件集产品管理、项目管理、质量管理、文档管理、组织管理和事务管理于一体，是一款功能完备的项目管理软件，完美地覆盖了项目管理的核心流程。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">禅道官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zentao.net%2F" target="_blank">https://www.zentao.net</a></span></p> 
<p>禅道17.4版本<strong>优化文档创建流程</strong>，提升您的内容创作体验！新增<strong>代号启用功能</strong>，满足您根据不同项目管理场景进行自定义配置。新版本会<strong>过滤掉登录用户无权访问的动态</strong>，避免私密的项目信息被暴露。新版本还<strong>集成了Gitea</strong>，您可以在禅道上便捷、高效地管理您的Gitea代码库，除此之外我们提供了<strong>对比代码、合并请求与禅道需求、Bug、任务建立关联</strong>等Gitea所不具备的功能，满足代码评审以及追溯代码修改历史记录的需求，更好地帮助您管理项目代码。</p> 
<p><strong>持续优化，定期更新，禅道一直在路上。</strong></p> 
<p><strong>禅道本次发布数据如下：</strong></p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202208/f_01f64e22f517634c246b1acc15ee061a&t=png&o=&s=&v=1659317226" referrerpolicy="no-referrer"></p> 
<h2><span>一、本次新增功能点</span></h2> 
<h3><strong style="color:#494949">文档：</strong></h3> 
<ul> 
 <li><span style="color:#494949">文档优化创建流程，提升内容创作体验。</span></li> 
</ul> 
<h3><span style="color:#494949">看板：</span></h3> 
<ul> 
 <li><span style="color:#494949">看板项目和专业研发看板增加设置菜单，包含概况、团队、产品、白名单等功能。</span></li> 
 <li><span style="color:#494949">通用看板团队成员支持选择系统通讯录中所有成员。</span></li> 
</ul> 
<h3><span style="color:#494949">地盘：</span></h3> 
<ul> 
 <li><span style="color:#494949">地盘、组织最新动态区块中过滤当前用户无权访问的动态。</span></li> 
 <li><span style="color:#494949">添加待办页面增加指派给操作。</span></li> 
</ul> 
<h3><span style="color:#494949">产品：</span></h3> 
<ul> 
 <li><span style="color:#494949">计划列表中查看需求、Bug详情后返回，列表保持排序。</span></li> 
 <li><span style="color:#494949">研发需求详情中增加相关版本、发布等信息。</span></li> 
</ul> 
<h3><span style="color:#494949">后台：</span></h3> 
<ul> 
 <li><span style="color:#494949">全局设置中增加代号启用功能。</span></li> 
</ul> 
<h3><span style="color:#494949">DevOps：</span></h3> 
<ul> 
 <li><span style="color:#494949">对DevOps下二级导航栏进行了优化，减少了导航选项，结构上更易理解。通过设置选项可以集中配置代码库、指令、GitLab等第三方工具，增加应用选项便于您快速跳转至第三方平台。</span></li> 
 <li><span style="color:#494949">集成Gitea,除了支持代码的克隆与下载、浏览代码文件、提交历史、提交评审意见、对比代码、合并请求等常用代码库管理功能外，还提供了合并请求与禅道需求、任务、Bug建立关联、追溯代码的修改历史记录等功能，从而可以便捷、高效、集中地管理Gitea代码库。</span></li> 
 <li><span style="color:#494949">优化了15项界面、交互设计以提升使用体验。</span></li> 
</ul> 
<h3><span style="color:#494949">禅道客户端：</span></h3> 
<ul> 
 <li><span style="color:#494949">新增单点登录功能，详见 《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xuanim.com%2Fbook%2Fxxbservice%2F276.html" target="_blank"> 单点登录配置</a>》。（增强版功能）</span></li> 
 <li><span style="color:#494949">新增基于RoadRunner的高性能版本，详见 《 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xuanim.com%2Fbook%2Fxxbservice%2F277.html" target="_blank">使用 RoadRunner 启动 xxb 服务</a>》。（增强版功能）</span></li> 
 <li><span style="color:#494949">新增客户端修改个人信息功能。</span></li> 
 <li><span style="color:#494949">新增仅群主和管理员可以添加群成员的设置功能。</span></li> 
 <li><span style="color:#494949">新增启用移动端的开关。</span></li> 
 <li><span style="color:#494949">新增群主的账号被删除后自动转让群的功能。</span></li> 
 <li><span style="color:#494949">一键安装包新增网页客户端。</span></li> 
 <li><span style="color:#494949">新增修复数据库的脚本，方便管理员修复损坏的表。</span></li> 
 <li><span style="color:#494949"><span>去掉XXD中无意义的错误日志，以免干扰用户。</span></span></li> 
</ul> 
<p><strong>本期优化的全部需求和bug</strong></p> 
<p>请点击查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzentaopms%2Fblob%2Fmaster%2Fdoc%2FCHANGELOG" target="_blank">https://github.com/easysoft/zentaopms/blob/master/doc/CHANGELOG</a></p> 
<h2><strong style="color:inherit">二、主要功能截图</strong></h2> 
<p><span>▼ 优化文档创建的流程，填写文档的基本信息后，进入文档内容的编辑页面，为您创作内容提供舒适的编辑空间。</span></p> 
<p><span><img align alt height="294" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_210226be60664d746b35631429ddee03&t=png&o=&s=&v=1658972855" width="600" referrerpolicy="no-referrer"></span></p> 
<p><span><img align alt height="380" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_f9868647ab6a1a13e6459394aa83f46d&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"></span></p> 
<p><span>▼ </span>看板项目和专业研发看板中增加设置功能，支持您快捷地管理和查看看板项目的概况、团队、产品、白名单等信息。</p> 
<p><img align alt height="363" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_5357bf9abefc2c701ab3b2df29c7eebb&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"><br> <span>▼ </span>维护通用看板的团队成员时，您可以选择系统通讯录中的所有成员，增加的成员会同步到看板的空间中。</p> 
<p><img align alt height="369" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_706898827e9b36f919ab53ce66f6d565&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"><br> <span>▼ </span>地盘和组织的最新动态会根据权限过滤掉当前用户无权访问的动态，避免私密项目、产品信息被暴露。</p> 
<p><img align alt height="213" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_eae836964f1c1215ae19870c3e650285&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"><br> <span>▼ </span>地盘中添加待办页面增加指派给的操作，当您需要给团队内其他成员创建待办时，您可以直接进行指派。</p> 
<p><img align alt height="190" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_d83bcb3996a9cdcfc637e63005d9bfd1&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"><br> <span>▼ </span>计划列表中优化了排序功能，您在查看需求、Bug详情后返回列表时，保持列表排序，方便您按原顺序继续查看。</p> 
<p><img align alt height="244" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_54e479f5ece8bb892944e36bf8c49ff8&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"><br> <span>▼ </span>软件需求的详情页中增加相关版本和发布的信息，方便您查看需求时同时查看关联的版本和发布。</p> 
<p><img align alt height="210" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_dc50e78dd40ace1a6a26b497aed4093d&t=png&o=&s=&v=1658972855" width="400" referrerpolicy="no-referrer"><br> <span>▼ </span>全局设置中增加“是否启用代号”功能，便于您根据不同场景对代号功能进行配置，代号启用时，系统中的产品、项目、执行等页面均会展示代号信息，否则隐藏。</p> 
<p><img align alt height="207" src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_bbc2125d7f59778b795641996cce8db0&t=png&o=&s=&v=1658972855" width="800" referrerpolicy="no-referrer"></p> 
<p><span>▼ </span>下载或克隆Gitea代码库代码。</p> 
<p><span><img alt src="https://blog.easycorp.cn/file.php?f=zentao/202207/f_950370ca434477a11cdeb49e185bba0e&t=png&o=&s=&v=1658984865" referrerpolicy="no-referrer"></span></p> 
<p><span>▼ 查看Gitea代码库提交历史，对比版本间代码差异。</span></p> 
<p><span><img alt src="https://blog.easycorp.cn/file.php?f=zentao/202207/f_42c400950a238cb5bee8c9025ef7d5cf&t=png&o=&s=&v=1658984865" referrerpolicy="no-referrer"></span></p> 
<p>▼ 在Gitea代码库下可以根据改动文件查看代码改动。</p> 
<p><span><img alt src="https://blog.easycorp.cn/file.php?f=zentao/202207/f_f9e2e953aae8d984982d5cd2df3ece30&t=png&o=&s=&v=1658984865" referrerpolicy="no-referrer"></span></p> 
<p>▼ 查看Gitea合并请求概况，可以在页面浏览历史记录。</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=zentao/202207/f_4663ba9841bb0dfd0b46858e8e3fa0c1&t=png&o=&s=&v=1658984865" referrerpolicy="no-referrer"></p> 
<p>▼ 将合并请求与Bug建立关联。</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=zentao/202207/f_96c379a4d2906f76e18d0305aed7266d&t=png&o=&s=&v=1658984865" referrerpolicy="no-referrer"></p> 
<p>▼ 客户端新增了修改个人信息功能，您可快捷的修改个人信息。</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_3fc3a1dc93f24476af03af6f153c75d6&t=png&o=&s=&v=1658903634" referrerpolicy="no-referrer">  <img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_36cb23a512bcb5f7fa89bbd5dca8b9ef&t=png&o=&s=&v=1658904551" referrerpolicy="no-referrer"></p> 
<p>▼ 新增仅群主和管理员可以添加群成员的设置功能，您可以设置多个管理员帮助维护群内成员。</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_158ce7932d9febeba589439e3dc1b9fc&t=png&o=&s=&v=1658890163" referrerpolicy="no-referrer"></p> 
<p>▼ 后台参数中配置修改后自动更新到xxd.conf文件，可以直接应用或重启并应用，管理员修改后台配置后不用再手动同步了。</p> 
<p><img alt src="https://blog.easycorp.cn/file.php?f=easycorp/202207/f_ba579a7bab06c17fee6ed468d10ffe53&t=png&o=&s=&v=1658972855" referrerpolicy="no-referrer"></p> 
<h2><span style="color:inherit">三、下载链接</span></h2> 
<table class="table table-kindeditor" style="width:957.333px"> 
 <tbody> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>安装包下载</span></td> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php5.4_5.6.zip" target="_blank"><span>php5.4_5.6</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.0.zip" target="_blank"><span>php7.0</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.1.zip" target="_blank"><span>php7.1</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.2_7.4.zip" target="_blank"><span>php7.2_7.4</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php8.0.zip" target="_blank"><span>php8.0</span></a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>Windows 一键安装包</span></td> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.win64.exe" target="_blank"><span>经典64位</span></a><span>     </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.zbox.win64.exe" target="_blank"><span>新版</span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.zbox.win64.exe" target="_blank"><span>64位</span></a>（升级了安装界面的交互）</td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"> <p><span>Linux 一键安装包（适用于Ubuntu17+，centos7.x）</span></p> </td> 
   <td style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.zbox_64.tar.gz" target="_blank"><span>64位</span></a><span> </span></td> 
   <td colspan="1" rowspan="2" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd; vertical-align:middle"><span style="color:#e53333">注：Linux 一键安装包必须直接解压到 /opt 目录下。</span></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"> <p><span>低版本 Linux 一键安装包（适用于ubuntu16及以下版本、centos7.3及以下版本）</span></p> </td> 
   <td style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.zbox_old.64.tar.gz" target="_blank"><span>64位</span></a></p> </td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>DEB包下载：可以通过dpkg包管理器在Ubuntu和Debian系统下安装</span></td> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php5.4_5.6.1.all.deb" target="_blank"><span>php5.4_5.6</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.0.1.all.deb" target="_blank"><span>php7.0</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.1.1.all.deb" target="_blank"><span>php7.1</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.2_7.4.1.all.deb" target="_blank"><span>php7.2_7.4</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php8.0.1.all.deb" target="_blank"><span>php8.0</span></a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>RPM包下载：可以通过rpm包管理器在Centos系统下安装</span></td> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php5.4_5.6.1.noarch.rpm" target="_blank"><span>php5.4_5.6</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.0.1.noarch.rpm" target="_blank"><span>php7.0</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.1.1.noarch.rpm" target="_blank"><span>php7.1</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php7.2_7.4.1.noarch.rpm" target="_blank"><span>php7.2_7.4</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentao%2F17.4%2FZenTaoPMS.17.4.php8.0.1.noarch.rpm" target="_blank"><span>php8.0</span></a></td> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="3" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd; vertical-align:middle"><span>最新版禅道客户端下载链接</span></td> 
   <td rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>Windows</span></td> 
   <td rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.win64.setup.exe" target="_blank"><span>安装包</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.win64.zip" target="_blank"><span>压缩包</span></a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><span>Linux</span></td> 
   <td rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.linux64.deb" target="_blank"><span>安装包</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.linux64.tar.gz" target="_blank"><span>压缩包 (.tar.gz)</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.linux64.zip" target="_blank"><span>压缩包 (.zip)</span></a></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><span>Mac</span></td> 
   <td rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.mac.dmg" target="_blank"><span>安装包</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzentaoclient%2F6.1%2Fzentaoclient.mac64.zip" target="_blank"><span>压缩包</span></a></td> 
  </tr> 
  <tr> 
  </tr> 
  <tr> 
  </tr> 
  <tr> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><span>最新版禅道客户端服务器下载链接</span></td> 
   <td colspan="2" rowspan="1" style="border-image:initial; border-left:1px solid #dddddd; border-right:1px solid #dddddd; border-top:1px solid #dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F6.1%2Fxxd.6.1.win64.zip" target="_blank"><span>Windows</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F6.1%2Fxxd.6.1.linux.x64.tar.gz" target="_blank"><span>Linux</span></a><span>    </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fxuanxuan%2F6.1%2Fxxd.6.1.mac.tar.gz" target="_blank"><span>Mac</span></a></td> 
  </tr> 
 </tbody> 
</table> 
<h3> </h3> 
<h4><span style="color:inherit"><span style="color:#e53333">Docker镜像:</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Feasysoft%2Fzentao%2Ftags" target="_blank">点击这里</a></span></h4> 
<h2><span style="color:inherit">四、帮助手册</span></h2> 
<p><span>安装文档：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.zentao.net%2Fbook%2Fzentaopmshelp%2F40.html" target="_blank"><span>https://www.zentao.net/book/zentaopmshelp/40.html</span></a></p> 
<p><span>升级文档：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.zentao.net%2Fbook%2Fzentaoprohelp%2F41.html" target="_blank"><span>https://www.zentao.net/book/zentaoprohelp/41.html</span></a></p> 
<p> </p>
                                        </div>
                                      
</div>
            