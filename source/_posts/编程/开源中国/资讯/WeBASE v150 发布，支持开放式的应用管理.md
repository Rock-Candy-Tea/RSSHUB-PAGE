
---
title: 'WeBASE v1.5.0 发布，支持开放式的应用管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5e678c16866e7438d3fe612098f3d0cc20c.JPEG'
author: 开源中国
comments: false
date: Wed, 14 Apr 2021 17:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5e678c16866e7438d3fe612098f3d0cc20c.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:justify"><span style="color:#555555">作为一个友好的、功能丰富的区块链中间件平台，WeBASE 一直致力于降低区块链开发者的门槛，提高区块链开发效率，简化区块链的运维操作和管理。</span></p> 
<p style="text-align:justify"><span style="color:#555555">如今，WeBASE v1.5.0来了，将更快捷高效地助力社区开发者搭建区块链应用。一起来看看v1.5.0带来了哪些新功能吧！</span></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong><span style="background-color:#ffffff; color:#1e53a4">应用的插件化管理</span></strong></span></span></p> 
<p style="text-align:justify"><span style="color:#555555">WeBASE做为一个区块链中间件平台，在部署架构上，处于FISCO BCOS和应用层之间。应用可以调用WeBASE提供的接口进行业务开发，同时，通过WeBASE提供的管理平台进行可视化管理。</span></p> 
<p style="text-align:justify"><span style="color:#555555">然而，在社区开发者长期的实践过程中，我们发现，对于每个区块链应用，即便使用了WeBASE做为管理平台，依然需要使用开发应用层的业务管理平台，导致业务管理人员需要通过两个入口管理区块链和业务。如何将这两类管理平台打通，实现协同式管理成了社区开发者面临的一个普遍性问题。</span></p> 
<p style="text-align:justify"><span style="color:#555555">WeBASE v1.5.0 的更新带来了新的操作方式，新增了应用管理功能，使WeBASE在架构上更加开放了；支持区块链应用以插件化的形式添加到WeBASE中，实现统一管理。</span></p> 
<p><span style="color:#555555">此功能主要包含了两个方面：</span></p> 
<ol> 
 <li> <p><span style="color:#555555">在管理台提供应用管理功能菜单。</span></p> </li> 
 <li> <p><span style="color:#555555">对接入应用提供接入规范。各个应用可以按照接入规范接入，以此来实现各应用之间从用户、区块链账户、基础配置到合约等方面的互通。</span></p> </li> 
</ol> 
<p><img alt height="434" src="https://oscimg.oschina.net/oscnet/up-5e678c16866e7438d3fe612098f3d0cc20c.JPEG" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong><span style="background-color:#ffffff; color:#1e53a4">应用接入标准及流程</span></strong></span></span></p> 
<p><span style="color:#555555">应用接入标准规范主要包括以下三方面的内容：</span></p> 
<ol> 
 <li> <p><span style="color:#555555">通过WeBASE管理平台获得注册信息，并通过API向WeBASE注册服务的标准。</span></p> </li> 
 <li> <p><span style="color:#555555">WeBASE管理平台通过“心跳检查”应用是否“存活”的标准。</span></p> </li> 
 <li> <p><span style="color:#555555">通过WeBASE提供的基础能力API和WeBASE连通的标准。</span></p> </li> 
</ol> 
<p><span style="color:#555555">通用性API是整个规范的核心，它圈定了WeBASE和应用协同的能力范围。目前接入规范开放的通用性API主要有：</span></p> 
<ul> 
 <li> <p><span style="color:#555555">服务注册API</span></p> </li> 
 <li> <p><span style="color:#555555">获取系统账号信息API</span></p> </li> 
 <li> <p><span style="color:#555555">获取节点信息API</span></p> </li> 
 <li> <p><span style="color:#555555">获取相关证书API</span></p> </li> 
 <li> <p><span style="color:#555555">获取群组信息列表API</span></p> </li> 
 <li> <p><span style="color:#555555">获取账户信息列表API</span></p> </li> 
 <li> <p><span style="color:#555555">合约信息导入API（多次导入可设置不同目录，相同目录则覆盖）等等</span></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#555555">详细接入规范可以参考应用接入说明<span style="color:#555555">文档</span>。<span style="color:#555555">文档地址：</span></span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Node-Manager/appintegration.html</span></p> 
<p style="text-align:justify"><span style="color:#555555">下面以WeIdentity为例来说明。WeIdentity已经按照规范进行了接入改造，在WeBASE中做成了一份默认的应用模板，此模板可以作为一个接入样例供其他应用接入时参考使用。</span></p> 
<p><span style="color:#555555">模板的使用步骤如下：</span></p> 
<ol> 
 <li> <p><span style="color:#555555">在应用管理中添加WeIdentity应用；</span></p> </li> 
 <li> <p><span style="color:#555555">复制注册信息；</span></p> </li> 
 <li> <p><span style="color:#555555">通过“WeIdentity + WeBASE集成模式”搭建WeIdentity管理台，过程中需要粘贴之前复制的注册信息。</span></p> </li> 
</ol> 
<p style="text-align:justify"><span style="color:#555555">简单三个步骤即可实现两者的互通。</span><span style="color:#555555">详细操作可以参考WeIdentity文档，使用 WeIdentity 部署工具完成部署（可视化部署方式）。具体文档见：</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://weidentity.readthedocs.io/zh_CN/latest/docs/deploy-via-web.html</span></p> 
<p><img alt height="674" src="https://oscimg.oschina.net/oscnet/up-ed68d17bbf73da89cc2622ffb374d5ca329.JPEG" width="1080" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong><span style="background-color:#ffffff; color:#1e53a4">管理台移动端功能</span></strong></span></span></p> 
<p style="text-align:justify"><span style="color:#555555">随着智能终端的普及，移动端作为重要的入口具有便携性好、功能性强、实时性强等特点。社区用户多次反馈希望浏览器和WeBASE管理台增加移动端的功能，以方便实时查看和展示。</span></p> 
<p style="text-align:justify"><span style="color:#555555">为积极响应广大社区开发者们的反馈，WeBASE v1.5.0 新增了管理台的手机端展示功能。目前该功能支持区块链数据概览、链上合约、链上用户、节点列表、区块列表和交易列表的展示，后续我们将持续新增和优化手机端功能。 </span></p> 
<p style="text-align:justify"><img alt height="553" src="https://oscimg.oschina.net/oscnet/up-37e65f06566bf7725b99dbb1b2b57c036b9.JPEG" width="908" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong><span style="background-color:#ffffff; color:#1e53a4">合约和用户管理体验优化</span></strong></span></span></p> 
<p style="text-align:justify"><span style="color:#555555">WeBASE经过一段时间的迭代开发，创建了对合约和合约用户的一套工具集和一套多角度展示窗口。这些功能当初是按照垒积木的方式一块一块快速叠加的，这样做的好处是使得社区用户可以尽早体验新功能，帮助大家快速开发。但是，经过一段时间的迭代，我们发现了其中的不足——各功能分散，功能菜单过多，没有实现有机结合。</span></p> 
<p style="text-align:justify"><span style="color:#555555">WeBASE v1.5.0 对合约和合约用户进行了一次整理，对功能菜单进行了梳理和整合，新增了全量的链上合约和链上用户展示。另外，开放了管理台已部署合约的编辑、编译和重新部署权限。如需关闭此功能，可在WeBASE-Node-Manager配置文件application.yml中修改——将deployedModifyEnable改为false，重启服务即可。权限的放开使得WeBASE管理台的使用更加方便，但同时，我们也需提醒用户，对生产环境的改动请谨慎操作。</span></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#555555"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong><span style="background-color:#ffffff; color:#1e53a4">其他优化和修复</span></strong></span></span></p> 
<ul> 
 <li> <p><span style="color:#555555">区块链浏览器通过数据导出jar（data-export-sdk.jar）导出区块和交易数据、升级mysql-connector-java.jar到8.0.22、支持预编译合约的解析。区块链浏览器地址：</span></p> <p><span style="color:#1e53a4">https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/browser/deploy.html</span></p> </li> 
 <li> <p><span style="color:#555555">WeBASE从web3sdk切换到javasdk，支持导出javasdk的合约java文件</span></p> </li> 
 <li> <p><span style="color:#555555">提供一键部署的升级脚本</span></p> </li> 
 <li> <p><span style="color:#555555">支持导出SDK证书，增加区块链的平均TPS等数据统计</span></p> </li> 
 <li> <p><span style="color:#555555">修复签名服务序列化问题</span></p> </li> 
 <li> <p><span style="color:#555555">修复合约列表搜索问题、修复合约中定长数组调用bug</span></p> </li> 
</ul> 
<p style="text-align:justify"><span style="color:#555555"><span style="background-color:#1e53a4; color:#1e53a4"><strong> </strong></span><span style="color:#1e53a4"><strong> </strong></span></span><span style="color:#1e53a4"><strong>即刻使用</strong></span></p> 
<p style="text-align:justify"><span style="color:#555555">上述优化及功能所涉及的最新代码和技术文档已同步更新，欢迎体验和 star 支持。</span></p> 
<p><strong><span style="color:#555555">WeBASE 代码仓库：</span></strong></p> 
<p><span style="color:#1e53a4">https://github.com/WeBankFinTech/WeBASE</span></p> 
<p><strong><span style="color:#555555">WeBASE 国内镜像：</span></strong></p> 
<p><span style="color:#1e53a4">https://gitee.com/WeBank/WeBASE</span></p> 
<p><strong><span style="color:#555555">WeBASE 技术文档：</span></strong></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest</span></p> 
<p><strong><span style="color:#555555">WeBASE 技术文档国内镜像：</span></strong></p> 
<p><span style="color:#1e53a4">https://fintech.webank.com/developer/docs/webase</span></p> 
<p><strong><span style="color:#555555">首次体验WeBASE，可参考一键部署文档：</span></strong></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE/install.html</span></p> 
<p><strong><span style="color:#555555">如需升级已有版本，可参考:</span></strong></p> 
<p style="text-align:justify"><strong><span style="color:#555555">WeBASE一键部署的一键升级：</span></strong></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Install/upgrade.html#auto</span></p> 
<p><strong><span style="color:#555555">WeBASE-Front升级说明</span></strong><span style="color:#555555">：</span></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Front/upgrade.html</span></p> 
<p><strong><span style="color:#555555">WeBASE-Node-Manager升级说明</span></strong><span style="color:#555555">：</span></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Node-Manager/upgrade.html</span></p> 
<p><strong><span style="color:#555555">WeBASE-Sign升级说明</span></strong><span style="color:#555555">：</span></p> 
<p style="text-align:justify"><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Sign/upgrade.html</span></p> 
<p><strong><span style="color:#555555">WeBASE-Web升级说明：</span></strong></p> 
<p><span style="color:#1e53a4">https://webasedoc.readthedocs.io/zh_CN/latest/docs/WeBASE-Web/upgrade.html</span></p> 
<p><strong><span style="color:#555555">向我们报告问题，欢迎提交issue：</span></strong></p> 
<p><span style="color:#1e53a4">https://github.com/WeBankFinTech/WeBASE/issues</span></p>
                                        </div>
                                      
</div>
            