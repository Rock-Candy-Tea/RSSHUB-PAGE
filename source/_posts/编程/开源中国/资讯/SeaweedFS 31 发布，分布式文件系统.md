
---
title: 'SeaweedFS 3.1 发布，分布式文件系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4629'
author: 开源中国
comments: false
date: Tue, 14 Jun 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4629'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">SeaweedFS 是一个简单且高度可扩展的分布式文件系统，主要有两个目标：存储数十亿的文件和快速响应。</span></p> 
<p style="margin-left:0px"><span style="color:#333333">目前 </span>SeaweedFS 发布 3.1 版本，</p> 
<p style="margin-left:0px"><strong>远程对象存储网关</strong></p> 
<ul> 
 <li>通过删除标记，修复与 BackBlaze 的兼容性问题。</li> 
</ul> 
<p><span style="color:#24292f"><strong>Mount</strong></span></p> 
<ul> 
 <li>提高序列读取速度 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3074" target="_blank">#3074</a></li> 
 <li>在挂载选项中添加 disableXAttr <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3140" target="_blank">#3140</a></li> 
</ul> 
<p><span style="color:#24292f"><strong>S3</strong></span></p> 
<ul> 
 <li>根据 fs.configure 设置检测 TTL <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F3075" target="_blank">#3075</a> </li> 
 <li>修复 NextCloud 中删除父目录的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3130" target="_blank">#3130</a></li> 
 <li>修复 S3 测试：远程请求的无效范围 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3154" target="_blank">#3154</a></li> 
</ul> 
<p><strong>文件管理器同步</strong></p> 
<ul> 
 <li>添加选项以从时间戳同步 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3155" target="_blank">#3155</a></li> 
</ul> 
<p><strong>文件管理器用户界面</strong></p> 
<ul> 
 <li>上传/删除/重命名/创建目录时，强制重新加载文件管理器页面 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fpull%2F3165" target="_blank">#3165</a></li> 
 <li>修复可自定义的本地套接字文件名 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Fissues%2F3147" target="_blank">#3147</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchrislusf%2Fseaweedfs%2Freleases%2Ftag%2F3.10" target="_blank">https://github.com/chrislusf/seaweedfs/releases/tag/3.10</a></p>
                                        </div>
                                      
</div>
            