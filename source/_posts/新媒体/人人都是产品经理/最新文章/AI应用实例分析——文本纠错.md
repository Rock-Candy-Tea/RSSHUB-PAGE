
---
title: 'AI应用实例分析——文本纠错'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/nWDeIN6lOsdeQah7GWPA.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 10 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/nWDeIN6lOsdeQah7GWPA.jpg'
---

<div>   
<blockquote><p>编辑导语：AI在现实中的应用有很多，你有没有想过，它还可以进行文本纠错呢？传统的校对既耗时又枯燥，通过AI纠错，不仅能更快完成，还能提高准确度。那么AI“文本纠错”背后的原理是什么呢？和我一起看看吧！</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5349063" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/nWDeIN6lOsdeQah7GWPA.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>前面跟大家分享了AI开放平台的相关内容，之后想围绕AI应用实例这块跟大家分享交流，这节主要讲述跟NLP相关的一个应用实例——“文本纠错”。</p>
<h2 id="toc-1"><strong>一、背景</strong></h2>
<p>虽然这几年短视频在内容传播方面发展得很火，但是文稿仍然占据重要地位。而文稿传播最重要的一点就是信息的准确性，尤其是一些有知名度的正式平台更是会在文稿发送前进行校对修正。</p>
<p>传统的人工校对工作量是非常大的，一篇5000字的文稿完成校对差不多需要1-2个小时，对于校稿人员来说既耗时又枯燥。有一家内容平台就提出，希望我们通过AI能力提供快速校对工具，主要针对中文文稿，帮助校稿人员和编辑人员减少内容错误。</p>
<p>为了满足该需求，我们基于NLP技术提供了文本纠错服务。</p>
<h2 id="toc-2"><strong>二、关键技术</strong></h2>
<p>文本纠错中用到的技术的前世今生在这不过多介绍了，目前文本纠错的主流方向还是使用机器学习的方式来完成，其中需要用到的核心技术主要包括语言知识学习、上下文理解和知识计算。</p>
<ul>
<li><strong>语言知识学习：</strong>可以理解为是对语言规则等先验知识的学习，通过学习词法、句法等规则进行语言模型构建，例如中英文的主谓宾结构就是不一样的。</li>
<li><strong>上下文理解：</strong>是指分析错误点上下文语境和语义，从纠错候选中选择最合适的。尤其是中文，相同的词汇在不同语境中往往表达不同的含义。</li>
<li><strong>知识计算：</strong>知识计算主要包括关联知识计算和文本理解，关联知识主要是通过对全局知识的统计来实现纠错，可以是局部不完整语句的补充。文本理解是通过统计理解全局句子内容，解决低频领域知识的泛化问题。</li>
</ul>
<h2 id="toc-3"><strong>三、产品设计</strong></h2>
<h3>1. 应用场景</h3>
<p><strong>（1）用户场景：</strong>审稿或者编辑人员输入中文文字信息，系统自动纠错，并给出修改建议，审稿人员对错误快速修订。</p>
<p><strong>（2）应用边界：</strong></p>
<ul>
<li>支持用词错误检测，针对音近、形近的错字和别字进行纠正</li>
<li>支持句子级错误检测，主要是针对句子中出现的多字、少字等错误，相对难度校大。</li>
<li>支持场景类错误纠正，这类错误需要具备一些特定领域的知识才能识别纠错，所以尽量支持。</li>
</ul>
<h3>2. 产品定位</h3>
<ul>
<li><strong>产品定位：</strong>为应用工具型产品，实现中文文本自动纠错功能。</li>
<li><strong>用户定位：</strong>满足两类B端用户，第一类针对具备自主的文稿编辑工具，提供API服务，与现有系统进行改造融合；第二类是针对缺少文稿编辑工具的用户，提供web页面功能。</li>
</ul>
<h3>3. 产品业务流程</h3>
<p>产品核心业务流程主要是产品端和算法端的交互，具体业务流程如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/CJgiiHrPnGyn7NyW3Cp6.png" alt width="1193" height="243" referrerpolicy="no-referrer"></p>
<h3>4. 产品功能设计</h3>
<p><strong>（1）页面功能设计</strong></p>
<p>页面核心功能主要包括如下：支持内容上传、内容审查、结果确认和内容下载。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/32gj4jGAuB5H0O0T3qRz.png" alt width="1130" height="201" referrerpolicy="no-referrer"></p>
<p>主要页面设计如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/J9oePlSwLUR9loH48hD9.png" alt width="945" height="607" referrerpolicy="no-referrer"></p>
<p><strong>（2）API接口设计</strong></p>
<p>包括内容纠错请求接口和结果回调接，分别用于内容审查纠错和结果返回，以下描述主要的输入和输出参数：</p>
<ul>
<li><strong>输入：</strong>接口鉴权、文本内容、文本编码格式等。</li>
<li><strong>输出：</strong>文本分析结果，包括源文本、纠错文本、文本位置，置信度。</li>
</ul>
<h3>5. 评估指标</h3>
<p>产品上线前，需要对产品的性能进行评估，主要包括三个指标：误报率、召回率和处理时间。</p>
<ul>
<li><strong>误报率：</strong>代表正确的句子被改错的比率，等于正确句子被纠错的个数/正确句子的个数。</li>
<li style="list-style-type: none;"></li>
<li><strong>召回率：</strong>代表错误的句子被全部纠正的比率，等于含有错误的句子被改正的数量/所有含错误的句子数量。</li>
<li><strong>处理性能：</strong>代表处理多少个字符的耗时，单位是千字耗时，s/千字符。</li>
</ul>
<h2 id="toc-4"><strong>四、结论</strong></h2>
<p>文本纠错是NLP非常基础的场景应用，但是实际业务价值却是很大的。在具体业务场景应用方面不仅可以用在在媒体编辑、电子病历等输入文本纠错，还可以应用于语音搜索、客服问答等业务。</p>
<p> </p>
<p>本文由@Eric_d 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p class="paragraph text-align-type-left pap-line-1 pap-line-rule-auto pap-spacing-before-0pt pap-spacing-after-0pt">题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5347709" data-author="678450" data-avatar="http://image.woshipm.com/wp-files/2019/01/WlgJv6IqlQDsnCmjBOyC.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            