
---
title: 'Jedis 4.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7553'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7553'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Jedis 是 Redis 的一个 Java 客户端库，旨在提高性能和易用性。Jedis 与 redis 2.8.x、3.xx 及更高版本完全兼容。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持 GEOSEARCH 和 GEOSEARCHSTORE 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2771" target="_blank">#2771</a>)</li> 
 <li>支持新的 ZRANGE(STORE) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2817" target="_blank">#2817</a>)</li> 
 <li>在 pipeline 中添加数据库和其他一些命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2832" target="_blank">#2832</a>)</li> 
 <li>在 JedisCluster（UnifiedJedis）中订阅 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2828" target="_blank">#2828</a>)</li> 
 <li>支持集群 addlotsrange 和集群 delslotsrange (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2823" target="_blank">#2823</a>)</li> 
 <li>支持 CLUSTER LINKS 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2776" target="_blank">#2776</a>)</li> 
 <li>为 bitcount（binary）增加了 BYTE|BIT 选项(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2768" target="_blank">#2768</a>)</li> 
 <li>为 bitcount（string）增加了 BYTE|BIT 选项 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2779" target="_blank">#2779</a>)</li> 
 <li>支持 SHUTDOWN [NOW] [FORCE] [ABORT] 参数 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2812" target="_blank">#2812</a>)</li> 
 <li>支持 XINFO STREAM FULL (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2746" target="_blank">#2746</a>)</li> 
 <li>改变地址 ACL V2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2841" target="_blank">#2841</a>)</li> 
 <li>支持 REPLICAOF 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2811" target="_blank">#2811</a>)</li> 
 <li>支持 LOLWUT 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2800" target="_blank">#2800</a>)</li> 
 <li>支持 SINTERCARD 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2821" target="_blank">#2821</a>)</li> 
 <li>支持 SORT_RO (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2843" target="_blank">#2843</a>)</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>使用 DNS 名称创建与主机的连接时，尝试 DNS 服务器能够解析的所有地址 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2722" target="_blank">#2722</a>)</li> 
 <li>修复事务中的 StackOverflowError (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2827" target="_blank">#2827</a>)</li> 
 <li>优化 XINFO STREAM FULL 实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fpull%2F2801" target="_blank">#2801</a>)</li> 
 <li>弃用未使用的接口 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Fcommit%2Fafcce7c1fc15732a2e4820b5e0ad58ac34053a1e" target="_blank">afcce7c</a>)</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fjedis%2Freleases%2Ftag%2Fv4.1.0" target="_blank">https://github.com/redis/jedis/releases/tag/v4.1.0</a></p>
                                        </div>
                                      
</div>
            