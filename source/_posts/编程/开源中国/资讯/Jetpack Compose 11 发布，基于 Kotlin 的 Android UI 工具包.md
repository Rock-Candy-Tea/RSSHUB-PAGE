
---
title: 'Jetpack Compose 1.1 发布，基于 Kotlin 的 Android UI 工具包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0212/070632_2pZX_4937141.png'
author: 开源中国
comments: false
date: Sat, 12 Feb 2022 07:07:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0212/070632_2pZX_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>Jetpack Compose 是 Android 基于 Kotlin 的现代原生 UI 工具包，可以帮助开发者更快地构建应用程序，由谷歌开源。Jetpack Compose 1.1 版本包含了一些新功能，如改进的焦点处理、强制扩展触摸目标大小、ImageVector 缓存，以及支持Android 12的拉伸滚动效果，此外一些实验性 api 变得稳定，并支持 Kotlin 的新版本。</p> 
<p><strong>注意：使用 Compose 1.1 需要使用 Kotlin 1.6.10。</strong></p> 
<h3>图像矢量缓存</h3> 
<p>Compose 1.1引入了图像矢量缓存，为 painterResource API 添加了一个缓存机制：缓存所有用给定资源 id 和主题解析的 ImageVectors 实例，带来了巨大的性能改进。</p> 
<p>注意：更改配置时，该缓存将失效。</p> 
<h3 style="margin-left:0px">强制扩展的触摸目标大小</h3> 
<p style="margin-left:0px">在 Jetpack Compose 1.1 版本，Material 组件将扩展布局空间，以满足 Material 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmaterial.io%2Fdesign%2Fusability%2Faccessibility.html" target="_blank">可访问性指南-触摸目标大小</a>标准。</p> 
<p style="margin-left:0px">例如 <code>RadioButton's</code>，即使开发者将 <code>RadioButton</code> 的尺寸设置得更小，触摸目标的最小尺寸也会扩大到 48x48dp。图下图：</p> 
<p style="margin-left:0px"><img height="386" src="https://static.oschina.net/uploads/space/2022/0212/070632_2pZX_4937141.png" width="960" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>左图为 Jetpack Compose 1.0 可用的触摸设置，右图为 Jetpack Compose 1.1 强制扩充触摸目标尺寸后的效果。</p> 
<p>可以通过设置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fmaterial3%2Fpackage-summary%23LocalMinimumTouchTargetEnforcement%28%29" target="_blank"><code>LocalMinimumTouchTargetEnforcement</code></a> 为 <code>false</code> 来禁用此功能。</p> 
<h3 style="margin-left:0px">从实验转为稳定的 API</h3> 
<ul> 
 <li>动画相关的API，如：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fanimation%2FEnterTransition" target="_blank"><code>EnterTransition</code></a> 、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fanimation%2FExitTransition" target="_blank"><code>ExitTransition</code></a> 、部分 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fanimation%2Fpackage-summary%23AnimatedVisibility%28kotlin.Boolean%2Candroidx.compose.ui.Modifier%2Candroidx.compose.animation.EnterTransition%2Candroidx.compose.animation.ExitTransition%2Ckotlin.String%2Ckotlin.Function1%29" target="_blank"><code>AnimatedVisibility</code></a> API、</li> 
 <li>矢量相关 API：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fui%2Fgraphics%2Fvector%2Fpackage-summary%23rememberVectorPainter%28androidx.compose.ui.unit.Dp%2Candroidx.compose.ui.unit.Dp%2Ckotlin.Float%2Ckotlin.Float%2Ckotlin.String%2Candroidx.compose.ui.graphics.Color%2Candroidx.compose.ui.graphics.BlendMode%2Ckotlin.Function2%29" target="_blank"><code>rememberVectorPainter</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fui%2Fgraphics%2Fvector%2FVectorProperty" target="_blank"><code>VectorProperty</code></a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fui%2Fgraphics%2Fvector%2FVectorConfig" target="_blank"><code>VectorConfig</code></a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Fui%2Fgraphics%2Fvector%2Fpackage-summary%23RenderVectorGroup%28androidx.compose.ui.graphics.vector.VectorGroup%2Ckotlin.collections.Map%29" target="_blank"><code>RenderVectorGroup</code></a></li> 
</ul> 
<h3 style="margin-left:0px">新的实验性 API</h3> 
<ul> 
 <li>使用 <code>rememberSaveable</code>.时，亦可保存和恢复 <code>AnimatedContent</code> </li> 
 <li>可以使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.com%2Freference%2Fkotlin%2Fandroidx%2Fcompose%2Ffoundation%2Flazy%2FLazyItemScope%23%28androidx.compose.ui.Modifier%29.animateItemPlacement%28androidx.compose.animation.core.FiniteAnimationSpec%29" target="_blank"><code>Modifier.animateItemPlacement()</code></a>.对 LazyColumn/LazyRow 进行动画定位</li> 
 <li>可以使用新的 <code>BringIntoView API</code> 向父级发送请求，滚动地将元素带入视图。</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fandroid-developers.googleblog.com%2F2022%2F02%2Fjetpack-compose-11-now-stable.html" target="_blank">https://android-developers.googleblog.com/2022/02/jetpack-compose-11-now-stable.html</a></p>
                                        </div>
                                      
</div>
            