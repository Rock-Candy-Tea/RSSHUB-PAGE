
---
title: '全网最全 ECMAScript 攻略 _ 创作者训练营第二期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a71bab3649444021bdd7804f6ebcf2f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Apr 2021 23:14:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a71bab3649444021bdd7804f6ebcf2f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>作为前端开发工程师，<strong>ES6</strong> 这个词想必不陌生，<strong>ECMAScript</strong> 这个奇怪发音的名字应该也应该有所了解，你是否好奇过 <strong>ECMA</strong> 世界的神秘数字代号，<strong>ECMA262</strong> 是什么，<strong>ESxxx</strong> 又是什么，<strong>TC39</strong> 是什么，<strong>Stage 3</strong> 、<strong>Stage 4</strong> 又意味着什么？你是否被层出不穷的 <strong>ES20XX</strong> 新特性所迷惑，需要掌握该特性到底是哪年推出的吗，这些提案在哪里能够看到，哪些已经可用，历年的 ES 标准去哪里查找？今天我来带大家揭开 ECMAScript 的神秘面纱，彻底理解掌握这些神秘代号，以及截止到 2021 年 ECMAScript 的特性。</p>
</blockquote>
<p>另：祝贺<a href="https://www.toutiao.com/i6950609447534412327" target="_blank" rel="nofollow noopener noreferrer">我国首个 JS 语言提案在 ECMA 进入 Stage 3</a>。</p>
<h2 data-id="heading-0">ECMAScript 历史</h2>
<p>我们首先来看 ECMA 是什么。<strong>ECMA</strong>，读音类似“埃科妈”，是<strong>欧洲计算机制造商协会</strong>（European Computer Manufacturers Association）的简称，是一家国际性会员制度的信息和电信标准组织。1994 年之后，由于组织的标准牵涉到很多其他国家，为了体现其国际性，更名为 <a href="https://www.ecma-international.org/" target="_blank" rel="nofollow noopener noreferrer"><strong>Ecma 国际</strong></a>（Ecma International），因此 Ecma 就不再是首字母缩略字了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a71bab3649444021bdd7804f6ebcf2f0~tplv-k3u1fbpfcp-watermark.image" alt="01-Ecma_International_Logo.svg.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解了这段历史，为了技术写的专业性，如果文章中提到 Ecma 的时候，<strong>可以写成 Ecma 或者 ecma，不要写成 ECMA</strong>，除非是 ECMAScript 或 ECMA-XXX 这类专有名词。</p>
<p>1995 年，著名的网景公司（Netscape）的 <a href="https://zh.wikipedia.org/wiki/%E5%B8%83%E8%98%AD%E7%99%BB%C2%B7%E8%89%BE%E5%85%8B" target="_blank" rel="nofollow noopener noreferrer">Brendan Eich</a> 开发了一种脚本语言，最初命名为 Mocha，后来改名为 LiveScript，最后为了蹭当时火热的 Java 热度重命名为了 JavaScript。</p>
<p>了解了 Ecma 国际和 JavaScript，就方便了解 ECMAScript 了，ECMAScript 是一种由 Ecma 国际在标准 ECMA-262 中定义的 <a href="https://zh.wikipedia.org/wiki/%E8%84%9A%E6%9C%AC%E8%AF%AD%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">脚本语言</a> 规范。这种语言在往往被称为 <a href="https://zh.wikipedia.org/wiki/JavaScript" target="_blank" rel="nofollow noopener noreferrer">JavaScript</a> 或 <a href="https://zh.wikipedia.org/wiki/JScript" target="_blank" rel="nofollow noopener noreferrer">JScript</a> ，但实际上 JavaScript 和 JScript 是 ECMA-262 标准的实现和扩展。</p>
<h2 data-id="heading-1">神秘的 ECMA-262</h2>
<p>上文提到了第一个神秘代码 <strong>ECMA-262</strong>，ECMA-262 到底是什么呢？原来 Ecma 国际的标准，都会以 Ecma-Number 命名，ECMA-262 就是 ECMA 262 号标准，具体就是<strong>指 ECMAScript 遵照的标准</strong>。1996 年 11 月，网景公司将 JavaScript 提交给 Ecma 国际进行标准化。ECMA-262 的第一个版本于 1997 年 6 月被 Ecma 国际采纳。</p>
<p>尽管 JavaScript 和 JScript 与 ECMAScript 兼容，但包含超出 ECMAScript 的功能。</p>
<p>我们如何查看最新最全的 Ecma 标准呢，可以查看 Ecma 国际官网的 <a href="https://www.ecma-international.org/publications-and-standards/standards/" target="_blank" rel="nofollow noopener noreferrer">Standards</a>。截止到 2021 年 4 月，最新的 Ecma 标准已经到了 <a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-418/" target="_blank" rel="nofollow noopener noreferrer">ECMA-418</a>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b8f135462b64d449f8da88e5313e66f~tplv-k3u1fbpfcp-watermark.image" alt="02-ecma-latest-standard.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Ecma 标准涉及的类别非常多，官网因此提供了按照类别和最新修改排序的功能，我们来看看 ECMA-262 属于哪个类别：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34f1bf43de6456bb93bdc061a502677~tplv-k3u1fbpfcp-watermark.image" alt="03-ecma262.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>ECMA-262 属于“软件工程与接口”类别</strong>，该类别一共有 12 个标准，详见上图。注意，ECMA-262 的最新更新日期是 2020 年 6 月，<strong>并且会在今年 6 月进行更新，更新之后，ES2021 就会成为 ECMA 标准。</strong></p>
<h2 data-id="heading-2">探秘 Ecma TC39 神秘组织</h2>
<p>揭开了 Ecma-262 神秘面纱之后，我们来探秘一个代号名为 <a href="https://www.ecma-international.org/technical-committees/tc39/" target="_blank" rel="nofollow noopener noreferrer">TC39</a> 的神秘组织。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e83674d79a534e7da1e9bf2fef666ddf~tplv-k3u1fbpfcp-watermark.image" alt="04-ecma-tc39.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实官网解释的已经很清楚了，我用中文简要概括下：</p>
<p>TC39 是 Technical Committee 39 的简称，<strong>是制定 ECMAScript 标准的委员会</strong>，由各个主流浏览器厂商的代表构成，主席团三人分别来自 PayPal、Bloomberg 和 Microsoft，下设两个工作组（task group） <a href="https://www.ecma-international.org/task-groups/tc39-tg1/" target="_blank" rel="nofollow noopener noreferrer">TC39-TG1</a>  和  <a href="https://www.ecma-international.org/task-groups/tc39-tg2/" target="_blank" rel="nofollow noopener noreferrer">TC39-TG2</a> 。</p>
<p>TC39-TG1 工作组主要工作是通用 ECMAScript® 语言， 包括语法、语义、类库以及支持该语言的技术。</p>
<p>TC39-TG2 工作组 ECMAScript® 国际化 API 标准。</p>
<p>我们经常会看到类似的新闻：XX 公司成为 Ecma TC39 成员。想要加入 TC39 会议，必须先成为 Ecma 会员：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/459948bbc08f45b993fd96aa835cc1ff~tplv-k3u1fbpfcp-watermark.image" alt="05-tc39-contribute.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那 Ecma 到底有哪些成员呢？<a href="https://www.ecma-international.org/about-ecma/members/" target="_blank" rel="nofollow noopener noreferrer">Ecma 官网</a>给出了答案：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a9f30a39a24463ab9eef02a66d24826~tplv-k3u1fbpfcp-watermark.image" alt="06-members.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>几大巨头赫然在列！看到这里，发现一共有 5 种类别，分别是 Ordinary members、Associate members、SME members、SPC members、NFP members，我们来看 Ordinary members 和 Associate members 的对比：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b87326076eb443689f06ea31a9adce5~tplv-k3u1fbpfcp-watermark.image" alt="07-memeber-fee.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Associate members 没有 Ecma 大会（General Assembly）的投票权</strong>！在 Associate members 中，我国的阿里巴巴、华为、腾讯、360 赫然在列。</p>
<p>Wait，CHF 70000，这是 70000 法郎？Ecma 果然是欧洲豪门，顶级会员年费接近 50 万人民币。算了一下 Ecma 国际会员费收入每年就有 1,134,000 法郎，约 800 万人民币。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b19512e002ad44ff8870becb28e60736~tplv-k3u1fbpfcp-watermark.image" alt="08-member-fee-all.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>了解更多关于 TC39 的内容，可以探索其官网 <a href="https://tc39.es/" target="_blank" rel="nofollow noopener noreferrer">TC39 – Specifying JavaScript.</a> 和 GitHub 仓库 <a href="https://github.com/tc39" target="_blank" rel="nofollow noopener noreferrer">Ecma TC39 · GitHub</a>，<strong>注意这个仓库很重要</strong>。查看一下 members，发现了 <a href="https://github.com/akira-cn" target="_blank" rel="nofollow noopener noreferrer">月影</a>、<a href="https://github.com/cncuckoo" target="_blank" rel="nofollow noopener noreferrer">李松峰</a> 和 <a href="https://github.com/yuanyan" target="_blank" rel="nofollow noopener noreferrer">元彦</a> 三位国内大佬。</p>
<h2 data-id="heading-3">我们熟悉的 ES6</h2>
<p>探究完神秘的 ECMA-262 和 TC39 之后，我们缓口气，来看看我们最为熟悉的 ESX 家族。</p>
<p>上文提到 ECMAScript 是由 Ecma 国际在标准 ECMA-262 中定义的脚本语言规范。<strong>到 2015 年，一共发布了 1、2、3、4、5、5.1、6 共 7 个版本</strong>（其中 4 被废弃）。</p>
<p>我们常把 5.1 之前的 ECMAScript 版本统称做 <strong>ES5</strong>，将 6 版本之后的版本统称做 <strong>ES6</strong>（因为从 2015 年起，ECMAScript 终于步入正轨，每年发布一次版本，到了 2021 年，已经发布了 6 个版本了，实在太多，<strong>所以用变革了 JavaScript 时代的 ES6 作为后续版本的代称</strong>）。</p>
<p>划重点，Web 前端招聘的 JD 中，经常出现的 ES6，<strong>不仅仅是 ES2015 这个版本，而是指代 ES2015 和其后每年发布的 ECMAScript 版本</strong>。</p>
<p>从 ECMAScript 第 6 版开始，每年发布一个 ECMAScript 版本，因此 ECMAScript 版本有了很多名字，包括全名 ECMAScript 6、简写 ES6、年份命名 ECMAScript 2015、年份简写 ES2015。最常见的名字还是 ES6，之后推出的 ES7、ES8 等同理。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb75f204f9934111b7c89a469ec0e0d1~tplv-k3u1fbpfcp-watermark.image" alt="09-历届版本.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要注意的是，自从 <a href="https://exploringjs.com/impatient-js/ch_history.html#tc39-process" target="_blank" rel="nofollow noopener noreferrer">TC39 进程</a> 制定以来，ECMAScript 版本的重要性就降低了很多。大家不必记住某一个 ES 特性到底是哪年推出的。现在真正重要的是提案处于哪个阶段：<strong>一旦提案到了第 4 阶段，那么它就可以使用了</strong>。但是即使这样，你仍然需要检查你的引擎是否支持该功能。</p>
<p>这里又提到了一个 <a href="https://exploringjs.com/impatient-js/ch_history.html#tc39-process" target="_blank" rel="nofollow noopener noreferrer">TC39 进程</a> 和阶段（Stage）的概念，我们接下来看看这两个概念是什么含义。</p>
<h2 data-id="heading-4">TC39 进程和 Stage X</h2>
<p><a href="https://exploringjs.com/impatient-js/ch_history.html#tc39-process" target="_blank" rel="nofollow noopener noreferrer">TC39 进程</a> 故名思义，肯定是 TC39 组织发布的一个进程。随着 ECMAScript 6 的发布，当时的发布流程出现了两个明显的问题：</p>
<ul>
<li>如果在两个 release 之间多次通过早已准备好的功能，势必在其 release 之前等待很长一段时间。而且功能准备如果很晚，会增加 deadline 之前匆忙赶工的风险。</li>
<li>很多功能在其实现和使用之前就花了很长时间在设计上，发现与实现和使用相关的设计缺陷会非常晚。</li>
</ul>
<p>为了解决上述问题， TC39 建立了新的 TC39 进程：</p>
<ul>
<li>ECMAScript 功能设计与每年的 ECMAScript 版本发布独立，使用不同阶段（Stage）来区分功能的状态，共 5 个阶段，从 Stage 0（strawman）开始，到 Stage 4 （finished）结束。</li>
<li>越往后的阶段，需要原型实现和真机测试，可以建立设计和实现之间的反馈机制。</li>
<li>ECMAScript 版本<strong>每年发布一次</strong>，发布的内容包含在 <strong>release deadline</strong> 之前的全部到达 <strong>Stage 4</strong> 的功能。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d8c77792884669836496a38a1bf00b~tplv-k3u1fbpfcp-watermark.image" alt="10-历届阶段.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Stage 0：代号“稻草人（strawman）”，草案阶段</li>
<li>Stage 1：代号“提案（proposal）”， TC39 帮助阶段</li>
<li>Stage 2：代号“草案（draft）”， 本阶段很有可能成为标准</li>
<li>Stage 3：代号“候选（candidate）”， 已完成，需要从实现中获得反馈</li>
<li>Stage 4：代号“结束（finished）”， 准备成为标准</li>
</ul>
<p>理解了 Stage 各阶段的含义，就能理解<a href="https://www.toutiao.com/i6950609447534412327" target="_blank" rel="nofollow noopener noreferrer">我国首个 JS 语言提案在 ECMA 进入 Stage 3</a>这个新闻的意义了。</p>
<p>如何查看各阶段的提案呢？可以查阅 <a href="https://github.com/tc39/ecma262/" target="_blank" rel="nofollow noopener noreferrer">GitHub - tc39/ecma262: Status, process, and documents for ECMA-262</a> 这个 repo。</p>
<h2 data-id="heading-5">历届 ES 特性全收录 ES2016 - ES2022</h2>
<p>网上有太多零散的 ES 特性总结，很多同学想知道，<strong>有官方的 ECMAScript 功能列表吗</strong>？</p>
<p>当然有，TC39 仓库列出了  <a href="https://github.com/tc39/proposals/blob/master/finished-proposals.md" target="_blank" rel="nofollow noopener noreferrer">已完成提案</a>  以及它们的版本。</p>
<p>虽然 6 年过去，但是新增的 ES 功能其实并不多，截至 2021 年 4 月 23 日，包括草案的功能，<strong>一共 39 个</strong>：</p>
<h3 data-id="heading-6">ES2016</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-Array.prototype.includes" target="_blank" rel="nofollow noopener noreferrer">Array.prototype.includes</a></p>
<ul>
<li>作者：Domenic Denicola</li>
<li>维护者：Domenic Denicola、Rick Waldron</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2015-11/nov-17.md#arrayprototypeincludes" target="_blank" rel="nofollow noopener noreferrer">November 2015</a></li>
<li>发布时间：2016</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-exponentiation-operator" target="_blank" rel="nofollow noopener noreferrer">Exponentiation operator</a></p>
<ul>
<li>作者：Rick Waldron</li>
<li>维护者：Rick Waldron</li>
<li>TC39 会议记录：  <a href="https://github.com/tc39/notes/blob/master/meetings/2016-01/jan-28.md#5xviii-exponentiation-operator-rw" target="_blank" rel="nofollow noopener noreferrer">January 2016</a></li>
<li>发布时间：2016</li>
</ul>
</li>
</ul>
<h3 data-id="heading-7">ES2017</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-object-values-entries" target="_blank" rel="nofollow noopener noreferrer">Object.values/Object.entr…</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2016-03/march-29.md#objectvalues--objectentries" target="_blank" rel="nofollow noopener noreferrer">March 2016</a></li>
<li>发布时间：2017</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-string-pad-start-end" target="_blank" rel="nofollow noopener noreferrer">String padding</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband、Rick Waldron</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2016-05/may-25.md#stringprototypepadstartend-jhd" target="_blank" rel="nofollow noopener noreferrer">May 2016</a></li>
<li>发布时间：2017</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-object-getownpropertydescriptors" target="_blank" rel="nofollow noopener noreferrer">Object.getOwnPropertyDescriptors</a></p>
<ul>
<li>作者：Jordan Harband、Andrea Giammarchi</li>
<li>维护者：Jordan Harband、Andrea Giammarchi</li>
<li>TC39 会议记录：<a href="https://github.com/tc39/notes/blob/master/meetings/2016-05/may-25.md#objectgetownpropertydescriptors-jhd" target="_blank" rel="nofollow noopener noreferrer">May 2016</a></li>
<li>发布时间：2017</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-trailing-function-commas" target="_blank" rel="nofollow noopener noreferrer">Trailing commas in function parameter lists and calls</a></p>
<ul>
<li>作者：Jeff Morrison</li>
<li>维护者：Jeff Morrison</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2016-07/jul-26.md#9ie-trailing-commas-in-functions" target="_blank" rel="nofollow noopener noreferrer">July 2016</a></li>
<li>发布时间：2017</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-async-await" target="_blank" rel="nofollow noopener noreferrer">Async functions</a></p>
<ul>
<li>作者：Brian Terlson</li>
<li>维护者：Brian Terlson</li>
<li>TC39 会议记录：<a href="https://github.com/tc39/notes/blob/master/meetings/2016-07/jul-28.md#10iv-async-functions" target="_blank" rel="nofollow noopener noreferrer">July 2016</a></li>
<li>发布时间：2017</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/ecmascript_sharedmem" target="_blank" rel="nofollow noopener noreferrer">Shared memory and atomics</a></p>
<ul>
<li>作者：Lars T Hansen</li>
<li>维护者：Lars T Hansen</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2017-01/jan-24.md#13if-seeking-stage-4-for-sharedarraybuffer" target="_blank" rel="nofollow noopener noreferrer">January 2017</a></li>
<li>发布时间：2017</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">ES2018</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-template-literal-revision" target="_blank" rel="nofollow noopener noreferrer">Lifting template literal restriction</a></p>
<ul>
<li>作者：Tim Disney</li>
<li>维护者：Tim Disney</li>
<li>TC39 会议记录：   <a href="https://github.com/tc39/notes/blob/master/meetings/2017-03/mar-21.md#10ia-template-literal-updates" target="_blank" rel="nofollow noopener noreferrer">March 2017</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-regexp-dotall-flag" target="_blank" rel="nofollow noopener noreferrer">s (dotAll) flag for regular expressions</a></p>
<ul>
<li>作者：Mathias Bynens</li>
<li>维护者：Brian Terlson、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2017-11/nov-28.md#9ie-regexp-dotall-status-update" target="_blank" rel="nofollow noopener noreferrer">November 2017</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-regexp-named-groups" target="_blank" rel="nofollow noopener noreferrer">RegExp named capture groups</a></p>
<ul>
<li>作者：Gorkem Yakin、Daniel Ehrenberg</li>
<li>维护者：Daniel Ehrenberg、Brian Terlson、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2017-11/nov-28.md#9if-regexp-named-captures-status-update" target="_blank" rel="nofollow noopener noreferrer">November 2017</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-object-rest-spread" target="_blank" rel="nofollow noopener noreferrer">Rest/Spread Properties</a></p>
<ul>
<li>作者：Sebastian Markbåge</li>
<li>维护者：Sebastian Markbåge</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-01/jan-23.md#restspread-properties-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">January 2018</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-regexp-lookbehind" target="_blank" rel="nofollow noopener noreferrer">RegExp Lookbehind Assertions</a></p>
<ul>
<li>作者：Gorkem Yakin、Nozomu Katō、Daniel Ehrenberg</li>
<li>维护者：Daniel Ehrenberg、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-01/jan-23.md#conclusionresolution-16" target="_blank" rel="nofollow noopener noreferrer">January 2018</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-regexp-unicode-property-escapes" target="_blank" rel="nofollow noopener noreferrer">RegExp Unicode Property Escapes</a></p>
<ul>
<li>作者：Mathias Bynens</li>
<li>维护者：Brian Terlson、Daniel Ehrenberg、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-01/jan-24.md#conclusionresolution-1" target="_blank" rel="nofollow noopener noreferrer">January 2018</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-promise-finally" target="_blank" rel="nofollow noopener noreferrer">Promise.prototype.finally</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband</li>
<li>TC39 会议记录 ：<a href="https://github.com/tc39/notes/blob/master/meetings/2018-01/jan-24.md#conclusionresolution-2" target="_blank" rel="nofollow noopener noreferrer">January 2018</a></li>
<li>发布时间：2018</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-async-iteration" target="_blank" rel="nofollow noopener noreferrer">Asynchronous Iteration</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband</li>
<li>TC39 会议记录 ：<a href="https://github.com/tc39/notes/blob/master/meetings/2018-01/jan-24.md#conclusionresolution-2" target="_blank" rel="nofollow noopener noreferrer">January 2018</a></li>
<li>发布时间：2018</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">ES2019</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-optional-catch-binding" target="_blank" rel="nofollow noopener noreferrer">Optional catch binding</a></p>
<ul>
<li>作者：Michael Ficarra</li>
<li>维护者：Michael Ficarra</li>
<li>TC39 会议记录 ： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-05/may-22.md#conclusionresolution-7" target="_blank" rel="nofollow noopener noreferrer">May 2018</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-json-superset" target="_blank" rel="nofollow noopener noreferrer">JSON superset</a></p>
<ul>
<li>作者：Richard Gibson</li>
<li>维护者：Mark Miller、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-05/may-22.md#conclusionresolution-8" target="_blank" rel="nofollow noopener noreferrer">May 2018</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-Symbol-description" target="_blank" rel="nofollow noopener noreferrer">Symbol.prototype.description</a></p>
<ul>
<li>作者：Michael Ficarra</li>
<li>维护者：Michael Ficarra</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2018-11/nov-27.md#conclusionresolution-12" target="_blank" rel="nofollow noopener noreferrer">November 2018</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/Function-prototype-toString-revision" target="_blank" rel="nofollow noopener noreferrer">Function.prototype.toString revision</a></p>
<ul>
<li>作者：Michael Ficarra</li>
<li>维护者：Michael Ficarra</li>
<li>TC39 会议记录：<a href="https://github.com/tc39/notes/blob/master/meetings/2018-11/nov-27.md#conclusionresolution-13" target="_blank" rel="nofollow noopener noreferrer">November 2018</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-object-from-entries" target="_blank" rel="nofollow noopener noreferrer">Object.fromEntries</a></p>
<ul>
<li>作者：Darien Maillet Valentine</li>
<li>维护者：Jordan Harband、Kevin Gibbons</li>
<li>TC39 会议记录：<a href="https://github.com/tc39/notes/blob/master/meetings/2019-01/jan-29.md#objectfromentries-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">January 2019</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-well-formed-stringify" target="_blank" rel="nofollow noopener noreferrer">Well-formed JSON.stringify</a></p>
<ul>
<li>作者：Richard Gibson</li>
<li>维护者：Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-01/jan-29.md#well-formed-jsonstringify-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">January 2019</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-string-left-right-trim" target="_blank" rel="nofollow noopener noreferrer">String.prototype.&#123;trimStart,trimEnd&#125;</a></p>
<ul>
<li>作者：Sebastian Markbåge</li>
<li>维护者：Sebastian Markbåge、Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-01/jan-29.md#stringprototypetrimstarttrimend-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">January 2019</a></li>
<li>发布时间：2019</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-flatMap" target="_blank" rel="nofollow noopener noreferrer">Array.prototype.&#123;flat,flatMap&#125;</a></p>
<ul>
<li>作者：Brian Terlson、Michael Ficarra、Mathias Bynens</li>
<li>维护者：Brian Terlson、Michael Ficarra</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-01/jan-29.md#arrayprototypeflatflatmap-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">January 2019</a></li>
<li>发布时间：2019</li>
</ul>
</li>
</ul>
<h3 data-id="heading-10">ES2020</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-string-matchall" target="_blank" rel="nofollow noopener noreferrer">String.prototype.matchAll</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-03/mar-26.md#stringprototypematchall-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">March 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-bigint" target="_blank" rel="nofollow noopener noreferrer">BigInt</a></p>
<ul>
<li>作者：Daniel Ehrenberg</li>
<li>维护者：Daniel Ehrenberg</li>
<li>TC39 会议记录：  <a href="https://github.com/tc39/notes/blob/master/meetings/2019-06/june-4.md#bigint-to-stage-4" target="_blank" rel="nofollow noopener noreferrer">June 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-promise-allSettled" target="_blank" rel="nofollow noopener noreferrer">Promise.allSettled</a></p>
<ul>
<li>作者：Jason Williams、Robert Pamely、Mathias Bynens</li>
<li>维护者：Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-07/july-24.md#promiseallsettled" target="_blank" rel="nofollow noopener noreferrer">July 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-global" target="_blank" rel="nofollow noopener noreferrer">globalThis</a></p>
<ul>
<li>作者：Jordan Harband</li>
<li>维护者：Jordan Harband</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-10/october-1.md#globalthis-to-stage-4" target="_blank" rel="nofollow noopener noreferrer">October 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-for-in-order" target="_blank" rel="nofollow noopener noreferrer">for-in mechanics</a></p>
<ul>
<li>作者：Kevin Gibbons</li>
<li>维护者：Kevin Gibbons</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-12/december-4.md#for-in-order-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">December 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-optional-chaining" target="_blank" rel="nofollow noopener noreferrer">Optional Chaining</a></p>
<ul>
<li>作者：Gabriel Isenberg、Claude Pache、Dustin Savery</li>
<li>维护者：Gabriel Isenberg、Dustin Savery、Justin Ridgewell、Daniel Rosenwasser</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2019-12/december-4.md#optional-chaining-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">December 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-nullish-coalescing" target="_blank" rel="nofollow noopener noreferrer">Nullish coalescing Operator</a></p>
<ul>
<li>作者：Gabriel Isenberg</li>
<li>维护者：Gabriel Isenberg、Justin Ridgewell、Daniel Rosenwasser</li>
<li>TC39 会议记录：<a href="https://github.com/tc39/notes/blob/master/meetings/2019-12/december-4.md#nullish-coalescing-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">December 2019</a></li>
<li>发布时间：2020</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-import-meta" target="_blank" rel="nofollow noopener noreferrer">import.meta</a></p>
<ul>
<li>作者：Domenic Denicola</li>
<li>维护者：Gus Caplan</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-03/april-1.md#importmeta-for-stage-4-continued-from-previous-day" target="_blank" rel="nofollow noopener noreferrer">March 2020</a></li>
<li>发布时间：2020</li>
</ul>
</li>
</ul>
<h3 data-id="heading-11">ES2021</h3>
<ul>
<li>
<p><a href="https://github.com/tc39/proposal-string-replaceall" target="_blank" rel="nofollow noopener noreferrer">String.prototype.replaceAll</a></p>
<ul>
<li>作者：Peter Marshall、Jakob Gruber、Mathias Bynens</li>
<li>维护者：Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-06/june-2.md#stringprototypereplaceall-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">June 2020</a></li>
<li>预计发布时间：2021</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-promise-any" target="_blank" rel="nofollow noopener noreferrer">Promise.any</a></p>
<ul>
<li>作者：Mathias Bynens、Kevin Gibbons、Sergey Rubanov</li>
<li>维护者：Mathias Bynens</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-07/july-21.md#promiseany--aggregateerror-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">July 2020</a></li>
<li>预计发布时间：2021</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-weakrefs" target="_blank" rel="nofollow noopener noreferrer">WeakRefs</a></p>
<ul>
<li>作者：Dean Tribble、Sathya Gunasekaran</li>
<li>维护者：Dean Tribble、Mark Miller、Till Schneidereit、Sathya Gunasekaran、Daniel Ehrenberg</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-07/july-21.md#weakrefs-for-stage-4--cleanupsome-for-stage-23" target="_blank" rel="nofollow noopener noreferrer">July 2020</a></li>
<li>预计发布时间：2021</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-logical-assignment" target="_blank" rel="nofollow noopener noreferrer">Logical Assignment Operators</a></p>
<ul>
<li>作者：Justin Ridgewell</li>
<li>维护者：Justin Ridgewell、Hemanth HM</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-07/july-21.md#logical-assignment-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">July 2020</a></li>
<li>预计发布时间：2021</li>
</ul>
</li>
<li>
<p><a href="https://github.com/tc39/proposal-numeric-separator" target="_blank" rel="nofollow noopener noreferrer">Numeric separators</a></p>
<ul>
<li>作者：Sam Goto、Rick Waldron</li>
<li>维护者：Sam Goto、Rick Waldron、Leo Balter</li>
<li>TC39 会议记录： <a href="https://github.com/tc39/notes/blob/master/meetings/2020-07/july-21.md#numericliteralseparator-for-stage-4" target="_blank" rel="nofollow noopener noreferrer">July 2020</a></li>
<li>预计发布时间：2021</li>
</ul>
</li>
</ul>
<h3 data-id="heading-12">ES2022</h3>
<ul>
<li>Class Fields ( <a href="https://github.com/tc39/proposal-private-methods" target="_blank" rel="nofollow noopener noreferrer">Private instance methods and accessors</a> ,  <a href="https://github.com/tc39/proposal-class-fields" target="_blank" rel="nofollow noopener noreferrer">Class Public Instance Fields & Private Instance Fields</a> ,  <a href="https://github.com/tc39/proposal-static-class-features" target="_blank" rel="nofollow noopener noreferrer">Static class fields and private static methods</a> )
<ul>
<li>作者：Daniel Ehrenberg</li>
<li>维护者：Daniel Ehrenberg、Kevin Gibbons</li>
<li>TC39 会议记录：April 2021</li>
<li>预计发布时间：2022</li>
</ul>
</li>
</ul>
<h2 data-id="heading-13">结语</h2>
<p><strong>授人以鱼，不如授人以渔</strong>，希望通过本文追根溯源，带领同学们走进 ECMAScript 的世界，ES 神秘代码不再神秘，ES 新特性不再彷徨。</p>
<p>我是清秋，一个有着教师梦的 Web 前端非典型程序员。公众号 <strong>Frontend Radio</strong> 刚刚起步，期待我的文章能够帮助到更多同学，让我们一起成长，早日成为 Frontend Master。</p>
<h2 data-id="heading-14">参考资料</h2>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/Ecma%E5%9B%BD%E9%99%85" target="_blank" rel="nofollow noopener noreferrer">Ecma国际 - 维基百科，自由的百科全书</a></li>
<li><a href="https://exploringjs.com/impatient-js/ch_history.html" target="_blank" rel="nofollow noopener noreferrer">History and evolution of JavaScript</a></li>
<li><a href="https://juejin.cn/post/6939061526154182686" target="_blank">【译】ECMAScript 2021: 最终功能集确定</a></li>
</ul></div>  
</div>
            