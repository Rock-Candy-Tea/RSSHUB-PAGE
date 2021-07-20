
---
title: '移动端开源 IM 框架 MobileIMSDK v6.0 发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 15:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:left"><strong>一、更新内容简介</strong></h3> 
<p style="text-align:left">本次为主要版本更新（<span style="color:#e74c3c">本次更新内容见文末“MobileIMSDK v6.0更新内容 ”一节</span>），强势升级，将同时支持<span style="color:#4e5f70"><strong>TCP、UDP、WebSocket</strong></span>三种协议，精心封装之下，实现同一套API、三种协议同时并存。可能是市面上唯一同时支持<span style="color:#4e5f70"><strong>UDP+TCP+WebSocket</strong></span>三种协议的同类开源IM框架。</p> 
<h3 style="text-align:left"><strong>二、MobileIMSDK简介</strong></h3> 
<p style="text-align:left"><img alt height="53" src="https://oscimg.oschina.net/oscnet/d4acb10eea465b539ca98a1a1b229aa6ab9.jpg" width="338" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong><a href="https://gitee.com/jackjiang/MobileIMSDK">MobileIMSDK</a> 是一套专为移动端开发的原创IM通信层框架：</strong></p> 
<ul> 
 <li>历经8年、久经考验；</li> 
 <li>超轻量级、高度提炼，lib包50KB以内；</li> 
 <li>精心封装，一套API同时支持UDP、TCP、WebSocket三种协议（可能是全网唯一开源的）；</li> 
 <li>客户端支持 <strong>iOS</strong>、<strong>Android</strong>、<strong>标准Java</strong>、<strong>H5</strong>、<strong>小程序</strong>(<span style="color:#999999">开发中..</span>)、<strong>Uniapp</strong>(<span style="color:#999999">开发中..</span>)；</li> 
 <li>服务端基于Netty，性能卓越、易于扩展；<img alt="👈" height="14" src="https://gitee.com/assets/emoji/point_left-4570b6929b8880ab2e8b8031007fef18.png" width="14" referrerpolicy="no-referrer"></li> 
 <li>可与姊妹工程 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-959-1-1.html" target="_blank">MobileIMSDK-Web</a> 无缝互通实现网页端聊天或推送等；<img alt="👈" height="14" src="https://gitee.com/assets/emoji/point_left-4570b6929b8880ab2e8b8031007fef18.png" width="14" referrerpolicy="no-referrer"></li> 
 <li>可应用于跨设备、跨网络的聊天APP、企业OA、消息推送等各种场景。</li> 
</ul> 
<p style="text-align:left">MobileIMSDK工程始于2013年10月，起初用作某产品的即时通讯底层实现，<span style="color:#e74c3c">完全从零开发，技术自主可控！</span></p> 
<p style="text-align:left"><strong>您可能需要：</strong><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-60-1-1.html" target="_blank">查看关于MobileIMSDK的</a><a href="https://gitee.com/jackjiang/MobileIMSDK/blob/master/README.md">详细介绍</a>。</p> 
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
<p style="text-align:left"><strong>整套MobileIMSDK框架由以下5部分组成：</strong></p> 
<ol> 
 <li><strong>Android客户端SDK：</strong>用于Android版即时通讯客户端，支持Android 2.3及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fandroid%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>iOS客户端SDK：</strong>用于开发iOS版即时通讯客户端，支持iOS 8.0及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fios%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>Java客户端SDK：</strong>用于开发跨平台的PC端即时通讯客户端，支持Java 1.6及以上，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fjava%2F" target="_blank">查看API文档</a>；</li> 
 <li><strong>H5客户端SDK：</strong>资料整理中，不日正式发布；</li> 
 <li><strong>服务端SDK：</strong>用于开发即时通讯服务端，支持Java 1.7及以上版本，<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.52im.net%2Fextend%2Fdocs%2Fapi%2Fmobileimsdk%2Fserver%2F" target="_blank">查看API文档</a>。</li> 
</ol> 
<p style="text-align:left"><strong>另：</strong>MobileIMSDK-Web版为独立工程，如有需要请联系作者。</p> 
<h3 style="text-align:left"><strong>六、MobileIMSDK v6.0更新内容 </strong></h3> 
<p style="text-align:left"><strong>【重要说明】：</strong></p> 
<blockquote> 
 <p><span style="color:#40485b"><span style="background-color:null">MobileIMSDK v6 为全新版本，新增了对WebSocket协议的优雅支持、多端互踢支持等！ </span></span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.52im.net%2Fthread-3630-1-1.html" target="_blank">查看详情</a></p> 
</blockquote> 
<p style="text-align:left"><strong>【新增重要特性】：</strong></p> 
<ol> 
 <li>服务端新增WebSocket协议支持，一套API优雅支持TCP、UDP、WebSocket 3种协议；</li> 
 <li>支持多端互踢功能（可应对复杂的移动端网络变动逻辑对多端互踢算法的影响）；</li> 
</ol> 
<p style="text-align:left"><strong>【解决的Bug】：</strong></p> 
<ol> 
 <li>[Andriod]解决了断线后，fireDisconnectedToServer()方法中的一处空指针隐患；</li> 
 <li>[iOS] 修复了TCP版代码中，调用[ClientCoreSDK releaseCore]方法会触发自动登陆逻辑的bug；</li> 
 <li>[服务端] 解决了UDP协议下，重连情况下的被踢者已被服务端注销会话后，客户端才发回登陆响应ACK应答，导致服务端错误地向未被踢者发出已登陆者重复登陆响应的问题；</li> 
</ol> 
<p style="text-align:left"><strong>【其它优化和提升】：</strong></p> 
<ol> 
 <li>[Andriod]废弃了SDK、Demo代码中的所有AsyncTask的使用；</li> 
 <li>[Andriod]将所有可使用Lambda表达式的代码全部用Lambda进行了简化。</li> 
 <li>[iOS] 解决了XCode12上编译SDK的.a包，打包成胖子.a时报“have the same architectures (arm64) and can't be in the same fat output file”的问题；</li> 
 <li>[iOS] Demo中所有使用过时的UIAlertView改为UIAlertController实现；</li> 
 <li>[iOS] 解决了iOS端SDK工程中两处因类名重构导致的在XCode12.5.1上编译出错。</li> 
 <li>[服务端] 将服务端Demo中的Log4j日志框架升级为最新的Log4j2；</li> 
 <li>[服务端] 服务端可控制是否为每条消息生成发送时间戳（可辅助用于客户端的消息排序逻辑等）。</li> 
</ol>
                                        </div>
                                      
</div>
            