
---
title: echarts在官方网站按需打包用了代码压缩后出现问题？
categories: 
    - 编程
    - 微信开放平台 - 微信开放社区 - 小程序问答
author: 微信开放平台 - 微信开放社区 - 小程序问答
comments: false
date: Sun, 21 Mar 2021 14:32:14 GMT
thumbnail: 
---

<div>   
<p>echarts在官方网站按需打包用了代码压缩后下载下来echarts.min.js的文件，</p><p>我将此文件名改为echarts.js，替换官方文档中文件夹ec-canvas中的echarts.js；</p><p style="line-height: 18px; font-size: 12px; font-family: Consolas, Consolas, "Courier New", monospace; color: rgb(51, 51, 51);">【按照官方文件要求：<span style="color: rgb(0, 16, 128);">发布时，如果对文件大小要求更高，可以在 </span><span style="color: rgb(173, 6, 193);">[</span><span style="color: rgb(130, 170, 255);">ECharts 在线定制</span><span style="color: rgb(173, 6, 193);">](</span><a href="http://echarts.baidu.com/builder.html" rel="noopener noreferrer" target="_blank" style="color: rgb(247, 140, 108);">http://echarts.baidu.com/builder.html</a><span style="color: rgb(173, 6, 193);">)</span><span style="color: rgb(0, 16, 128);">网页下载仅包含必要组件的包，并且选择压缩。</span></p><p style="line-height: 18px; font-size: 12px; font-family: Consolas, Consolas, "Courier New", monospace; color: rgb(51, 51, 51);"><br></p><p style="line-height: 18px; font-size: 12px; font-family: Consolas, Consolas, "Courier New", monospace; color: rgb(51, 51, 51);"><span style="color: rgb(0, 16, 128);">下载的文件放在 </span><span style="color: rgb(173, 6, 193);">`</span><span style="color: rgb(0, 16, 128);">ec-canvas/echarts.js</span><span style="color: rgb(173, 6, 193);">`</span><span style="color: rgb(0, 16, 128);">，</span><strong style="color: rgb(173, 6, 193);">**</strong><strong style="color: rgb(240, 113, 120);">注意一定需要重命名为 </strong><strong style="color: rgb(173, 6, 193);">`</strong><strong style="color: rgb(240, 113, 120);">echarts.js</strong><strong style="color: rgb(173, 6, 193);">`**</strong><span style="color: rgb(0, 16, 128);">。</span>】</p><p>在运行的时候出现TypeError: Cannot read property 'get' of undefined错误，请问是怎么回事呢？</p>  
</div>
            