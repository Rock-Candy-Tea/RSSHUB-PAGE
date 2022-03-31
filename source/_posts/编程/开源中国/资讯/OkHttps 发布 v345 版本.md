
---
title: 'OkHttps 发布 v3.4.5 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7943'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 14:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7943'
---

<div>   
<div class="content">
                                                                    
                                                        <h4>更新内容：</h4> 
<ol> 
 <li>【修复】当 Stomp 的<span> </span><code>connect()</code><span> </span>与<span> </span><code>disconnect(true)</code><span> </span>被依次快速调用时，可能会报 "You must call connect before send" 异常的问题:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fejlchina%2Fokhttps%2Fissues%2F59" target="_blank">https://github.com/ejlchina/okhttps/issues/59</a></li> 
 <li>【优化】Stomp 的<span> </span><code>isConnected()</code><span> </span>方法：当内部的 websocket 连接被主动断开时，该方法立即返回<span> </span><code>false</code></li> 
 <li>【优化】Stomp 的 订阅机制 与 状态判断逻辑。</li> 
</ol> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">用到 Stomp 功能的同学可升级。</p> 
</blockquote> 
<p><span style="background-color:#ffffff; color:#17181a">OkHttps 是一个前后端通用的 HTTP 客户端，同时支持 WebSocket 与 Stomp 协议:</span></p> 
<p><span style="background-color:#ffffff; color:#333333">https://github.com/ejlchina/okhttps</span><br> <span style="background-color:#ffffff; color:#333333">https://gitee.com/ejlchina-zhxu/okhttps</span><br> <span style="background-color:#ffffff; color:#333333">https://okhttps.ejlchina.com/</span></p> 
<p><span style="background-color:#ffffff; color:#17181a">如果觉得还不错，顺手点个 STAR 吧。</span></p>
                                        </div>
                                      
</div>
            