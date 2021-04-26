
---
title: 'JavaScript 的诞生'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1298'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 19:24:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=1298'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>1994年，网景公司（Netscape）发布了Navigator浏览器0.9版。这是历史上第一个比较成熟的网络浏览器，轰动一时。但是，这个版本的浏览器只能用来浏览，不具备与访问者互动的能力。网景公司急需一种网页脚本语言，使得浏览器可以与网页互动。</p>
<p>1995年4月，网景公司录用了34岁的系统程序员Brendan Eich。网景公司招聘他的目的，是研究将Scheme语言作为网页脚本语言的可能性。但同时期，网景公司与Sun公司结成联盟，考虑直接将Java作为脚本语言嵌入网页。</p>
<p>1995年5月，网景公司做出决策，未来的网页脚本语言必须"看上去与Java足够相似"，但是比Java简单，使得非专业的网页作者也能很快上手。这个决策实际上将Perl、Python、Tcl、Scheme等非面向对象编程的语言都排除在外了。Brendan Eich被指定为这种"简化版Java语言"的设计师。</p>
<h2 data-id="heading-1">早期</h2>
<p>Eich 创造了 Mocha，一种可以直接嵌入HTML文档并可以无需编译就被浏览器直接处理的语言。后改名为 LiveScript ，在 1995 年 9 月随 Netscape Navigator 2.0的 Beta 版发布，并在当年 12 月发布的Netscape Navigator 2.0 Beta 3 中更名为 JavaScript。</p>
<p>总的来说，他的设计思路是这样的：</p>
<ol>
<li>借鉴C语言的基本语法；</li>
<li>借鉴Java语言的数据类型和内存管理；</li>
<li>借鉴Scheme语言，将函数提升到"第一等公民"（first class）的地位；</li>
<li>借鉴Self语言，使用基于原型（prototype）的继承机制。</li>
</ol>
<p>所以，Javascript语言实际上是两种语言风格的混合产物 ——（简化的）函数式编程+（简化的）面向对象编程。这是由Brendan Eich（函数式编程）与网景公司（面向对象编程）共同决定的。</p>
<p>微软公司于同年(1995)年首次推出Internet Explorer，并根据 JavaScript 创造了 JScript ，从而引发了与网景公司的浏览器大战。</p>
<p>1996年11月，网景正式向ECMA（欧洲计算机制造商协会）提交语言标准。1997年6月，ECMA以JavaScript语言为基础制定了ECMAScript标准规范ECMA-262。JavaScript成为了ECMAScript最著名的实现之一。</p>
<p>但在21世纪初期，Netscape 的开发失去了活力，而 IE 持续改进，并获得了更大的市场份额。这个时期包括 Mozilla 和微软在内的厂商开始尝试推动并引领了标准化，另一方面浏览器的兼容性问题也大量显现。由此带来的后果就是，编写在不同浏览器下都能工作的脚本复杂而冗长，甚至很多情况下完全不可行。</p>
<p>事情在 2000 年后有了转机，并取得了一些幸运的进展，造成了JS的真正腾飞。众多成就中的一件事情就是由JS驱动的前端和后端服务器之间的异步通讯，包括最终被所有主流浏览器接受的 XMLHttpRequest (XHR)。其他还有稍后出现的一众开发框架，如 Prototype、 MooTools 以及不得不提的 jQuery。</p>
<h2 data-id="heading-2">jQuery时代</h2>
<p>处理跨多个浏览器的DOM访问是21世纪初web开发者主要面临的问题，但并非他们唯一关心的。诸如微软、谷歌和其他大公司等，作为早期的先锋，利用 AJAX 做出了大量激动人心的事情，但直到 2004 年发布的 Gmail，才真正点燃了 web 开发界。完全用全新的方式处理电子邮件：全部事情都在浏览器中进行，并把邮件储存在谷歌的服务器上，这意味着用户可以在世界各地任何支持互联网的设备上访问其邮件，也不用特别安装电子邮件应用程序。Gmail 用了一种很少被其他网站用到的 DHTML 和类 Ajax 的代码编写方式，并且还做到了其他开发者渴望的快速和易用，这些都导致了包括 jQuery 在内的框架的流行。</p>
<p>jQuery 聚焦于提供一个以基本的 JS 为基础的框架，短期内这种途径就被证明非常成功。jQuery确保了其在所有浏览器中都能工作，而工程师就不必花费精力又担惊受怕了，也不必花费同样多的时间造轮子了。简而言之， jQuery 和类似框架加速并简化了使用者的开发。</p>
<p>事情发展到某一天。随着网站变得越来越动态化，以及众多公司在缺乏谷歌那种级别的工程师团队的情况下，也以Gmail等为目标开始构建如此复杂的应用，麻烦就接踵而至了。由成千上万行 jQuery 代码组成的大量代码库变得难以维护，又包含了非常多的自定义函数，使得新上手的开发者头疼不已。如果网页上有5个可点击的元素，那就有5个 $('#myElement').click() 的实例要管理；如果有500个可点击的元素呢，麻烦就出现了；如果是5000个元素，可能噩梦就来临了。</p>
<p>需要做更多的事情了。JS框架开始进化，开始呈现明显的类似后端的特性和开发方法。单页应用时代已经到来。</p>
<h2 data-id="heading-3">单页应用时代</h2>
<p>在谷歌贡献了Chrome浏览器和 V8 JavaScript 渲染引擎后，为 Node.js 这类JS独立运行平台的出现创造了条件。在单页应用的世界里，情况没那么复杂了。因为疲于应付成千上万行 jQuery 代码造成的乱局，开发者们开始另寻他法。</p>
<p>Backbone.js 和 AngularJS ，开发者在2010年拥有了两个用来开发单页应用的完整工具箱，可以应对之前大规模 jQuery 开发中的短板，并继续用熟悉的方法开发。但它们都算不上小巧和快速(特别是在移动设备上)。</p>
<p>Facebook 在 2013 年发布了 React，一个小巧和极速渲染的前端框架。随后其又在 2014 年发布了其基于事件的应用管理和开发工具 Flux。这些产品以及围绕其成长的相关技术，再一次改变了 JS 应用开发。</p>
<h2 data-id="heading-4">现代</h2>
<p>在此期间，精心编写的智能化框架大量出现，更关注速度、易用和模块化，并回归原生JS。</p>
<p>在过去的几年，网页的访问方式发生了深刻的变化。曾经是家用 PC 独占的网站访问领域，现在变成了手机、平板电脑、笔记本电脑，以及台式机并存的情况。这些设备的带宽、处理器能力以及可用的屏幕分辨率各有不同。</p>
<p>所有这些框架都倾向于解决相同的问题：创建很多工具方便开发者快速构建，以使单页 web 应用能很好的工作于多种设备上。它们很注重数据流和显示：基本上，对于取得终端用户所需的显示数据，并在数据变化时自动更新显示这部分工作，减轻了开发者必须的工作量。</p>
<p>JS 生态系统繁荣而混乱。没人能预测前方的情况，持续生长的只有变化。web 裹足不前也就意味着 JS 的止步，大家也很期待未来的 5G 时代能带来什么。</p>
<hr>
<p>参考自：</p>
<ol>
<li><a href="http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html" target="_blank" rel="nofollow noopener noreferrer">Javascript诞生记</a></li>
<li><a href="https://zh.wikipedia.org/wiki/JavaScript#%E5%8E%86%E5%8F%B2" target="_blank" rel="nofollow noopener noreferrer">JavaScript</a></li>
<li><a href="https://cloud.tencent.com/developer/article/1644747?from=information.detail.js%20%E5%8F%91%E5%B1%95%E5%8F%B2%E6%97%B6%E9%97%B4%E8%BD%B4" target="_blank" rel="nofollow noopener noreferrer">[译]JS简史</a></li>
</ol></div>  
</div>
            