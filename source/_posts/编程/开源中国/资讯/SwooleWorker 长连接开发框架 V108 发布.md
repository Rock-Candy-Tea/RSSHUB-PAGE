
---
title: 'SwooleWorker 长连接开发框架 V1.0.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 21:17:00 GMT
thumbnail: 'https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67'
---

<div>   
<div class="content">
                                                                    
                                                        <pre style="text-align:start">  _____                    _   __          __        _
 / ____<span style="color:var(--color-prettylights-syntax-keyword)">|</span>                  <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>  \ \        / /       <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>           ®
<span style="color:var(--color-prettylights-syntax-keyword)">|</span> (_____      _____   ___ <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span> __\ \  /\  / /__  _ __<span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span> _____ _ __
 \___ \ \ /\ / / _ \ / _ \| <span style="color:var(--color-prettylights-syntax-keyword)">|</span>/ _ \ \/  \/ / _ \| <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">'</span>__| |/ / _ \ <span style="color:var(--color-prettylights-syntax-string)">'</span></span>__<span style="color:var(--color-prettylights-syntax-keyword)">|</span>
 ____) \ V  V / (_) <span style="color:var(--color-prettylights-syntax-keyword)">|</span> (_) <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>  __/\  /\  / (_) <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>  <span style="color:var(--color-prettylights-syntax-keyword)">|</span>   <span style="color:var(--color-prettylights-syntax-keyword)"><</span>  __/ <span style="color:var(--color-prettylights-syntax-keyword)">|</span>
<span style="color:var(--color-prettylights-syntax-keyword)">|</span>_____/ \_/\_/ \___/ \___/<span style="color:var(--color-prettylights-syntax-keyword)">|</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>\___<span style="color:var(--color-prettylights-syntax-keyword)">|</span> \/  \/ \___/<span style="color:var(--color-prettylights-syntax-keyword)">|</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>  <span style="color:var(--color-prettylights-syntax-keyword)">|</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>\_\___<span style="color:var(--color-prettylights-syntax-keyword)">|</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>

=================================================
SwooleWorker is a distributed long connection
development framework based on Swoole4.

[Github] https://github.com/xielei/swoole-worker
=================================================

Press [Ctrl+C] to exit, send <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">'</span>help<span style="color:var(--color-prettylights-syntax-string)">'</span></span> to show help.
<span style="color:var(--color-prettylights-syntax-keyword)">></span> </pre> 
<p><span style="background-color:#ffffff; color:#24292f">SwooleWorker是基于swoole4开发的一款分布式长连接开发框架。常驻内存，协程，高性能高并发；分布式部署，横向扩容，使得能支持庞大的连接数；无感知安全重启，无缝升级代码；接口丰富，支持单个发送，分组发送，群发广播等接口。可广泛应用于云计算、物联网（IOT）、车联网、智能家居、网络游戏等领域。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35%2F68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67" target="_blank"><img alt="架构图" src="https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:start">基本接口</h2> 
<table cellspacing="0" style="width:max-content"> 
 <thead> 
  <tr> 
   <th>接口</th> 
   <th>参数</th> 
   <th>返回值</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>sendToClient</td> 
   <td>string $client, string $message</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>sendToUid</td> 
   <td>string $uid, string $message, array $without_client_list = []</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>sendToGroup</td> 
   <td>string $group, string $message, array $without_client_list = []</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>sendToAll</td> 
   <td>string $message, array $without_client_list = []</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>isOnline</td> 
   <td>string $client</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>isUidOnline</td> 
   <td>string $uid</td> 
   <td>bool</td> 
  </tr> 
  <tr> 
   <td>getClientListByGroup</td> 
   <td>string $group, string $prev_client = null</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getClientCount</td> 
   <td> </td> 
   <td>int</td> 
  </tr> 
  <tr> 
   <td>getClientCountByGroup</td> 
   <td>string $group</td> 
   <td>int</td> 
  </tr> 
  <tr> 
   <td>getClientList</td> 
   <td>string $prev_client = null</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getClientListByUid</td> 
   <td>string $uid, string $prev_client = null</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getClientInfo</td> 
   <td>string $client, int $type = 255</td> 
   <td>array</td> 
  </tr> 
  <tr> 
   <td>getUidListByGroup</td> 
   <td>string $group, bool $unique = true</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getUidList</td> 
   <td>bool $unique = true</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getUidCount</td> 
   <td>float $unique_percent = null</td> 
   <td>int</td> 
  </tr> 
  <tr> 
   <td>getGroupList</td> 
   <td>bool $unique = true</td> 
   <td>iterable</td> 
  </tr> 
  <tr> 
   <td>getUidCountByGroup</td> 
   <td>string $group</td> 
   <td>int</td> 
  </tr> 
  <tr> 
   <td>closeClient</td> 
   <td>string $client, bool $force = false</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>bindUid</td> 
   <td>string $client, string $uid</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>unBindUid</td> 
   <td>string $client</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>joinGroup</td> 
   <td>string $client, string $group</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>leaveGroup</td> 
   <td>string $client, string $group</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>unGroup</td> 
   <td>string $group</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>setSession</td> 
   <td>string $client, array $session</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>updateSession</td> 
   <td>string $client, array $session</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>deleteSession</td> 
   <td>string $client</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>getSession</td> 
   <td>string $client</td> 
   <td>?array</td> 
  </tr> 
 </tbody> 
</table> 
<h2> 更新日志 V1.0.8</h2> 
<ul> 
 <li>新增 客户端限流配置</li> 
 <li>新增 HttpApi接口 方便和其他系统整合</li> 
</ul>
                                        </div>
                                      
</div>
            