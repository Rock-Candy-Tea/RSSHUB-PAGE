
---
title: 'libGDX 1.10.0 发布，时隔五年的主要版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1186'
author: 开源中国
comments: false
date: Mon, 19 Apr 2021 23:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1186'
---

<div>   
<div class="content">
                                                                    
                                                        <p>libGDX 是一个免费开源的游戏开发应用框架，用 Java 编程语言编写，并加入一些 C 和 C++ 组件，用于性能依赖性代码。它允许使用相同的代码库开发桌面游戏和手机游戏。支持 Windows、Linux、macOS、Android、iOS 和支持 WebGL 的网络浏览器。</p> 
<p>自从 libGDX 的上一个主要版本 1.9.0 发布以来，已经过去了五年多的时间。今天 libGDX 1.10.0 版本正式发布，本次更新内容如下：</p> 
<h4>原生：</h4> 
<p>几周前，我们将整个构建设置迁移到 GitHub Actions 上。虽然我们此前已经使用 GitHub Actions 作为我们的 CI 服务，但到目前为止，原生版本和快照版本都是通过一个自托管的 Jenkins 实例构建的。这很容易出现故障，而且难以维护。作为这次迁移的结果，构建现在变得更加方便和可重现，这将帮助我们使所有内容保持最新状态。</p> 
<p>在这次更新的过程中，我们也改变了一些原生构建的平台：</p> 
<ul> 
 <li>Android ARMv5 的支持已经被移除，因为自2018年6月以来，它已经与Android NDK不兼容。要迁移你的项目，请从你的 gradle 构建文件中删除任何带有 <code>natives-armeabi</code> 限定符的依赖关系。这适用于 gdx-platform、gdx-bullet-platform、gdx-freetype-platform 和 gdx-box2d-platform。</li> 
 <li>tvOS 库已被移除，因为目前你无法用 MobiVM 对其进行定位。</li> 
 <li>删除了对 Linux x86 (32位) 的支持。</li> 
 <li>增加了对 Linux ARM 和 AARCH64 的支持。</li> 
</ul> 
<h4>Java 7：</h4> 
<ul> 
 <li>libGDX 现在需要 Java 7 或以上版本。请注意，这对平台支持的最大 Java 版本没有任何影响。</li> 
</ul> 
<h4>JCenter 正在关闭：</h4> 
<p>上月底，JCenter 存储库停止接受新的提交。这是版本库关闭的第一步，随后在 2022 年 2 月，JCenter 将停止服务任何包。这意味着依赖于这个版本库的项目需要迁移。要更新你的 libGDX Gradle 项目，需要在你的项目中打开主要的 build.gradle 文件，在两个 <code>repositories&#123;&#125;</code> 部分用 <code>gradlePluginPortal()</code> 替换 <code>jcenter()</code>。</p> 
<h4>其他改动：</h4> 
<ul> 
 <li><code>Scaling</code> 现在是一个对象而不是一个枚举。这可能会改变与序列化一起使用时的行为。</li> 
 <li><code>Group#clear()</code> 和 <code>#clearChildren()</code> 现在可以取消对子代的关注。添加了 <code>clear(boolean)</code> 和 <code>clearChildren(boolean)</code> 以备不需要时使用。覆盖 <code>clear()</code>/ <code>clearChildren()</code> 的代码可能应该改为覆盖其对应的布尔参数。</li> 
 <li><code>Lwjgl3WindowConfiguration#autoIconify</code> 默认为启用。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flibgdx.com%2Fnews%2F2021%2F04%2Fgdx-1-10" target="_blank">https://libgdx.com/news/2021/04/gdx-1-10</a></p>
                                        </div>
                                      
</div>
            