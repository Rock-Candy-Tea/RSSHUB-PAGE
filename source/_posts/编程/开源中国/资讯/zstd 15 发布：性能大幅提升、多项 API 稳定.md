
---
title: 'zstd 1.5 发布：性能大幅提升、多项 API 稳定'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bc2f679480d5e7c64d78304bbe0b77297d0.png'
author: 开源中国
comments: false
date: Mon, 17 May 2021 00:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bc2f679480d5e7c64d78304bbe0b77297d0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>zstd 1.5 已正式发布，新版本在性能方面再度带来了令人印象深刻的改进，其中包括：</p> 
<ul> 
 <li>提升 Middle-Level 压缩的速度</li> 
 <li>提升 High-Level 压缩的压缩率</li> 
 <li>更快的解压速度</li> 
 <li>升级动态库</li> 
 <li>……</li> 
</ul> 
<p><strong>提升 Middle-Level 压缩的速度</strong></p> 
<p>zstd 1.5.0 为压缩策略<code>greedy</code>、<code>lazy</code>和<code>lazy2</code>引入了新的默认匹配查找器（对于大于 256K 的输入，它们映射到 5-12 级）。该优化极大地提升了压缩速度，同时压缩率略有波动（<0.5％），并且内存使用量相等或减少。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bc2f679480d5e7c64d78304bbe0b77297d0.png" referrerpolicy="no-referrer"></p> 
<p><strong>提升 High-Level 压缩的压缩率</strong></p> 
<p>在新版本中，默认情况下对于 High-Level 级别 (16+) 的压缩， 启用通过块拆分 (block splitting) 以提高压缩率的功能。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-0d0dc930f477c09b668ff8a82be7e5414a8.png" referrerpolicy="no-referrer"></p> 
<p><strong>更快的解压速度</strong></p> 
<p>在此版本中，使用 large window 设置（例如<code>--long</code>或<code>--ultra</code>）压缩的数据的解压缩速度已得到显着提升。具体效果取决于编译器和版本，<code>clang</code>效果通过最好。</p> 
<p><img height="643" src="https://oscimg.oschina.net/oscnet/up-b3b4161905b002dac102664c4081e57d1e9.png" width="559" referrerpolicy="no-referrer"></p> 
<p>更多的细节和下载地址<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Fzstd%2Freleases%2Ftag%2Fv1.5.0" target="_blank">查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            