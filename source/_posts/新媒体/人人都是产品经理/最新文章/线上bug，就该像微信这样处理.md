
---
title: '线上bug，就该像微信这样处理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wKm8dO6wowH7a7KeRYQh.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 24 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wKm8dO6wowH7a7KeRYQh.jpg'
---

<div>   
<blockquote><p>编辑导语：产品在运行过程中出现bug是很常见的事情，有些bug可能是致命的，有些bug可能只是轻微地影响用户的产品使用体验，那么，面对不同等级的bug，产品经理应该如何处理？本文作者就对bug的处理发表了他的看法，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5454627 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wKm8dO6wowH7a7KeRYQh.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近感觉微信bug不断。</p>
<p>先是Android 8.0.22版本里，出现了一个奇怪的用户完全看不懂的Matrix<strong>「性能检测工具」。</strong></p>
<p>Matirx是腾讯的性能检测，这<strong>大概率是不小心把debug工具打进了正式包。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="线上bug，就该像微信这样处理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/QnzJMvWK3tOBzl5KmnPf.jpeg" alt="线上bug，就该像微信这样处理" width="530" height="582" referrerpolicy="no-referrer"></p>
<p>因为这个看不懂的功能，网上炒的不可开交，微信云淡风轻，在2周后的Android 8.0.23内测版中又去掉了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="线上bug，就该像微信这样处理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cxF0A9RXNbqPYlCIq9SA.jpeg" alt="线上bug，就该像微信这样处理" width="529" height="557" referrerpolicy="no-referrer"></p>
<p>然后，是公众号<strong>「朋友还关注」网络出错</strong>，而同一个手机上视频号「朋友还关注」能打开。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="线上bug，就该像微信这样处理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/bQCBJfmlonpqYBYiI97u.png" alt="线上bug，就该像微信这样处理" width="536" height="608" referrerpolicy="no-referrer"></p>
<p><strong>这应该也是个bug。</strong></p>
<p>看了微信的这两个小bug，你有什么想法？</p>
<p>对了！微信都时常出bug，你的产品有bug也正常。</p>
<p>所以，我们需要正确的认识bug，<strong>树立正确的bug观：</strong></p>
<p><strong>1）bug是产品的一部分，在产品发展过程中不可避免</strong></p>
<p>就像我们偶尔会生病一样，你没法保证你永远不生病。</p>
<p><strong>2）业务越复杂、功能越复杂、迭代越迅速，bug也会相对越多</strong></p>
<p>所谓做得越多，犯错概率越大。</p>
<p>如果要不出bug，最好的办法，就是啥也不做。</p>
<p><strong>3）事情有紧急，bug有大小</strong></p>
<p>大bug，就是事故，很紧急，快速处理。</p>
<p>小bug，是虫子，正常灭杀即可。</p>
<h2 id="toc-1">01</h2>
<p><strong>先说说bug的来源。</strong></p>
<p>bug，原意为虫子，现在通常指产品缺陷、故障、问题等。</p>
<p>第一代计算机是由许多庞大且昂贵的继电器组成，并利用大量的电力来使继电器工作。可能正是由于计算机运行产生的光和热，引得一只小虫子bug钻进了一支继电器内，导致整个计算机无法工作。</p>
<p>研究人员费了半天时间，总算发现原因所在，把这只小虫子从继电器中取出后，计算机又恢复正常。后来，bug这个名词就沿用下来，表示电脑系统或程序中隐藏的错误、缺陷，漏洞或问题。</p>
<p>与Bug相对应，人们将发现bug并加以纠正的过程叫做“debug”，意即“捉虫子”或“杀虫子”。</p>
<h2 id="toc-2">02</h2>
<p><strong>再说说bug的等级。</strong></p>
<p>专业的测试同学，一般把bug分为四级。一级最致命，四级最轻。</p>
<h3>一级：致命bug</h3>
<p>通常表现为，主流程无法跑通，系统无法运行，崩溃或严重资源不足，应用模块无法启动或异常退出，主要功能模块无法使用。这属重大事故。</p>
<p>比如系统无法登录，支付报错。</p>
<h3>二级：严重bug</h3>
<p>通常表现为，影响系统功能或操作，主要功能存在严重缺陷，但不会影响到系统稳定性。</p>
<p>比如会员权益派发错误。</p>
<h3>三级：一般bug</h3>
<p>通常表现为界面、性能缺陷。</p>
<p>比如商品详情页头图、评论区没有显示。</p>
<h3>四级：提示bug</h3>
<p>通常表现为易用性及建议性问题。</p>
<p>比如文字排列不整齐，出现错别字等。</p>
<p>如果按照上面的标准。</p>
<p>微信误上线「性能检测工具」，公众号「朋友还关注」报错，应该都属于三级bug。</p>
<p><strong>但是不同的公司，bug等级定义标准略有差异。</strong></p>
<p><strong>更规范的公司，会将bug带来影响进行量化，然后定级。</strong></p>
<p>比如从影响用户和带来经济损失来定级，不如。</p>
<p>一级bug：影响10w以上用户，或收入损失100w以上</p>
<p>二级bug：影响5w-10w用户，或收入损失30w-100w</p>
<p>三级bug：影响1-5w用户，或收入损失5w-30w</p>
<p>四级bug：影响1w用户以下，或收入损失5w以下</p>
<p>这是我举例定义的数值，不一定合理。</p>
<h2 id="toc-3">03</h2>
<p><strong>不同的bug等级，处理方式不一样。</strong></p>
<p>对于一二级bug，要一时间修复，没得商量。</p>
<p>这个bug直接带来的是用户流失、坏口碑和经济损失。</p>
<p>对于三级bug，可紧急发版修复。</p>
<p>对于四级bug，如果资源紧张，可正常排期修复。</p>
<p>但是很多情况下，大家谈bug色变。</p>
<p>特别是研发，一说到线上bug，就内心OS就开始骂娘。</p>
<p>并且很多情况下，只要是bug，就放下工作，第一时间去处理。</p>
<p>这都不是正确的bug观。</p>
<p>你看，上文中微信的线上问题，只要不影响核心体验，就正常排期发布。</p>
<p><strong>bug不是天大的事，正确看待。</strong></p>
<p><strong>当然也不要把bug不当回事。</strong></p>
<p><strong>需要对线上bug，保持敬畏。</strong></p>
<p>尽量减少线上问题的产生，这是基本的工作态度。</p>
<h2 id="toc-4">04</h2>
<p>一般，产品测试阶段，bug由测试提出，由程序员修复。</p>
<p>产品上线后，bug由用户、业务、产品反馈，由程序员修复。</p>
<p>测试对整体产品质量负责。</p>
<p><strong>那bug的产生，是不是测试和程序员的事情呢？和产品经理无关呢？</strong></p>
<p>代码是技术写的，功能是测试测的，表面上看，好像是和产品经理无关。</p>
<p>但是进一步去探究，你就会发现，<strong>产品经理也是产品质量把控过程中的重要角色。</strong></p>
<p>产品经理如果能从<strong>下面几个方面做得更到位</strong>，也能大大降低线上bug的出现。</p>
<ol>
<li>需求设计阶段，方案反复推敲几遍，需求更加完备和明确，产品逻辑要闭环。</li>
<li>需求讲解阶段，进一步明确需求和细节。</li>
<li>测试用例评审阶段，认真参与，补充重点关注的case和隐藏case。</li>
<li>上线前PM验收阶段，充分验收。</li>
</ol>
<p>如此，bug出现概率将进一步下降。</p>
<p><strong>所以，产品质量不只是测试和研发的事，也和产品经理有关。</strong></p>
<h2 id="toc-5">05</h2>
<p><strong>小结下，关于bug说了几个观点：</strong></p>
<ol>
<li>bug是产品的一部分，平常心对待。</li>
<li>bug原意为虫子，现在通常指产品缺陷、故障、问题等。</li>
<li>一般bug分为致命、严重、一般、提示四个等级。</li>
<li>不同的bug等级，处理方式紧急程度不一样。</li>
<li>对线上问题保持敬畏。</li>
<li>bug不只是测试、研发的事。</li>
</ol>
<p>最后，关于产品bug，你有啥想说的。</p>
<h3>#专栏作家#</h3>
<p>岳老三，微信公众号：产品笔记（ID：cpbiji），人人都是产品经理专栏作家。7年产品工作经验，前网易、陌陌高级产品经理。任何商业进化的方向是效率的提升，喜欢用产品思维挖掘事物本质。相对擅长产品分析、产品设计、逻辑思维等。</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5454462" data-author="67974" data-avatar="http://image.woshipm.com/wp-files/2016/01/未标题-111.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            