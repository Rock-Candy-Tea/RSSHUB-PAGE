
---
title: 'xRedis 1.5.0 发布，Redis 的 C++ 客户端库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=209'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 00:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=209'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">xRedis 1.5.0 版本发布！</p> 
<p style="text-align:left"><a href="http://www.oschina.net/p/xredis" target="_blank">xRedis </a>是一个 C++ 开发的 redis 客户端，是对 hiredis 的 C++ 封装，提供易用的 redis 操作接口。</p> 
<p style="text-align:start"><em><strong>功能与特点：</strong></em></p> 
<ul> 
 <li>支持数据多节点分布存储，可自定义分片规则;</li> 
 <li>支持同时连接到每个分片的主从节点，支持主从读写分离;</li> 
 <li>支持对每个存储节点建立连接池;</li> 
 <li>支持同时连接多个数据分片集群;</li> 
 <li>支持连接到官方集群，支持自动计算节点索引位置,支持REDIS集群节点变化连接自动切换; 当官方集群节点有添加/删除/slot分布变化时，到集群的连接池会自动更新。</li> 
 <li>提供简单易用的C++接口封装，已实现大部分REDIS命令;</li> 
 <li>只依赖hiredis库;</li> 
 <li>多线程安全</li> 
 <li>支持带密码连接;</li> 
 <li>支持linux、windows平台</li> 
</ul> 
<p style="text-align:left">release 1.5.0 更新:</p> 
<ol> 
 <li> <p><span style="background-color:#ffffff; color:#24292e">支持自动计算节点索引位置,支持REDIS集群节点变化连接自动切换; 当官方集群节点有添加/删除/slot分布变化时，到集群的连接池会自动更新。</span> </p> </li> 
 <li> <p>修复redis官方集群连接重连接BUG。</p> </li> 
 <li> <p>xRedis添加内部日志模块。</p> </li> 
</ol> 
<p style="text-align:left">更多内容见：</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F0xsky%2Fxredis" target="_blank">https://github.com/0xsky/xredis</a></p>
                                        </div>
                                      
</div>
            