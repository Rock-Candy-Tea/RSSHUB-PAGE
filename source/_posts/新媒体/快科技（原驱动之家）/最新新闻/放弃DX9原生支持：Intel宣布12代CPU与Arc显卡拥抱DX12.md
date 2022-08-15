
---
title: '放弃DX9原生支持：Intel宣布12代CPU与Arc显卡拥抱DX12'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220815/s_c48d95e6fa7b4b54acc0502d7528dbb5.png'
author: 快科技（原驱动之家）
comments: false
date: Mon, 15 Aug 2022 11:55:50 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220815/s_c48d95e6fa7b4b54acc0502d7528dbb5.png'
---

<div>   
<p>近日，Intel已经将原生DirectX 9支持从自家的Arc独显，以及12代CPU中的Xe集显中移除，全面拥抱DirectX 12。</p>
<p>根据Intel的说法，<span style="color:#ff0000;"><strong>之前DX9的支持将被转移到DX12的仿真模式，在微软“D3D9On12”开源转换层上运行。</strong></span></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220815/c48d95e6fa7b4b54acc0502d7528dbb5.png" target="_blank"><img alt="放弃DX9原生支持：Intel宣布12代CPU与Arc显卡拥抱DX12" h="315" src="https://img1.mydrivers.com/img/20220815/s_c48d95e6fa7b4b54acc0502d7528dbb5.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p>转换通过将DX9的图形命令发送到D3D9On12层，而不是直接发送到D3D9图形驱动程序的方式进行；一旦D3D9On12层从D3D9 API接收到命令，就会将所有命令转换为D3D12 API调用。</p>
<p>也就是说，D3D9On12将作为一个GPU驱动程序运行。</p>
<p>微软表示，<strong>这种通过DX12模拟DX9的过程，在性能上堪比原生的DX9硬件支持</strong>，这也是Intel选择放弃DX9原生支持的原因。</p>
<p>不过，需要注意的是，通过API转译并非完美，<strong>它很可能会带来更高的CPU使用率，并且在对老游戏的适配兼容上容易出现问题。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20220815/db19c76d29c74704807457ba6b1b147f.png" target="_blank"><img alt="放弃DX9原生支持：Intel宣布12代CPU与Arc显卡拥抱DX12" h="399" src="https://img1.mydrivers.com/img/20220815/s_db19c76d29c74704807457ba6b1b147f.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
           <p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p>
<div style="overflow: hidden;font-size:14px;">
           <p class="zhuanzai"><strong>如需转载请务必注明出处：快科技</strong></p>  
          <p class="url"><span style="color:#666">责任编辑：乃河</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/intel.htm">Intel</a><a href="https://news.mydrivers.com/tag/dx12.htm">DX12</a><a href="https://news.mydrivers.com/tag/directx.htm">DirectX</a>  </p>
        
</div>
            