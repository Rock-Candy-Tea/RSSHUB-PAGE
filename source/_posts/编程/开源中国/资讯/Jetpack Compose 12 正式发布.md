
---
title: 'Jetpack Compose 1.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2714'
author: 开源中国
comments: false
date: Fri, 29 Jul 2022 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2714'
---

<div>   
<div class="content">
                                                                                            <p>Android 团队发布了 Jetpack Compose 1.2 版本，这是 Android 的现代原生 UI 工具包，可以帮助开发者更快地构建应用程序。这个版本包含新的功能，如可下载的字体、以及对平板电脑和 chromeOS 的改进。</p> 
<p>Compose 是官方推荐的为手机、平板电脑和可折叠设备构建 Android 应用的方式。此次还发布了适用于 Wear OS 的 Compose 1.0，这使得 Compose 也成为构建 Wear OS 应用的最佳方式。</p> 
<h3>新的稳定功能和 API</h3> 
<ul> 
 <li><code>LazyHorizontalGrid</code> 和 <code>LazyVerticalGrid</code> 的 API 让你在网格中放置项目列表。这些 API 已经存在于 Compose 1.1 中，但被标记为 <code>@Experimental</code> (实验性)。</li> 
 <li><code>WindowInsets</code> 类提供了 <code>windowInsetsPadding</code>、 <code>systemBarsPadding</code> 和 <code>windowInsetsTopHeight</code> 等修改器来处理设备的嵌入。这个类在很大程度上是基于 Accompanist insets 库，并取代它成为 Insets 的首选机制。</li> 
 <li><code>Modifier.nestedScroll</code> 提供了与视图的嵌套滚动互操作性</li> 
 <li>增加了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fanimation%2Fcore%2Fpackage-summary%23Ease%28%29" target="_blank">Easing curves</a>，能够有效地编写出更好的动画</li> 
 <li>通过添加 <code>Modifier.pointerHoverIcon</code>、 <code>PointerEventType.Scroll</code> 和 <code>PointerEvent.scrollDelta</code>，改进了对鼠标的支持。</li> 
</ul> 
<h3>新的实验性 API</h3> 
<ul> 
 <li>用 <code>LazyLayout</code> 创建你自己的高效滚动布局。使用 <code>Modifier.overscroll</code> 为你的可滚动容器添加自定义的过度滚动效果</li> 
 <li>使用 <code>GoogleFont</code> 下载字体</li> 
 <li>增加了许多文本功能，比如允许自定义 <code>includeFontPadding</code>、 <code>Brush</code> API，并增加了 <code>pluralStringResource</code></li> 
 <li>改进了测试 API</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>让动画遵循系统定义的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissuetracker.google.com%2F161675988" target="_blank">“Animator duration scale”</a></li> 
 <li>通过添加 <code>userScrollEnabled</code> 参数，允许禁用 lazy layouts 的滚动</li> 
 <li>让 <code>TextField</code> 中的返回按钮行为与 <code>EditText</code> 中的行为相同</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F07%2Fjetpack-compose-1-2-is-now-stable.html" target="_blank">https://android-developers.googleblog.com/2022/07/jetpack-compose-1-2-is-now-stable.html</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            