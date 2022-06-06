
---
title: '知名开发者Arminder Singh建立新项目 让Windows 11在苹果M1等硬件上原生运行'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0606/e37138cfcc86b02.jpg'
author: cnBeta
comments: false
date: Mon, 06 Jun 2022 09:03:37 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0606/e37138cfcc86b02.jpg'
---

<div>   
如果你想在基于苹果Apple Silicon芯片的计算机上运行Windows 11，现在只能通过Parallels运行，去年，微软曾澄清，它不太可能在Mac或M1上支持Windows 11，这意味着非官方支持是爱好者们所期待的。<strong>而鉴于此，根据一位开发者Arminder Singh的说法，可能很快就能在苹果M1和其他Apple Silicon硬件上原生运行微软的Windows 11，他正在发起一个项目来实现这一目标。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0606/e37138cfcc86b02.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0606/e37138cfcc86b02.jpg" title alt="1654496865_apple_m1_(source-_apple_via_neowin)_expanded_top_with_windows_11_story.jpg" referrerpolicy="no-referrer"></a></p><p>但是，现在是非常早期的阶段，他说有几个挑战必须克服。</p><p>与表面上的情况相反，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的芯片在架构上与高通或联发科等公司的标准ARM64芯片非常不同，因此需要做大量的硬件适配和启用工作。值得庆幸的是，作为先行者的Asahi Linux项目在这一领域已经做了大量的工作。</p><blockquote><p>这不会是一个简单的项目，我必须考虑到许多苹果的特殊情况，以及我需要做的事情，以确保M1能够以稳定的方式启动<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>。 - Arminder Singh</p></blockquote><p>对于那些想知道Asahi Linux项目是什么的人来说，它是一个类似的项目，目的是在Apple Silicon上运行Linux。</p><p>然而，如上所述，苹果的硬件存在着特殊的挑战。辛格解释说，主要问题与苹果的专有中断控制器有关，被称为苹果中断控制器（AIC）。第二个问题与M1的输入-输出内存管理单元（IOMMU）有关，它只支持16K页而不是8K。</p><p>面对这些障碍，Singh重申，尽管他正在积极努力绕过这些障碍，但该项目可能不会成功。因此，目前还没有项目完成的预计时间。</p><blockquote><p>这个项目不保证会成功。我会尽最大努力确保它的完成，但最终，我是否能在这一切结束时让Windows以一种很好的方式工作，没有什么可以保证的。但我将绝对努力地去尝试。我需要时间来确保一切正常工作，所以到目前为止还没有任何ETA。 - Arminder Singh</p></blockquote><p>你可以在Arminder Singh的博客文章中找到更多细节：</p><p><a href="https://amarioguy.github.io/m1windowsproject/" _src="https://amarioguy.github.io/m1windowsproject/" target="_blank">https://amarioguy.github.io/m1windowsproject/</a><br></p>   
</div>
            