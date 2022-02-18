
---
title: 'Google开放Android 12动态主题色彩系统源代码：iOS也能用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0218/27bf4192f2f2ec4.jpg'
author: cnBeta
comments: false
date: Fri, 18 Feb 2022 13:15:18 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0218/27bf4192f2f2ec4.jpg'
---

<div>   
在Android 12中，Google新增了Material You动态主题，<strong>该功能可根据用户壁纸的颜色为主题进行着色。</strong>近日，Google宣布，将把该功能核心的Material Color Utilities代码库进行<a class="f14_link" href="https://github.com/material-foundation/material-color-utilities" target="_blank">开源</a>，从而将这一功能带到包括iOS在内的更多平台。<br>
<p><a href="https://img1.mydrivers.com/img/20220218/29e527b90dcb4454998731478e7483fd.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0218/27bf4192f2f2ec4.jpg"><img data-original="https://static.cnbetacdn.com/article/2022/0218/27bf4192f2f2ec4.jpg" src="https://static.cnbetacdn.com/thumb/article/2022/0218/27bf4192f2f2ec4.jpg" referrerpolicy="no-referrer"></a></p><p>据悉，Material Color Utilities的本质是一个跨平台的颜色代码库，通过这一代码库，<strong>开发者能够在任何平台实现Material You动态主题的功能。</strong></p><p>根据GitHub上的信息，该代码库目前包含Dart、Java和Typecript三种语言的版本，其Google计划在后续加入适用于iOS、CSS和GLSL的版本。</p><p><a href="https://img1.mydrivers.com/img/20220218/ce03a8a1706d45db9abf7197c453eefa.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0218/08a4d3361dd8a47.png"><img data-original="https://static.cnbetacdn.com/article/2022/0218/08a4d3361dd8a47.png" src="https://static.cnbetacdn.com/thumb/article/2022/0218/08a4d3361dd8a47.png" referrerpolicy="no-referrer"></a></p><p>此外，<strong>Googel还在开源文档中详细说明了这套动态主题系统的工作原理。</strong></p><p><a href="https://img1.mydrivers.com/img/20220218/b3250c91d0c34c648304e12d7ea02105.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0218/75f26c15c588966.png"><img data-original="https://static.cnbetacdn.com/article/2022/0218/75f26c15c588966.png" src="https://static.cnbetacdn.com/thumb/article/2022/0218/75f26c15c588966.png" referrerpolicy="no-referrer"></a></p><p>简单来说，当用户在运行Android 12系统的设备上修改壁纸时，系统将自动采集壁纸的颜色，并逐级进行整合，最终统计为少数几种主要色彩，交由用户选择或算法盲选。</p><p>可以预见的是，随着Material Color Utilities代码库的开源，这套动态主题色彩系统将逐渐不再是Android原生系统的专属，<strong>我们将会在越来越多的系统上看到类似功能的身影。</strong></p>   
</div>
            