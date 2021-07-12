
---
title: '涉及上千款，2021 Chrome插件性能影响分析报告新鲜出炉'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210712/v2_c537a4e4c69d4905956c7ce08ab42780_img_000'
author: 36kr
comments: false
date: Mon, 12 Jul 2021 08:28:58 GMT
thumbnail: 'https://img.36krcdn.com/20210712/v2_c537a4e4c69d4905956c7ce08ab42780_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/fRLSDbSr_zJoj5UQv1ySig">“CSDN”（ID:CSDNnews）</a>，译：弯月，责编：晋兆雨，36氪经授权发布。</p> 
<p>这篇报告调查了 1000 个最流行的 Chrome 插件对浏览器性能和最终用户体验的影响。</p> 
<p>2021 年报告的主要发现： </p> 
<ul class=" list-paddingleft-2"> 
 <li><p> Honey、Evernote Web Clipper 和 Avira Browser Safety 等流行插件会对网站的速度产生重大负面影响；</p></li> 
 <li><p> 在包含大量广告的网站上，广告拦截器和隐私工具可以大大提高性能。</p></li> 
</ul> 
<p>由于不同网站对性能的影响各不相同，因此我们的测试主要包含五个不同的页面：一个简单的测试页面、apple.com、toyota.com 以及 The Independent 和 Pittsburgh Post-Gazette 的新闻文章。 </p> 
<p>如果你想知道你使用的插件是否会影响速度，可以查看此处的插件列表。</p> 
<p>(https://www.debugbear.com/chrome-extension-performance-lookup)</p> 
<p>文本主要内容：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>网站 CPU 使用率的增加；</p></li> 
 <li><p>对页面渲染时间的影响；</p></li> 
 <li><p>后台 CPU 的使用率；</p></li> 
 <li><p>浏览器内存的消耗；</p></li> 
 <li><p>广告拦截器与隐私工具对浏览器性能的影响；</p></li> 
 <li><p>安装多个插件有何影响？</p></li> 
 <li><p>这些浏览器的性能与去年相比如何？</p></li> 
 <li><p>针对每个插件的分析；</p></li> 
 <li><p>方法论。</p></li> 
</ul> 
<h2 label="一级标题" style>网站 CPU 使用率的增加</h2> 
<p>许多 Chrome 插件都能够在你打开的每个页面上运行额外的代码，尽管正常的插件仅在必要的时候才运行代码。</p> 
<p>在 100 个最流行的 Chrome 插件中，Evernote Web Clipper 对性能的负面影响最大。在打开每个页面时，该插件运行代码所占据的时间约为 368 毫秒。如果你尝试在此期间内与页面交互，则响应会非常迟钝。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_c537a4e4c69d4905956c7ce08ab42780_img_000" data-img-size-val="1043,923" referrerpolicy="no-referrer"></p> 
<p>上述插件的安装次数都超过了一百万。虽然几百毫秒听起来并不算多，但是如果安装多个插件，就会对用户体验产生重大影响。 </p> 
<p>浏览器插件对速度的影响取决于用户打开的网站。以上结果是在一个非常简单的网站上收集的，通常在这种页面上，Chrome插件对性能的影响最低。 </p> 
<p>在苹果主页上测试插件时，我们可以看到一个名为 Dark Reader 的夜间模式插件需要 25 秒来分析和调整图像，从而更好地转换成黑暗主题。结果导致页面的加载速度大幅降低，如下所示。 </p> 
<p><img src="https://img.36krcdn.com/20210712/v2_62c41de301024870bf7f04f266833992_img_000" data-img-size-val="953,848" referrerpolicy="no-referrer"></p> 
<p>优惠券代码查找器 Honey 会严重影响电子商务网站的加载速度，CPU 的处理时间大约会增加 825 毫秒。 </p> 
<p>最后，在 Toyota 主页上运行测试时，我们可以看到 Norton Password 导致 CPU 活动增加的幅度最大，增加了大约 1 秒钟。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_cd8c12a28adc4d14897887536af9f2fc_img_000" data-img-size-val="1015,529" referrerpolicy="no-referrer"></p> 
<p>上图仅显示了对性能影响最大的 5 个插件。即使没有安装任何扩展，toyota.com 的加载时间也会超过 3 秒钟，因此很难将随机变化与插件的影响区分开来。</p> 
<p label="正文" style><strong>最受欢迎的 1000 个插件 </strong></p> 
<p>让我们看看其他不太受欢迎但安装量仍然超过了 10万+ 的插件。 </p> 
<p>Ubersuggest 是一款拥有超过 20 万用户的营销工具，它会导致每个页面的加载时间增加1.6 秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_9bd50b7584f343028a6463e23ecbb5b0_img_000" data-img-size-val="714,717" referrerpolicy="no-referrer"></p> 
<p>Substitutions 是一个 Chrome 插件，可以自动替换页面上的某些单词。在小型网站上，它对性能的影响很小（增加了大约 10 毫秒的 CPU 时间），但在像 toyota.com 这样的较大页面上，CPU 的活动增加了 9.7 秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_d192dea58bf74759aa6334031b0dbb2b_img_000" data-img-size-val="795,693" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>对页面渲染时间的影响</h2> 
<p>CPU 活动会导致页面挂起或无响应，并增加电池消耗。如果处理是在页面加载完毕后进行的，那么对用户体验的影响可能不会那么大。 </p> 
<p>Loom 和 Ghostery 等几款插件会运行大量代码，但不会影响页面的渲染时间。 </p> 
<p>但是，有一些插件，比如 Clever、Lastpass 和 DuckDuckGo Privacy Essentials，会在页面开始加载<a class="project-link" data-id="173252" data-name="时立" data-logo="https://img.36krcdn.com/20201024/v2_dc108a27d27b48b0961e72bfa2511730_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/173252" target="_blank">时立</a>即运行代码，并最终导致用户的等待时间加长。下图的测量使用了 First Contentful Paint 指标。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_1b1267facadf4d68b73484f97b85e293_img_000" data-img-size-val="801,761" referrerpolicy="no-referrer"></p> 
<p>虽然苹果页面能够在一秒钟内完成渲染，但在安装了 Dark Reader 后，需要近 4 秒的时间。 </p> 
<p>在一个电子商务网站上，Honey导致页面加载的时间延迟了近半秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_4e35b99df2b64b7cb289fff8a5711458_img_000" data-img-size-val="879,706" referrerpolicy="no-referrer"></p> 
<p>当页面内容开始显示时，Avira 浏览器安全和一些广告拦截器也可能会造成延迟。 </p> 
<p label="正文" style><strong>最受欢迎的 1000 个插件 </strong></p> 
<p>让我们看看最受欢迎的 1000 个插件，一个名为“<a class="project-link" data-id="3967238" data-name="壹伴" data-logo="https://img.36krcdn.com/20210712/v2_cb2a821ef2084fd088f3a1c0ffae211d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4750401230" target="_blank">壹伴</a> · 小插件”的社交媒体工具导致渲染时间延迟了 342 毫秒，而一个名为 Outreach Everywhere 的销售工具则引发了 251 毫秒的延迟。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_bb98b4bebdc4487d99d28d00b5c552aa_img_000" data-img-size-val="769,745" referrerpolicy="no-referrer"></p> 
<p>在Toyota 主页加载期间，名为 anonymoX 的匿名浏览代理会造成渲染延迟 2 秒以上，不过这也并不奇怪，因为流量是通过另一台服务器路由的。 </p> 
<p>Avira 浏览器安全导致渲染延迟 369 毫秒。这不是由访问页面上运行的代码引起的，而是由插件执行的后台工作引起的。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_7891a49c221f45be897abcfd19bc0791_img_000" data-img-size-val="823,743" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>后台 CPU 的使用率</h2> 
<p>Chrome 插件不仅可以在你访问的页面上运行代码，还可以在插件的后台页面上运行代码。例如，有些插件的代码包含可以阻止对某些域发送请求的逻辑。 </p> 
<p>即使访问一个简单的页面，Avira Safe Shopping 也会引发 2 秒多的延迟。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_7a182593ec224973adf901a97cd457a1_img_000" data-img-size-val="921,791" referrerpolicy="no-referrer"></p> 
<p>在较为复杂的页面（在本例中是 Toyota 主页）上，Dashlane 密码管理器和 AdGuard AdBlocker 的后台活动花费了 2 秒以上。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_d12c59fc4b184e7cbac3cf939611117c_img_000" data-img-size-val="861,753" referrerpolicy="no-referrer"></p> 
<p label="正文" style><strong>最受欢迎的 1000 个插件 </strong></p> 
<p>在浏览 The Independent 的新闻文章时，有三个插件导致 CPU 活动超过 20 秒：uberAgent、Dashlane 和 Wappalyz。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_c0b6337056a64e16ac0b4ec2fbbbf0c4_img_000" data-img-size-val="911,720" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>浏览器内存的消耗</h2> 
<p>Chrome 插件会导致你所访问的每个页面的内存使用量增加，而且扩展本身还会消耗内存。这会严重影响性能，尤其是在低配置设备上。 </p> 
<p>通常，广告拦截器和隐私工具会存储有关大量网站的信息，需要大量内存来存储这些数据。话虽如此，当在浏览器中打开的页面包含大量广告时，这些插件可以减少整体内存的消耗。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_67899a7348914f40bcee63aa76974885_img_000" data-img-size-val="695,690" referrerpolicy="no-referrer"></p> 
<p><strong>最受欢迎的 1000 个插件</strong></p> 
<h2></h2> 
<p>查看前 1000 个插件就会发现，广告拦截器占用了大量内存，Trustnav 广告拦截器增加了近 300 MB 的内存消耗。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_bee1572ba0b24fd7ad08f7f89165b7ba_img_000" data-img-size-val="903,765" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>广告拦截器与隐私工具对浏览器性能的影响</h2> 
<p>虽然广告拦截器可能会添加过滤广告的处理，但遇到包含大量的广告的网站时，它们可以大幅提升页面的速度。我们调查了 15 款安装次数超过 50 万的广告拦截器。</p> 
<p>加载跟踪器和呈现广告通常都耗费大量 CPU，但具体影响因网站而异。新闻网站的广告一般都特别多，因此这篇报告集中测试了两大新闻网站的CPU使用率：The Independent 与 Pittsburgh Post-Gazette。</p> 
<p>在没有广告拦截器的情况下，每个页面需要的 CPU 时间为 17.5 秒。即使是性能最低的拦截器（Trustnav）也能减少 57%（ 7.4 秒）的 CPU 时间。</p> 
<p>在我们的测试中，表现最佳的广告拦截器是 Ghostery，它将 CPU 活动减少了 90%，平均仅为 1.7 秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_8e40e16b7a7d4114a31de5bc68d88647_img_000" data-img-size-val="1011,936" referrerpolicy="no-referrer"></p> 
<p>此外，广告拦截器和隐私工具还可以减少 43% ～ 66% 的数据量。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_f25e2ac8908c491887ff62bae1761b42_img_000" data-img-size-val="835,837" referrerpolicy="no-referrer"></p> 
<p>如果没有广告拦截器，每篇文章平均会产生 793 个网络请求。在使用了 Ghostery之后，这一比例下降了 90%，仅为 83 个请求。 </p> 
<p><img src="https://img.36krcdn.com/20210712/v2_9d2c13f99a1a43f089f246cd8174359a_img_000" data-img-size-val="904,747" referrerpolicy="no-referrer"></p> 
<p>在不安装广告拦截器的情况，浏览器打开一篇新闻文章的平均内存消耗为 574 MB。Disconnect 插件可以减少 54% 的内存消耗，降至仅 260 MB。 </p> 
<p>然而，由于浏览器的插件需要一些内存来运行，因此 Trustnav 的广告拦截器等插件会导致整体的内存消耗略微增加。也就是说，因阻止广告而节省下来的资源还不足以抵消广告阻止程序本身的消耗。 </p> 
<p>但是，请记住，当你只打开一个包含大量广告的页面才会出现这种情况。如果你打开 10 个页面，全部显示新闻文章，那么就会节省 10 倍的内存，但广告拦截器消耗的内存通常不会增加。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_7b5d27d82b574f11b66422b7a5462111_img_000" data-img-size-val="1080,1013" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>安装多个扩展有何影响？</h2> 
<p>在大多数情况下，多个 Chrome 插件造成的影响是叠加的。 </p> 
<p>下图显示了 Chrome DevTools 页面性能评测工具中 Apple.com 的加载，我们安装了4个插件：ax Web Accessibility Testing、Evernote Web Clipper、LastPass 和 Skype。 </p> 
<p>可以看到，这些插件一个接一个地运行。如果插件在页面开始加载时立即运行，则会延迟页面的显示速度。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_23c2a79af1994fa8812248b6ae9dffbf_img_000" data-img-size-val="1080,543" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>这些浏览器的性能与去年相比如何？</h2> 
<p>我翻看了今年和去年测试中都包含的 96 个最受欢迎的插件。 </p> 
<p>平均每个页面的加载时间减少了 28 毫秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_835c015be89a4f6aa311e06014e1fd35_img_000" data-img-size-val="1027,914" referrerpolicy="no-referrer"></p> 
<p>但是，2021 年的测试使用的 Chrome 91，而2020 年的测试使用的是 Chrome 83。Chrome 本身的提升也越来越快，因此这些提升可能并不一定是 Chrome 插件本身优化的结果。 </p> 
<p>在使用旧版 Chrome 运行今年的测试时，平均提升时间仅为 13 毫秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_0554653bbb52461bbdc8343e869080fc_img_000" data-img-size-val="1043,963" referrerpolicy="no-referrer"></p> 
<p>请注意，上述比较仅查看了一个网站（一个简单的测试页面）。 </p> 
<p>Grammarly、<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a> Office、Okta 浏览器插件、Avira Safe Shopping 和 Avira Browser Safety 显示页面的加载时间减少超过了 100 毫秒。退步最大的是 Save to Pocket、Loom 和 Evernote。</p> 
<h2 label="一级标题" style>针对每个插件的分析</h2> 
<p label="正文" style><strong>Grammarly的提升</strong></p> 
<p>去年，Grammarly 在每个页面上加载了一个 1.3 MB 的 Grammarly.js 文件。如今，在大多数网站上只加载了 112 KB Grammarly-check.js 脚本。例如，只有当用户关注文本区域时，该插件才会加载完整的 Grammarly.js 文件。 </p> 
<p>但是在一些网站上，Grammarly仍然会加载完整的脚本。比如 Gmail、Twitter、YouTube、LinkedIn、Medium、Slack、Reddit、Upwork、Zendesk 和其他常见的文本输入网站。Grammarly对这些网站的性能影响远大于测试中显示的数据。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_79f3a2073f9f497a9d59367927850dfe_img_000" data-img-size-val="965,587" referrerpolicy="no-referrer"></p> 
<p label="正文" style><strong>Save to Pocket 的退步</strong></p> 
<p>在去年的测试中，Save to Pocket 向每个页面注入了一个很小的样式表，对性能没有明显影响。 </p> 
<p>但是，如今 Save to Pocket 会加载 2 MB 的 JavaScript 文件，导致 CPU 时间增加了 110 毫秒。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_8f17bc105cdf44d9885535bba6946275_img_000" data-img-size-val="1041,637" referrerpolicy="no-referrer"></p> 
<p label="正文" style><strong>Evernote、Outreach Everywhere 和 Ubersuggest</strong></p> 
<p>Evernote 会在每个页面上加载 4.3 MB 的脚本，高于一年前的 2.9 MB。因此，解析、编译和运行此代码需要花费大量时间。 </p> 
<p>Outreach Everywhere 会在每个页面上加载 4.5 MB 的代码。但是，这些代码对性能的影响非常大，因为它是在 document_start 上加载的。这意味着代码在页面开始渲染之前就会运行，因此会延迟页面的显示。 </p> 
<p>下图利用 Chrome DevTools 性能配置文件针对安装了这两个插件的页面进行了分析。 </p> 
<p><img src="https://img.36krcdn.com/20210712/v2_7943cdba72c042b5a06b897d7bce91f0_img_000" data-img-size-val="1080,395" referrerpolicy="no-referrer"></p> 
<p>Ubersuggest 会在每个页面上加载一个 7.5 MB 的 JavaScript 文件。其中很多是地理数据，比如下面的代码包含 38,279 个不同的地理位置。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_8759d22736af44108ac11ac879faad98_img_000" data-img-size-val="1080,497" referrerpolicy="no-referrer"></p> 
<p label="正文" style><strong>Avira 安全购物</strong></p> 
<p>Avira Safe Shopping 拥有超过 300 万用户。为什么有时候页面渲染会延迟将近半秒？ </p> 
<p>这是因为该插件包含 39,328 个网站的安全列表。每当打开新网站时，Avira 就会遍历此列表，结果就会导致网站加载速度变慢。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_8487b7399d5348e58ab09f2451b6d88f_img_000" data-img-size-val="1080,104" referrerpolicy="no-referrer"></p> 
<p label="正文" style><strong>Dashlane 和 uberAgent </strong></p> 
<p>在查看 The Independent 的一篇文章时，Dashlane 和 uberAgent 都引发了 20 多秒的后台 CPU 活动。 </p> 
<p>uberAgent 会针对每个网络请求，设置一个计时器，每 50 毫秒触发一次，以检查页面是否已完成加载。如果页面发送出1000 个请求，uberAgent就会创建大量计时器，从而拉垮整个页面速度。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_262281594d7e4f9f9ccf200bde78c3a2_img_000" data-img-size-val="1080,437" referrerpolicy="no-referrer"></p> 
<p>uberAgent 会运行许多小任务，但 Dashlane 偶尔运行超过 500 毫秒的长时间任务。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_c72c79a667f24800833000fe3a873023_img_000" data-img-size-val="1080,374" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>查看某个插件对性能的影响</h2> 
<p>如果你想知道某个插件对性能的影响，请点击这里：https://www.debugbear.com/chrome-extension-performance-lookup。</p> 
<p><img src="https://img.36krcdn.com/20210712/v2_19ca5a616ec241d6b22934c1b938a64c_img_000" data-img-size-val="1080,692" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>方法论</h2> 
<p>我们的测试是在Google 云实例 n2-standard-2 上运行的，本篇报告中显示的数字采用了 7 次测试结果的中位数。 </p> 
<p>我们使用的数据是使用 Lighthouse 收集的，测试中的结果是在没有任何网络限流下的观察结果，并不是模拟结果。 </p> 
<p>我们的测试总共包含 1004 个插件。很多插件只修改了新标签页面，通常不会影响性能，因此不包含在结果中。还有一些测试结果出错的插件也不包括在内。</p> 
<p>原文链接：https://www.debugbear.com/blog/chrome-extension-performance-2021</p> 
<p>声明：本文由CSDN翻译，转载请注明来源。 </p>  
</div>
            