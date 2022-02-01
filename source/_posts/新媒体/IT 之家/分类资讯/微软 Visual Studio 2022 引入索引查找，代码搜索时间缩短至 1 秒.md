
---
title: '微软 Visual Studio 2022 引入索引查找，代码搜索时间缩短至 1 秒'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/67bc83ca-d32d-4594-b934-79acf3c8fb3b.gif'
author: IT 之家
comments: false
date: Tue, 01 Feb 2022 07:25:30 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/67bc83ca-d32d-4594-b934-79acf3c8fb3b.gif'
---

<div>   
<p data-vmark="17c3"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 2 月 1 日消息，微软近日在官方<a href="https://devblogs.microsoft.com/visualstudio/code-search-in-visual-studio-is-about-to-get-much-faster/" target="_blank">博客平台</a>发文称，Visual Studio 2022 中的代码搜索将变得更快。</p><p data-vmark="4b0e">据官方介绍，与 Visual Studio 2019 相比，对于 95% 的搜索，Visual Studio 2022 在文件中查找的速度已经提高了 2 倍以上。微软希望使代码搜索更加出色，在最新的 <span class="accentTextColor">Visual Studio 2022 17.1 Preview 3</span> 引入了文件中的索引查找，让搜索更快。</p><p data-vmark="c499"><img src="https://img.ithome.com/newsuploadfiles/2022/2/67bc83ca-d32d-4594-b934-79acf3c8fb3b.gif" w="1440" h="545" alt="VS 17.0（左）和 VS 17.1 Preview（右）对比，1560 个项目中搜索约 50000 个文件" title="微软 Visual Studio 2022 引入索引查找，代码搜索时间缩短至 1 秒" width="1440" height="310" referrerpolicy="no-referrer"></p><p data-vmark="8545">▲ VS 17.0（左）和 VS 17.1 Preview（右）对比，1560 个项目中搜索约 50000 个文件</p><p data-vmark="4be2">官方发布了一张图标，展示了自 Visual Studio 2019 以来，95% 的搜索都得到了性能改进。在 17.1 Preview 3 中，<span class="accentTextColor">95% 的搜索在 1 秒多的时间内找到了搜索查询的所有匹配项</span>。</p><p data-vmark="9588"><img src="https://img.ithome.com/newsuploadfiles/2022/2/a93296ca-0769-45d3-bbef-0499e02dd41c.png" w="1248" h="691" alt="Image FiF Graph" title="微软 Visual Studio 2022 引入索引查找，代码搜索时间缩短至 1 秒" width="1248" height="454" referrerpolicy="no-referrer"></p><p data-vmark="cce1">IT之家了解到，用户想要体验最新的搜索改进，需要下载 Visual Studio 2022 17.1 Preview 3 版本，在工具 > 选项 > 环境 > 预览功能并选中“启用索引以获得更快的查找体验”。</p><p data-vmark="737b">当用户启用该功能后，在解决方案加载或文件夹打开时，Visual Studio 会启动一个附属进程“ServiceHub.IndexingService.exe”并将文件列表传输给它以进行索引。然后，索引器会遍历文件并构建每个文件中包含的所有 n-gram 的索引。</p><p data-vmark="434a">索引进程通过在 Visual Studio 主进程之外以低于正常操作系统优先级运行来避免影响解决方案加载、构建和用户活动。</p>
          
</div>
            