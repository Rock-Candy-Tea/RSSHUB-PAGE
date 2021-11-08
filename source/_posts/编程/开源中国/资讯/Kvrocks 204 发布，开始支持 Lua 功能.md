
---
title: 'Kvrocks 2.0.4 发布，开始支持 Lua 功能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7077'
author: 开源中国
comments: false
date: Mon, 08 Nov 2021 09:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7077'
---

<div>   
<div class="content">
                                                                                            <p style="color:#b8bfc6; text-align:start"><span style="color:#000000">Kvrocks 发布 v2.0.4， 开始支持 Lua 功能和多 Column Family 共享缓存功能， 变更如下:</span></p> 
<p style="color:#b8bfc6; text-align:start"><strong><span style="color:#000000">新特性</span></strong></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 Lua 脚本，目前除了 script kill/debug，其他命令已经全部支持，其中包含 eval、evalsha 以及 script 命令</span></p> </li> 
</ul> 
<p style="text-align:start"><span style="color:#000000"><strong>优化点</strong></span> </p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持 Colunm Family 之间共享缓存，新版本已经默认开启。该配置可以提高缓存命中率，从而提高查询性能</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Info 命令输出增加 master_repl_offset 字段</span></p> </li> 
</ul> 
<p style="text-align:start"><span style="color:#000000"><strong>问题修复</strong></span></p> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复动态调整的 RocksDB 配置项 target_file_size_base 只对部分 Column Family 生效</span></p> </li> 
</ul> 
<p><span><span style="color:#000000"><strong>GitHub：</strong></span></span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKvrocksLabs%2Fkvrocks%2Freleases%2Ftag%2Fv2.0.4" target="_blank">https://github.com/KvrocksLabs/kvrocks/releases/tag/v2.0.4</a></span></p>
                                        </div>
                                      
</div>
            