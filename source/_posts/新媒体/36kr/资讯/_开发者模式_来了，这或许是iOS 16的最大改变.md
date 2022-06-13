
---
title: '_开发者模式_来了，这或许是iOS 16的最大改变'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220611/v2_66876f517e2442b089a596f6191cad41_img_000'
author: 36kr
comments: false
date: Mon, 13 Jun 2022 00:31:03 GMT
thumbnail: 'https://img.36krcdn.com/20220611/v2_66876f517e2442b089a596f6191cad41_img_000'
---

<div>   
<p>在日前刚刚拉开帷幕的WWDC22中，苹果带来了大幅更新的iOS 16、更加关注健康监测的watchOS 9、更像PC操作系统的iPadOS 16，以及基于M2芯片的两款新MacBook产品。此外，苹果方面还悄然在开发者网站上更新了这样一则名为“Enabling Developer Mode on a device（在设备上启用开发者模式）”的内容。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_66876f517e2442b089a596f6191cad41_img_000" referrerpolicy="no-referrer"></p> 
<p>在这篇面向开发者的内容中，苹果方面介绍到，iOS 16与watchOS 9中引入的开发者模式可以防止用户无意中在设备上安装潜在的有害软件，并减少开发者专用功能暴露的攻击媒介。并且开启开发者模式不会影响从App Store下载应用、或是使用TestFlight，而是侧重于在Xcode中执行构建、运行，或通过Apple Configurator来安装ipa文件。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_29ae5a94c41e42bfa17ffde060e7ff9f_img_000" referrerpolicy="no-referrer"></p> 
<p>根据苹果方面的说法，启动开发者模式需要在设备上的“设置 > 隐私与安全性”下，找到开发者模式开关，点击后系统会显示警告，提示用户打开开发者模式后会降低设备的安全性。要继续启用开发者模式则需要点击警告的重新启动按钮。在设备重启、并解锁后还会显示一条警报，需要再次确认是否启用开发者模式，然后才是点击打开，并在出现提示时输入设备密码。 </p> 
<p>苹果之所以会将开发者模式的开启设置得如此复杂，无疑就是为了避免普通用户不小心打开这个功能，进而导致后续一系列的麻烦。没错，苹果方面在这一内容的开头就已明确要求，使用开发者模式的人需要确认是开发者、并知晓相关风险。但实际上，这个功能与苹果此前推出的开发者模式是完全不同的，iOS 16上的开发者模式其实更类似于Android上同一名称的功能。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_60367acd32454548890cea69a6a2186b_img_000" referrerpolicy="no-referrer"></p> 
<p>在WWDC22之前，iOS中其实是存在开发者模式的，要不为苹果开发APP的开发者要如何进行测试呢。但其需要通过数据线将iPhone连接到Mac上，还要用到专门的集成开发工具Xcode，然后再找到“Window”里的“Devices and Simulators”并点击，在弹出的页面里选择相应的iPhone，此后才能在iPhone上看到开发者模块的选项。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_d733fea44f8247bd9d4108964310a651_img_000" referrerpolicy="no-referrer"></p> 
<p>显而易见，在iOS 16之前的开发者模式需要借助Mac与专业工具，才是真正面向开发者的“开发者模式”，而现在则仅需在手机上就能开启“开发者模式”。要知道在过去的十余年间，苹果一直都没有向普通用户开放过类似的功能，甚至可以说普通用户不能完全掌握自己的手机，才是iPhone与Android机型最大的区别所在。 </p> 
<p>在Android和iOS的市场竞争中，Android打出的是自由开放的旗帜，用户在购买Android手机后可以通过谷歌主动开放的ROOT功能、进而掌控手机的全部权限。而iOS则恰恰相反，卖点是通过苹果对系统的完善保护和对开发者的严格要求、打造出高质量的封闭生态，用户买到手机后几乎什么都不用做就可以直接使用，当然用户也几乎什么都不能做。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_4f93d1f2f85a4efb966a8129c6ee9a36_img_000" referrerpolicy="no-referrer"></p> 
<p>长期以来，iOS给消费者的感觉就是苹果包办一切、做出了一个不透明但更好用的“黑盒子”，用户只需“知其然”而不用“知其所以然”。相比之下，Android给用户的则是一个拥有更多可能的“积木”，用户可以根据自己的喜好打造独属于自己的体验。这种南辕北辙的系统设计理念也从智能手机时代早期一直延续到了今天，并成为了消费者选择iOS或Android的重要缘由。 </p> 
<p>诚然近年来iOS与Android之间的分野正在逐步变窄，但有观点认为，给用户提供“开发者模式”几乎等同于抹杀了iOS的特色。那么为什么开发者模式在iOS上会如此敏感呢？因为面向普通用户提供开发者模式基本等同于开放了侧载（sideloading）功能，用户可以不再通过App Store，也无需使用麻烦的企业版应用就能获得应用程序了。而苹果对于侧载的态度一直都是强硬的拒绝，甚至其CEO库克更是曾直言不讳的表示，“想要侧载的用户应该去买安卓手机。” </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_afee8cd74f1d40fdbd745083adb3d106_img_000" referrerpolicy="no-referrer"></p> 
<p>苹果的看法是侧载会降低用户所期待的隐私性与安全性，而这种担忧也是有充足理由的。毕竟侧载会在一定程度上破坏系统的整体安全性，在这一功能之下，也很难溯源到应用的来源，对其安全性也更是难以判断。例如在Android上，想必大家都遇到过从非官方应用商店下载的APP，会受到系统提示来源未知的警告。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_b8c45b62c13c48f6ab3fe422afb9a5f5_img_000" referrerpolicy="no-referrer"></p> 
<p>在苹果看来，侧载是完全不可控的、安全性也难以判断，而普通用户在使用iOS时的舒适使用体验，是建立在App Store的审核团队过滤了大量低质应用。换而言之，iOS良好的生态环境是建立在苹果排除了侧载带来的不良应用的基础上。 </p> 
<p>大家不妨想象一下，如果iOS也能进行侧载，那么在Mac上的故事就极有可能会再次重演。Mac设备中的App Store里提供的软件数量与iOS上的App Store无疑不可同日而语，大量应用都会引导用户通过在官网下载的方式进行安装，而在iOS端更有可能出现的则是开发者仅在App Store中提供基础功能，想要体验更多功能就需要打开开发者模式后在其官网进行下载。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220611/v2_46ddbc36980e4a24810c656f6d343730_img_000" referrerpolicy="no-referrer"></p> 
<p>别的不说，Spotify、Netflix、Epic Games这样的“刺头”几乎肯定会这么做。而至于说苹果是为什么会“食言而肥”，当然是因为来自外界的压力。 </p> 
<p>无论是美国的《美国选择与创新法案》、还是欧盟的《数字市场法案》，都要求苹果在App Store之外为用户提供额外的应用下载渠道。现在看来，苹果方面可能已经认为改变欧盟与美国的态度已经不太可能了，那么既然支持侧载或许无法避免，那么让用户更难发现侧载功能的入口就成为了备选项。 </p> 
<p>或许iOS 16真正的“改变”就在这里，只是这样的变化苹果应该是不太想要的。 </p> 
<p>【本文图片来自网络】 </p> 
<p>本文来自微信公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzA4MTk2NTk5Nw==&mid=2649815094&idx=2&sn=0f4f2ac285d410064168e5e3d335dd55&chksm=8788bef4b0ff37e2c47249b72362ea5ea40d155fc5ba76760cbdecaf4220ad0154057f91d4d1#rd">“三易生活”（ID：IT-3eLife）</a>，作者：三易菌，36氪经授权发布。</p>  
</div>
            