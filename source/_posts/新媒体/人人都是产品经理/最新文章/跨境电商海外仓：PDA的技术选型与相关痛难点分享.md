
---
title: '跨境电商海外仓：PDA的技术选型与相关痛难点分享'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/LLCQn88W9wjnRQdQbiPW.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 29 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/LLCQn88W9wjnRQdQbiPW.jpg'
---

<div>   
<blockquote><p>什么是PDA？一般可以将PDA理解为掌上电脑，这一操作系统的存在可以帮助我们完成移动状态下的作业。那么，你知道PDA产品设计应该如何进行吗？有哪些难点是需要注意的呢？本文作者结合个人经验进行了总结，一起来看看吧。</p>
</blockquote><p><img data-action="zoom" class="size-full wp-image-5581601 aligncenter" src="https://image.woshipm.com/wp-files/2022/08/LLCQn88W9wjnRQdQbiPW.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>之前写了很多关于WMS相关的产品文章，市面上也有很多相似的WMS的文章，对于一个WMS的新手产品来说，这些内容已经足够学习和消化了。</p>
<p>但是在我实际的过往工作中，我发现市面上关于PDA介绍的文章很少，而且相关的竞品和一些参考资料也比较少。当初我在WS做第一版安卓的PDA的时候，由于没有专业的安卓开发和UI设计，我还学了很多安卓的知识和UI切图方面的东西，现在想来，也是积累的一笔财富。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/TpKHgHPwNC90U3o2DU4L.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">像素相关的知识笔记</p>
<p>既然市面上少有人写，我刚好又做过一些这方面的内容，那就自己动手吧。</p>
<h2 id="toc-1">一、关于PDA的定义</h2>
<p>现在聊到仓库端的PDA，很多人第一印象就是一个安卓APP安装在了一个特殊的设备（手持终端）中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/KoiYoMyI3W88STChhkv9.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图源：东大集成官网</p>
<p>所以会想当然的认为PDA间接性就等于安卓APP，这个理解<strong>在大多数场景下是可以算对的，但是肯定是不严谨的。</strong></p>
<p>因为除了安卓系统之外，WinCE和iOS都算是一种移动端的操作系统。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/iBmU7jRmuRM9gpAQYrh3.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图源：京东</p>
<p>所以，关于PDA的定义更严谨一些的说法应是：</p>
<blockquote><p>PDA（Personal Digital Assistant），又称为掌上电脑，可以帮助我们完成在移动中工作，学习，娱乐等。按使用来分类，分为消费级PDA和工业级PDA。消费级PDA包括的比较多，智能手机、平板电脑、手持的游戏机等都属于消费级PDA；工业级PDA主要应用在工业领域，常见的条码扫描器、RFID读写器、POS机等都可以称作工业级PDA。</p></blockquote>
<p>官方定义太难理解，可以简单化地定义为：<strong>带有操作系统的智能化的手持终端都可以称之为PDA。</strong></p>
<h2 id="toc-2">二、PDA的操作系统</h2>
<p>早期的时候，WinCE应该是工业级PDA的主流操作系统，在之前公司我们就用了好几年的WinCE。画风比较简陋，交互动作也比较落后，而且屏幕还是电阻屏，尺寸也很小，能展示的内容都比较少。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/FVF1nztnrk4NLArqzVb6.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p>后来，随着安卓系统的普及和厂家的推广，越来越多的公司开始选择使用安卓版的PDA，所以相应的一些产品设计也会遵循安卓的风格。安卓系统有更佳的交互体验，维护成本低，电容屏，更大的屏幕，总体来说优势非常明显。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/ZbNMz580oTNbYMZr4Vut.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p>除了WinCE和安卓之外，还有少量的公司也会采用iOS系统的PDA，基本上就是内置一个iPhone或者iTouch等，例如Apple Store的员工们用的就是iOS的PDA，这一块市面上的资料比较少，这里就暂时不多介绍了。</p>
<h2 id="toc-3">三、安卓PDA的技术选型</h2>
<p>当确定了要使用安卓操作系统的PDA之后，团队接下来马上就会面临一个小难题，那就是：<strong>技术选型选哪个？</strong></p>
<p>对于一个安卓APP来说，目前主流的开发方式有三类，分别是：</p>
<ol>
<li>原生APP（Native）</li>
<li>Web APP（HTML5）</li>
<li>混合APP（Hybrid，即“Native+H5”）</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/3JIjvba5lUdlzNotNdqW.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图源网络</p>
<p>关于这三类开发方式的原理和优劣势，我只能算半吊子水，就不做过多的讲解了。我重点从用户的使用场景和研发的一些考虑点来分析一下，我们当时做技术选型的时候，是怎么考虑的，也和有相似经历的朋友们交流学习一下。</p>
<h3>1. 服务端和客户端的版本对应</h3>
<p>PDA本质上是一个客户端，需要和服务端进行数据交互和通信。如果是海外仓，因为服务端可能部署在不同的国家或地区，这样会导致服务端的版本可能会有差异，从而也导致了客户端的版本有差异。</p>
<p>例如，今天WMS（服务端）发布了一个V1.2版本，发布到美国的服务器上，刚好这个版本有对应的PDA功能改版更新，那么就会要求美国的仓库将PDA升级到最新版，与V1.2版本进行适配；而欧洲因为一些业务的原因，并没有直接升级发布，所以它们还是用的V1.1版本，那么PDA自然就不能升级为最新的了。</p>
<p>在设计PDA的版本更新检测的时候，需要考虑这种版本对应的需求，避免出现阻塞生产的现象。</p>
<h3>2. PDA演示的频率如何？</h3>
<p>之前在WS的时候，我们是给自己的仓库做PDA软件，所以不太需要考虑演示的问题，因为演示的频率很低。</p>
<p>但是到了LX的时候，我们是做SaaS WMS，需要和很多客户演示交流系统怎么使用，这里就包含了PDA的使用。</p>
<p>这个时候如果可以直接用网页打开PDA的功能界面（H5 APP），在演示的时候是会比较流畅的，而且将测试账号发给客户之后，客户也可以直接用网页体验PDA的功能，而不用自己再找一个安卓PDA或者安卓手机去安装一个APP，对客户试用来说是比较方便的。</p>
<p>但是这样做的成本也比较高，需要研发一套H5的APP，后面又要研发一套原生的APP。</p>
<p><strong>所以我的建议是，大家结合自己的演示频率以及客户的接受方式来综合考量</strong>。如果有研发资源，那么就做两套，一个演示，一个真实使用；如果没有太多资源，那就直接研发原生的APP，到时候演示用虚拟机，客户体验也用虚拟机或者找个安卓设备安装APP。</p>
<h3>3. 版本升级是否频繁？</h3>
<p>PDA的版本升级和多版本的兼容性也是一个不容小觑的问题，最好是尽早完成在线更新的功能，支持用户手动更新版本和系统强制升级版本的功能。</p>
<p>之前在WS的时候，由于技术架构设计的问题，迟迟没有做PDA的在线升级，每次都要让仓库的人员手动去下载安装包，然后覆盖安装等，很容易出现操作遗漏或者更新失败的问题，而且仓库在海外，远程运维和指导的成本非常高。</p>
<p>所以，在技术选型的时候，也要考虑这个APP的更新频率和版本兼容的问题，什么版本是必须要强制升级的？什么版本是可以稍后升级的？然后在什么环节检测升级等都需要考虑清楚。<strong>一切以节省仓库作业时间和成本为导向。</strong></p>
<h3>4. 仓库的硬件是否统一？可控？</h3>
<p>如果是自家的仓库，那么一般来说PDA设备都是统一采购的，型号基本上是固定的几款，APP的兼容性也比较好做，开发就不需要在安卓版本和硬件兼容性上花太多的时间。</p>
<p>但是如果是做SaaS WMS，而且还让客户自行采购安卓PDA设备的话，一般很容易踩了兼容性的坑，因为市面上稀奇古怪的设备太多了。</p>
<p>建议提前和客户沟通，告知硬件的基础要求，例如安卓9.0以上，屏幕4.0以上，4核以上，4G内存以上等。</p>
<p>最后，我做了一个表来简单总结一下，安卓PDA的几种开发方式的优劣势，至于怎么选？请大家自行判断。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/iVM9z8xUivmj9F4u8IrB.jpeg" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">仅供参考</p>
<h2 id="toc-4">四、PDA产品设计中的难点与踩坑点</h2>
<p>对于B端产品经理来说，做习惯了Web端的产品设计，突然去接手APP的设计，还是有一定难度的。一方面是不熟悉APP的一些规范，另一方面是PDA可参考的资料不是很多。</p>
<p>我总结了几个当时出设计方案的时候感觉比较难或者踩了坑的点，分享给大家。</p>
<h3>1. 竞品难找</h3>
<p>当时因为没有做过APP设计，同时也没有UI，导致设计出来的界面惨不忍睹，于是我找了很多竞品和相关的资料，最后发现“竞品的PDA也做得很丑”……</p>
<p>于是只能自己硬着头皮学了一些基础的概念和知识，例如设计稿用375还是用750，状态栏应该用多少像素？导航栏应该用多少像素？设计稿的字体对应的设备的字体是多少？</p>
<p>最后实在没有办法，就只能对着友商的APP截图，一个一个标注，然后进行学习了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/6tUYOXuteUZ42MlAhA0n.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">万里牛的PDA</p>
<p>这个时候可能会朋友跳出来说，哎呀，你是产品经理，你应该专注在业务和更有价值的方面，你学那么多UI的东西干嘛？</p>
<p>我只能说：<strong>有这个观点的朋友都是“没吃过苦的”，也是没有在小公司待过的</strong>。他的内心已经默认了所有的资源都是配套的，产品经理只要拧自己的螺丝就够了……</p>
<h3>2. 布局与组件的纠结</h3>
<p>再回到上面的话题，当我学习了一些基础规范之后，我发现大体上的布局已经没啥问题了，主要就是一些组件和样式方面还是有疑问。</p>
<p>例如，输入框/扫描框到底是固定放在底部，还是跟普通的输入组件一样放在字段的后面？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/ZIGfTO9iamn4SXH55dsq.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">三种不同的组件</p>
<p>例如，提交/确定按钮是放在右上角，还是底部固定？有一些文案类的组件是上下放还是左右放？列表页展示是用卡片还是分隔线，一屏要展示多少？</p>
<p>总之，以上的种种难题，其实都是因为产品技能不对口导致的，说白了就是资源不够，只能让一个“小朋友去扛大梁”了，于是就边学边做，也自然而然就踩坑了。</p>
<p>如果放到现在来做这件事，我可能会转头就去淘宝找个UI帮忙来搞，哪怕自己出点钱，也没必要在这个地方花费太多的时间精力，因为一整套流程下来，要学的东西太多了，最终的效果也不一定很好。</p>
<p>当然，如果是作为初学者，那么我感觉这一段的经历，还是很有价值的，因为帮助自己查缺补漏了，意识到了很多专业知识的不足。</p>
<h3>3. 光标/激活框处理</h3>
<p>抛开上面的UI问题，光标/激活框是PDA设计中要注意的点，也是体验上最容易感知到的点。</p>
<p>简单来说，大多数工人在使用PDA的时候，进入了某个页面之后，会直接扫描条码，而不会关注到光标是否在输入框，已经是激活状态。如果这一块没有做特殊处理，就会发现无论怎么扫描，都不能将内容录入到输入框中。</p>
<p>一般有两种实现方式，第一种最简单的就是默认进入某个页面之后，将光标聚焦在输入框中，呈激活状态，同时默认隐藏键盘的弹出，这样就可以直接启用PDA的扫描头，扫描后的内容直接获取在输入框中。</p>
<p>另一种方式是利用安卓底层的广播功能，对PDA的扫描头做监听，当进入到了某个页面之后，监听到了PDA扫描的内容之后，自动将扫描的值赋给默认的输入框（一般是第一个），然后进行数据请求。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/gxhHvdsLEockdGt022mf.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">吉客云的PDA默认是激活状态</p>
<h3>4. 国际化翻译难题</h3>
<p>由于参考的很多竞品都是国内的，所以在布局方面一般来说相对比较成熟，但是如果是海外仓，有多语言的场景下，那么国内的很多设计可能就会出问题，最简单的问题就是文本超长，所以导致内容放不下了。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/mnCjtyUZ4fqt481Q1B7i.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" width="773" height="614" referrerpolicy="no-referrer"></p>
<p>一方面是要在文案上进行优化和精简，另一方是在布局上，要尽量多采用“上下布局”而不是“左右布局”，这样才能尽可能地避免出现文案挤压、展示不下的问题。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓：PDA的技术选型与相关痛难点分享" src="https://image.woshipm.com/wp-files/2022/08/xOFaR3DY553H4wnOXUxw.png" alt="跨境电商海外仓：PDA的技术选型与相关痛难点分享" width="766" height="741" referrerpolicy="no-referrer"></p>
<p>除了布局之外，国际化翻译还需要特别注意一些专有名词的一致性，尤其是大量采用机翻的时候，例如上架有些时候翻译为Putaway，有些时候又翻译为Shelves。</p>
<h2 id="toc-5">五、总结</h2>
<p>无论是国内仓的WMS还是海外仓的WMS，目前PDA都可以算得上的标配，而且PDA设计的好与坏与仓库作业有非常大的直接关系，但是我发现大家交流最多的还是WMS相关的内容。</p>
<p>本人才疏学浅，希望借此篇文章，可以抛砖引玉，与各位大佬们多交流交流PDA这一块的内容。</p>
<div class="article--copyright"><p><b>专栏作家</b></p>
<p>我叫维他命（Vitamin），微信公众号：PM维他命。前PHPer，做过在线教育类产品，也做过4年多的跨境仓储物流方向的产品，目前是一位外贸SaaS领域的供应链产品经理。主要专注于WMS/OMS/TMS/BMS/ERP等领域，分享供应链相关的产品知识。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5581412" data-author="227259" data-avatar="https://image.woshipm.com/wp-files/2021/07/Ubf7DEfcVQI43v46YkSc.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            