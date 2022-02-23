
---
title: '干货分享：B端表单设计优化'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BatPaOhGsWSdZQO0mcfO.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 23 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BatPaOhGsWSdZQO0mcfO.jpg'
---

<div>   
<blockquote><p>导读：表单作为B端产品中的基础通用组件，也是在各个B端产品中出现频率最高的元素之一。表单的设计也是比较考验设计师综合能力和设计细节的。一定程度上，表单设计的好坏也决定了产品的成败。本文作者分享了自己关于B端表单设计优化的经验，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5328640 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BatPaOhGsWSdZQO0mcfO.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是表单设计</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/gyISHaZjO4voo6A3ylwl.png" alt width="800" height="600" referrerpolicy="no-referrer"></p>
<p>“录入”是B端产品常见的任务场景，常用于<strong>向用户收集或验证信息</strong>。</p>
<p>在设计录入表单时，应尽量减少用户的思考和理解负担，提高表单的操作效率，降低用户出错的概率，才能提高录入任务的<b>完成度</b>和<b>满意度</b>。</p>
<p>针对不同的用户数据要进行不同的表单设计，以便适用各个场景功能。</p>
<p><img data-action="zoom" class="alignnone" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/50iEDZxm28DNcmAIL9j8.png" alt="表单入口" width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">表单入口</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/w4nahGLKBxaOd5NBzpt1.png" alt="新零售业务场景中表单无处不在" width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">新零售行业中，表单应用场景无处不在</p>
<h2 id="toc-2">二、表单种类</h2>
<h3>1. 基础表单</h3>
<p>基础表单是目前最常用的录入模式，在系统内用一个独立页面承载表单内容。页面内通常会包含：页面标题、表单区和操作区三部分。</p>
<p><b>适用范围：</b>适用于录入项较少的表单，所有录入项在一个页面内呈现。</p>
<p><b>操作按钮的位置：</b></p>
<p>1.若录入项很少不足半屏时，操作按钮可放置在表单结尾处展示，减少鼠标移动路径；</p>
<p>2.若录入项较多时，操作按钮悬浮页面底部展示。</p>
<h3>2. 分步表单</h3>
<p>该类表单录入模式通常用于拆分复杂录入流程。步骤条的展示可以较好地帮助用户理解完成任务所需步骤，以及当前所处阶段。</p>
<p><b>适用范围：</b>适用于录入项较多，且填写任务有先后之分的表单；在完成上一步任务的填写时，才可进入下一步。</p>
<blockquote><p>有些场景下，系统只需要用户录入简单的信息，此时可以考虑使用录入弹窗模式。还有些情况，比如用户处在一个任务流程中，当需要进行某些任务操作时，系统需要向用户采集信息，但又不想打断用户所处的流程，此时可以运用录入弹窗的模式，降低页面跳出感。</p></blockquote>
<p><b>适用范围：</b>通常用于轻量级任务，弹窗内可承载少量的录入项。</p>
<p><b>注意事项：</b></p>
<ul>
<li>弹窗不适用于复杂录入场景，若采用分步录入弹窗，一般不超过三步。</li>
<li>弹窗内的录入项平铺展示，一般不做页面内滚动，若录入项较多可使用基础表单页承载。</li>
</ul>
<h3>3. 分组表单</h3>
<p>对于录入项较多的页面，将信息按一定规律分组呈现，将大大降低用户的理解和操作成本。</p>
<p>这里可以按如下原则进行分组：</p>
<p><b>以必填项划分：</b>若表单内有必填项和非必填项，且各项之前关联度不高，可采用将必填项划分为一组进行优先呈现。该种方式有助于让用户快速发现自己需要录入的内容。</p>
<p><b>以相关性划分：</b>若录入项较多，且各项内容之间存在明显的关联度区分，可考虑以内容相关性进行信息分组。该种方式有助于让用户理解各项内容间的逻辑关系。</p>
<p><b>以操作成本划分：</b>若录入项间的操作存在差异或用户对需要录入的内容的信息获取途径存在难易之分，可将易录入或易获取信息的录入项放在表单靠前的位置，优先展示。该种方式有助于降低用户的录入门槛。</p>
<h2 id="toc-3">三、表单的组成</h2>
<p>表单由表单标签、表单域、提示信息、操作按钮组成。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/PyFkcAENvegKz3JfzJQQ.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>1. 标签</h3>
<blockquote><p>签用于提示用户需要输入什么信息。</p></blockquote>
<p>合理的标签布局结构，能够提高用户的阅读效率，还能降低信息填写时的错误率。常见的标签布局形式有：<strong>左右结构、上下结构和内部结构</strong>。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Bqm9rOwvS2ci7TkuJjmO.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><b>1.1 左右结构</b></p>
<p>左右结构是目前常见的表单布局形式，它减少了页面的垂直占用空间，而增加了横向占用空间。因PC端的横向空间很大，当录入项不多时，可以采用该种结构。</p>
<p>左右结构又分为右对齐标签和左对齐标签。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/adXq8nudYKEiMnrcc9nd.png" alt="右对齐标签" width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">右左对齐标签</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/XsPTV9mhqSwpTxCEAprZ.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">左对齐标签</p>
<p><b>1.2 上下结构</b></p>
<p>上下结构拥有较强的信息浏览和填写效率，用户的视觉浏览路径相对左右结构来说较短。该种结构适用于一行需要放置多项录入项的情况，或标签名称通常较长的表单。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/BrVSF09mzJbm6t2Q9tNZ.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">上下标签</p>
<p><b>1.3 内部结构</b></p>
<p>内部结构很少出现在B端，有时会用在C端。这里对于用户需要输入的内容，只保留了提示性文字，当用户进行输入时，内部的标签/提示性文字就会消失，将导致用户很难判别输入的信息是否准确。这种形式适用于极少输入项的表单（如登录）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/zZISHIG8vPYQcmeR4NGl.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>马泰奥·彭佐研究得出标签对齐方式的时间表</p>
<blockquote><p>根据马泰奥·彭佐的对齐方式研究出的时间表总结：单从效率角度看，顶对齐>右对齐>左对齐，根据不同的业务场景，效率并不是唯一的考虑指标。</p></blockquote>
<ul>
<li>希望用户放慢速度，好好考虑每个表单内容填写，那么采用左对齐；</li>
<li>顶对齐针对标签文字过多或者需要英文时，延展性更好</li>
<li>右对齐要考虑能否精简标签内容，确定好表单与界面的间距。</li>
</ul>
<h3>2. 输入域</h3>
<blockquote><p>输入域是用来采集用户数据信息的核心内容，每个输入域字段都包含一个类型的数据信息。</p></blockquote>
<p><b>选择合适的输入域：</b>对于用户来说，表单的填写体验再好也会造成一定的负担，所以表单设计的时候尽可能减少用户的思考、理解，选择合适的输入域类型，提升表单的输入效率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MmxYc4PKihH7uEnQTfMf.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、表单设计原则</h2>
<p>通过SaaS新零售表单设计总结出表单设计的3大原则：<b>明确、高效、安全感</b></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/SRdCx9cqz8JMuGsPVmsV.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>1. 明确</h3>
<p><strong>1.1 视觉降噪</strong></p>
<p>根据倒金字塔设计原则，最先呈现最重要的资料，然后呈现附加的详细信息，重要性依先后顺序递减，能够快速传递重要信息，让浏览变得更有效率。</p>
<p>通过合理的信息输入组件&页面布局&交互方式可以使用户快速完成表单也的信息填写任务。</p>
<p>例：必填项和非必填项标星（此规则非必须，根据不同业务属性灵活调整0</p>
<ul>
<li>全部为必填or非必填时，不标识</li>
<li>必填项比重很大，可适当提示非必填项，而非全部添加“*”，降低用户的视觉干扰，增加心里负担</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ZZekP589kwGkHLQNO3w4.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1.2 准确性</strong></p>
<p>输入框的长度根据用户输入信息的多少进行智能设置，非必要情况下，不需要为了让输入框长度保持一致，而出现太长或太短的情况，需要结合实际情况，设置长度，提前给用户心理预期。太长的输入框会增加用户负担。</p>
<p>表现形式要为用户填写提供有用线索，采用不同长度的文本框提供了暗示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/QGH1hCdwr0HJFd7Uktv5.png" width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>长度不同的输入框比相同尺寸的输入框视觉看上去更加和谐</p>
<p>注意：根据产品的模度值设置几个通用的长度，不要设定太多宽度，会让表单显得凌乱。</p>
<blockquote><p>Tips：什么是模度值？受柯布西耶模度的启发，追求「秩序之美」，Ant Design提取了一组可以用于 UI 布局空间决策的数组，他们都保持了 8 倍数的原则、具备动态的韵律感。经过验证，可以在一定程度上帮助我们更快更好的实现布局空间上的设计决策。模度具体落实在设计上，先梳理产品中常见的表单类型，然后设置一个默认宽度在这里的使用，根据模度的规则，设置了XS、S、 M、L、XL五个尺寸，根据输入内容选择不同长度的输入框。</p></blockquote>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/NVPiy7d3wVs2XeO8Jp8o.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">如何确定输入框的长度</p>
<h3>2. 高效</h3>
<p>依据尼尔森十大可用性原则中的灵活高效和协助记忆原则，做到<strong>灵活、易用、高效、智能</strong>，尽量减少用户对操作目标的记忆负荷。</p>
<p><strong>2.1 设置合理默认值</strong></p>
<p>系统还可以自动为用户填写一部分表单，从而降低录入成本，让用户减少操作步骤，提高操作效率</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MKKWYkhhoeQyHQAphRtX.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">将一些输入框给默认的值会提升表单提交效率</p>
<p><strong>2.2 自动获取/搜索</strong></p>
<p>有些业务场景，用户大概率会复用之前已填写的内容作为模板，并在上面稍作修改，此时在新建立的录入页面时，可以默认带入用户之前的数据。</p>
<p>系统根据上下文或搜索自动获取填写信息，降低用户的记忆负荷，提升效率。</p>
<p>在新零售业务场景中，这类输入通常是输入商品名称或者商品名称，我们采用「模糊搜索」的方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/W6PYK8Fy6Abh8BUYsAkE.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>2.3 智能录入</strong></p>
<p>对于一些标准证件类信息的录入，可以通过OCR识别文件内容。当用户上传图片后，运用图像识别技术提取关键信息并自动填入结果。值得注意的是，如果图片不清晰或存在水印，将大大降低识别准确度。此时应提供修正渠道，让用户可以逐一校对并修改文本内容。</p>
<p><strong>2.4 组件化设计</strong></p>
<p>通过设计评审敲定后提炼出规范，组建标准，提取组合用法以覆盖各个业务场景。实现设计和开发一体化，让设计面向开发，让开发贴近设计，减少设计及开发人员的额外工作量，让工作变得十分高效。</p>
<p>目前工作阶段处于中台全面改版中，改版的最大难题在于组件库落地，我们在实际工作中，总结梳理了通用组件库和实际业务场景结合的定制组件库，根据下图进行实际的开发跟进。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6OJYtD6DDDZ6KQDDXNbo.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>3. 可信任</h3>
<p>依据尼尔森十大可用性原则中的<strong>容错、防错以及反馈原则</strong>，在操作的前中后分别进行防错、实时反馈、提醒和纠错。比在发生错误时设置提醒弹窗更好的设计方式，是在这个错误发生之前就避免它。可以帮助用户排除一些容易出错的情况，或在用户提交之前给他一个确认的选项。在此，特别要注意在用户操作具有毁灭性效果的功能时要有提示，防止用户犯不可挽回的错误。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Wd6edaGUyI403OA5lstB.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>1.预防错误</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/L6QGcRyFWRm2FW4Y4CsL.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>2.实时反馈</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6Pb64VBEjHv2WUjuXBi1.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>3.提醒/纠错</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Z9FgReYnWYdocztQMVyl.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><strong>4.所见即所得</strong></p>
<p>依据尼尔森十大可用性原则中的贴近场景原则，遵循真实场景的认知、习惯，让信息的呈现更加自然，易于辨识和接受。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Bo8kHpmifQ3mb1Tys2Ry.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、总结与反思</h2>
<blockquote><p>表单的优化，对于整个产品的体验都有着重大的意义，需要结合实际的业务场景，不停的优化细节，为商业和用户助力。</p></blockquote>
<ul>
<li>提升表单的易用性可以让公司降本增效，减少现场实施的工作量，提升用户的签约率。</li>
<li>对于设计师而言，运用组件化的设计思维，可以大大提高工作效率，将精力投入到设计验证和用户研究中，发挥更大的设计价值。</li>
</ul>
<p> </p>
<p>本文由@萌夏夏夏 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5327215" data-author="710065" data-avatar="http://image.woshipm.com/wp-files/2022/02/7OGXrhcP09tbbHZacGjB.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            