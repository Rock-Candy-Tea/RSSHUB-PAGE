
---
title: 'CentOS 8.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0606/073300_YJE8_4937141.png'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 07:34:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0606/073300_YJE8_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CentOS Linux 8 最新版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.centos.org%2F2021%2F06%2Fcentos-linux-8-2105-released%2F" target="_blank"> CentOS 8.4 </a>已正式 GA，版本号 2105，rebuild 自 <a href="https://www.oschina.net/news/142968/rhel-8-4-released">RHEL 8.4</a>。</p> 
<p><img alt height="233" src="https://static.oschina.net/uploads/space/2021/0606/073300_YJE8_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>镜像下载：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmirror.centos.org%2Fcentos%2F8%2Fisos%2F" target="_blank">http://mirror.centos.org/centos/8/isos/</a></p> 
<h3><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.centos.org%2FManuals%2FReleaseNotes%2FCentOS8.2105" target="_blank">主要变化</a></h3> 
<p>此版本在可选的 module stream 中增加了以下新版本软件包：</p> 
<ul> 
 <li>Python 3.9</li> 
 <li>SWIG 4.0</li> 
 <li>Subversion 1.14</li> 
 <li>Redis 6</li> 
 <li>PostgreSQL 13</li> 
 <li>MariaDB 10.5</li> 
</ul> 
<p>多个滚动更新的 AppStream 重新采用新的底层版本：</p> 
<ul> 
 <li>LLVM Toolset 11.0.0</li> 
 <li>Rust Toolset 1.49.0</li> 
 <li>Go Toolset 1.15.7</li> 
</ul> 
<p>发布说明还写道：“自 CentOS Linux 8 首个版本发布后，Boot ISO 出现了一些问题，导致用户需要手动输入镜像 URL。开发团队称最近在 CentOS Stream 8 中修复了此问题，并在 CentOS Linux 8 (2105) 中带来了同样的修复。”因此，在这个版本中，Boot ISO 现在将默认使用最近的镜像，不再需要手动输入镜像 URL。</p> 
<h3>针对 Yum repo 文件和 repoid 软件库名称的更改</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.centos.org%2Fpipermail%2Fcentos-devel%2F2020-September%2F056069.html">按照开发团队的解释</a>，此处更改主要是为了使 CentOS Stream 作为独立于 CentOS Linux 的发行版运行，以及简化从 CentOS Linux 迁移到 CentOS Stream 的过程。</p> 
<p>因此开发团队修改了 /etc/yum.repos.d 目录中某些文件的名字，并更新了 repoid 以进行匹配。具体如下：<br>  </p> 
<table> 
 <tbody> 
  <tr> 
   <td><strong>Repoid (8.2.2004 and before)</strong></td> 
   <td><strong>Repoid (8.3.2011 and later)</strong></td> 
  </tr> 
  <tr> 
   <td>BaseOS</td> 
   <td>baseos</td> 
  </tr> 
  <tr> 
   <td>AppStream</td> 
   <td>appstream</td> 
  </tr> 
  <tr> 
   <td>PowerTools</td> 
   <td>powertools</td> 
  </tr> 
  <tr> 
   <td>centosplus</td> 
   <td>plus</td> 
  </tr> 
  <tr> 
   <td>HighAvailability</td> 
   <td>ha</td> 
  </tr> 
  <tr> 
   <td>base-debuginfo</td> 
   <td>debuginfo</td> 
  </tr> 
  <tr> 
   <td>Devel</td> 
   <td>devel</td> 
  </tr> 
  <tr> 
   <td>BaseOS-source</td> 
   <td>baseos-source</td> 
  </tr> 
  <tr> 
   <td>AppStream-source</td> 
   <td>appstream-source</td> 
  </tr> 
  <tr> 
   <td>centosplus-source</td> 
   <td>plus-source</td> 
  </tr> 
  <tr> 
   <td>base-debuginfo</td> 
   <td>debuginfo</td> 
  </tr> 
 </tbody> 
</table> 
<p>详细更新说明查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.centos.org%2FManuals%2FReleaseNotes%2FCentOS8.2105" target="_blank">release note</a>。</p>
                                        </div>
                                      
</div>
            