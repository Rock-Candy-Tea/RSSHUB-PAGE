
---
title: 'SeaweedFS 3.0 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8400'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8400'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</span></p> 
<p style="margin-left:0px"><span style="color:#333333">目前 </span>SeaweedFS 发布 3.0 版本，此版本删除了编译时不常用的大尺寸库，包括：“elastic、gocdk、sqlite、hdfs”。如果需要，请直接使用 Makefile 编译这些库。其他改动如下：</p> 
<p><strong>Shell</strong></p> 
<ul> 
 <li>按集合和卷 ID 划分 shell 真空卷 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2936" target="_blank">#2936</a></li> 
 <li><code>volume.list</code> 添加新选项：通过集合名称模式或通过 volumeId 显示只读卷 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2940" target="_blank">#2940</a></li> 
</ul> 
<p><strong>Filer</strong></p> 
<ul> 
 <li><span style="color:#2e3033">修复读取错误时的 http 响应错误代码</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2960" target="_blank">#2960</a></li> 
</ul> 
<p><strong>Volume</strong></p> 
<ul> 
 <li><span style="color:#2e3033">修复在卷服务器有多个目录时，删除卷或卸载卷时的错误</span></li> 
</ul> 
<p><strong>Minor</strong></p> 
<ul> 
 <li>Helm Charts：使用 leveldb2 的文件管理器可能会丢失数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2935" target="_blank">#2935</a></li> 
</ul> 
<p><strong>S3</strong></p> 
<ul> 
 <li>处理隐式用户名  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F2957" target="_blank">#2957</a></li> 
</ul> 
<p style="margin-left:0px">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F3.00" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/3.00</a></p>
                                        </div>
                                      
</div>
            