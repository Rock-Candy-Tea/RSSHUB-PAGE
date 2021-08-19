
---
title: 'React Native 0.65 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9375'
author: 开源中国
comments: false
date: Thu, 19 Aug 2021 06:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9375'
---

<div>   
<div class="content">
                                                                                            <p>React Native 0.65 已经发布了，此版本主要亮点包括：</p> 
<ul> 
 <li>Hermes 0.8.1。</li> 
 <li>react-native-codegen 0.0.7 版现在需要作为 package.json 中的 devDependency。</li> 
 <li>JCenter 现已弃用且为只读。官方已将 JCenter 作为 maven 仓库移除并更新了依赖项以使用 MavenCentral 和 Jitpack。</li> 
 <li>将 OkHttp 从 v3 升级到 v4.9.1。有关更改的更多详细信息，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsquare.github.io%2Fokhttp%2Fupgrading_to_okhttp_4%2F" target="_blank">Upgrading to OkHttp 4</a>。</li> 
 <li>升级到 Flipper 0.93 以支持 Xcode 12.5。可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fflipper%2Fblob%2Fmaster%2Fdesktop%2Fstatic%2FCHANGELOG.md" target="_blank">此处的 Flipper 更新日志</a>。</li> 
 <li>Android Gradle Plugin 7 支持。</li> 
</ul> 
<h4>Hermes</h4> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhermesengine.dev%2F" target="_blank">Hermes</a> 是 Facebook 为 React Native 优化的开源 JavaScript VM，已升级到 0.8.1 版本。此版本中的一些突出功能包括：</p> 
<ul> 
 <li>一个名为“Hades”的新并发 garbage collector，可在 64 位设备上将暂停时间缩短多达 30 倍。在 Facebook，它将一些 CPU 密集型工作负载提高了 20%-50%。可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhermesengine.dev%2Fdocs%2Fhades%2F" target="_blank">在此处了解有关 Hades 的更多信息</a>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhermesengine.dev%2Fdocs%2Fintl" target="_blank">ECMAScript Internationalization API（ECMA-402 或<code>Intl</code>）</a>现在内置在 Android 上的 Hermes 中并默认启用，每个 API size overhead 只有 57-62K（相比之下，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Freact-native-community%2Fjsc-android-buildscripts" target="_blank">JSC 的为 6MiB</a>）。通过此更改，Hermes 用户不再需要 locale polyfills。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fblog%2F2021%2F03%2F12%2Fversion-0.64" target="_blank">Hermes on iOS</a> 现在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2Fpull%2F546" target="_blank">支持 Apple M1 Mac 和 Mac Catalyst</a>。</li> 
 <li>内存改进，包括 SMI（Small Integers）和指针压缩，将 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Ftmikov%2Fstatus%2F1385629737121243140" target="_blank">JS 堆缩小了 30%</a>。</li> 
 <li>对<code>Function.prototype.toString</code>的更改，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2Fissues%2F471%23issuecomment-820123463" target="_blank">修复了由于 feature detection 不当而导致的性能下降，</a>并<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fhermes%2Fissues%2F114" target="_blank">支持源代码注入用例</a>。</li> 
</ul> 
<h4>辅助功能修复和添加</h4> 
<ul> 
 <li>允许为 iOS 指定高对比度明暗值。有关更多详细信息可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fdocs%2Fdynamiccolorios" target="_blank">文档</a>。</li> 
 <li>在 Android 上添加了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fdocs%2Faccessibilityinfo%23getrecommendedtimeoutmillis-android" target="_blank"><code>getRecommendedTimeoutMillis</code></a>API。</li> 
 <li>一般性修复，以确保 TalkBack/VoiceOver 正确 announce UI states，例如组件上的<code>disabled</code>和<code>unselected</code>。</li> 
</ul> 
<p>完整更新内容可以查看： </p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freactnative.dev%2Fblog%2F2021%2F08%2F17%2Fversion-065" target="_blank">https://reactnative.dev/blog/2021/08/17/version-065</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Freact-native%2Freleases%2Ftag%2Fv0.65.0" target="_blank">https://github.com/facebook/react-native/releases/tag/v0.65.0</a></li> 
</ul>
                                        </div>
                                      
</div>
            