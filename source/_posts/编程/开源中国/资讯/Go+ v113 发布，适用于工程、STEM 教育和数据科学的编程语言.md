
---
title: 'Go+ v1.1.3 发布，适用于工程、STEM 教育和数据科学的编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=227'
author: 开源中国
comments: false
date: Thu, 04 Aug 2022 08:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=227'
---

<div>   
<div class="content">
                                                                                            <p>Go+ 刚刚发布了 v1.1.3。1.1.3 是 1.1 系列的最新版本，<a href="https://www.oschina.net/news/198845/goplus-1-1-0-released">Go+ v1.1 </a>属于大版本更新，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FCoDV-2eahWh33eE_sjPGXA" target="_blank">作者称</a>该版本解决了几个影响面比较大的“硬骨头”：</p> 
<ul> 
 <li>支持 Go+ module</li> 
 <li>对 Go/Go+ 混合工程的支持</li> 
 <li>Go+ 调用 C 代码的支持（预览版）</li> 
</ul> 
<blockquote> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Go+ 是一门适用于工程、STEM 教育和数据科学的编程语言。主要特性包括：</p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li>静态类型语言。</li> 
  <li>与 Go 完全兼容。</li> 
  <li>脚本化的风格，以及比 Go 更易于阅读的数据科学代码。</li> 
  <li> <p style="margin-left:0; margin-right:0">支持字节码后端和 Go 代码生成。在字节码模式下，Go+ 不支持 <code>cgo</code>。然而，在 Go 代码生成模式下，Go+ 完全支持 <code>cgo</code>。</p> </li> 
 </ul> 
</blockquote> 
<p style="color:#24292f; text-align:start"><strong>1.1.3 变化</strong></p> 
<p style="color:#24292f; text-align:start"><strong>新特性</strong></p> 
<ul> 
 <li>cmd/gop:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F207a7a44f987f1e5597988e60b77fac9105d50f1" target="_blank">gop build/run/install/test pass build flags</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fissues%2F1300" target="_blank">#1300</a>)</li> 
 <li>cl:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2Ff68ea55de74433cd04843f3cc4230f55a27b4849" target="_blank">os.File: 支持 Gop_Enum</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fissues%2F1320" target="_blank">#1320</a>)</li> 
 <li>cl:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F6110e496e89ee32500ccbeaee9c33b43b20fe7bc" target="_blank">blines</a></li> 
</ul> 
<p style="color:#24292f; text-align:start"><strong>变更</strong></p> 
<ul> 
 <li>cmd/gop:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2Fa5f77fd9d40cef8ee3df7d709bd2b7a1952fdf64" target="_blank">gop run/build/install/test -v => -debug</a></li> 
 <li>cl:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F6a00e1fab02cfc06e778a58790a1d758a9ef0157" target="_blank">command style invalid operation mismatched types</a><span> </span>(fix<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fissues%2F1312" target="_blank">#1312</a>)</li> 
 <li>parser:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F94eb7249947c300064dfafc8e7bece0f8e4c8124" target="_blank">cmd style check tuple to list</a><span> </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fpull%2F1315" target="_blank">#1315</a>)</li> 
 <li>parser:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F824f1c81da87e94bf8a2b3ef7405cecee0635942" target="_blank">return isTuple if allowTuple</a></li> 
 <li>parser:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Fcommit%2F8c96f79ecf364b5cea098f5847b5669424eb8fc4" target="_blank">parseBinaryExpr check tuple</a></li> 
 <li>mod: gox v1.11.21</li> 
 <li>mod: c2go v0.7.10</li> 
 <li>mod: libc v0.3.12</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoplus%2Fgop%2Freleases%2Ftag%2Fv1.1.3" target="_blank">Release Note</a></p>
                                        </div>
                                      
</div>
            