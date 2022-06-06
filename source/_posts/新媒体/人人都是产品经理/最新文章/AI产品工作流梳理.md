
---
title: 'AI产品工作流梳理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Kcw0PwuhthoF0VcI85ql.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 06 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Kcw0PwuhthoF0VcI85ql.jpg'
---

<div>   
<blockquote><p>编辑导语：本文作者根据自己从0到1搭建指尖查词功能的经验，以大力智能台灯产品为例，从产品经理的视角，梳理了AI产品（计算机视觉产品）的工作流，感兴趣的小伙伴们一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5473293" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Kcw0PwuhthoF0VcI85ql.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近在做类似大力和有道的智能台灯产品，从0到1搭建了指尖查词功能，对AI产品算是有了一些基础的理解。</p>
<p>本文试图以产品经理的视角梳理AI产品（计算机视觉产品）的工作流。</p>
<h2 id="toc-1"><strong>一、工作流框架</strong></h2>
<p>下图是一个AI产品的大概框架。这里面关键的认知是，AI能力迭代是跟产品功能迭代平行的、一条需要基于反馈不断迭代的一个子工作流。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/TttQ9Xv4P4hcuACUYyqM.png" alt="AI产品工作流" width="675" height="310" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">引用自微软《人工智能系统》</p>
<p>基于两者是平行的流程，我们可以借鉴产品经理的工作流，对AI产研的工作流程进行拆解和构建。下面，我们来看一下每个流程中AI产研应该关注的问题。</p>
<h2 id="toc-2"><strong>二、需求分析</strong></h2>
<p>在需求分析阶段，对AI产研来说，同样需要了解用户、场景、需求。接下来举一些例子。</p>
<h3><strong>1. 场景分析</strong></h3>
<p>不同的场景对于AI的需求是不一样的。比如在于指尖查词项目中，我们需要了解用户在使用智能硬件产品时的灯光环境，这个涉及到我们对于算法训练集的选择。</p>
<blockquote><p>在学习场景中，可能很多家长或者孩子会在光线很暗情况下看书，但是他们可能自己并不知道。</p>
<p>还有的人家里的灯光很黄，拍出来的图像就会显模糊。还有的图像会有一些暗光甚至局部曝光。</p>
<p>另外，有些摄像头会在不同的光线之下自动做白平衡，这会导致最后出来的图像差异非常大，这些都会导致最后算法的准确率很差。</p>
<p>——纸上世界创始人分享</p></blockquote>
<h3><strong>2. 痛点分析</strong></h3>
<p>我们需要了解用户在某个场景下的问题，然后分析AI对此问题能否有效（提升效率、降低成本、提升体验）。</p>
<p>比如在指尖查词项目中，用户原有的解决方案比如查纸质字典，就存在以下问题：</p>
<p><strong>1）便捷性差</strong></p>
<p>字典是个大块头，不方便携带，一般都放在书桌。</p>
<p><strong>2）查找效率低</strong></p>
<p>寻找一个目标单词需要先找到首个字母所在的大概位置，然后再进一步去找该单词，定位比较麻烦。</p>
<p><strong>3）信息维度不够</strong></p>
<p>比如词典里面的单词音标，目的是教小朋友学习发音，但是低年级的小朋友是没有学到音标的。所以这些学生要有标准的发音进行引导，除此之外，还需要有发音的口型教学内容。基于计算机视觉的AI能力，类似有道词典笔的产品可以大幅提升查找效率，这是整个产品能够成立的关键。</p>
<h3><strong>3. 可行性分析</strong></h3>
<p>除了验证AI能否有效以外，我们还需要知道我们的AI是否可行。比如在指尖查词项目中，我们就需要知道用户对于AI的要求，比如以下指标：</p>
<ul>
<li>精度、召回率</li>
<li>结果返回耗时</li>
</ul>
<p>如果我们算法的精度大大低于用户的预期，则项目无法成功。</p>
<h2 id="toc-3"><strong>三、竞品研究</strong></h2>
<p>AI能力也需要进行竞品研究，我觉得可以从技术的成熟程度来进行对应的竞品研究。</p>
<h3><strong>1. 前沿技术创新</strong></h3>
<p>很多前沿技术虽然还没有被大规模投入使用，但是已经能产出很多demo了。寻找这一类的竞品，我觉得可以在github上面找到。</p>
<p>比如，我跟算法同学聊了指尖的轨迹跟踪，立马丢给我一个github的轨迹跟踪的项目deepsort。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/YXXFgJ1C8r80oAW74eps.gif" alt="AI产品工作流" width="512" referrerpolicy="no-referrer"></p>
<p>类似这种，github上的技术，对于自研AI的团队来说非常重要，一方面这些内容能够让我们了解技术的能力边界，另外一方面，基于这些开源的算法，我们能够快速搭建demo。</p>
<h3><strong>2. 业界成熟的技术</strong></h3>
<p>这一类可以从AI平台找到，比如百度、华为、阿里、腾讯这种AI大厂的开放平台，就展示各种已经成熟的AI能力，以及成功案例。</p>
<p>比如以百度AI为例，其官网就有非常多的技术，值得学习。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/k672CBGI7DP72OsoqA8D.png" alt="AI产品工作流" width="831" height="361" referrerpolicy="no-referrer"></p>
<h2 id="toc-4"><strong>四、算法设计</strong></h2>
<p>在算法同学进行算法设计时，我们AI产品需要知道算法，这样有利于我们进行产品设计，我觉得以下两个是一个好的切入点。</p>
<h3><strong>1. 整体框架</strong></h3>
<p>对于AI产品来说，虽然不需要写算法，但是知道整个算法的框架有利于产品设计。</p>
<p>比如在指尖查词项目中，如果在客户端部署了指尖检测的算法，我们就可以在检测到指尖时，给予用户及时的状态反馈，而不用等到整个文字识别结果返回才给到反馈。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/X6JucvaBnaqsJ3JfnPzP.jpeg" alt="AI产品工作流" width="832" height="353" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">推测大力的整体框架</p>
<p>对于算法，我们产品经理不应该把它当做黑盒子，而是应该了解，然后在此基础上做出更好的产品。</p>
<h3><strong>2. 接口文档</strong></h3>
<p>除了整体的框架，我们AI产品还可以通过了解接口文档，来增进对于算法的了解。</p>
<p>比如我们看了百度OCR的接口文档，我们发现AI能够识别文字的角度。基于这个能力，我们可以在发现用户书本方向放错时，给予用户及时的反馈。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/aperD9rw7Wgy3tBx5PiW.png" alt="AI产品工作流" width="653" height="468" referrerpolicy="no-referrer"></p>
<h2 id="toc-5"><strong>五、需求文档</strong></h2>
<p>在需求文档这块，除了传统的需求文档模块之外，AI产品（计算机视觉产品）可能需要需要在以下几个层面进行深入。</p>
<h3><strong>1. AI交互细节</strong></h3>
<p>大力台灯在指尖查词上的交互给业界定了一个标杆。具体而言，大力定义了几种交互状态：</p>
<ol>
<li>开始检测：方括号开始闪动</li>
<li>检测到用户的手指：方括号内出现手指</li>
<li>识别到手指后，开始进行文字识别：方括号开始出现转圈</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/sm2PNTuJCyo0oBWR27vV.jpeg" alt="AI产品工作流" width="834" height="381" referrerpolicy="no-referrer"></p>
<p>大力交互厉害的地方在于通过对三个图标（方括号、手指、加载圆圈）进行简单的组合，就构建了一套交互体系，给到用户即时反馈。</p>
<p>整个解决方案，对于用户来说学习成本比较低，是一个比较优雅的解决方案。</p>
<h3><strong>2. 异常情况处理</strong></h3>
<p>由于算法在早期的效果是不够理想的，所以我们要界定一些超出AI能力的异常情况，也就是黑话“兜底”。</p>
<p>比如计算机视觉中一直没有返回图像识别结果，对话机器人中一直无法判断用户是否说完话或者用户意图，等等。大部分的兜底策略就是用开玩笑的口吻回应用户，比如“这个单词还没学会”、“这个技能还要再练习”。</p>
<h3><strong>3. 指标需求</strong></h3>
<p>一些关于AI能力的指标需求，常见的指标如下：</p>
<ul>
<li>准确率、错误率</li>
<li>精确率（查准率）、召回率、F1</li>
<li>ROC曲线、AUC</li>
<li>计算速度、结果返回耗时、鲁棒性</li>
</ul>
<h2 id="toc-6"><strong>六、冷启动策略</strong></h2>
<h3><strong>1. 算法冷启动流程</strong></h3>
<p>算法最终会达到一个正向循环，即上线后拿到用户数据，对这些数据标注后，训练算法，提升算法性能，然后会有更好的体验，会有更多的用户使用，接着拿到更多的用户数据，走向正循环。</p>
<p>但是刚开始的时候，没有大量数据进行训练的时候，算法性能是不高的，需要慢慢达到正循环，再次之前的过程，我理解为算法的冷启动。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/mT5DfvfKuWR21ylePBMD.jpeg" alt="AI产品工作流" width="748" height="397" referrerpolicy="no-referrer"></p>
<h3><strong>2. 接入服务 vs 自研</strong></h3>
<p>如果我们是接入百度、华为等大平台的AI能力，那冷启动的过程相对来说要快很多，但是一个要注意的问题是大平台的服务相对来说是通用的，可能对于我们自己的垂直场景没有做过优化，估计数据表现也不会很好。</p>
<p>百度有一个EasyDL的平台，是专门解决这个问题的。</p>
<p>如果我们的深度学习算法是自研，我们可以通过以下几个层面的行动进行算法的冷启动：</p>
<p><strong>算法层面：</strong>把开源的算法拿来用，进行迁移学习，从而快速达到一定的算法精度。</p>
<p><strong>数据采集/标注:</strong></p>
<ul>
<li>购买市面上已有的数据集</li>
<li>机器合成对应场景的数据，快速生成训练集</li>
<li>通过人工或者工具产品的方式，收集对应场景的真实数据，进行标注</li>
</ul>
<h3><strong>3. 场景容错性判断</strong></h3>
<p>我们知道算法的精准度等指标刚开始是不理想的，尤其是在自研的情况下，我们需要让用户先用起来，然后收集数据之后，再进行训练和迭代。</p>
<p>其实这个跟产品的MVP很像，刚开始发布的第一个版本，也不是一个完美的版本，需要用户用起来之后进行迭代才行。</p>
<p>但是在冷启动的时候，要考虑场景的容错性。比如自动驾驶领域，可能对于计算机视觉的能力要求非常高，出错了会造成乘客的生命危险，这个场景的容错性是很低的，所以这种产品内部要做很多测试，达到较高的标准之后，才能发布给用户体验。</p>
<p>但是，对于很多场景容错性相对较高，比如娱乐游戏场景，则标准比较低，可以尽快上线，接受用户的反馈。</p>
<h2 id="toc-7"><strong>七、算法迭代</strong></h2>
<h3><strong>1. 准备测试集</strong></h3>
<p>我在做指尖查词的产品过程中，跟着算法工程师一起把算法的准确率从70%+提升到了90%+，可以分享一下整个过程。</p>
<p>深度学习作为监督学习，需要大量数据进行训练。这些数据分为三个部分，训练集、验证集和测试集。</p>
<ul>
<li>训练集：相当于课后的练习题，用于日常的知识巩固</li>
<li>验证集：相当于周考，用来纠正和强化学到的知识</li>
<li>测试集：相当于期末考试，用来最终评估学习效果</li>
</ul>
<p>对于AI产品经理来说，我们需要测试集，这样方便我们对深度学习算法进行评估。</p>
<h3><strong>2. 分析测试集数据</strong></h3>
<p>准备测试集之后，我们基于算法的框架，使用漏斗模型，得出每个节点的准确率。</p>
<p>比如，对于指尖查词来说，算法从开始识别，到最终识别成功，可以用以下的漏斗模型进行表示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/O5oS1Cib1KOSTY4RO95k.png" alt="AI产品工作流" width="409" height="421" referrerpolicy="no-referrer"></p>
<p>通过测试集的数据分析，我们发现，主要的问题出现在3-4层、4-5层漏斗中，即指尖识别的坐标错了（识别到别的字了）、文字识别错误（类似把apple识别为abble）。</p>
<p>更具体而言，整个测试集样本中，有12%的样本是指尖识别坐标错误，有6%是因为文字识别错误，所以我们第一个版本的准确率大概只有70%左右。</p>
<h3><strong>3. 找到改进机会点</strong></h3>
<p><strong>1）指尖识别坐标错误</strong></p>
<p>算法同学对于错误的样本原因进行分析，发现对于指尖识别坐标错误这一类型，是属于算法优化的点。</p>
<p>主要理由是，算法同学判断指尖附近内容的方法存在问题。优化之后，后面几乎没有坐标识别错误，正确率一下子提升了12%个点。</p>
<p><strong>2）文字识别错误</strong></p>
<p>对于识别错误，算法同学同样对错误的样本进行分析，并且分类。如下面所示：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/K70UjJLrK7HXd3dfVqvI.jpeg" alt="AI产品工作流" referrerpolicy="no-referrer"></p>
<p>主要的解决方案是针对细分场景，准备更多的数据进行训练，或者基于更优的规则，以提升准确率。</p>
<h3><strong>4. 迭代算法</strong></h3>
<p>经过一个周期的努力，我们把算法的准确率从70%+提升到了90%+，用户的体验有了质的提升。</p>
<h2 id="toc-8"><strong>八、用户体验管理</strong></h2>
<p>早期算法还不是很厉害的时候，我们需要主动做一些用户体验管理。我觉得可以从以下几个层面进行管理：</p>
<h3><strong>1. 预期管理</strong></h3>
<p>基于我们场景的容错率，我们的产品要在满足用户的最低要求后，才能给到他们使用。发布之后，最好也要进行预期管理，告知目前哪些场景可以支持，准确率怎么样，哪些又不能支持，希望能够给到用户合理的预期。</p>
<h3><strong>2. 容错设计</strong></h3>
<p>比如指尖查词场景里面，当算法不确定用户是指哪一个单词时，我们可以把两个相近的两个单词都给出来，方便用户进行挑选。</p>
<p>类似以下场景中，大力台灯把【朱】【旭】都展示出来，用户可以通过切换得到自己想要的词。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="AI产品工作流" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/DslbTASwkSJYEztucMQR.png" alt="AI产品工作流" width="600" height="400" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">竞品的指尖查词（图来自蓝鲸教育）</p>
<h3><strong>3. 用户反馈问题入口</strong></h3>
<p>某些场景我们的算法确实搞错了，则可以留一个入口给到用户。一方面给到用户一个宣泄的渠道，另外一方面也可以作为一个样本给到我们去判断底层的问题。</p>
<h3><strong>4. 规范用户行为</strong></h3>
<p>有一些场景AI功能还未覆盖，则我们需要规范用户行为，告知目前不支持这些场景。</p>
<p>比如，我们的OCR识别还不识别手写体，则用户拿手写体过来时，则要告知用户不支持手写体，不然用户会很有挫败感，类似还有：</p>
<ul>
<li>灯光过暗</li>
<li>字体过大或过小</li>
<li>书本折叠</li>
<li>手指盖住单词</li>
<li>识别非目标语言的文字</li>
</ul>
<h3><strong>5. 系统思考：不止AI</strong></h3>
<p>不能把所有的体验问题都归咎于AI算法，比如在识别过程中的耗时问题，除了AI算法可能存在问题外，我们的app可能在摄像头打开、识别结果数据库对比等环节都存在耗时过多的问题。</p>
<p>我们要进行系统思考，这样才能定位到真正的问题。</p>
<p>以上就是从产品经理的视角梳理AI产品的工作流，请多多指教。</p>
<p> </p>
<p>本文由 @小明的产品笔记 原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5472849" data-author="831840" data-avatar="http://image.woshipm.com/wp-files/2020/11/Vqz7FZuy6YgPdo63NO6u.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            