
---
title: '华为鸿蒙OS发布会解析，这些干货你应该知道'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210603/v2_a8f9fda584ee463e991e3243e003f7e3_img_000'
author: 36kr
comments: false
date: Thu, 03 Jun 2021 00:23:08 GMT
thumbnail: 'https://img.36krcdn.com/20210603/v2_a8f9fda584ee463e991e3243e003f7e3_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/SVqSUMHtmp86hQw5HLuugw">“三易生活”（ID:IT-3eLife）</a>，作者：三易菌，36氪经授权发布。</p> 
<p>2021年6月2日晚间，<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>用一场规模盛大的发布会，正式推出了HarmonyOS 2，并且还带来了多款搭载这一系统的硬件产品。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_a8f9fda584ee463e991e3243e003f7e3_img_000" data-img-size-val="750,373" referrerpolicy="no-referrer"></p> 
<p>很显然对于许多朋友来说，这都是一场期待已久的活动。但一方面由于这场发布会是在晚间举行，加之持续时间较长，所以导致不一定所有人都有精力看到最后。但另一方面来说，纵观今天的整场发布会，大量时间被用于展示相对细致的使用场景，而非进行技术原理解释，所以也可能会使得不少对于HarmonyOS 2抱有期待的朋友，未能正确和深入地了解这套新系统的特性与意义。</p> 
<p>有鉴于此，我们三易生活试图从这场发布会中提取出一些大家可能会关心的信息，并从技术角度对其进行了一些解析。</p> 
<h2 label="一级标题" style>鸿蒙是“一个”系统吗？严格来说并不是</h2> 
<p>在今天发布会的一开始，华为方面就强调了鸿蒙OS的“万能性”。其可以运行在手机上，可以运行在电视上，可以运行在智能手表上，也能运行在各种智能家电设备上。</p> 
<p>那么一个问题就出现了，所有这些设备上的“鸿蒙OS”是同一个吗？</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_451e4bda0c8745d0acf9768b4ca2fd5b_img_000" data-img-size-val="750,350" referrerpolicy="no-referrer"></p> 
<p>实际上在今天的发布会上，有一张PPT已经回答了这个问题。在这里我们可以看到，在不同设备上运行的鸿蒙OS，实际上更类似于一个“模块化”的概念，比如智能手机里的鸿蒙OS，当然就需要具备能够兼容Android应用的底层相关模块，但IoT或智能手表上的鸿蒙OS，则未必包含这一模块。</p> 
<p>如此一来，我们可以说运行在不同形态产品中的鸿蒙OS，在部分模块的代码上可能确实是打通的，但与此同时，它们相互之间其实还会有着一定的差异，并不是说真的就把同一个系统塞进了各种各样不同的设备里。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_ed5508378e5049c897b5ff9c89ca5dd8_img_000" data-img-size-val="750,419" referrerpolicy="no-referrer"></p> 
<p>可能有的朋友会因此觉得，这好像没什么神奇的，隔壁<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>的Windows不也有针对IoT设备的Windows Core版本吗？</p> 
<p>的确如此，但与其他那些同样采用了模块化设计的操作系统相比，华为如今的HarmonyOS 2则明显在不同版本、不同设备间的互联互动上，下了更多的功夫。</p> 
<h2 label="一级标题" style>分布式功能确实强大，也能让智能设备更实用</h2> 
<p>早在初版鸿蒙OS诞生时，“分布式计算”就被界定为最重要的特性之一。那么在实际的消费电子产品上，这种“分布式计算”到底是如何体现的呢？</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_ace3a8682d134cef8cf31dd4df3af9d5_img_000" data-img-size-val="750,408" referrerpolicy="no-referrer"></p> 
<p>首先，通过鸿蒙OS的模块化架构，不同形态的设备之间可以实现一些特定功能的打通。例如今天刚刚发布、搭载HarmonyOS 2的Watch 3系列智能手表，就可以访问华为智能手机的摄像头，在手表的屏幕上控制手机拍照。不仅如此，华为智能电视、智能手机、平板，甚至是一些合作伙伴的无人机摄像头也可以像这样相互“借用”，甚至还能够实现多个不同设备从不同角度同步拍摄。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_a915e517d3854dfda090a9fdbc6436af_img_000" data-img-size-val="750,429" referrerpolicy="no-referrer"></p> 
<p>又比如说，通过在Windows PC上安装鸿蒙OS的互联插件，也可以让它们拥有与刚刚发布、搭载HarmonyOS 2的MatePad Pro平板电脑分享屏幕显示内容的功能。这样一来，就可以将平板电脑变成PC的无线扩展显示器，甚至是作为绘图板来使用。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_02d7d26200354f00a93e4bdfb7e3e784_img_000" data-img-size-val="750,422" referrerpolicy="no-referrer"></p> 
<p>其次，鸿蒙OS相比华为此前的EMUI大幅强化了对于智能设备的控制体验。其中特别是手机版的HarmonyOS 2，现在也拥有了业界流行的IoT设备控制中心，用户不再需要进入特定的智能家居APP，直接在手机状态栏下拉界面就可以执行一些智能设备的简单开关控制。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_3f2d0faec7114622a7e94ad8d99b8ff1_img_000" data-img-size-val="750,372" referrerpolicy="no-referrer"></p> 
<p>不仅如此，得益于鸿蒙OS的模块化设计，如果智能设备本身也搭载的是鸿蒙OS，那么它将不只是能够通过智能手机进行快速连接和操控，还可以实现比传统AIoT设备更多的设备间信息共享。例如豆浆机可以读取手机中用户的身体健康数据，从而更精准地推荐相应菜单，而这种AIoT设备与手机间更为深度的<a class="project-link" data-id="634111" data-name="互联互通" data-logo="https://img.36krcdn.com/20201107/v2_adb614ed5631408680264dce0823fad5_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/634111" target="_blank">互联互通</a>以往则是不存在的。</p> 
<h2 label="一级标题" style>鸿蒙如何做好适配？“卡片”和原子服务是关键</h2> 
<p>早在鸿蒙OS登录消费设备前，相信它的应用兼容性就已经是许多朋友所关注的事情。而从今天发布会上官方对于鸿蒙“模块化”架构的解释我们不难发现，虽然根据目前的种种信息显示，手机版HarmonyOS 2保留了对Android 10的兼容性，但我们显然不可能说，让搭载鸿蒙OS的热水器、豆浆机、空调等产品也去兼容Android 10，并安装Android应用来实现功能扩展和互联特性。</p> 
<p>那么华为是如何解决鸿蒙OS的软件适配问题，在诸如智能手表、智能电视等硬件性能并不强的设备上，去确保鸿蒙生态的可扩展性呢？答案其实就在全新的应用卡片式界面和“原子服务”体系中。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_827086fc266e473498f4da730572defd_img_000" data-img-size-val="750,421" referrerpolicy="no-referrer"></p> 
<p>实际上华为方面在今天的发布会中，对这一关键部分并没有做太多的阐述，但是官方曾提及，Android开发者可以直接在原有应用的基础上上叠加一个华为原子服务和卡片界面，从而使得应用可以在HarmonyOS 2手机上开启一个特定的，包含应用一部分关键功能的“卡片”，而“卡片”本身则会成为鸿蒙OS扩展功能、打通服务体验的关键所在。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_2b3182afe3a04d3eb384117b62516cf6_img_000" data-img-size-val="750,420" referrerpolicy="no-referrer"></p> 
<p>从以上这段描述中，其实就已经不难理解“卡片”的本质了，它应该非常类似于现在很多机型都支持的“快应用”。只不过在其他手机上，快应用更类似于网页应用，而在鸿蒙OS里，则将这种“迷你应用”与传统Android应用进行了开发上的打包，同时为其分配了更加现代化的界面和更多的功能。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_09e4282fe6484e9f9b2891d0945ee7d2_img_000" data-img-size-val="750,421" referrerpolicy="no-referrer"></p> 
<p>打个简单的比方，就是当你在一部使用鸿蒙OS的手机上安装了一个为其做过适配的Android应用时，就会同时在手机中安装一个对应的“卡片应用”。这个卡片应用可以用来增强原应用的体验，提供快速访问核心功能的入口，但与此同时，“卡片应用”本身又构成了当前鸿蒙OS的一个独立软件生态，可以实现对智能电视、智能手表、平板电脑等更多鸿蒙设备的兼容，甚至也衍生出了如“应用流转（将正在使用的卡片应用分享给另外一台设备，该设备<a class="project-link" data-id="624283" data-name="即刻" data-logo="https://img.36krcdn.com/20200917/v2_9f5a419745ea412581759f54eda1b309_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/624283" target="_blank">即刻</a>打开对应的卡片应用，而无需下载完整版的应用）”这种颇具创意，使用起来也会很流畅的有趣功能。</p> 
<h2 label="一级标题" style>鸿蒙迈出了关键一步，而它的影响才刚刚开始</h2> 
<p>在华为今天的这场发布会上，主题事实上还是为了推出新的硬件产品，并向消费者宣传HarmonyOS 2体验的独特性。因此很多技术上的细节和具体的实现方式并没有进行详细描述，我们三易生活也只能逐字逐句地从现有演示文档与演讲中寻找线索，为大家撰写这篇并不能说是绝对准确的分析内容。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_fbd08a50e29d4345934e760d1341dc70_img_000" data-img-size-val="750,422" referrerpolicy="no-referrer"></p> 
<p>从我们目前所了解到，华为已经展现出来关于鸿蒙OS的种种信息来看。首先，HarmonyOS 2确实是华为自研、不同于Android、iOS，或者Windows的一个操作系统体系，尽管其手机与平板电脑版本不可避免地会含有Android的开源代码，但实际上“卡片应用”和“原子服务”本身，就已经可以看作是鸿蒙OS独特的、不同于其他操作系统的自有软件生态了。而拥有一个与其他操作系统不兼容的独立软件生态，也已经可以证明鸿蒙OS的独立性。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_39ace71d90b54e768f8da85085b302fc_img_000" data-img-size-val="750,390" referrerpolicy="no-referrer"></p> 
<p>其次我们也要看到，华为方面虽然目前正在大力发展鸿蒙生态，但令人欣慰的是他们并没有以牺牲消费者和开发者的体验为代价，所以鸿蒙手机还是得兼容Android，鸿蒙电视也依旧可以安装Android的各种应用。与此同时，得益于目前鸿蒙OS所采用“在Android应用基础上叠加卡片应用”的开发方式，也不会给开发者带来太多的麻烦。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_2d367a1fc6b646b8856701ac99d2ae60_img_000" data-img-size-val="750,422" referrerpolicy="no-referrer"></p> 
<p>不过客观的来说，HarmonyOS 2今天所展示出的很多能力，虽然在底层上可能很高深、很强大，实现的原理也有一定的独创性，但从表面上对其进行模仿，却未必是难以做到的事情。比如功能更多的AIoT控制卡片，比如平板电脑与PC之间的投屏能力，比如应用在不同设备间的分享，这些功能其他品牌用“笨”一点的办法也可以实现，甚至有些是此前就已经做到。这就意味着，虽然从技术的角度来说，我们可以称赞现在的鸿蒙OS已经很强大、很独特，但站在消费者的角度来看，鸿蒙OS当前展现出的功能，可能很快就会被其他厂商“致敬”。</p> 
<p><img src="https://img.36krcdn.com/20210603/v2_a25f1088602d4450a007a89b3ad060e9_img_000" data-img-size-val="750,421" referrerpolicy="no-referrer"></p> 
<p>而要想真<a class="project-link" data-id="214173" data-name="正解" data-logo="https://img.36krcdn.com/20201106/v2_67a7b1b51d1b4a2290589f4ec3cf5c40_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/214173" target="_blank">正解</a>决这个问题，一是需要鸿蒙OS开发出更多、更深层次的分布式计算特性，真正实现难以被模仿的功能体验（例如直接将手机的算力分给家中的电视，让电视的AI画质运算能力更强）。其二则是需要依靠华为来推出更多本身性能足够强、规格足够高，能够让消费者只看产品力就大为叫好的硬件设备才行。</p>  
</div>
            