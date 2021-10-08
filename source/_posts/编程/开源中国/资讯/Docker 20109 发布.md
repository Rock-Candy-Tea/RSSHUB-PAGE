
---
title: 'Docker 20.10.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7843'
author: 开源中国
comments: false
date: Thu, 07 Oct 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7843'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Docker 20.10.9 现已发布。这</span>是一个安全版本，在 CLI、runtime 以及 containerd.io 包和 Go runtime 的更新版本中进行了安全修复。<span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<h4><strong>Client</strong></h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41092" target="_blank">CVE-2021-41092</a> 确保默认身份验证配置设置了地址字段，以防止将凭据发送到默认注册表。</li> 
</ul> 
<h4>Runtime</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41089" target="_blank">CVE-2021-41089</a> 在<code>docker cp</code>过程中，在 chroot 中创建父目录，以防止特制容器更改主机文件系统中现有文件的权限。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41091" target="_blank">CVE-2021-41091</a> 锁定文件权限以防止非特权用户发现和执行<code>/var/lib/docker</code>中的程序。</li> 
</ul> 
<h4>Packaging</h4> 
<ul> 
 <li>将 Golang runtime 更新到 Go 1.16.8，其中包含针对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-36221" target="_blank">CVE-2021-36221</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-39293" target="_blank">CVE-2021-39293 的修复</a>。</li> 
 <li>将静态二进制文件和 containerd.io rpm 和 deb 包更新到 containerd v1.4.11 和 runc v1.0.2 以解决 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-41103" target="_blank">CVE-2021-41103 问题</a>。</li> 
 <li>将 rpm 和 deb 包的捆绑 buildx 版本更新到 v0.6.3。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmoby%2Fmoby%2Freleases%2Ftag%2Fv20.10.9" target="_blank">https://github.com/moby/moby/releases/tag/v20.10.9</a> </p>
                                        </div>
                                      
</div>
            