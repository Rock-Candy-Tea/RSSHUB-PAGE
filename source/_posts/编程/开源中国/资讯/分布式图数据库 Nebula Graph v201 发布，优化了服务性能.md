
---
title: '分布式图数据库 Nebula Graph v2.0.1 发布，优化了服务性能'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://discuss-cdn.nebula-graph.com.cn/uploads/default/optimized/2X/6/6fb8b27d36947c06d29523546297e33c4c47bb7e_2_690x293.jpeg'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 16:15:00 GMT
thumbnail: 'https://discuss-cdn.nebula-graph.com.cn/uploads/default/optimized/2X/6/6fb8b27d36947c06d29523546297e33c4c47bb7e_2_690x293.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start">
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiscuss-cdn.nebula-graph.com.cn%2Fuploads%2Fdefault%2Foriginal%2F2X%2F6%2F6fb8b27d36947c06d29523546297e33c4c47bb7e.jpeg" target="_blank"><img alt="Release note" height="293" src="https://discuss-cdn.nebula-graph.com.cn/uploads/default/optimized/2X/6/6fb8b27d36947c06d29523546297e33c4c47bb7e_2_690x293.jpeg" width="690" referrerpolicy="no-referrer"></a> 
 <div>
   
 </div> 
</div> 
<p style="text-align:start">Nebula Graph v2.0.1 主要优化服务性能，修复了一些已知 bug。</p> 
<h2 style="text-align:start">Improvements</h2> 
<ul> 
 <li>优化了 <code>StorageClient</code>，提高了服务性能，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F468" target="_blank">#468 <span style="background-color:var(--primary-low); color:var(--primary-medium)">1</span></a></li> 
 <li>增加 HTTP <code>GetFlags</code> 接口对无符号整型的支持，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F469" target="_blank">#469</a></li> 
 <li>增加对 Raft Listener 和 Storage Service IP/Port 的冲突检查，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F875" target="_blank">#875</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F470" target="_blank">#468</a></li> 
</ul> 
<h2 style="text-align:start">Bugfix</h2> 
<ul> 
 <li>修复了 <code>GO</code> 在特殊场景下未返回起点属性的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F859" target="_blank">#859</a></li> 
 <li>修复了以某些方式启动服务时，因 <code>logs</code> 目录不存在导致启动失败的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F873" target="_blank">#873</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F403" target="_blank">#403</a></li> 
 <li>修复了 <code>FIND SHORTEST PATH xxx UPTO N STEPS</code> 当 N 为奇数步时，返回了 N+1 步路径的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F912" target="_blank">#912</a></li> 
 <li>修复了使用其它语句的输出作为<code>DELETE</code>语句的输入时，返回 <code>SementicError</code> 的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F917" target="_blank">#917 <span style="background-color:var(--primary-low); color:var(--primary-medium)">1</span></a></li> 
 <li>修复了聚合函数的默认返回值与 openCypher 不一致的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F901" target="_blank">#901</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F480" target="_blank">#480</a></li> 
 <li>修复了集群模式下，<code>GetNeighborsIter</code> 接口返回部分结果的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F922" target="_blank">#922</a></li> 
 <li>修复了 <code>MATCH</code> 语句中，对聚合函数过滤时 graphd 会 crash 的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F919" target="_blank">#919</a></li> 
 <li>修复了 <code>MATCH</code> 无法查询 id 为负数的点的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F932" target="_blank">#932</a></li> 
 <li>修复了在 <code>SHOW CREATE TAG/EDGE INDEX <index_name></code> 中指定 <code>TAG</code> 或 <code>EDGE</code> 无效的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph%2Fpull%2F933" target="_blank">#933</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F426" target="_blank">#426</a></li> 
 <li>修复了在某些情况下 <code>REBUILD INDEX</code> 失败却返回成功的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F405" target="_blank">#405</a></li> 
 <li>修复了重建索引过程中，某些情况下可能导致正在插入的数据索引更新失败的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-storage%2Fpull%2F408" target="_blank">#408</a></li> 
 <li>修复了当 <code>substr()</code> 或 <code>substring()</code> 函数中任一参数为 <code>NULL</code> 时，graphd 会 crash 的问题，pr 参见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-common%2Fpull%2F491" target="_blank">#491</a></li> 
</ul> 
<p style="text-align:start">最后是 Nebula 的 GitHub 地址，欢迎大家试用，有什么问题可以向我们提 issue。GitHub 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvesoft-inc%2Fnebula-graph" target="_blank">https://github.com/vesoft-inc/nebula-graph</a>；</p>
                                        </div>
                                      
</div>
            