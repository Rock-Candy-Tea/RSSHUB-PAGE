
---
title: 'Tinker 1.9.14.17 发布，微信开源的 Android 热修复框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9190'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9190'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Tinker v1.9.14.17 发布了。Tinker 是腾讯开源的 Android 热解决方案库，它支持在不重新安装 apk 的情况下对 dex、library 和 resources 进行更新。</p> 
<p>更新内容如下：</p> 
<p><strong>注意</strong></p> 
<p>因 Bintray 和 JCenter 已停止服务，Tinker 已将包含此版本在内的所有版本迁移到了 MavenCentral。若升级后编译失败，请在项目根目录的 build.gradle 中增加 mavenCentral() 这个 Repo 后重新编译一次。</p> 
<p><strong>Bugfix & ChangeLog</strong></p> 
<ol> 
 <li> <p>Fix: TinkerInlineFence 中可能出现的 Message 泄漏。</p> </li> 
 <li>在 Android R 上开启 secondary dexopt hack 以解决部分 Android R 机型加载 patch 后启动慢的问题。</li> 
</ol> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftinker%2Freleases%2Ftag%2Fv1.9.14.17" target="_blank">https://github.com/Tencent/tinker/releases/tag/v1.9.14.17</a></p>
                                        </div>
                                      
</div>
            