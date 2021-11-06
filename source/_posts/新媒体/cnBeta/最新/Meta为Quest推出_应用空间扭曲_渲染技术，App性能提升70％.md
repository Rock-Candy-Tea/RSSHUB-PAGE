
---
title: 'Meta为Quest推出_应用空间扭曲_渲染技术，App性能提升70％'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1106/33fa41d522cc925.jpg'
author: cnBeta
comments: false
date: Sat, 06 Nov 2021 06:46:57 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1106/33fa41d522cc925.jpg'
---

<div>   
Meta曾在Connect 2021大会亮相了一种名为Application Spacewarp（应用空间扭曲）的渲染技术。据称，<strong>它类似于Oculus PC应用中的异步Asynchronous Spacewarp（异步空间扭曲）技术，并且可以将Quest应用的性能提高70%。</strong><br>
 <p style="text-align: left;">Quest是由移动处理器提供支持，为了达到的72 FPS的最低标准，开发者必须仔细考虑性能优化，另外，如果希望支持90Hz或120Hz，这一点就尤为重要。</p><p style="text-align: left;">所以，任何有助于提高应用性能的工具和技术都是开发者的福音。针对这种情况，Meta为开发者带来了可将应用性能提高近70%的Application Spacewarp。</p><p style="text-align:center"><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1106/33fa41d522cc925.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1106/33fa41d522cc925.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1106/33fa41d522cc925.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;"><strong>1. 将开发者的可用渲染时间增加70%</strong></p><p style="text-align: left;">这项技术类似于PC端的Asynchronous Spacewarp（异步空间扭曲），可允许应用以半帧速率运行，比方说72 FPS的一半36 FPS。具体来说，系统可以基于前一帧中的运动生成合成帧，并每隔一帧填充一次。从视觉上看，画面看起来与全帧速类似，但渲染工作只需后者的一半。</p><p style="text-align: left;">与以72 FPS速度运行的应用相比，36 FPS意味着每帧多出了两倍时间，而额外的时间可以由开发者随意支配，例如实现更高的分辨率渲染、采用效果更好的抗锯齿、增加几何复杂性、放置更多对象等等。</p><p style="text-align: left;">当然，Asynchronous Spacewarp本身需要一定的空间计算时间来完成工作。Meta已经通过一系列的现有Quest应用测试了所述系统，并表示所述技术可以将可用的渲染时间最高增加70%。</p><p style="text-align: left;"><strong>2. 开发者控制</strong></p><p style="text-align: left;">采用Asynchronous Spacewarp技术的开发者可以瞄准36 FPS（对应72Hz），45 FPS（对应90Hz），或60 FPS（对应120Hz）。</p><p style="text-align: left;">Meta技术负责人尼尔·贝代卡（Neel Bedekar）认为，对于开发者而言，45 FPS（对应90Hz）最为平衡和适合，并使得它成为一个相当简单的“插入式”解决方案，不需要任何额外的优化。</p><p style="text-align: left;">当然，从刷新率的角度来看，120Hz要优于60 FPS速度会更好，但在这种情况下，与原生72 FPS应用相比，由于Application Spacewarp需要开销计算，60 FPS应用增加了额外的优化工作。</p><p style="text-align: left;">Meta强调，所述功能完全可以由开发者逐帧控制。这意味着开发者能够灵活地在需要时使用，或者在不需要时禁用。</p><p style="text-align: left;">开发者同时可以完全控制一系列的关键数据：深度缓冲和运动矢量。Meta进一步指出，这种控制可以帮助开发者处理边缘情况，甚至发现能够最佳利用所述系统的创造性解决方案。</p><p style="text-align: left;"><strong>3. 延迟低于全帧速率</strong></p><p style="text-align: left;">这家公司表示，结合其他技术，使用Application Spacewarp的Quest应用在延迟方面甚至可以低于不适用任何额外技术的全帧速率应用。</p><p style="text-align: left;">这主要归功于Phase Sync，Late Latching和Positional Timewarp等优化技术。</p><p style="text-align: left;"><strong>4. Application Spacewarp（Quest）和Asynchronous Spacewarp（PC）之间的差异</strong></p><p style="text-align: left;">PC端有一项类似的技术Asynchronous Spacewarp，但贝代卡解释道，Quest版本可以产生“显著”更好的结果，因为应用可以生成自己的高精度运动矢量，并为合成帧的创建提供信息。作为对比，PC版本的运动矢量是基于完成的帧进行估计，所以会导致精度较低的结果。</p><p style="text-align: left;"><strong>5. 何时向开发者提供</strong></p><p style="text-align: left;">Meta表示，计划在未来两周左右开始向Quest开发者提供Application Spacewarp，并承诺所述功能将支持Unity、Unreal和原生Quest开发。</p>   
</div>
            