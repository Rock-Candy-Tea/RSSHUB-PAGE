
---
title: '移动端开源 IM 框架 MobileIMSDK v6.1 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg'
author: 开源中国
comments: false
date: Mon, 02 Aug 2021 14:15:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:left"><strong>一、更新内容简介</strong></h3> 
<p style="text-align:left">本次更新为次要版本更新，进行了若干优化（<span style="color:#999999">更新历史详见：</span><a href="https://gitee.com/jackjiang/MobileIMSDK/tree/master/release_notes">码云 Release Nodes</a>）。可能是市面上唯一同时支持UDP+TCP+WebSocket三种协议的同类开源IM框架。</p> 
<h3 style="text-align:left"><strong>二、MobileIMSDK简介</strong></h3> 
<p style="text-align:left"><img alt height="53" src="https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg" width="338" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><a href="https://gitee.com/jackjiang/MobileIMSDK">MobileIMSDK</a>是一套专为移动端开发的原创IM通信层框架：</strong></p> 
<ul> 
 <li>历经8年、久经考验；</li> 
 <li>超轻量级、高度提炼，lib包50KB以内；</li> 
 <li>精心封装，一套API同时支持UDP、TCP、WebSocket 三种协议（可能是全网唯一开源的）；</li> 
 <li>客户端支持iOS、Android、标准Java平台、H5(稍后开源)、小程序(开发中..)、Uniap(开发中..)；</li> 
 <li>服务端基于Netty，性能卓越、易于扩展；<img alt="👈" height="14" src="https://gitee.com/assets/emoji/point_left-4570b6929b8880ab2e8b8031007fef18.png" width="14" referrerpolicy="no-referrer"></li> 
 <li>可与姊妹工程 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-959-1-1.html" target="_blank">MobileIMSDK-Web</a> 无缝互通实现网页端聊天或推送等；<img alt="👈" height="14" src="https://gitee.com/assets/emoji/point_left-4570b6929b8880ab2e8b8031007fef18.png" width="14" referrerpolicy="no-referrer"></li> 
 <li>可应用于跨设备、跨网络的聊天APP、企业OA、消息推送等各种场景。</li> 
</ul> 
<p style="text-align:left">MobileIMSDK工程始于2013年10月（2021年07月30日发布了最新版v6.1），起初用作某产品的即时通讯底层实现，完全从零开发。</p> 
<p style="text-align:left">您可能需要：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-60-1-1.html" target="_blank">查看更多关于MobileIMSDK的疑问及解答</a>。</p> 
<h3 style="text-align:left"><strong>三、代码托管同步更新</strong></h3> 
<p style="text-align:left"><strong><strong>OsChina.net</strong></strong></p> 
<ul> 
 <li> <p>代码托管： <a href="http://git.oschina.net/jackjiang/MobileIMSDK">http://git.oschina.net/jackjiang/MobileIMSDK</a></p> </li> 
 <li> <p>项目资料： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fforum-89-1.html" target="_blank">点击查看更多资料</a></p> </li> 
</ul> 
<p style="text-align:left"><strong>GitHub.com</strong></p> 
<ul> 
 <li> <p>代码托管： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJackJiang2011%2FMobileIMSDK" target="_blank">https://github.com/JackJiang2011/MobileIMSDK</a></p> </li> 
 <li> <p>项目资料： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fforum-89-1.html" target="_blank">点击查看更多资料</a></p> </li> 
</ul> 
<h3 style="text-align:left"><strong>四、MobileIMSDK设计目标</strong></h3> 
<p style="text-align:left">让开发者专注于应用逻辑的开发，底层复杂的即时通讯算法交由SDK开发人员，从而解偶即时通讯应用开发的复杂性。</p> 
<h3 style="text-align:left"><strong>五、MobileIMSDK框架组成</strong></h3> 
<p style="text-align:left"><strong>整套MobileIMSDK框架由以下6部分组成：</strong></p> 
<ol> 
 <li><strong>Android客户端SDK：</strong>用于Android版即时通讯客户端，支持Android 2.3及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fandroid%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>iOS客户端SDK：</strong>用于开发iOS版即时通讯客户端，支持iOS 8.0及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fios%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>Java客户端SDK：</strong>用于开发跨平台的PC端即时通讯客户端，支持Java 1.6及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fjava%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>H5客户端SDK：</strong>（暂未开源）</li> 
 <li><strong>小程序客户端SDK：（</strong>开发中...）</li> 
 <li><strong>服务端SDK：</strong>用于开发即时通讯服务端，支持Java 1.7及以上版本，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fserver%2F" target="_blank">查看API文档</a>。</li> 
</ol> 
<p style="text-align:left"><strong>另：</strong>MobileIMSDK-Web版为独立工程，如有需要请联系作者。</p> 
<h3 style="text-align:left"><strong>六、MobileIMSDK v6.1更新内容</strong></h3> 
<p style="text-align:left"><strong>【重要说明】：</strong></p> 
<blockquote> 
 <p>MobileIMSDK v6.1 为次要版本，进行了若干优化。详见：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-1270-1-1.html" target="_blank">http://www.52im.net/thread-1270-1-1.html</a></p> 
</blockquote> 
<p style="text-align:left"><strong>【其它优化和提升】：</strong></p> 
<ul> 
 <li>1. 重新设计了心跳算法逻辑，断网感知速度提升1倍；</li> 
 <li>2. 增加了5S心跳模式；</li> 
 <li>3. 优化了客户端Demo中关于网络连接状态图标的显示。</li> 
</ul>
                                        </div>
                                      
</div>
            