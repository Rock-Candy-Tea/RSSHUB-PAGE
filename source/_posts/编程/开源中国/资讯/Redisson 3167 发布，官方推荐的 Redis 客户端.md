
---
title: 'Redisson 3.16.7 发布，官方推荐的 Redis 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4875'
author: 开源中国
comments: false
date: Sat, 25 Dec 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4875'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0"> 
    <div style="margin-left:0; margin-right:0"> 
     <div style="margin-left:0; margin-right:0"> 
      <p style="margin-left:0; margin-right:0">Redisson 3.16.7 已发布，这是一个 Java 编写的 Redis 客户端，具备驻内存数据网格（In-Memory Data Grid）功能，并获得了 Redis 的官方推荐。</p> 
      <p style="margin-left:0; margin-right:0">此版本更新内容如下：</p> 
      <ul style="margin-left:0; margin-right:0"> 
       <li>修复<span> </span><span style="color:#2e3033"><code>RScript.scriptLoad()</code><span> </span>方法不会将脚本加载到 Slave 节点的问题</span></li> 
       <li><span style="color:#2e3033">Spring Data RedissonConnection 评估现在会使用 ByteArrayCodec</span></li> 
       <li><span style="color:#2e3033">修复<span> </span><code>RSet.distributedIterator()</code><span> </span>和<span> </span><code>RScoredSortedSet.distributedIterator()</code><span> </span>方法抛出脚本错误的问题</span></li> 
       <li><span style="color:#2e3033">修复 RLock 对象中没有检查同步的 slave 数量的问题</span></li> 
       <li><span style="color:#2e3033">修复哨兵模式（</span>sentinel mode<span style="color:#2e3033">）下解析主机名时出现竞争状态，可能导致从机关闭的问题</span></li> 
       <li><span style="color:#2e3033">修复了 如果 slave 在 MasterSlave 模式下未定义，并且<span> </span><code>readMode != MASTER</code>，则会抛出错误的问题</span></li> 
       <li><span style="color:#2e3033">在单节点模式下，主节点不应该被初始化为从节点</span></li> 
       <li><span style="color:#2e3033">修复复制状态（</span><span style="color:#24292f">replicated mode</span><span style="color:#2e3033">）下出现的<span> </span></span><code>can't find node</code><span> </span>错误</li> 
      </ul> 
      <p style="margin-left:0; margin-right:0"><span style="color:#2e3033">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Freleases%2Ftag%2Fredisson-3.16.7" target="_blank">https://github.com/redisson/redisson/releases/tag/redisson-3.16.7</a></p> 
     </div> 
    </div> 
   </div> 
   <p style="margin-left:0; margin-right:0"> </p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            