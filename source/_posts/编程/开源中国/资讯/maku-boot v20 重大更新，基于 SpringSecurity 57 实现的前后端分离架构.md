
---
title: 'maku-boot v2.0 重大更新，基于 SpringSecurity 5.7 实现的前后端分离架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7071843d00bea17c142b5289e9a2c64311b.jpg'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 09:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7071843d00bea17c142b5289e9a2c64311b.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>maku-boot 是采用 SpringBoot、SpringSecurity、Mybatis-Plus 等框架，开发的一套 SpringBoot 快速开发平台，使用门槛极低，且采用 MIT 开源协议，完全免费开源，可免费用于<strong>商业项目</strong>等场景。</li> 
 <li>采用组件模式，扩展不同的业务功能，可以很方便的实现各种业务需求，且不会导致系统臃肿，若想使用某个组件，按需引入即可，反之亦然。</li> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaku.net%2Fdocs%2Fmaku-boot" target="_blank">https://maku.net/docs/maku-boot</a></li> 
 <li>演示环境：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.maku.net%2Fmaku-boot" target="_blank">https://demo.maku.net/maku-boot</a></li> 
</ul> 
<h2 style="margin-left:0em; margin-right:0em; text-align:start">项目名称</h2> 
<p>我们成立项目之初，就想好了愿景：【让开发更简单】，帮助开发者快速开发项目，所以采用 fast 开头命名，如：fast-boot、fast-admin等等，后来我们发现这个名称没有含义，如：fastboot一般指设备快速启动的意思，且也不能申请商标，对后期推广也不利，经过一番思考，最终决定以 maku 开头，这样识别度高很多，也不会造成混淆。再次感谢大伙对 MAKU 的支持，为成为国内最好用的快速开发平台，我们一直在努力！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新日志</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>从2.0开始，由原来的项目名【fast-boot】变更为【maku-boot】，感谢支持</li> 
 <li>重构安全模块，采用springsecurity5.7+token技术，实现前后端分离架构</li> 
 <li>移除oauth2.0认证，oauth2.0不太适合做站内登录</li> 
 <li>新增手机短信登录，现支持账号和短信登录</li> 
 <li>新增登录日志功能，方便查看登录用户</li> 
 <li>优化账号密码登录逻辑</li> 
 <li>升级element-plus到2.2.15</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">前端工程</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/maku-admin">https://gitee.com/makunet/maku-admin</a></li> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Fmaku-admin" target="_blank">https://github.com/makunet/maku-admin</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">后端工程</h2> 
<ul> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/maku-boot">https://gitee.com/makunet/maku-boot</a></li> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Fmaku-boot" target="_blank">https://github.com/makunet/maku-boot</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">代码生成器</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Gitee 仓库：<a href="https://gitee.com/makunet/maku-generator">https://gitee.com/makunet/maku-generator</a></li> 
 <li>Github 仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmakunet%2Fmaku-generator" target="_blank">https://github.com/makunet/maku-generator</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">交流和反馈</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官方社区：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaku.net" target="_blank">https://maku.net</a></li> 
 <li>技术解答、交流、反馈、建议等，请移步到官方社区，我们会及时回复，也方便今后的小伙伴寻找答案，感谢理解！</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">效果图</h2> 
<p><img alt height="1758" src="https://oscimg.oschina.net/oscnet/up-7071843d00bea17c142b5289e9a2c64311b.jpg" width="3449" referrerpolicy="no-referrer"></p> 
<p><img alt height="1832" src="https://oscimg.oschina.net/oscnet/up-3ba660169011ab86deee0b69409555b7b4a.jpg" width="3434" referrerpolicy="no-referrer"></p> 
<p><img alt height="1823" src="https://oscimg.oschina.net/oscnet/up-1099ad75bda44d1fd0636745df4f0fc0fa7.jpg" width="3436" referrerpolicy="no-referrer"></p> 
<p><img alt height="1806" src="https://oscimg.oschina.net/oscnet/up-3ac2267c393b0ce47f3cb67b1b3c8a6d3e6.jpg" width="3456" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            