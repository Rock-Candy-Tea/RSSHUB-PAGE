
---
title: 'Furion v4.2.0 发布，支持 .NET5，.NET6，.NET7'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-790eaa9a46ff00fbcbe956d8b279dd43347.png'
author: 开源中国
comments: false
date: Mon, 15 Aug 2022 11:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-790eaa9a46ff00fbcbe956d8b279dd43347.png'
---

<div>   
<div class="content">
                                                                                            <h2>序言</h2> 
<p>在 .NET 7 Preview 7 发布当天，Furion 第一时间做了适配并修正了 2个升级兼容问题，同时从该版本开始，Furion 将通过迭代重构掉现有的 37个功能模块，为未来即将暴增的用户量做准备。</p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-790eaa9a46ff00fbcbe956d8b279dd43347.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-18321f5e29135882796cbc1ac04c6171ba8.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>项目地址</h2> 
<ul> 
 <li>Gitee：<a href="https://gitee.com/dotnetchina/Furion" target="_blank">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>GitHub：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmonksoul%2FFurion" target="_blank">https://github.com/monksoul/Furion</a></li> 
 <li>国外文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffurion.icu%2F" target="_blank">https://furion.icu</a></li> 
</ul> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p><strong>突破性变化</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[支持]<span> </span><code>.NET 6.0.8</code><span> </span>和<span> </span><code>.NET 7 Preview 7</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/842d4f739c92366e05fb1d2c619c9b2c2c2c21b7" target="_blank">842d4f7</a></li> 
    <li>[调整]<span> </span><code>[LoggingMonitor]</code><span> </span>命名空间为<span> </span><code>System</code>，因为使用频率越来越高<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/b879861c9db5cf3cb0f4ae023d1e96b06fad3e46" target="_blank">b879861</a></li> 
   </ul> </li> 
  <li> <p><strong>问题修复</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[修复]<span> </span>日志上下文数据多次写入被清空问题以及数据库日志出现异常后停止写入<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5LIWF" target="_blank">#I5LIWF</a></li> 
    <li>[修复]<span> </span>个别情况下跨域默认配置的响应缓存导致嵌入式资源异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7a57efe15a9a2d76475d758f2b64395f96d94077" target="_blank">7a57efe</a></li> 
    <li>[修复]<span> </span>远程请求传入不合法的请求报文头数据触发校验失败问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I5LPFE" target="_blank">#I5LPFE</a></li> 
    <li>[修复]<span> </span>多线程中使用静态日志写数据库日志导致连接池耗光问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/8d5cdd6ca04d55e33322000ecc176e47195b6f4d" target="_blank">8d5cdd6</a></li> 
   </ul> </li> 
  <li> <p><strong>其他更改</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[优化]<span> </span>底层迭代改进优化</li> 
   </ul> </li> 
  <li> <p><strong>文档</strong></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>[更新]<span> </span>日志文档、静态类文档、数据校验文档、Worker Service 文档</li> 
   </ul> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            