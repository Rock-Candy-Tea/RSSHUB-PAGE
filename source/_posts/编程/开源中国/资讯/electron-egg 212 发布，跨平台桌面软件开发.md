
---
title: 'electron-egg 2.1.2 发布，跨平台桌面软件开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/logo.png?ynotemdtimestamp=1645751463279'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 09:04:00 GMT
thumbnail: 'https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/logo.png?ynotemdtimestamp=1645751463279'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <h1 style="margin-left:0; margin-right:0"><img alt height="150" src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/logo.png?ynotemdtimestamp=1645751463279" width="150" referrerpolicy="no-referrer"></h1> 
</div> 
<div style="text-align:start"> 
 <div> 
  <div> 
   <div style="text-align:left"> 
    <p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">一个入门简单、跨平台桌面软件开发框架。</p> 
    <p><strong>师傅们点个star，迈向 2000 star   胜利了嘿</strong></p> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li>为什么使用？桌面软件（办公方向、 个人工具），仍然是未来十几年PC端需求之一，提高工作效率</li> 
     <li><span style="color:#40485b">简单：只需懂 JavaScript</span></li> 
     <li>🏆 码云最有价值开源项目</li> 
     <li>地址：<a href="https://gitee.com/wallace5303/electron-egg" target="_blank">https://gitee.com/wallace5303/electron-egg</a></li> 
     <li>地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwallace5303%2Felectron-egg" target="_blank">https://github.com/wallace5303/electron-egg</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fu34495%2Fmivcfg" target="_blank">5分钟教程，立刻体验</a></li> 
    </ul> 
    <h2 style="margin-left:0; margin-right:0; text-align:start">特性</h2> 
    <div> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li style="text-align:left"><span style="color:#40485b">跨平台：一套代码，可以打包成windows版、Mac版、Linux版运行</span></li> 
      <li style="text-align:left"><span style="color:#40485b">简单高效：只需学习js语言，同时支持vue、react、html等前端技术</span></li> 
      <li style="text-align:left"><span style="color:#40485b">前端独立：理论上支持任何前端技术，编写出精美的UI效果</span></li> 
      <li style="text-align:left"><span style="color:#40485b">工程化：可以用服务端的开发思维，来编写桌面软件</span></li> 
      <li style="text-align:left"><span style="color:#40485b">高性能：</span><span style="color:#222222">事件驱动、非阻塞式IO</span></li> 
      <li style="text-align:left"><span style="color:#40485b">功能丰富：服务端的技术场景等</span></li> 
      <li style="text-align:left"><span style="color:#40485b">功能demo：桌面软件常见功能，后续逐步集成或提供demo</span></li> 
      <li style="text-align:left"><span style="color:#40485b">更多功能请看文档</span></li> 
     </ol> 
    </div> 
    <h2 style="margin-left:0; margin-right:0; text-align:start">本次更新</h2> 
    <div> 
     <div> 
      <div> 
       <ul> 
        <li><span style="color:#000000">ipc通信增加 invoke/handle 模型</span></li> 
        <li><span style="color:#000000">ipcRender增加 invoke异步/sendSync同步方法</span></li> 
        <li><span style="color:#000000">优化ee-core代码</span></li> 
        <li><span style="color:#000000">优化storage demo</span></li> 
        <li><span style="color:#000000">优化ipc通信 同步、异步、双向通信demo</span></li> 
        <li><span style="color:#000000">替换所有前端ipcCall为ipcInvoke</span></li> 
        <li><span style="color:#000000">修复ipc并发请求问题</span></li> 
        <li><span style="color:#000000">修复托盘窗口关闭问题</span></li> 
        <li><span style="color:#000000">修复ee-core窗口事件</span></li> 
        <li><span style="color:#000000">优化mac系统应用坞点击显示</span></li> 
        <li><span style="color:#000000">优化单应用模式</span></li> 
        <li><span style="color:#000000">优化代码加密</span></li> 
       </ul> 
      </div> 
     </div> 
    </div> 
    <h2 style="margin-left:0; margin-right:0; text-align:start">使用场景</h2> 
    <h3 style="margin-left:0; margin-right:0; text-align:start">1. 常规桌面软件</h3> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">windows平台</p> <p style="margin-left:0; margin-right:0"><img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/home.png" referrerpolicy="no-referrer"></p> </li> 
     <li> <p style="margin-left:0; margin-right:0">macOS平台<br> <img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/mac-socket.png" referrerpolicy="no-referrer"></p> </li> 
     <li> <p style="margin-left:0; margin-right:0">linux平台 (ubuntu)<span> </span></p> </li> 
     <li> <p style="margin-left:0; margin-right:0"><img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/ubuntu-db.png" referrerpolicy="no-referrer"></p> </li> 
    </ul> 
    <h3 style="margin-left:0; margin-right:0; text-align:start">2. vue、react、web 转换成桌面软件</h3> 
    <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
     <li> <p style="margin-left:0; margin-right:0">vue-ant-design（本地）</p> <p style="margin-left:0; margin-right:0"><img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/vue-antd.png" referrerpolicy="no-referrer"></p> </li> 
     <li> <p style="margin-left:0; margin-right:0">禅道项目管理（web项目地址）</p> <p style="margin-left:0; margin-right:0"><img alt src="https://kaka996.coding.net/p/resource/d/tx-resource/git/raw/master/img/electron-egg/ee-project-7.png" referrerpolicy="no-referrer"></p> </li> 
    </ul> 
    <div> 
     <h3 style="margin-left:0; margin-right:0"><span>3. 用户案例</span></h3> 
    </div> 
    <p style="margin-left:0; margin-right:0">    <img height="613" src="https://oscimg.oschina.net/oscnet/up-bcb1bc56fdae33132b8bf7615ce3b92b5cb.png" width="976" referrerpolicy="no-referrer"></p> 
    <p style="margin-left:0; margin-right:0">    <img height="1650" src="https://oscimg.oschina.net/oscnet/up-60da0ec34998164fe0a8440db42faf41b7b.jpg" width="2878" referrerpolicy="no-referrer"></p> 
    <p style="margin-left:0; margin-right:0">    <img height="663" src="https://oscimg.oschina.net/oscnet/up-2d0645212cbffe3bcd1d540d6b671e8745d.png" width="1125" referrerpolicy="no-referrer"></p> 
    <h3 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fu34495%2Fmivcfg" target="_blank">访问官网：</a><a href="https://gitee.com/wallace5303/electron-egg">https://gitee.com/wallace5303/electron-egg</a></h3> 
   </div> 
  </div> 
 </div> 
</div> 
<div> 
 <div>
   
 </div> 
</div>
                                        </div>
                                      
</div>
            