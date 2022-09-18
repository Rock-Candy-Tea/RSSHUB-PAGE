
---
title: 'Tinker 1.9.14.25 发布，微信开源的 Android 热修复框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=567'
author: 开源中国
comments: false
date: Sun, 18 Sep 2022 07:51:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=567'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">Tinker v</span>1.9.14.25<span style="color:#333333"> 发布了。Tinker 是腾讯开源的 Android 热解决方案库，它支持在不重新安装 apk 的情况下对 dex、library 和 resources 进行更新。</span></p> 
<p style="margin-left:0px"><span style="color:#333333"><strong>更新内容：</strong></span></p> 
<h3><strong>Bugfix & ChangeLog</strong></h3> 
<ol> 
 <li>增加了32位 Android N 及更旧的系统上使用解释模式触发 dexopt 的开关，以帮助减少 32位上 VmSize 的开销。</li> 
 <li>修复部分机型上资源有变更时 patch 失败的问题。</li> 
 <li>base 包更新或有新 patch 合成成功后，删除老 patch 的逻辑改为异步实现，以降低启动耗时。</li> 
 <li>dexopt 触发重试次数缩减到 10 次，避免部分机型 apply patch 耗时太长。</li> 
</ol> 
<p style="margin-left:0px">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FTencent%2Ftinker%2Freleases%2Ftag%2Fv1.9.14.25" target="_blank">https://github.com/Tencent/tinker/releases/tag/v1.9.14.25</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            