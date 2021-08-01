
---
title: 'SwooleWorker 长连接开发框架 V1.0.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67'
author: 开源中国
comments: false
date: Sat, 31 Jul 2021 10:29:00 GMT
thumbnail: 'https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67'
---

<div>   
<div class="content">
                                                                                            <pre style="text-align:start">  <span style="color:#032f62">_____</span>                    <span style="color:#032f62">_   _</span><span style="color:#032f62">_          _</span><span style="color:#032f62">_        _</span>
 / <span style="color:#032f62">___</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>                  <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>  \ \        / /       <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span>           ®
<span style="color:var(--color-prettylights-syntax-keyword)">|</span> (<span style="color:#032f62">_____</span>      <span style="color:#032f62">_____</span>   <span style="color:#032f62">___ </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> __</span>\ \  /\  / /<span style="color:#032f62">__  _ __</span><span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:var(--color-prettylights-syntax-keyword)">|</span> <span style="color:#032f62">_____</span> <span style="color:#032f62">_ _</span>_
 \<span style="color:#032f62">___ \ \ /\ / / _ \ / _ \| </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">/ _ \ \/  \/ / _ \| </span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'</span></span><span style="color:#032f62">__</span>| |/ / <span style="color:#032f62">_ \ </span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">'</span></span></span><span style="color:#032f62">_</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>
 <span style="color:#032f62">____) \ V  V / (_) </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> (_) </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">  __</span>/\  /\  / (<span style="color:#032f62">_) </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">  </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">   </span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62"><</span></span><span style="color:#032f62">  _</span>_/ <span style="color:var(--color-prettylights-syntax-keyword)">|</span>
<span style="color:var(--color-prettylights-syntax-keyword)">|</span><span style="color:#032f62">_____</span>/ \<span style="color:#032f62">_/\_</span>/ \<span style="color:#032f62">___/ \__</span><span style="color:#032f62">_/</span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">_</span><span style="color:var(--color-prettylights-syntax-keyword)">|</span>\<span style="color:#032f62">___</span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62"> \/  \/ \__</span><span style="color:#032f62">_/</span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">_</span><span style="color:var(--color-prettylights-syntax-keyword)">|</span>  <span style="color:var(--color-prettylights-syntax-keyword)">|</span><span style="color:#032f62">_</span><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">|</span></span><span style="color:#032f62">\_</span>\<span style="color:#032f62">___</span><span style="color:var(--color-prettylights-syntax-keyword)">|</span>_<span style="color:var(--color-prettylights-syntax-keyword)">|</span>

=================================================
SwooleWorker is a distributed long connection
development framework based on Swoole4.

<span style="color:#22863a">[HomePage] https://swoole.plus
=================================================</span>

Press [Ctrl+C] to exit, send <span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">'</span>help<span style="color:var(--color-prettylights-syntax-string)">'</span></span> to show help.
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#032f62">></span></span><span style="color:#032f62"> </span></pre> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#24292f">SwooleWorker是基于swoole4开发的一款分布式长连接开发框架。常驻内存，协程，高性能高并发；分布式部署，横向扩容，使得能支持庞大的连接数；无感知安全重启，无缝升级代码；接口丰富，支持单个发送，分组发送，群发广播等接口。可广泛应用于云计算、物联网（IOT）、车联网、智能家居、网络游戏等领域。</span></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#24292f">【官方网站】<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswoole.plus" target="_blank">https://swoole.plus</a></span></p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35%2F68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67" target="_blank"><img alt="架构图" src="https://camo.githubusercontent.com/7583a650f84363177c315c9a516924245ac5f83ff612feadb3d82dcf741f3e35/68747470733a2f2f7374617469632e6562636d732e636f6d2f696d672f73772e706e67" referrerpolicy="no-referrer"></a></p> 
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
   <td style="border-color:#dddddd">sendToClient</td> 
   <td style="border-color:#dddddd">string $client, string $message</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">sendToUid</td> 
   <td style="border-color:#dddddd">string $uid, string $message, array $without_client_list = []</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">sendToGroup</td> 
   <td style="border-color:#dddddd">string $group, string $message, array $without_client_list = []</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">sendToAll</td> 
   <td style="border-color:#dddddd">string $message, array $without_client_list = []</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">isOnline</td> 
   <td style="border-color:#dddddd">string $client</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">isUidOnline</td> 
   <td style="border-color:#dddddd">string $uid</td> 
   <td style="border-color:#dddddd">bool</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientListByGroup</td> 
   <td style="border-color:#dddddd">string $group, string $prev_client = null</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientCount</td> 
   <td style="border-color:#dddddd"> </td> 
   <td style="border-color:#dddddd">int</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientCountByGroup</td> 
   <td style="border-color:#dddddd">string $group</td> 
   <td style="border-color:#dddddd">int</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientList</td> 
   <td style="border-color:#dddddd">string $prev_client = null</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientListByUid</td> 
   <td style="border-color:#dddddd">string $uid, string $prev_client = null</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getClientInfo</td> 
   <td style="border-color:#dddddd">string $client, int $type = 255</td> 
   <td style="border-color:#dddddd">array</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getUidListByGroup</td> 
   <td style="border-color:#dddddd">string $group, bool $unique = true</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getUidList</td> 
   <td style="border-color:#dddddd">bool $unique = true</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getUidCount</td> 
   <td style="border-color:#dddddd">float $unique_percent = null</td> 
   <td style="border-color:#dddddd">int</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getGroupList</td> 
   <td style="border-color:#dddddd">bool $unique = true</td> 
   <td style="border-color:#dddddd">iterable</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getUidCountByGroup</td> 
   <td style="border-color:#dddddd">string $group</td> 
   <td style="border-color:#dddddd">int</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">closeClient</td> 
   <td style="border-color:#dddddd">string $client, bool $force = false</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">bindUid</td> 
   <td style="border-color:#dddddd">string $client, string $uid</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">unBindUid</td> 
   <td style="border-color:#dddddd">string $client</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">joinGroup</td> 
   <td style="border-color:#dddddd">string $client, string $group</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">leaveGroup</td> 
   <td style="border-color:#dddddd">string $client, string $group</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">unGroup</td> 
   <td style="border-color:#dddddd">string $group</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">setSession</td> 
   <td style="border-color:#dddddd">string $client, array $session</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">updateSession</td> 
   <td style="border-color:#dddddd">string $client, array $session</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">deleteSession</td> 
   <td style="border-color:#dddddd">string $client</td> 
   <td style="border-color:#dddddd"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">getSession</td> 
   <td style="border-color:#dddddd">string $client</td> 
   <td style="border-color:#dddddd">?array</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">更新日志 V1.0.9</h2> 
<ul> 
 <li>可开启或关闭限流服务</li> 
 <li>限流服务由针对fd变更为针对ip</li> 
</ul>
                                        </div>
                                      
</div>
            