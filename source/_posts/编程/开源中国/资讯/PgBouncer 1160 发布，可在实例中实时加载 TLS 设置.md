
---
title: 'PgBouncer 1.16.0 发布，可在实例中实时加载 TLS 设置'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4421'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4421'
---

<div>   
<div class="content">
                                                                                            <p>PgBouncer 是一个开源的、轻量级的、用于 PostgreSQL 的连接池。它可以为一个或多个数据库建立连接池，并通过 TCP 和 Unix domain sockets 为客户提供服务。</p> 
<p>PgBouncer 1.16.0 正式发布，更新内容如下：</p> 
<h3>功能：</h3> 
<ul> 
 <li>支持热重载 TLS 设置。当配置文件被重新加载时，改变的 TLS 设置会自动生效；</li> 
 <li>密码和用户名的最大长度已分别增加到 996 和 128；</li> 
 <li>现在可以为每个数据库设置最小池大小；</li> 
 <li>在 <code>SHOW POOLS</code> 中显示了待定查询取消的数量。</li> 
</ul> 
<h3>修复：</h3> 
<ul> 
 <li>配置解析现在在许多地方有更严格的错误处理。以前它可能会记录一个错误并继续进行，现在这些配置错误会导致启动失败；</li> 
 <li>查询取消处理已被修复。此前在某些情况下，取消请求似乎会被卡住很长时间；</li> 
 <li>通过 hba 混合使用 md5 和 scram 的问题已被修复；</li> 
 <li>在 Windows 上用 c-res 构建的问题已被修复；</li> 
 <li>"FIXME: query end, but query_start == 0" 信息已被修复；</li> 
 <li>修复了重新加载 <code>default_pool_size</code>、 <code>min_pool_size</code> 和 <code>res_pool_size</code> 的问题。以前重新加载这些设置时，并不奏效。</li> 
</ul> 
<h3>清理：</h3> 
<ul> 
 <li>现在使用 Cirrus CI 而不是 Travis CI；</li> 
 <li>跟以往一样，增加了许多测试；</li> 
 <li>不能再使用 "pgbouncer" 作为数据库名称；</li> 
 <li>在连接关闭前发送给客户端的错误现在被标记为 "FATAL"，而不仅仅是 "ERROR"；</li> 
 <li>修正了 GCC 11 的编译器警告；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgbouncer.org%2Fchangelog.html%23pgbouncer-116x" target="_blank">https://www.pgbouncer.org/changelog.html#pgbouncer-116x</a></p>
                                        </div>
                                      
</div>
            