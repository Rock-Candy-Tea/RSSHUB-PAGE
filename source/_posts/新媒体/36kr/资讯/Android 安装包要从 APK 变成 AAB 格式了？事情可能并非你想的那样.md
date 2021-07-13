
---
title: 'Android 安装包要从 APK 变成 AAB 格式了？事情可能并非你想的那样'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210713/v2_fa637fcbd864472f9f534f4dc00871bc_img_000'
author: 36kr
comments: false
date: Tue, 13 Jul 2021 11:51:09 GMT
thumbnail: 'https://img.36krcdn.com/20210713/v2_fa637fcbd864472f9f534f4dc00871bc_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/ILYfatIjR36hVAehqmoFug">“爱范儿”（ID:ifanr）</a>，作者：王贺龙，36氪经授权发布。</p> 
<p>玩过王者<a class="project-link" data-id="3969307" data-name="荣耀" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969307" target="_blank">荣耀</a>的朋友，几乎无人不晓「鲁班七号」这个英雄。</p> 
<p>作为 Android 的应用程序包，「APK」对于资深 Android 用户来说，知名度并不亚于前者。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_fa637fcbd864472f9f534f4dc00871bc_img_000" data-img-size-val="720,405" referrerpolicy="no-referrer"></p> 
<p>也正因如此，日前 Google 的一份声明，牵动了许多 Android 用户的神经。</p> 
<p>Google 宣布，从 2021 年 8 月开始，Google Play 商店将要求开发者使用 Android App Bundle（AAB）发布新应用。这将取代 APK 作为标准发布格式。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_4783bd9676324c78853e6ad3a22d9b8b_img_000" data-img-size-val="720,495" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：hitechglitz</p> 
<p>消息一出，一些用户开始猜测甚至担忧：「以后还能借一部 APK 说话吗」？「Google 是不是在故意为难国产品牌」？</p> 
<p>实际上，有这些疑问的朋友，大概率误解 Google 的这个动作了。</p> 
<h2 label="一级标题" style>什么是 AAB？</h2> 
<p>这次舆论漩涡的中心，就是 AAB 格式。所以首先我们要搞清楚，AAB 是什么。</p> 
<p>在 2018 年 5 月举行的 Google 开发者大会上，Google 就已公布了 Android App Bundle（AAB）格式，并称这是其现代化开发的一部分。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_e844be84125d40f094c711fa9232f097_img_000" data-img-size-val="720,405" referrerpolicy="no-referrer"></p> 
<p>Google 介绍道，开发者在上传应用至 Google Play 时，需采用 AAB 格式。Google Play 将负责生成 APK 文件及签名。</p> 
<p>这句话有两个重点。</p> 
<p>一是 AAB 只是上传时应用的格式，用户下载时，获取的依旧是 APK。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_53aa59ec2b9d4492ac59eb04f97171d9_img_000" data-img-size-val="720,356" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：techlog360</p> 
<p>对于开发者来说，从 APK 转战到 AAB 没什么痛点。AAB 是一种开源格式，在构建时，选择相关的工具或引擎即可。</p> 
<p>另外根据 Google 的声明，已经存在的应用，无需重新上传 AAB 文件。只是今年 8 月份开始，提交新应用时才需要使用 AAB。</p> 
<p>用户这边更不必担忧，因为我们在终端设备上看到的，依旧是 APK 格式。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_c3d4f2abf9da47de89e84b1780af2c62_img_000" data-img-size-val="720,360" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：9to5google</p> 
<p>二是生成 APK 的工作，将由 Google Play 完成。</p> 
<p>Google Play 将根据用户设备的配置，从 AAB「源文件」里提取、组装适合该用户设备的代码及资源，从而生成 APK 安装包。</p> 
<p>也就是说，这时用户下载的应用，已经过 Google Play 优化，以确保该应用可在当前设备上以最佳状态运行。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_1a3a10009cdb47c4af06e3f1cd582fc2_img_000" data-img-size-val="720,480" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：beebom</p> 
<p>换种说法，方便你理解：AAB 就像是一袋方便面，里面有各种口味的调料包。Google Play 就是大厨，它会根据你设备的喜好，来判断面要煮多久、放什么调料包。</p> 
<p>最终煮好的面，就是 APK 了。</p> 
<h2 label="一级标题" style>AAB 的三大优势</h2> 
<p>Google 之所以要「强硬」地推行 AAB 格式，很大原因是 AAB 相比 APK 有着多种先天优势。</p> 
<p>第一点，是体积轻盈。</p> 
<p>上文说到，Google Play 会从 AAB 里，个性化地生成并优化 APK，以针对不同配置的设备、语言进行分发。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_a89e113346ca47a09fb0b79dcf9f7dff_img_000" data-img-size-val="686,380" referrerpolicy="no-referrer"></p> 
<p>举个例子：假设你的手机是 2K 屏幕，首选语言是中文。那么 Google Play 在拼装 APK 时，就会只把 2K 分辨率、中文字符包的资源放进 APK 里。</p> 
<p>而传统的 APK，开发者会将各种分辨率和语言包，打包在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>。用户下载下来，手机需要从中挑出适合自己的资源安装运行。</p> 
<p>随着机型的不断增加，开发者需要在 APK 文件里塞上越来越多的资源，来提高适配性。因此，App 越来越大，动辄上百 MB。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_28a0d3f7cad542148e7c9282d58475b6_img_000" data-img-size-val="720,480" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：altavia</p> 
<p>那么 AAB 的应用，相当于「把复杂留给 Google Play，把简单留给用户」。用户下载的 APK，是经过 Google 精简过的，因此体积会小一些。</p> 
<p>那么会小多少呢？根据 Google 的说法，此举可将 APK 的体积压缩 15%。</p> 
<p>不过实际情况可能要好于这一预期。例如<a class="project-link" data-id="3969607" data-name="爱彼迎" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969607" target="_blank">爱彼迎</a>在拥抱 AAB 后，体积减少了 22%。Netflix 更甚，达到了 57%。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_845778276ac045b8b49efe24a98ae1d2_img_000" data-img-size-val="720,567" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>利用 AAB 特性缩减体积的案例</p> 
<p>所以对于用户来说，可感知的一点就是安装包变小了，下载、安装的速度会更快。</p> 
<p>其次，AAB 使得用户下载的应用，最大程度的符合设备配置，因此运行起来或许会更流畅。某种程度上算是提升了设备性能。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_b6ed0b86befc44f3ae59166746fa87a7_img_000" data-img-size-val="720,360" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：angelseoservices</p> 
<p>第二点，是应用模块化。</p> 
<p>AAB 允许开发者将应用的功能拆分开来。让有需要的用户，自行下载。</p> 
<p>我们继续举例子。假设开发者现在要做一个拍照 app，我的手机是单摄，你的手机是双摄。为了减小应用初始的大小，开发者可以把某些功能，设置为按需下载。</p> 
<p>比如你想用这款 app 里，针对双摄手机推出的功能，你就下载额外的资料包即可。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_93bfe71a5dc0445f8dcf44bc61ae7bca_img_000" data-img-size-val="720,480" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：unsplash</p> 
<p>开发者还可以决定什么时间，向什么机型推送应用的新功能。相当于自定义和掌控各类用户的体验。</p> 
<p>「你我用着同一个 app，但享受着不<a class="project-link" data-id="51403" data-name="同功" data-logo="https://img.36krcdn.com/20200729/v2_052c082c2c7749ef8999deb700ed36e1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/51403" target="_blank">同功</a>能」的情况，或在将来成为常态。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_0d4f020d342845588e6564d4eb5e718b_img_000" data-img-size-val="720,541" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：unsplash</p> 
<p>第三点，是免下载体验。</p> 
<p>AAB 的免安装分发特性，可让用户在 Google Play 里，无需下载应用，便可体验到应用的某些功能。</p> 
<p>比如有一款游戏，我们不确定是否值得下载，就可以点击「立即体验」，试玩前几个关卡，且不用下载该应用。</p> 
<p>这有点像 iOS 14 新增的 App Clip 功能，可以被看作完整版应用的快捷方式，当中会包含应用的一部分功能。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_c2c79a5a89064050b98ce5f2b34288ab_img_000" data-img-size-val="720,403" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>iOS 14 的 App Clip 功能</p> 
<p>所以对于用户来说，AAB 格式的推广，我们是可以感知到的，且会有更好的体验。</p> 
<p>光打用户体验牌肯定不行，还得考虑开发者的感受。为了让他们有动力转战 AAB 格式，Google 给出了多个理由：</p> 
<p>1.<span style="letter-spacing: 0px;">版本管理更高效，一个工件便可包含应用所有经过编译的代码、资源和原生库。</span></p> 
<p>2.<span style="letter-spacing: 0px;">模块化应用开发功能，可提升工程速度。</span></p> 
<p>3.<span style="letter-spacing: 0px;">编译系统的优化，可缩短编译时间。</span></p> 
<p>4.<span style="letter-spacing: 0px;">自定义功能传送，可掌控用户体验。</span></p> 
<p>不感兴趣也没关系，那就来「硬的」：8 月起，应用程序包不改成 AAB 格式，就不许上传，逼迫着开发者进行转变。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_2100f7a2073942a1a61a1c53e869bee9_img_000" data-img-size-val="720,405" referrerpolicy="no-referrer"></p> 
<p>这足以见得 AAB 对于 Google Play 未来规划的重要性。</p> 
<h2 label="一级标题" style>这对 Android 用户有何影响？</h2> 
<p>推广 AAB 格式，对于<a class="project-link" data-id="3969555" data-name="大众" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969555" target="_blank">大众</a>用户来说绝对是一件好事。谁不希望自己下载的应用，体积又小、适配又好呢？</p> 
<p>不过，Google 只是要求 Google Play 这样做，没有强制其他应用商店跟进。</p> 
<p>也就是说，如果你没有在使用 Google Play，那么这个改动暂时是感知不到的。</p> 
<p><img src="https://img.36krcdn.com/20210713/v2_e14ffb1ca1a745149e1b7eb1405185de_img_000" data-img-size-val="720,403" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自：unsplash</p> 
<p>但 AAB 格式的优点这么多，我们有理由相信，国内的应用商店会逐步跟上 Google 的步伐，拥抱 AAB。</p> 
<p>而且我们上文说到，用户下载的安装包，依旧会以 APK 格式呈现。因此那些「Google 此举是为了针对国内厂商」的谣言，也就不攻自破了。</p> 
<p>何况<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>等应用商店，从前两年开始，就已经支持开发者上传 AAB 格式的应用。所以用户们大可放宽心，静等 AAB 格式推广的红利即可。</p>  
</div>
            