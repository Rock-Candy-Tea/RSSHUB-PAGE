
---
title: '放弃DX9原生支持：Intel宣布12代CPU与Arc显卡拥抱DX12'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0815/d27e552fb2c98d3.png'
author: cnBeta
comments: false
date: Mon, 15 Aug 2022 03:59:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0815/d27e552fb2c98d3.png'
---

<div>   
近日，Intel已经将原生DirectX 9支持从自家的Arc独显，以及12代CPU中的Xe集显中移除，全面拥抱DirectX 12。根据Intel的说法，<strong>之前DX9的支持将被转移到DX12的仿真模式，在微软“D3D9On12”开源转换层上运行。</strong><br>
 <p><a href="https://img1.mydrivers.com/img/20220815/c48d95e6fa7b4b54acc0502d7528dbb5.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0815/d27e552fb2c98d3.png"><img data-original="https://static.cnbetacdn.com/article/2022/0815/d27e552fb2c98d3.png" src="https://static.cnbetacdn.com/thumb/article/2022/0815/d27e552fb2c98d3.png" referrerpolicy="no-referrer"></a></p><p>转换通过将DX9的图形命令发送到D3D9On12层，而不是直接发送到D3D9图形驱动程序的方式进行；一旦D3D9On12层从D3D9 API接收到命令，就会将所有命令转换为D3D12 API调用。</p><p>也就是说，D3D9On12将作为一个GPU驱动程序运行。</p><p>微软表示，<strong>这种通过DX12模拟DX9的过程，在性能上堪比原生的DX9硬件支持</strong>，这也是Intel选择放弃DX9原生支持的原因。</p><p>不过，需要注意的是，通过API转译并非完美，<strong>它很可能会带来更高的CPU使用率，并且在对老游戏的适配兼容上容易出现问题。</strong></p><p><a href="https://img1.mydrivers.com/img/20220815/db19c76d29c74704807457ba6b1b147f.png" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0815/2551032a0271c74.png"><img data-original="https://static.cnbetacdn.com/article/2022/0815/2551032a0271c74.png" src="https://static.cnbetacdn.com/thumb/article/2022/0815/2551032a0271c74.png" referrerpolicy="no-referrer"></a></p>   
</div>
            