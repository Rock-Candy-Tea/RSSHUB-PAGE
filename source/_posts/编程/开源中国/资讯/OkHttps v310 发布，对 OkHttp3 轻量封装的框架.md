
---
title: 'OkHttps v3.1.0 发布，对 OkHttp3 轻量封装的框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=342'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 08:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=342'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OkHttps v3.1.0 已经发布，这是一个对 OkHttp3 轻量封装的框架。</p> 
<p>此版本更新内容包括：</p> 
<ol> 
 <li>类 <code>OkHttps</code> 与 <code>HttpUtils</code> 开放 <code>getHttp()</code> 方法</li> 
 <li>类 <code>WebSocketTask</code> 新增 <code>close</code> 方法，用于关闭当前连接</li> 
 <li>优化 <code>WebSocketTask</code>：同一时间只能建立一个连接，如果已经建立连接并未断开，重复调用 <code>listen()</code> 方法将直接返回原有连接</li> 
 <li>类 <code>Stomp</code> 新增 <code>disconnect(int maxWaitSeconds)</code> 方法</li> 
 <li>类 <code>Stomp</code> 新增 <code>disconnect(boolean immediate)</code> 方法，用于立即断开连接</li> 
 <li>类 <code>Stomp</code> 新增 <code>isConnecting()</code> 与 <code>isDisconnecting()</code> 方法</li> 
 <li>Stomp 模块抽象出 <code>MsgCodec</code> 接口，使得编解码模块易于扩展</li> 
 <li>Stomp 模块新增 <code>MsgCodecImpl</code> 实现类，并实现了半包粘包处理逻辑</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/ejlchina-zhxu/okhttps/releases/v3.1.0">https://gitee.com/ejlchina-zhxu/okhttps/releases/v3.1.0</a></p>
                                        </div>
                                      
</div>
            