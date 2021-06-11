
---
title: '谷歌在自然语言的最新技术成果LaMDA，在I_O大会化身冥王星'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210611/v2_7ced20d84ec64e648c7f542ff907e820_img_000'
author: 36kr
comments: false
date: Fri, 11 Jun 2021 03:02:53 GMT
thumbnail: 'https://img.36krcdn.com/20210611/v2_7ced20d84ec64e648c7f542ff907e820_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/kCKi4wzUM7JA7pg4Gmyx2g">“将门创投”（ID:thejiangmen）</a>，作者：让创新获得认可，36氪经授权发布。</p> 
<p>LaMDA的全称是Language Model for Dialogue Applications，简单而言，它是一种能力更强的语言模型，适用于对话应用程序。与前辈BERT、GPT-3一样，LaMDA也基于Transformer架构。但面对语言的丰富性、灵活性以及随之伴生的复杂性， LaMDA的能力还称不上成熟。在现实运行中，它仍可能出错，给出荒谬的回应。</p> 
<p>本文以作者James <a class="project-link" data-id="343984" data-name="Vince" data-logo="https://img.36krcdn.com/20200917/v2_3572aee30c1d4e5ebd46db5a40ec28b7_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/343984" target="_blank">vince</a>nt的第一视角对<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>最新黑科技LaMDA的能力、风险和优化空间提出了思考。</p> 
<p>在上周的Google I/O 2021发布会上，谷歌表示未来的搜索“对话”将取代“文本”。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,720" src="https://img.36krcdn.com/20210611/v2_7ced20d84ec64e648c7f542ff907e820_img_000" referrerpolicy="no-referrer"></p> 
<p>谷歌展示了两个“开创性的”人工智能系统——LaMDA和MUM，希望有一天它们能集成到所有的产品中。</p> 
<p>LaMDA也是Google在自然语言方面的最新技术成果，这是一个用于对话应用的语言模型，现在仍在研究和开发中，但很快就可以供第三方测试。</p> 
<p>为了显示它的潜力，谷歌在Google I/O大会上把LaMDA语言模型拟物化为冥王星，用户与这颗星球说话，系统就会做出反应。Google还将LaMDA展示为<a class="project-link" data-id="477187" data-name="纸飞机" data-logo="https://img.36krcdn.com/20200729/v2_ff0884df80c04fd2970d6c6de2df3d2a_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/477187" target="_blank">纸飞机</a>的形象，让用户与纸飞机进行对话。</p> 
<p class="image-wrapper"><img data-img-size-val="700,394" src="https://img.36krcdn.com/20210611/v2_e42d23bd14cc409fa79f633905877464_img_000" referrerpolicy="no-referrer"></p> 
<p>变身为冥王星形象时，LaMDA回答了“新地平线”探测器关于这个天体的环境和它的飞越问题。</p> 
<p class="image-wrapper"><img data-img-size-val="700,394" src="https://img.36krcdn.com/20210611/v2_7c8659f5928843228922f2ee2a1bf249_img_000" referrerpolicy="no-referrer"></p> 
<h2>谷歌的梦想是在谈话中完成搜索</h2> 
<p>随着这项技术的应用，用户将能够“与谷歌对话”，使用自然语言从网络上检索信息或查<a class="project-link" data-id="511479" data-name="找他" data-logo="https://img.36krcdn.com/20201106/v2_b31d77ce4d2c43f2b8517deb87d89a64_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/511479" target="_blank">找他</a>们的个人信息档案、日程安排、照片等。</p> 
<p>这不仅仅是谷歌的营销。苹果多年来也一直在考虑核心产品的重大转变。谷歌四名工程师最近发表的一篇题为<strong>《Rethinking Search》</strong>的研究论文提出了如下问题和假设：</p> 
<p><strong>是时候用人工智能语言模型代替“经典”搜索引擎了吗?</strong></p> 
<p>人工智能语言模型可以直接提供这些答案。</p> 
<p>在这里，我有两个问题要问。</p> 
<p>首先是<strong>它能做到吗？</strong>经过多年缓慢但明确的进步，计算机真的准备好理解人类语言的所有细微差别了吗？</p> 
<p>其次，<strong>应该这样做吗？</strong>如果把传统搜索抛在脑后，谷歌会发生什么？</p> 
<p>这两个问题都还没有答案。</p> 
<p>毫无疑问，谷歌很长一段时间以来一直在推动语音驱动搜索。2011年谷歌推出语音搜索，2012年谷歌将它升级为谷歌Now，2016年推出Assistant，在无数I/Os中，突出了语音驱动的环境计算（ambient computing）。</p> 
<p>谷歌语音驱动的演示则通常是由谷歌的另一产品<strong>Google Home</strong>呈现的。</p> 
<p>Google Home是一款可以对话的小型扬声器，它将公司的搜索引擎和人工智能融入人们日常生活的方方面面，最重要的是，Home代表了谷歌对竞争对手亚马逊Alexa语音助手的回应。</p> 
<p>尽管有明显的进步，但我认为这项技术的实际效用远不及演示。例如，看看2016年Google Home的介绍，谷歌承诺，这款设备很快将连接用户生活的方方面面，比如订车、订晚餐、送花给妈妈等等。<strong>其中一些东西现在技术上是可行的，但我不认为它们是普遍的，语言并没有被证明是我们与梦想生活灵活和完美的接口。</strong></p> 
<p>看了今年的I/Os演示，我想起了围绕自动驾驶汽车的炒作，这项技术迄今未能兑现其承诺。</p> 
<p>还记得埃隆·马斯克承诺的自动驾驶汽车将在2018年进行一次越野旅行吗？</p> 
<p>它还没有发生！</p> 
<p class="image-wrapper"><img data-img-size-val="1080,720" src="https://img.36krcdn.com/20210611/v2_36f1ecc4d98f4348af4c9704fe46133c_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>自动驾驶和语音技术之间有着惊人的相似之处。</strong></p> 
<p>近年来，由于新的机器学习技术的到来，加上丰富的数据和廉价的计算，这两个领域都取得了重大进步。但两者都在与现实世界的复杂性作斗争。</p> 
<p>语音技术可以处理简单、直接的命令，只需要识别少量的动词和名词，比如“播放音乐”、“查看天气”等，以及一些基本的后续操作，但如果把这些系统扔进对话的深水区，它们就会陷入困境。</p> 
<p>正如谷歌首席执行官桑达尔·皮查伊上周在I/O大会上所说:“语言的复杂性是无止境的。通过语言我们讲故事、讲笑话和分享想法。<strong>语言的丰富性和灵活性使它成为人类最伟大的工具之一，也是计算机科学最大的挑战之一。”</strong></p> 
<p>在线搜索功能与过去只搜索一个单词相比已经有了长足的进步。能够输入整个短语要归功于BERT（Transformers的双向编码器表示形式）的上下文搜索。<strong>Transformer现在支撑着世界上最强大的自然语言处理系统，包括OpenAI的GPT-3。</strong></p> 
<p>而LaMDA，这个用于对话应用程序的语言模型以其对话式的语言风格将搜索的进程又搬上了一级台阶。</p> 
<p>在谷歌I/O大会中，一位用户问冥王星状态下的LaMDA “有人来看过你吗?”。冥王星答道:“是的，有一些，其中印象最深刻的是’新地平线’探测器，这艘飞船访问了我。”</p> 
<p><strong>MUM则是一种多模态模型，不仅能理解文本，还能理解图像和视频，它的演示也同样关注对话领域。</strong></p> 
<p>当模型被问到:“我已经攀登过亚当斯山，现在想明年秋天攀登富士山，我应该做些什么不同的准备?”</p> 
<p>MUM足够聪明地理解到提问者不仅要比较山脉，而且“准备”意味着找到适合天气的装备和相关的地形训练。如果这种细微之处可以转化为商业产品，那么这将是语音计算真正向前迈出的一步。当然，这个“如果”显然是一个巨大的、摩天大楼大小的“如果”！</p> 
<p>那么，应该这样做吗？</p> 
<p>这就引出了下一个大问题：如果谷歌可以把讲话变成对话，它应该吗？</p> 
<p>我不确定这个问题有一个明确的答案，但不难看到，如果谷歌沿着这条路走下去，将会出现大问题。</p> 
<p>首先是技术问题。最大的问题是，谷歌或任何公司无法可靠地验证该公司目前演示的语言模型所产生的答案。<strong>没有办法确切地知道这些模型学到了什么，或者它们提供的答案的来源是什么。他们的训练数据通常来源于互联网，这既包括可靠数据，也包括垃圾信息。</strong></p> 
<p>语言模型给出的任何回复都可以从网上找到来源，这也会导致他们产生的训练数据中存在性别歧视、种族歧视和偏见观念等，这也是近年来被反复提及的问题。然而，谷歌本身似乎也不愿正视这些批评。</p> 
<p>凯文·拉克尔是前谷歌搜索质量工程师，在一篇博客中他就列举了GPT-3中的许多常识错误，比如：</p> 
<p>Q：哪个更重，一个烤面包机还是一支铅笔？</p> 
<p>GPT-3说:“一支铅笔。”</p> 
<p>Q：我的脚有几只眼睛?</p> 
<p>GPT-3答:“你的脚有两只眼睛。”</p> 
<h2>人工智能语言模型“对世界还缺乏真正的理解”</h2> 
<p>引用谷歌的工程师们在《Rethinking Search》中的一句话，这些系统“对世界没有真正的理解，它们容易产生幻觉，更重要的是，它们无法通过引用他们接受过训练的语料库中的支持文件来证明自己的言论是正确的。”</p> 
<p>2017年的一个著名事件是一位用户发现了谷歌特别惊人的错误，这一发现直接登顶成为了头条新闻。2017年当谷歌被问及“奥巴马正在计划戒严令吗?”<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>的答案居然引用自一个阴谋论新闻网站“是，是的，他当然是！”</p> 
<p class="image-wrapper"><img data-img-size-val="1080,399" src="https://img.36krcdn.com/20210611/v2_c395c65015f2420288a1644d1167e3f5_img_000" referrerpolicy="no-referrer"></p> 
<p>在今年的LaMDA和MUM的I/O演示中，谷歌似乎仍然倾向于这种“唯一真实答案”的格式——用户提问，机器回答。在MUM的演示中，谷歌指出，用户得到的回答也将“得到深入讨论”，但很明显，谷歌梦想的交互是与谷歌问答本身的直接交互。</p> 
<p>由此我认为，对于复杂的问题，比如那些谷歌在I/O上用MUM演示的问题，它们达不到要求。像计划假期、研究医疗问题、购买大件物品、寻求DIY建议、或钻研自己喜欢的爱好等，<strong>都需要个人判断，而不是电脑总结。</strong></p> 
<h2>谷歌想要给出的“唯一真实答案”的愿望最终可能会伤害它</h2> 
<p>那么问题来了，谷歌能否抵挡住提供一个“唯一真实答案”（one true answer）的诱惑？科技观察人士注意到，随着时间的推移，谷歌的搜索产品越来越以谷歌为中心。</p> 
<p>该公司越来越多地将搜索结果隐藏在外部(指向第三方公司)和内部(引导用户使用谷歌服务)的广告之下。我认为“Talk to 谷歌”模式符合这一趋势。潜在的动机是一样的，移除中介，直接为用户提供答案，大概也是因为谷歌认为自己最适合这样做。</p> 
<p>在某种程度上，这是谷歌的企业使命“组织全球信息，使其人人都能访问和使用”。</p> 
<p>谷歌是索引，而不是百科全书，它不应该以牺牲搜索结果为代价。</p> 
<p>From: The Verge; 编译：Shelly</p> 
<p>Illustrastion by Ivan Haidutsk from Icons8</p> 
<p>- The End</p>  
</div>
            