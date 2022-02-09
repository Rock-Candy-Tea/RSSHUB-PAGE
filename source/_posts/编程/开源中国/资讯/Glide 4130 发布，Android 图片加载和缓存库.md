
---
title: 'Glide 4.13.0 发布，Android 图片加载和缓存库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2223'
author: 开源中国
comments: false
date: Wed, 09 Feb 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2223'
---

<div>   
<div class="content">
                                                                                            <p>Glide 4.13.0 发布了，Glide 是一个 Android 上的图片加载和缓存库，其目的是实现平滑的图片列表滚动效果。</p> 
<p>该版本带来如下变更：</p> 
<h3>特性</h3> 
<ul> 
 <li>添加集成库，以支持解码 AVIF ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F3fd8e777e2be6a3fedc5f5c5f688970a212a285f" target="_blank">3fd8e77</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2Ff5e78ed03c99a9804285360b36b04d3089c80cff" target="_blank">f5e78ed</a> , <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F2b52437cd52bbacf0376d84aa2eec5b63ba53ac4" target="_blank">2b52437</a> )</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>提高取消挂起请求的性能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F627d04af1ec5d81c23908c27e1a646806dce7b30" target="_blank">627d04a</a>）</li> 
 <li>改善解码 byte[] 和 ByteBuffer 时的内存开销 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F042f6b57d511c9d1652d280f5d385d5fef071647" target="_blank">042f6b5</a>)</li> 
 <li>避免在注册表中返回重复的转码类（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2Fce8b5e31d7c8ee8e98725142b9c22c478f78cefd" target="_blank">ce8b5e3</a>）</li> 
 <li>避免在较低层完成时，取消较高层（通常是更高分辨率）的预加载请求 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F4733d1d3309e0f9af1e751f266c5fb0f9fd3a9ce" target="_blank">4733d1d</a>)</li> 
 <li>降低某些设备的最大 FD 大小限制，以避免本机崩溃 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F808a685f3c538621d5dfecd9928d2f75a4b7f68e" target="_blank">808a685</a>)</li> 
 <li>修复由异常活动/片段生命周期交互引起的内存泄漏 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F8bebf71e80c2cd1f260d919e6b0697436da6e302" target="_blank">8bebf71</a>)</li> 
 <li>修复从 <span style="color:#24292f">assets</span> 中解码视频的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F52a8cf84a9c10123777db805b235bf47e18ec234" target="_blank">52a8cf8</a>)</li> 
</ul> 
<h3><strong>弃用</strong></h3> 
<ul> 
 <li><span style="color:#24292f">弃用 .thumbnail(float) ，以简化缩略图逻辑，尤其是围绕请求侦听器。</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2Faa23eedb79196c29c61b366d8c9b93c34564fe09" target="_blank">aa23eed</a>)</li> 
</ul> 
<h3><strong>行为改变</strong></h3> 
<ul> 
 <li>将默认颜色空间设置为 null 而不是 SRGB（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2Fce6852d372b2b6fe6d52fe039b7003b1891a8435" target="_blank">ce6852d</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F9dc1f608540039c29931c22e7c7512caa842fe90" target="_blank">9dc1f60</a>）</li> 
 <li>将源写入磁盘缓存失败时，如果可能，回退到从源解码数据 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F755c39fb1ff49895ada9f13d808fa46153112980" target="_blank">755c39f</a> )</li> 
 <li>避免使用已弃用的 API 来检测 API 24+上的连接状态（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2Fdbdae568a37e9aabdab4ceb0ab9c7294de53861d" target="_blank">dbdae56、833ef21</a>）</li> 
 <li>为 Glide 的 ImageHeaderParser 添加了对检测动画 webp 的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F42654b298ebf2d2931a1b6d099f9f2b901dc37b1" target="_blank">42654b2</a> )</li> 
</ul> 
<h2><strong>构建更改</strong></h2> 
<ul> 
 <li><span style="color:#2e3033">升级到 Gradle </span>5.6.4<span style="color:#2e3033"> 版本，然后用检查过的版本替换现有 Gradle 版本 </span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fpull%2F4484" target="_blank">#4484</a>）</li> 
 <li>将 Jcenter 替换为 Maven Central ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F0d3204907f09c713e9dcf104e879b4dea8c2f5f6" target="_blank">0d32049</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Fcommit%2F87a77cea15a0eed253fabc57ff36a1f9b3556fff" target="_blank">87a77ce</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbumptech%2Fglide%2Freleases%2Ftag%2Fv4.13.0" target="_blank">https://github.com/bumptech/glide/releases/tag/v4.13.0</a></p>
                                        </div>
                                      
</div>
            