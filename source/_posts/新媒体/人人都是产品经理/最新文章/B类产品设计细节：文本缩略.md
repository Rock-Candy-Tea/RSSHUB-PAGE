
---
title: 'B类产品设计细节：文本缩略'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/92xYrOKF2cE5hdRF4R0N.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 13 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/92xYrOKF2cE5hdRF4R0N.jpg'
---

<div>   
<blockquote><p>编辑导语：文本缩略是产品界面常见的显示形式之一，当文本内容无法展示、或者自适应调整宽度有所变化时，文本则可能进行缩略。那么，具体有哪些缩略方式？本篇文章里，作者总结了文本缩略的具体形式以及设计时的注意要点，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5040093 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/92xYrOKF2cE5hdRF4R0N.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>说明：文本缩略是指展示空间不足时，隐去部分内容并用‘…’ 替代。包括但不限于以下情况：</p>
<ul>
<li>文本内容长度或高度超过列宽或行高；</li>
<li>图表中空间有限，文本内容无法完全显示；</li>
<li>自适应调整时宽度变小。</li>
</ul>
<h2 id="toc-1">一、缩略方式</h2>
<h3>1. 末端截断</h3>
<ul>
<li>单行内容超过列宽，超出的用‘…’ 省略；</li>
<li>多行内容超过设置行数，超出的部分用‘…’ 省略；</li>
<li>标签内文案超出由‘…’ 省略。</li>
<li>末端截断为长文本截断的通用模式。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/k6gJQYBi6IYZw8b6xSoN.png" alt width="758" height="689" referrerpolicy="no-referrer"></p>
<h3>2. 中间截断</h3>
<ul>
<li>设置开头、末端保留的字符数，在末端保留字符前显示‘…’ 。</li>
<li>开头保留字符数根据列宽以「显示尽量多的字符」的原则来确定（极端情况为开头不保留字符，即为「开头截断」；若空间十分有限，则尽量多地保留末端字符）。</li>
<li>中间截断在文本的开头相同、末尾字符对区别字段起到关键作用时使用。</li>
</ul>
<p><strong>场景举例 1：末尾为数字</strong></p>
<p>通常用于实例名（任务名、文件名、表名、系统）。</p>
<p>典型案例：完整字段如下</p>
<p>company_sales_record_20150116 company_sales_record_20150117</p>
<p>缩略结果：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/sNDeuQMqJ1tupx5X8gGV.png" alt width="750" height="296" referrerpolicy="no-referrer"></p>
<p><strong>场景举例 2：系列名称</strong></p>
<p>开头统一的系列长名称，比如部门名称，或者其他通过后半部分区分的字段。</p>
<p>典型案例：阿里集团的 BU 完整名称如下：</p>
<p>口碑-本地生活事业部-北方大区-北方运营 口碑-本地生活事业部-七星大区-东南运营</p>
<p>缩略结果：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RrdrCC1M1sQjGwUSYKsk.png" alt width="750" height="296" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、设计要点</h2>
<p>重要数字、时间不建议缩略。</p>
<p>名称列缩略可结合表头的拖拉控制显示与缩略，内容完全显示时‘…’ 消失。</p>
<p>单行文本省略使用 tooltip，多行文本省略使用展开与收起。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/2KwRBz9stfVjNV0u1bpM.png" alt width="751" height="600" referrerpolicy="no-referrer"></p>
<p>描述‘…’ 支持 hover，标签整个支持 hover。</p>
<p>标签文案过长时建议截断；标签数量多时建议通过折行全部展示，不建议通过‘…’ 隐藏后面的标签。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nGgZU5KBc1tKzutcDV4Y.png" alt width="748" height="407" referrerpolicy="no-referrer"></p>
<p>tooltip 不承载复杂文本和操作。</p>
<p>根据使用场景为字段设置合理的字数上限和展示空间，避免隐藏过多的内容。</p>
<p>tooltip 的尺寸不应过大，建议最大尺寸不超过长 320px、宽 160px。</p>
<p> </p>
<p>作者：林叶，蚂蚁集团设计师</p>
<p>本文由 @Ant Design 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5037842" data-author="1275742" data-avatar="http://image.woshipm.com/wp-files/2021/05/qQzaYS0DiYKZrsomCZyR.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            