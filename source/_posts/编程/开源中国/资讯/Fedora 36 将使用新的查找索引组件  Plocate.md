
---
title: 'Fedora 36 将使用新的查找索引组件  Plocate'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1215/085054_Dxgb_5430600.jpg'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 08:52:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1215/085054_Dxgb_5430600.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>目前 Fedora 使用的查找索引组件是 <code>mlocate</code><em> 。 </em> Fedora 36 计划使用 <code>Plocate</code><em> </em>作为 <em>locate（查找） </em>命令的新<span style="color:#212529">索引</span>组件，用于在文件系统上查找文件。</p> 
<p>Plocate 可以更快地定位磁盘上的文件，并且使用更少的 CPU 周期。通过使用 <code>liburing</code> ：利用 IO_uring 和 libzstd 来实现更快的 I/O 和更新数据库的压缩。根据测试的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fplocate.sesse.net%2F" target="_blank">项目站点</a>，plocate 花费的时间不到 mlocate 的一半，同时还拥有一个更小的数据库：</p> 
<p><img alt height="299" src="https://static.oschina.net/uploads/space/2021/1215/085054_Dxgb_5430600.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p>虽然 Fedora 经常处于此类技术变更的前沿，但这次属于是拾人牙慧了，因为 Debian 已经将 <code>Plocate</code> 设为默认设置。</p> 
<p>下一个 Fedora 36 版本将转移到 Plocate 作为兼容的重新实现，有关此更改的详细信息可以通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffedoraproject.org%2Fwiki%2FChanges%2FPlocate_as_the_default_locate_implementation" target="_blank">Fedora Wiki</a> 找到。Fedora 工程和指导委员会 (FESCo) 已批准 Plocate 作为 Fedora 36 的默认设置。</p>
                                        </div>
                                      
</div>
            