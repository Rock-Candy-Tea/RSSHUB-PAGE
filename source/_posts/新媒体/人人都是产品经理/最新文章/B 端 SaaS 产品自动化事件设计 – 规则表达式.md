
---
title: 'B 端 SaaS 产品自动化事件设计 – 规则表达式'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/03/4N4JN1mf9DuwbGcDuUAR.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 14 Mar 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/03/4N4JN1mf9DuwbGcDuUAR.jpg'
---

<div>   
<blockquote><p>编辑导语：随着B端行业的热度不断上升，相关讨论度也在不断上升，一些产品经理想进入B端行业，但是了解甚少。在B端SaaS产品中，我们经常会遇到一些自动化事件设计模块。本文就B端SaaS产品自动化事件设计进行了分析讲解。推荐对B端SaaS产品自动化感兴趣的用户阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5212725 aligncenter" src="https://image.yunyingpai.com/wp/2022/03/4N4JN1mf9DuwbGcDuUAR.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>背景：由于疫情或政策原因，目前某预约SaaS平台商家反馈希望能够对用户进行身份识别，以便判断用户是否具备预约资格。</p>
<h2 id="toc-1">一、需求分析</h2>
<h3>1. 商家的声音(Voc)</h3>
<ul>
<li>商家A ：xxx市只允许<strong>某某省（某某市除外）</strong>的用户进行预约。</li>
<li>商家B：xxx市本地市民凭xxxx<strong>身份证开头</strong>可购买预约特惠票。</li>
<li>商家C： xxx市疫情指挥部要求，具备<strong>48小时核酸记录</strong>才能进行预约。</li>
<li>商家D： xxx市提供的<strong>老人/小孩用户</strong>定向预约。</li>
</ul>
<h3>2. 场景分类</h3>
<p>经过信息收集整理，了解到目前商家提及的需求场景主要有以下3类：</p>
<ol>
<li>商家仅提供本地化服务项目。</li>
<li>商家配合疫情防控弹性约束。</li>
<li>限定特定年龄段、性别等属性。</li>
</ol>
<h3>3. 业务价值</h3>
<ul>
<li><strong>降本增效：</strong>自动化便于商家高效管理预约订单，代替人工完成繁琐重复的工作，降低劳动成本，提升效率。</li>
<li><strong>政策法规：</strong>自动化配置满足目前疫情大流行背景下，配合地方政府进行风控管理。</li>
<li><strong>业务弹性：</strong>对于特定约束的服务项目，能够自由组合规则匹配符合的定向用户，自动过滤甄别。</li>
<li><strong>可用程度：</strong>需求具备丰富预约业务可落地场景，自动化产品能力具备标准化特性，具备高度可复用特性。</li>
<li><strong>技术成本：</strong>技术实现周期短，属于商家业务关键痛点，付费升级意愿高，已有xx家意向商家。</li>
<li><strong>紧急程度：</strong> 紧急重要程度高，目前已有xx家商家受到地方政府管控影响业务正常运营。</li>
</ul>
<h2 id="toc-2">二、产品规划</h2>
<h3>1. 现有业务流</h3>
<p>（1）现有业务流程不具备用户身份识别能力，需要构建新的基础能力或在已有能力上改造已满足业务需求。</p>
<p>表单模块与「自动化」的理念高度吻合，而且表单在预约业务流程可以广泛适用于各行各业。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/HgCx4TFAILLcEGhKtLmA.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="543" height="371" referrerpolicy="no-referrer"></p>
<p>SaaS平台在预约业务流程中，目前已初步具备预约资料表单功能，但在此之前仅用作信息收集用途。</p>
<p>（2）目前平台预约资料表单提供的字段类型有“联系信息字段”和“通用字段”，总结已有字段可以划分为4种类型进行识别，分别是：字符串、数字、日期和多选项。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/01X99dF7yDOXuHJTNEDI.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="646" height="235" referrerpolicy="no-referrer"></p>
<p>（3）对于不同的字段类型，经过竞品分析调研，整理出以下常见的字段匹配规则。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/J9QHBlHXGO7sXyYy7C4l.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="672" height="411" referrerpolicy="no-referrer"></p>
<p>以“字符串”类型的信息项为例说明：提供了“是”、“不是”、“包含”、“不包含”、“以…开始”、“以…结束”的规则选项。</p>
<p>对于“字符串”类型题目：你最喜欢的篮球明星是谁？</p>
<p>假设你设定规则为【是“科比”】，那么对于该题目来说，只有用户填写的内容完全匹配【科比】，才算匹配上规则。</p>
<p>如果你设置的是【包含“科比”】，那么用户填写的内容只要有【科比】，即匹配规则，如果不含则不匹配规则。</p>
<p>以此类推，理解其他字段和对应的规则。</p>
<h3>2. 迭代业务流</h3>
<p>为了能从用户填写的预约资料进行身份识别，需要对于预约资料进行改造，在预约资料表单模块添加“自动化事件”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/byctGFvi9L0LD7ZFZrsr.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="646" height="668" referrerpolicy="no-referrer"></p>
<p>大致流程是商家端需要先针对预约资料信息项设定好规则表达式，启动自动化事件。</p>
<p>当用户进行服务项目预约时，会进行3轮的检查。分别是“是否启用自动化事件” → “是否匹配规则”→ “匹配规则是否可以预约”。</p>
<p>商家预设匹配规则「可以预约服务项目」的话，3项检查都通过，用户即可进行服务项目预约。</p>
<h3>3. 逻辑规则表达式</h3>
<p>（1）在预约资料表单设定规则时，存在多项规则组合设定的情况，比如，<strong>只允许A省但不含A1市的市民可以预约特惠项目</strong>，用逻辑语言翻译就是：<strong>用户身份“是A省”且“不是A1市”</strong>。</p>
<p>（2）面对这种情况需要使用到逻辑语言进行匹配规则串联，逻辑语言会有：“且(&)、“或(|)”、“非(!)”3种常见的类型。</p>
<p>目前在产品的现有字段中，只需要用到“且(&)”和“或(|)”2种就能满足需求，未来根据新增字段类型，再决定增加“非(!)”条件。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/GWwNy8yXZ3tFMFwMl9NA.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="670" height="244" referrerpolicy="no-referrer"></p>
<p>（3）“且”、“或”用法示例：</p>
<p>A且B =A&B =同时满足A和B规则，即为匹配。</p>
<p>A或B =A|B=只要满足A或B其中一项规则，即为匹配。</p>
<p>另外，在设计过程中，逻辑语言存在一定使用门槛，需要尽可能降低商家在设定时的难度。</p>
<h2 id="toc-3">三、方案设计</h2>
<h3>1. 自动化事件</h3>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/98mVSLAKM28fCA3tNI9z.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="616" height="242" referrerpolicy="no-referrer"></p>
<p>经过讨论，决定基于原有预约资料表单业务增加「自动化事件」。预约资料表单已被大量商家投入业务运营，对于不需管控的商家，默认设定为“不限制”。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/57xvGSjRoji9MWN2XIG2.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="691" height="251" referrerpolicy="no-referrer"></p>
<p>商家可以依据运营需要，自行设定自动化事件规则表达式并启用。</p>
<h3>2. 复合规则表达式</h3>
<p><strong>（1）单项规则</strong></p>
<p>单项规则时，比如限制身份证是“440300”开始的规则，可以这样表达：(&#123;身份证&#125;[以…开始]&#123;440300&#125;)。</p>
<p><strong>（2）“且”组合规则</strong></p>
<p>多项“且”规则时，比如限制身份证是“440300”开始，并且不含“440399”的规则。可以这样表达：(&#123;身份证&#125;[以…开始]&#123;440300&#125;)且(&#123;身份证&#125;[不含]&#123;440399&#125;)…。</p>
<p><strong>（3）“或”组合规则</strong></p>
<p>多项“或”规则时，比如限制身份证以“440300”开始，或者以“440399”开始的规则。可以这样表达：(&#123;身份证&#125;[以…开始]&#123;440300&#125;)或(&#123;身份证&#125;[以…开始]&#123;440399&#125;)…。</p>
<p><strong>（4）混合组合规则</strong></p>
<p>多项“且”和“或”规则时，比如限制身份证是“440300”开始，并且不含“440399”。或者身份证是“440100”开始，并且不含“440199”的规则。可以这样表达：(&#123;身份证&#125;[以…开始]&#123;440300&#125;)且(&#123;身份证&#125;[不含]&#123;440399&#125;)或(&#123;身份证&#125;[以…开始]&#123;440100&#125;)且(&#123;身份证&#125;[不含]&#123;440199&#125;)。</p>
<p><strong>从上面的讲解可以看出，随着组合规则的增加，设定和阅读规则变成一件极具难度的事情，对于使用者来说，有很高的学习成本。</strong></p>
<p>经过使用者测试发现，<strong>基本超过3项后都在“或”组合规则的时候，会对规则阅读和理解产生障碍</strong>，接下来问题就是考验实际UI界面展示的时候如何进行交互表达。</p>
<h3>3. 规则表达式方案</h3>
<p>在经过市面上5款类似产品设计后，提出了 A/B/C 3种设计方案。通过给定设定任务和阅读任务，对 3 位使用者进行易用性测试，大致的结论如下。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/U40O9vxA1DBWewrPaSXI.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="755" height="337" referrerpolicy="no-referrer"></p>
<p>方案A：直接条列式设定规则，对于不同的规则可以根据需要选择“且”和“或”组合方式。方案虽然满足可用性，<strong>但是并没有解决使用者在使用上设定和阅读的障碍</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/DHacaKJXHyfBKXRDKjQu.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="650" height="350" referrerpolicy="no-referrer"></p>
<p>方案B：在方案A的基础上，拆分为规则组，把规则拆分成更小的单元来看待。规则组很好解决了设定的问题，但是对于阅读来说，还是存在不小的问题。比如，<strong>在第一个规则组后再使用“且”进行组合，那就变成两个组其实是一个组，在阅读上并不直观</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/5Ck5pd04nJaoTdvnyNRP.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="701" height="313" referrerpolicy="no-referrer"></p>
<p>方案C：在前面总结的问题，最后决定采用规则组内只可使用“且”，规则组间只可使用“或”组合。对于专业人士来说，设置复杂的规则表达式会变得重复。<strong>但是对于普通人来说，却是更加直观和直觉</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/dpqwqqvJ0l6ycXMTEMfH.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="705" height="687" referrerpolicy="no-referrer"></p>
<p>所以，在规则表达式设定上，<strong>采用“方案C”</strong>。</p>
<h3>4. 规则表达式更新机制</h3>
<p>预约资料表单在实际使用过程中，会面对业务需要进行表单内容的调整。由于自动化事件是关联在表单之上，会受到表单内容的约束。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/nTlFeQkBSjiI8VA44bIe.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="700" height="175" referrerpolicy="no-referrer"></p>
<p>当修改预约资料表单的字段影响自动化设定规则时，系统需要进行检查并引导使用者进行操作。针对表单修改影响规则，可以在“?”预览，并可以快速一键排除。如果不确定，可以暂不处理。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B 端 SaaS 产品自动化事件设计 - 规则表达式" src="https://image.yunyingpai.com/wp/2022/03/jn0Drr1q4NJpq5PfsPMr.png" alt="B 端 SaaS 产品自动化事件设计 - 规则表达式" width="686" height="315" referrerpolicy="no-referrer"></p>
<p>又或者点击“马上更新”进入自动化设置页进行调整，对于影响的规则进行突出显示，原则上还是希望能最大程度简化使用者的操作难度，提高操作效率。</p>
<h2 id="toc-4">四、总结</h2>
<p>对于B端产品，特别是对于SaaS产品来说，接收到客户的需求，通常信息是比较片面的。客户只会告诉你需要什么，设计产品的能力不能只站在单个需求上来考虑问题，需要抽离出来看“某一类能力”或“某些业务场景”，结合业务价值一起进行判断。</p>
<p><strong>对于“自动化事件”的能力设计，可以应用的场景非常多。比如，数据变更、顾客下单、取消业务、定时任务等等，只要涉及一个标准的条件(触发项)，都可以通过逻辑表达式进行判别。</strong></p>
<p>而后续的行动，当然也不止本文提及的限制顾客进行下单预约。还可以根据实际业务提供行动，比如，发送短信、赠送优惠券、自动打标签等等。</p>
<p>这是一个SaaS产品能力原子化之后的结果，作为SaaS产品经理不只是要增加产品能力，拓展产品解决问题的深度。<strong>能力不是越多越好，是有限的能力可以产生更多元的业务组合</strong>，这需要思考怎么把产品能力可以抽象成更为基础的能力单元，便于组合能力单元不断发展，深化。</p>
<p>希望对你有所帮助。</p>
<p> </p>
<p>作者：龙国富，公众号：龙国富，分享用户研究、客户体验、服务科学等领域资讯，观点和个人见解。</p>
<p>本文由@龙国富 原创发布于人人都是产品经理，未经授权，禁止转载。</p>
<p>题图来Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5353172" data-author="100850" data-avatar="http://image.woshipm.com/wp-files/2021/05/WBiO9KeJKiEALvtJhClA.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            