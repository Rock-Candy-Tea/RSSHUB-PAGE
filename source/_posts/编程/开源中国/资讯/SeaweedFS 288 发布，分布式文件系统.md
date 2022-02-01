
---
title: 'SeaweedFS 2.88 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9582'
author: 开源中国
comments: false
date: Tue, 01 Feb 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9582'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">目前<span> </span></span>SeaweedFS 发布 2.88 版本，带来如下改动：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Volume</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将卷并行移动到其他层。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2618" target="_blank">#2618</a> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>FUSE Mount</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>切换到内存缓冲区进行大文件随机写入。</li> 
 <li>还原“POSIX：如果目录不为空，则不应删除”。它导致<code>rm -Rf</code>linux上的文件夹删除错误。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Master</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加指标端口。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2613" target="_blank">#2613</a></li> 
 <li>删除 gRPC 最大连接时长限制<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fcommit%2Fb9b684194f8269325ec9c1666c7202a6f4dabe15" target="_blank">b9b6841</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Gateway to remote object store（远程对象存储网关）</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">确保为一个边缘情况复制数据，即使旧条目没有复制到远程存储。</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases" target="_blank">https://github.com/chrislusf/seaweedfs/releases</a></p>
                                        </div>
                                      
</div>
            