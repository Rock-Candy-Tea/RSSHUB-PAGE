
---
title: '开源文本引擎HarfBuzz 5.0发布 在支持"Boring Expansion"字体规范方面取得进展'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0724/fcd6f40ee922b43.webp'
author: cnBeta
comments: false
date: Sat, 23 Jul 2022 23:49:02 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0724/fcd6f40ee922b43.webp'
---

<div>   
HarfBuzz是开源的文本引擎，被许多不同的库和应用程序广泛使用。HarfBuzz的代码对Linux桌面和许多开源应用程序至关重要，而本周末其将迎来重大的5.0版发布。随着HarfBuzz
5.0的发布，开发者一直在致力于发展出对"Boring Expansion"字体规格的支持。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0724/fcd6f40ee922b43.webp" title alt="image.webp" referrerpolicy="no-referrer"></p><p>HarfBuzz 5.0的许多变化都集中在"BE"字体支持方面。这个"BE"被称为开放字体格式的"Boring Expansion"，以及一些"Better Engineered"字体格式的引用。</p><p>"Boring Expansion"规格旨在克服Open Font Format每个文件65k字形的限制，这样就可以在字体文件中存储数百万字形。对于亚洲字体特别是中文来说，突破65k的限制是必要的，泛Unicode字体超过了目前的限制，更好地拥抱渐进式字体丰富化，而COLR字体的容量需求也可能会超出这个限制。</p><p>Google Fonts参与了这个"BE"规范，并努力解决目前冲击开放字体格式的问题。作为一个整体，拟议的变化使我们能够创建由可重复使用的部分组成的紧凑的泛Unicode字体，这些部分是使用增强的变化能力建立的。此外，设计者被授权将这些部件的制作和组装方式与它们呈现给用户的方式分开。</p><p>关于这项工作的更多细节可以通过GitHub上的无聊扩展规范找到：</p><p><a href="https://github.com/be-fonts/boring-expansion-spec" _src="https://github.com/be-fonts/boring-expansion-spec" target="_blank">https://github.com/be-fonts/boring-expansion-spec</a><br></p><p>在BE-Fonts的带领下，扩展规范后会有更好的人机工程学和更好的围绕字体格式的仿真的暂定计划。</p><p>这个Google Docs幻灯片有更多关于BE字体工作的细节：</p><p><a href="https://docs.google.com/presentation/d/1dVfuU7YhUBXg9MtU6kYBXVs9082PiHpwhGPYa--yA7c/edit#slide=id.ge1e66518a2_0_241" _src="https://docs.google.com/presentation/d/1dVfuU7YhUBXg9MtU6kYBXVs9082PiHpwhGPYa--yA7c/edit#slide=id.ge1e66518a2_0_241" target="_blank">https://docs.google.com/presentation/d/1dVfuU7YhUBXg9MtU6kYBXVs9082PiHpwhGPYa--yA7c/edit#slide=id.ge1e66518a2_0_241</a><br></p><p>今天的HarfBuzz 5.0已经支持更多表格中超过65k字形的字体，支持AVAR表格的第二版，以及这项扩展规范工作的其他变化。</p><p>HarfBuzz 5.0还包括一些修复，改进了多个草书附件之间的互动，改进了COLR表的子集，改进了API的模糊处理，构建修复以及其他工作。</p><p>关于HarfBuzz 5.0的下载和更多细节请参见GitHub：</p><p><a href="https://github.com/harfbuzz/harfbuzz/releases/tag/5.0.0" _src="https://github.com/harfbuzz/harfbuzz/releases/tag/5.0.0" target="_blank">https://github.com/harfbuzz/harfbuzz/releases/tag/5.0.0</a><br></p>   
</div>
            