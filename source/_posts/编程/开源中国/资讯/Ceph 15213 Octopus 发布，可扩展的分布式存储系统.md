
---
title: 'Ceph 15.2.13 Octopus 发布，可扩展的分布式存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2008'
author: 开源中国
comments: false
date: Fri, 28 May 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2008'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ceph 15.2.13 正式发布，这是 Octopus 系列的第 13 个 backport 版本。</p> 
<p><strong>值得关注的变化：</strong></p> 
<ul> 
 <li>RADOS：能够在监视器中动态调整修剪率，并修复了其他的一些错误。</li> 
</ul> 
<p><strong>更新日志：</strong></p> 
<ul> 
 <li>blk/kernel：修复 io_uring got (4) 中断的系统调用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fceph.spec.in%2F" target="_blank">ceph.spec.in</a>：在 IBM Power 和 Z 上启用 tcmalloc；</li> 
 <li><code>cephadm ls</code> 在 SUSE 下游的 alertmanager 容器中被破坏；</li> 
 <li>cephadm：允许在所有 <_devices> drivegroup 部分使用路径；</li> 
 <li>cephadm：在 systemd 单元中添加 docker.service 依赖；</li> 
 <li>cephadm：允许在容器运行时重新部署处于错误状态的守护进程；</li> 
 <li>cephadm：修正使用 -apply-spec 和 -shh-user 时的失败；</li> 
 <li>cephadm：使用<code>init</code>运行容器；</li> 
 <li>cephfs：客户端：只检查常规文件的池权限；</li> 
 <li>cephfs：客户端：唤醒 front pos waiter；</li> 
 <li>客户端：在缓冲区被刷新后启动 finish_cap_snap()；</li> 
 <li>cmake：全局定义 BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fceph.io%2Freleases%2Fv15-2-13-octopus-released%2F" target="_blank">https://ceph.io/releases/v15-2-13-octopus-released/</a></p>
                                        </div>
                                      
</div>
            