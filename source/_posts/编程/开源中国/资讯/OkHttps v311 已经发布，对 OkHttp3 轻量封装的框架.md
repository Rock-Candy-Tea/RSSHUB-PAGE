
---
title: 'OkHttps v3.1.1 已经发布，对 OkHttp3 轻量封装的框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9526'
author: 开源中国
comments: false
date: Sat, 19 Jun 2021 13:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9526'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OkHttps v3.1.1 已经发布，对 OkHttp3 轻量封装的框架</p> 
<p>此版本更新内容包括：</p> 
<ol> 
 <li>新增：Stomp 异常回调：<code>setOnException(OnCallback<Throwable> onException)</code></li> 
 <li>优化：<code>AynscHttpTask</code>、<code>WebsocketTask</code>、<code>Stomp</code> 保证各回调设置方法的线程安全</li> 
 <li>修复：在 Android 5 系统上使用 Stomp 在断开连接时出现 找不到 Class 的问题</li> 
 <li>修复：在未设置 <code>onConnected</code> 回调时，Stmop 连接成功 但 <code>isConnecting()</code> 方法仍然返回 <code>true</code> 的问题</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/ejlchina-zhxu/okhttps/releases/v3.1.1">https://gitee.com/ejlchina-zhxu/okhttps/releases/v3.1.1</a></p>
                                        </div>
                                      
</div>
            