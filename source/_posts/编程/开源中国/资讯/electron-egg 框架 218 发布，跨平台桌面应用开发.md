
---
title: 'electron-egg 框架 2.1.8 发布，跨平台桌面应用开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-54968d2e7f9e0e92423499b56e8f7841a42.png'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 08:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-54968d2e7f9e0e92423499b56e8f7841a42.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:center"><img height="693" src="https://oscimg.oschina.net/oscnet/up-54968d2e7f9e0e92423499b56e8f7841a42.png" width="1150" referrerpolicy="no-referrer"></p> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0; text-align:center"><strong><span>值得信赖</span></strong></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><img alt height="545" src="https://oscimg.oschina.net/oscnet/up-9782877bbfdcfcc1beeaac4bd5a259a8de6.png" width="860" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><strong><span>为什么使用</span></strong></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span>桌面软件（</span><span style="color:#f5222d">办公方向</span><span>、<span> </span></span><span style="color:#f5222d">个人工具</span><span>），仍然是</span><span style="color:#f5222d">未来十几年 PC 端</span><span>需求之一，提高工作效率</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#f5222d">electron 技术是流行趋势</span><span>，百度翻译、阿里网盘、迅雷、有道云笔记 ......</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span>ee 框架使用</span><span><span> </span>b（浏览器）s（主进程）s（远程后端服务）开发思想</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#f5222d">前端</span><span>、</span><span style="color:#f5222d">服务端</span><span>同学都能快速入门</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><strong><span>愿景</span></strong></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#40485b">所有开发者都能学会桌面软件研发</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><strong><span>简单</span></strong></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#40485b">只需懂 JavaScript</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><strong><span>开源</span></strong></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#40485b">gitee：</span><a href="https://gitee.com/wallace5303/electron-egg" target="_blank"><span>https://gitee.com/wallace5303/electron-egg</span></a><span><span> </span>1900+</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#40485b">github：</span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fwallace5303%2Felectron-egg" target="_blank"><span>https://github.com/wallace5303/electron-egg</span></a><span><span> </span>400+</span></p> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">本次更新</h2> 
<div style="text-align:left"> 
 <ol> 
  <li>安全性更新</li> 
  <li>支持bytecode字节码加密</li> 
  <li>优化压缩混淆加密</li> 
  <li>将废弃compress、restore命令，使用encrypt替代</li> 
  <li>mainServer增加option支持</li> 
  <li>限制控制器业务必须为class文件</li> 
 </ol> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:start">使用场景</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">1. 常规桌面软件</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">windows 平台</p> <p style="margin-left:0; margin-right:0"><img height="986" src="https://oscimg.oschina.net/oscnet/up-2a139cc82c2ee95161e0255761c62f8cd91.png" width="1468" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">macOS 平台<br> <img height="514" src="https://oscimg.oschina.net/oscnet/up-7fe23fb230b5fd6c5c9a5db4ba980240d3c.png" width="768" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">linux 平台 (ubuntu)<span> </span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><img height="946" src="https://oscimg.oschina.net/oscnet/up-bdcffde5db5e605fb4b56b408a1a90e68f2.png" width="1339" referrerpolicy="no-referrer"></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">2. vue、react、web 转换成桌面软件</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">vue-ant-design（本地）</p> <p style="margin-left:0; margin-right:0"><img height="1290" src="https://oscimg.oschina.net/oscnet/up-f62948e6737771c09978e5ca9cccbbfc138.png" width="2144" referrerpolicy="no-referrer"></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">禅道项目管理（web 项目地址）</p> <p style="margin-left:0; margin-right:0"><img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/ee-project-7.png" referrerpolicy="no-referrer"><img alt height="826" src="https://oscimg.oschina.net/oscnet/up-f2ec517e12505ceb5d54958f73b13c5eebe.png" width="1345" referrerpolicy="no-referrer"></p> </li> 
</ul> 
<div style="text-align:left"> 
 <h3 style="margin-left:0; margin-right:0"><span>3. 用户案例</span></h3> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    <img height="620" src="https://oscimg.oschina.net/oscnet/up-4c4d6f6195f0cf9cc4d9edae198f8664f01.png" width="1040" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    <img height="1650" src="https://oscimg.oschina.net/oscnet/up-60da0ec34998164fe0a8440db42faf41b7b.jpg" width="2878" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    </p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fu34495%2Fmivcfg" target="_blank">访问官网：</a><a href="https://gitee.com/wallace5303/electron-egg">https://gitee.com/wallace5303/electron-egg</a></h3> 
<p> </p>
                                        </div>
                                      
</div>
            