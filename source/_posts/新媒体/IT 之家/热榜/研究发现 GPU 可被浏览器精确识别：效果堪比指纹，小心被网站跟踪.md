
---
title: '研究发现 GPU 可被浏览器精确识别：效果堪比指纹，小心被网站跟踪'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/40d5fcfc-c1ef-4da1-ad02-eaee6b551f08.jpg@s_2,w_820,h_174'
author: IT 之家
comments: false
date: Tue, 01 Feb 2022 15:12:08 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/40d5fcfc-c1ef-4da1-ad02-eaee6b551f08.jpg@s_2,w_820,h_174'
---

<div>   
<p data-vmark="7883"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 2 月 1 日消息，在题为“DRAWNAPART：基于远程 GPU 指纹识别的设备识别技术”的<a href="https://arxiv.org/pdf/2201.09956.pdf" target="_blank">研究论文</a>中，研究人员提出了一种<span class="accentTextColor">基于 GPU 生成的浏览器“指纹”识别用户</span>的方法。</p><p style="text-align: center;" data-vmark="d5de"><img src="https://img.ithome.com/newsuploadfiles/2022/2/40d5fcfc-c1ef-4da1-ad02-eaee6b551f08.jpg@s_2,w_820,h_174" w="1200" h="254" title="研究发现 GPU 可被浏览器精确识别：效果堪比指纹，小心被网站跟踪" srcset="https://img.ithome.com/newsuploadfiles/2022/2/40d5fcfc-c1ef-4da1-ad02-eaee6b551f08.jpg 2x" width="1200" height="174" referrerpolicy="no-referrer"></p><p data-vmark="ddeb">目前，网站可以通过 Cookie、浏览器用户代理、网络 IP、鼠标移动和其他技术跟踪用户，以提供更准确的广告。然而研究人员已经证实，有一种新的高精度识别用户的方法：<span class="accentTextColor">GPU 指纹</span>。</p><p data-vmark="7440">在涉及 2500 个设备的大规模实验测试中，比其他已知方法的跟踪速度快了 67%。目前依赖 WebGL 2.0 APU 的方法需要至少 8 秒来对 GPU 进行识别，但已经有新的 Web API 将这个时间缩短到了 <span class="accentTextColor">150 毫秒</span>，并将准确率提高到了 <span class="accentTextColor">98%</span>。</p><p style="text-align: center;" data-vmark="e4f8"><img src="https://img.ithome.com/newsuploadfiles/2022/2/27b6393b-1da7-4a93-acc4-8f4e5a692681.png" w="768" h="351" title="研究发现 GPU 可被浏览器精确识别：效果堪比指纹，小心被网站跟踪" width="768" height="351" referrerpolicy="no-referrer"></p><p data-vmark="1af4">据介绍，这种方法依赖于硬件识别，特别是 GPU。研究人员利用测量包含各种计算的向量的可能性，可用于验证用户。研究人员甚至已经证实，移除和更换某些组件不会影响用于跟踪用户的“分类器”。</p><p data-vmark="676a">不过，这种识别方法需要 <span class="accentTextColor">WebGL 2.0 API</span>，目前只有谷歌地图或宜家等少数网站仍在使用 WebGL 2.0。在 Alexa 排名前 10K 的网站中，只有 1% 的网站需要 WebGL 标准，这表明浏览器可以默认禁用此 API。</p><p data-vmark="35be">IT之家了解到，负责 WebGL 的非营利组织 Khronos 已经在研究可能的缓解措施，以阻止这种识别方法。</p>
          
</div>
            