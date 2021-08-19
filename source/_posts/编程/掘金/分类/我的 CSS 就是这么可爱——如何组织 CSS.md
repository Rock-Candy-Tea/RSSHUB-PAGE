
---
title: '我的 CSS 就是这么可爱——如何组织 CSS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 17:51:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c76d4c01b6d4d439c34fdaf6c145e5a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>许浩星，微医前端技术部前端工程师。一个认为人生的乐趣一半在静，一半在动的有志青年！</p>
</blockquote>
<h2 data-id="heading-0">写在前面</h2>
<p>  开局先问大家一个问题：前端三剑客分别是谁？</p>
<p>  不用说，绝大部分前端开发都会脱口而出：HTML、CSS 和 JavaScript。要是这个还需要犹豫的话，朋友自己去墙角反省一下自己[手动狗头]。既然被称为三剑客，那么就意味着这三者在前端开发中起到了重要的作用。HTML 负责页面结构的搭建，CSS 负责页面的布局与美化，而 JS 负责的是赋予静态页面以动态的逻辑。从这个角度来看，这三者真的是缺一不可。但是随着业务需求的紧逼，我们往往做不到“雨露均沾”，有意无意得忽略了某个角色——CSS。</p>
<p>  就比如我自己，在日常的业务开发中，就经常将注意力放在了 HTML 结构和 JS 逻辑上，对于 CSS 就冷淡了很多。这样子造成的后果就是当页面的交互丰富、样式多样的时候，我们写的 CSS 代码行数多的吓人，而且再也不想再看第二遍。用高情商的话说就是，我们写的 CSS 代码让后续的开发者维护起来很有挑战性。</p>
<p>  静下心来，我仔细地剖析了一下原因，发现主要是因为样式代码的稳定性高。写完了一遍 CSS，以后基本不可能再要修改了。这种“一次性”很难不让人带着一点糊弄的“心态”去开发，然后留下一堆烂摊子给后面的同事骂人🤬。</p>
<p>  但是！天道好轮回！如果碰到了需要去修改别人写过的 CSS 样式，那么这就是噩梦👿。很难不让人改的怀疑人生，最后选择重写一遍（呜呜呜，别骂了，别骂了）！在碰到过这种情况后，我意识到我们需要从一个整体的角度来指导 CSS 书写，从而让样式文件变得更加美丽！这也是我写这篇文章的初衷。</p>
<h2 data-id="heading-1">一、CSS 与审美</h2>
<p>  审美是主观的，它受到各方面因素的影响，例如文化背景，知识体系和性格爱好等等。我们作为前端开发，在编程这个领域内更是经常与审美打交道。有时候我们经常说某某代码写的垃圾，看半天也看不懂。某某大佬代码写的强无敌，条理清晰和逻辑完备。这些对于代码的评价就是我们对于审美认知的体现。</p>
<p>  CSS 的存在就是赋予页面美丽，如下面动图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd6a5abe4edf42cf9a19a9bb34905407~tplv-k3u1fbpfcp-watermark.image" alt="CSS 的美化作用" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  上面的动图我想每一位用户都更喜欢加了 CSS 文件之后的页面吧，因为符合人的审美。</p>
<p>  既然 CSS 能够让页面更加漂亮，那么对于 CSS 本身，我们更应该让它美起来！</p>
<h2 data-id="heading-2">二、什么样的 CSS 是受人喜欢的？</h2>
<p>  前面我们已经找到了我们的目的：让 CSS 更加好看！那么好看的目的是什么呢？是让人喜欢。让我们在需求开发时不抗拒去修改原有的代码。那么这就引出了一个问题：什么样的代码让人抗拒去修改？我们看看下面的两种 CSS 代码：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/450e39f3e180400fbac80722e7d5dd16~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>  我个人来说，第一眼看上去，左边的代码“挤”在一起，显得乱糟糟的。而右边的代码更为清晰，每块之间还有空行，让人感觉更为舒服。那么问题来了，为什么右边的代码会让我看上去舒服点？我在仔细比较这两块代码的区别之后，我找到了答案：</p>
<ol>
<li>每块代码之间间隔有序，不至于给人一个无比庞大的概念。</li>
<li>层级控制不超过 3 层，避免了过多嵌套层级“恶心”人</li>
<li>遵循了 BEM 命名规范，潜在的传递了关于元素之间的层级关系</li>
</ol>
<p>  总结起来就是：<strong>将代码的逻辑关注点分割个多个开发者可以轻易消化的小块，同时做到一定意义的自解释</strong>。这样的处理减少了人脑需要处理这些代码逻辑的难度，自然会给人舒服的感觉！</p>
<p>​  那么我们下面思考的更加深入点，抽象出 CSS 的书写原则。</p>
<h2 data-id="heading-3">三、CSS 的一些书写原则</h2>
<p>  CSS 本身是没有什么内置的组织方式的，并且有各种书写的方式，例如：内联和外链等等。所以我们需要自己完成建立编写 CSS 时维持统一性和规则性的工作。Web 社区也已经存在了多种工具和方法，来帮助开发者管理大的 CSS 项目。我们可以借鉴并调整为适合我们自己的书写方式。但在这之前，我们需要明确几个 CSS 书写原则。</p>
<blockquote>
<ol>
<li>少即是多</li>
<li>自解释</li>
<li>可复用</li>
</ol>
</blockquote>
<p>  上面 3 条原则是我在开发过程中自己总结出来的，如果大家有更多的想法💡，欢迎和我一起探讨。先说说第一条原则：少即是多（Less is more）。这句话的英文版本是建筑师凡德罗在建筑领域提出的观点。他反对机械化生产的产品中存在的繁复的无意义的装饰。这同样也适用于 CSS 的编写中。在前端三剑客中，HTML 是结构，JS 是行为，CSS 则是表现。换句话说，CSS 的作用是装饰页面。在这个前提下，去除那些冗余繁复的 CSS 代码不仅能减小浏览器的性能消耗，还能让开发者更加深入的思考表现与结构之间的关系。我认为这对于前端开发工程师的思维成长是有帮助的。</p>
<pre><code class="hljs language-css copyable" lang="css">// 存在多余的代码
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">20px</span>;
&#125;

// 优化
<span class="hljs-selector-class">.footer</span> &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">30px</span> <span class="hljs-number">0</span> <span class="hljs-number">20px</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  上面的代码就是最简单的少即是多的实践，但不仅限于此。<strong>我们更需要从整体上进行思考与实践</strong>。那么如何做到这一点呢？无它，惟手熟尔。所以每次开发中，都要记住我们的口号：“绝不多写一行 CSS！”。</p>
<p>  第 2 条原则自解释的意思是 CSS 的书写要尽量说明自己是干什么的，减少额外的注释代码。</p>
<pre><code class="hljs language-css copyable" lang="css">// 存在模糊地方
<span class="hljs-selector-class">.footer</span><span class="hljs-selector-pseudo">:first</span>-child &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
&#125;

// <span class="hljs-selector-class">.footer-title</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">18px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  上面的代码解释了这个元素的目的，是 footer 部分中关于 title 的文本。这样可以让我们很容易定位到对应的 html 元素，从而进行样式的修改。对于这条原则的实现，社区已经有了一套很完善的方案：BEM 命名。这套规范即避免了不同文件下的命名冲突，还很好的赋予了 CSS 类名的语义化。让我们的脑子对于 CSS 那种模糊的印象变得条理清晰。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><div class="person-center__wrap">
<div class="person-center__main">
    <div class="userInfo-name">
      王狗蛋
    </div>
    <div class="userinfo-age">
      24
    </div>
  </div>
  <div class="person-center__footer">
    <div class="sctions-comfirm">
      确定
    </div>
  </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  上面这段代码就较好的使用 BEM 命名将额外的页面结构信息塞到了 CSS 类名上了，让开发者不至于摸不清 CSS 的对应 DOM 结构。再配上预处理语言 SASS 等，更加从心智上将消除了 CSS 的信息缺少与模糊性，保证了页面结构、表现和行为的统一性。</p>
<p>  最后一条可复用的原则就不多说了，懂得都懂。这条原则的基础是 CSS 预处理语言的使用。因为 CSS 本身是一种描述语言，本身是没有逻辑的。但是随着业务的越来越复杂，我们渴望将逻辑代码加入 CSS 中。这也是 SASS 预处理语言兴起的原因之一。加入逻辑的 CSS 预处理语言中，我们可以定义变量、使用循环和条件判断，从而复用 CSS 代码。</p>
<h2 data-id="heading-4">四、保持 CSS 整洁的技巧</h2>
<p>  在了解了书写 CSS 的原则之后，我们还需要在实践中运用它们。在这个过程，一些保持 CSS 整洁的技巧对我们实践是很有帮助的。</p>
<h4 data-id="heading-5">1. 确定项目的代码规范</h4>
<p>  在和多人进行项目的开发时，第一时间需要检查该项目是否有了 CSS 的代码规范。遵循项目的代码规范进行开发，是保持 CSS 整洁的基础，也是不让别人吐槽的护盾。如果你的个人喜好跟规范相冲突，那么还是请遵守规范，因为别人或许不喜欢你的风格。</p>
<h4 data-id="heading-6">2. 保持统一</h4>
<p>  当你开始进行需求开发并书写 CSS 代码时，最重要的是保持各方面的统一。例如之前的代码使用的是 rem 单位，并且在代码开头进行了换算和变量定义。那么你需要做的就是跟随！！而不是标新立异的使用另一套自己的方式。</p>
<p>  统一在所有的地方都会起到实际作用，例如对类使用<strong>相同的命名常规</strong>，<strong>选择一种描述颜色的方式</strong>，或者<strong>维护一个统一的格式化方式</strong>（例如你是使用 Tab 还是空格来缩进代码？如果是代码，用多少个？）</p>
<p>  一直遵守一系列规则，你会在编写 CSS 的时候省去不少精神上的预负担，因为一些决定已经定型了。要知道代码是写给人看的，顺带着可以在机器上运行。在这里给我们团队的开发规范打个广告：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDUVpsV3ZPZlZmbHZE" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.qq.com/doc/DUVpsV3ZPZlZmbHZE" ref="nofollow noopener noreferrer">微医前端开发手册 1.1（修订中）</a>，欢迎大家提出意见，共同进步。</p>
<h4 data-id="heading-7">3. 将 CSS 格式化成可读的形式</h4>
<p>  你可以看到很多 CSS 格式化的方式，一些开发者将所有的规则放在一行里面，像是这样：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123; <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#567895</span>; &#125;
<span class="hljs-selector-tag">h2</span> &#123; <span class="hljs-attribute">background-color</span>: black; <span class="hljs-attribute">color</span>: white; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  还有的开发者更喜欢将所有的东西放在新的一行，并且不同元素之间空行：</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-class">.person-center</span> &#123;
  <span class="hljs-selector-tag">&</span><span class="hljs-selector-tag">-wrap</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  &#125;
  
  <span class="hljs-selector-tag">&</span><span class="hljs-selector-tag">-main</span> &#123;
<span class="hljs-attribute">color</span>: <span class="hljs-number">#FFF</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    <span class="hljs-attribute">font-weight</span>: <span class="hljs-number">500</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  CSS 不会管你使用哪种方式来进行格式化，我的看法是在遵循代码规范的前提下让 CSS 代码更加具有可读性。保证了你自己还愿意下次看，才能保证其他开发者能够看的下去你的代码。</p>
<h4 data-id="heading-8">4. 为你的 CSS 加上注释</h4>
<p>  代码自解释为前提，但是在某些定制需求时需要加上注释，表明相关业务背景和其他信息。这样做不仅可以帮任何未来的开发者处理你的 CSS 文件，也可以在你离开项目一段时间后，帮你在回来时重新上手。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 这是一条 CSS 注释，
它可以分成好几行。*/</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>  在你的样式表里面的逻辑段落之间，加入一块注释，是个好技巧。在你快速掠过的时候，这些注释可以帮你快速定位不同的段落，甚至给了你搜索或者跳转到那段 CSS 的关键词。如果你使用了一个不存在于代码里面的字符串，你可以从段落到段落间跳转，只需要搜索一下，下面我们用的是<code>||</code>。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* || General styles */</span>

...

<span class="hljs-comment">/* || Typography */</span>

...

<span class="hljs-comment">/* || Header and Main Navigation */</span>

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  或许你是照着一个社区教程来做事的，CSS 有些不够直观。此时，你应该在注释里面加入教程的 URL。你应该在你一年或者更长时间以后重新审视你的项目，但只是模模糊糊地想起来之前有个优秀的教程，不知道它在哪里的时候，感谢之前加入注释的自己。</p>
<h4 data-id="heading-9">5. 在你的样式表里面加上逻辑段落</h4>
<p>  在样式表里面先给一般的东西加上样式是个好想法。这也就是除了你想特定对某个元素做点什么以外，所有将会广泛生效的样式。典型地，你可以为以下的元素设定规则：</p>
<ul>
<li>body</li>
<li>p</li>
<li>h1, h2, h3, h4, h5</li>
<li>ul 和 ol</li>
<li>table 属性</li>
<li>链接</li>
</ul>
<p>  在这段样式表里面，我们提供了用于站点类型的<strong>默认样式</strong>，为数据表格、列表等设立了一份默认的样式。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* || GENERAL STYLES */</span>

<span class="hljs-selector-tag">body</span> &#123; ... &#125;

<span class="hljs-selector-tag">h1</span>, <span class="hljs-selector-tag">h2</span>, <span class="hljs-selector-tag">h3</span>, <span class="hljs-selector-tag">h4</span> &#123; ... &#125;

<span class="hljs-selector-tag">ul</span> &#123; ... &#125;

<span class="hljs-selector-tag">blockquote</span> &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  在这段之后，我们可以定义一些实用类，例如一个用来<strong>移除默认列表样式的类</strong>，我们打算将其展示为灵活样式或者其他样式。如果你知道你想要在许多不同的元素上应用的东西，那么你可以把它们加到这里。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* || UTILITIES */</span>

<span class="hljs-selector-class">.nobullets</span> &#123;
  <span class="hljs-attribute">list-style</span>: none;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;

...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  然后我们可以加上在<strong>整个站点都会用到的所有东西</strong>，这可能是像基础页面布局、抬头或者导航栏样式之类的东西。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* || SITEWIDE */</span>

<span class="hljs-selector-class">.main-nav</span> &#123; ... &#125;

<span class="hljs-selector-class">.logo</span> &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  最后我们可以在 CSS 里面加上特指的东西，将它们分成上下文、页面甚至它们使用的组件。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* || STORE PAGES */</span>

<span class="hljs-selector-class">.product-listing</span> &#123; ... &#125;

<span class="hljs-selector-class">.product-box</span> &#123; ... &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  通过使用这种方式排布代码，我们至少能大致了解，我们能在样式表的哪个部分寻找想要更改的东西。</p>
<h4 data-id="heading-10">6. 避免太特定的选择器</h4>
<p>  如果你创建了很特定的选择器，你经常会发现，你需要在你的 CSS 中复用一块代码，以将同样的规则应用到其他元素上。例如，你也许会有像是下面的选择器那样的代码，它在带有<code>main</code>类的<code><article></code>里面的带有<code>box</code>类的<code><p></code>上应用了规则。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">article</span><span class="hljs-selector-class">.main</span> <span class="hljs-selector-tag">p</span><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  如果你之后想要在<code>main</code>外的什么地方上应用相同的规则，或者在<code><p></code>外的其他地方，你可能必须在这些规则中加入另一个选择器，或者直接新建个规则。或者，你也可以建立一个名为<code>box</code>的类，在任何地方应用。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.box</span> &#123;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#ccc</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>  将东西设置的更为特定，有时也有意义，但是这一般与其说是通常实践，倒不如说是例外。</p>
<h4 data-id="heading-11">7. 分割大样式表为多个小样式表</h4>
<p>  这个技巧可以说是我们已经做到很好了。一般项目中都会有一个 <code>styles</code>，里面存储一些全局共用的样式文件。根据这些文件的作用，一般又会被细分为<code>reset.csss</code>、<code>variables.less</code>等文件。搭配上预处理语言的 mixin 功能，我们就可以维护一份常用的样式文件，避免在具体的页面书写冗杂的 CSS 代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce6db56fac4d4968a5c4a892baa1dbeb~tplv-k3u1fbpfcp-watermark.image" alt="styles" loading="lazy" referrerpolicy="no-referrer"></p>
<p>  这可以让你更容易保持 CSS 的组织性，也意味着如果有多人在写 CSS，你会更少遇到有两个人需要同时编写相同的样式表的情况，防止在源代码的控制上产生冲突。</p>
<h4 data-id="heading-12">8.善用工具</h4>
<p>  人区别于大猩猩的一处就是善于使用工具解决我们遇到的困难。身处于互联网的浪潮中，我们更应该拥抱那些有帮助的工具🔧。使用 stylelint + githook 来规范我们的 CSS 代码，使用 Less/Sass 预处理语言让 CSS 更加有“逻辑”  。它们解放了我们的大脑，也在潜移默化中培养我们的编码规范。</p>
<h4 data-id="heading-13">9. 学习与模仿</h4>
<p>  没有人是完美的，人的一个优势就是可以通过学习来提升自己。那么我们作为程序员，更需要与厉害的同行交流经验，学习别人好的编码规范融入自己的日常开发中。每个人都是独立的个体，每个人也都有着自己的想法，身处于这行，开放思想，用于承认自己的不足，才是能够永远进步的源泉！！</p>
<p>  这包括了线下团队之间开展专题讨论和线上参与社区讨论等等措施，多与人沟通才能开拓我们的技术视野。</p>
<h2 data-id="heading-14">五、写代码是与自己的对话</h2>
<p>  原谅我在最后的小结起了一个很文艺的标题。我最近在看一部蛮老的日剧：《龙樱》，剧中男主阿部宽跟备考东大的几个“笨蛋”说考试是一场与自己的对话，也是一场与竞争对手的对话。</p>
<p>  走上职场的我们，无论是初入职场的激情满满还是磨练了几年后的波动如山，限制着影响着我们的只有自己。但是信息茧房不仅封闭了我们对外界的认知，更剥夺了我们对自己的认知。</p>
<p>  将时间尺度拉到，拉到 1 年、3 年、5 年乃至 10 年。你写的代码作为时间的锚点一直存在于那里，这又不是一种另类的未来与现在的对话吗？所以如何组织 CSS 呢？第一原则就是当成与自己的对话，做到你不嫌弃自己。在这基础上，掌握并找到适合自己的编码原则，使用规范和工具来纠正监督自己，剩下的就是实践 => 修改 => 再实践 => 再修改的无限循环。</p>
<p>  整洁的代码是由整洁的人写出来的，写出可爱的代码也一定是个可爱的人。我最开始写代码的理想的想通过虚拟世界来帮助我理解现实世界的复杂性。我们在将复杂、错乱的 CSS 代码进化为整洁、逻辑关注点清晰的代码。这一过程同时也是一场与自己的对话，问自己喜欢什么，问自己想要什么。在这种潜意识的一个个疑问中，我们整理着内心。</p>
<p>  我们在 0 和 1 的世界里，思考着物理世界的喜怒哀乐，希望朋友们能够撇去浮燥世界带来的浮沫，都能找到生活的真谛！毕竟努力工作只是手段，我们的目标是未来的幸福快乐生活！诸君共勉！</p>
<hr>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwy.guahao.com%2F%3F_channel%3Dinfluence" target="_blank" rel="nofollow noopener noreferrer" title="https://wy.guahao.com/?_channel=influence" ref="nofollow noopener noreferrer">前往微医互联网医院在线诊疗平台，快速问诊，3分钟为你找到三甲医生。</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwy.guahao.com%2F%3F_channel%3Dinfluence" target="_blank" rel="nofollow noopener noreferrer" title="https://wy.guahao.com/?_channel=influence" ref="nofollow noopener noreferrer"><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2b31f455723404b8394538bd4b0b35b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/554f3134d8b84e62afdacc1c9252289a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            