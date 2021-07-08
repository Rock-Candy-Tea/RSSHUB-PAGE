
---
title: '这篇鸟文，助你彻底玩透执行上下文、调用栈、作用域、变量提升、this值、闭包等王者技能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2740aa1534b54ad19f60b2ec4aa10a39~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 23:03:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2740aa1534b54ad19f60b2ec4aa10a39~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">这篇鸟文，助你彻底玩透执行上下文、调用栈、作用域、变量提升、this值、闭包等王者技能</h1>
<h2 data-id="heading-1">1、执行上下文</h2>
<h3 data-id="heading-2">1、为什么要有执行上下文</h3>
<p>大家平时写项目的时候，肯定是一个文件一个文件去写；具体到每一个文件里，又会细分出不同的方法、模块 ——我想应该不会有同学会把成千上万行的庞大的代码逻辑塞进一个文件里。当大家这样做的时候，其实已经在践行一种软件世界里非常重要的思想 ——  分治。
困难只能吓倒懦夫懒汉，而胜利永远属于敢于攀登科学高峰的人。 —— 茅以升
分治是编写软件的一种策略，它意味着你会把一个庞大的问题拆分成若干个具体的小问题，然后逐个去解决它们，
以此来化解问题的复杂度。表现在代码上，就是把庞大的逻辑拆分成独立的代码块。这些 “ 代码块 ”  根据粒度的不同，有着不同的名字，它可以是函数、模块、包等等等等。
如果说把代码逻辑划分成 “ 块 ” ，是我们程序员在编写阶段的智慧。那么把庞大的执行任务划分成不同的执行上下文，就是 JS  引擎在执行阶段的智慧了。
我们可以把执行上下文理解为引擎在执行过程中对代码进行了又一次的 “ 划分 ” ，这样做的目的，仍然是为了分解复杂度。</p>
<h3 data-id="heading-3">2、执行上下文是什么</h3>
<blockquote>
<p>JavaScript标准把一段代码（包括函数）执行所需的所有信息定义为“执行上下文”（可理解为当前代码的执行环境，同一个函数在不同的环境中执行，会因访问的数据不同产生不一样的结果），其是执行的基础设施。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2740aa1534b54ad19f60b2ec4aa10a39~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行上下文在不同的版本中定义不同，《重学前端》中对此进行了总结，目前主要有三个版本：</p>
<p>大部分同学，看的应该都是ES3版本的，有作用域链，活跃变量对象这些的解释，没关系，看了这些内容的同学，淡定，这些不代表就是错误的，就是版本问题而已。</p>
<p>如果有朋友还想详细了解这个版本解释的话，我给推荐一个超级好博客，一定可以帮助到你。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fcavszhouyou.top%2FJavaScript%25E6%25B7%25B1%25E5%2585%25A5%25E7%2590%2586%25E8%25A7%25A3%25E4%25B9%258B%25E4%25BD%259C%25E7%2594%25A8%25E5%259F%259F%25E9%2593%25BE.html%25EF%25BC%2588%25E5%25B9%25B3%25E6%2597%25B6%25E6%2588%2591%25E9%2583%25BD%25E4%25B8%258D%25E8%2588%258D%25E5%25BE%2597%25E6%2594%25BE%25E5%2587%25BA%25E6%259D%25A5%25EF%25BC%258C%25E6%2588%2591%25E6%2580%2595%25E4%25BD%25A0%25E4%25BB%25AC%25E5%25AD%25A6%25E5%258E%25BB%25E4%25BA%2586%25EF%25BC%258C%25E5%258D%25B7%25E7%259A%2584%25E6%2588%2591%25E5%25A4%25B1%25E4%25B8%259A%25E5%2595%25A6%25EF%25BC%258C%25E5%2593%2588%25E5%2593%2588%25E5%2593%2588%25EF%25BC%258C%25E5%25BC%2580%25E4%25B8%25AA%25E7%258E%25A9%25E7%25AC%2591%25E3%2580%2582%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="http://cavszhouyou.top/JavaScript%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%E4%B9%8B%E4%BD%9C%E7%94%A8%E5%9F%9F%E9%93%BE.html%EF%BC%88%E5%B9%B3%E6%97%B6%E6%88%91%E9%83%BD%E4%B8%8D%E8%88%8D%E5%BE%97%E6%94%BE%E5%87%BA%E6%9D%A5%EF%BC%8C%E6%88%91%E6%80%95%E4%BD%A0%E4%BB%AC%E5%AD%A6%E5%8E%BB%E4%BA%86%EF%BC%8C%E5%8D%B7%E7%9A%84%E6%88%91%E5%A4%B1%E4%B8%9A%E5%95%A6%EF%BC%8C%E5%93%88%E5%93%88%E5%93%88%EF%BC%8C%E5%BC%80%E4%B8%AA%E7%8E%A9%E7%AC%91%E3%80%82%EF%BC%89" ref="nofollow noopener noreferrer">cavszhouyou.top/JavaScript%…</a></p>
<blockquote>
<p>1、执行上下文在ES3中，包含三个部分。
scope：作用域，也常常被叫做作用域链。
variable object：变量对象，用于存储变量的对象。
this value：this值。</p>
</blockquote>
<blockquote>
<p>2、在ES5中，我们改进了命名方式，把执行上下文最初的三个部分改为下面这个样子。
lexical environment：词法环境，当获取变量时使用。（通过let、const、with（）、try-catch创建的变量存在词法环境中）
variable environment：变量环境，当声明变量时使用。（通过var声明或function（）&#123;&#125;声明的变量存在变量环境中）
this value：this值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8baafbbfdd394688a81a4d0d4c05ee99~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<blockquote>
<p>3、在ES2018中，执行上下文又变成了这个样子，this值被归入lexical environment，但是增加了不少内容。
lexical environment：词法环境，当获取变量或者this值时使用。
variable environment：变量环境，当声明变量时使用
code evaluation state：用于恢复代码执行位置。
Function：执行的任务是函数时使用，表示正在被执行的函数。
ScriptOrModule：执行的任务是脚本或者模块时使用，表示正在被执行的代码。
Realm：使用的基础库和内置对象实例。
Generator：仅生成器上下文有这个属性，表示当前生成器。</p>
</blockquote>
<p>在这里，我用ES5版本的给大家介绍，当然啦，作用域这些也会给大家解释的，不用太纠结执行上下文到底是个啥，死扣概念（说实话，我学的时候就死扣这个字眼啦，搞的我很难受，那个时候)，请继续往下看。</p>
<p><strong>注意点：</strong></p>
<p>1、其实在每个执行上下文的变量环境中，都包含了一个外部引用outer，用来指向外部的执行上下
文，我们把这个外部引用称为outer，这个跟作用域链有关系，后需会详细讲解。</p>
<h3 data-id="heading-4">3、执行上下文的分类</h3>
<p><strong>执行上下文主要分为三类：全局执行上下文、函数执行上下文、eval函数执行上下文。</strong></p>
<blockquote>
<p>1、全局执行上下文：
当JavaScript执行全局代码的时候，会编译全局代码并创建全局执行上下文，而且在整个页面的生存周期内，全局执行上下文只有一份。</p>
</blockquote>
<blockquote>
<p>2、函数执行上下文：
只有当调用一个函数的时候，函数体内的代码会被编译，并创建函数执行上下文，一般情况下，函数执行结束之后，创建的函数执行上下文会被销毁。需要注意的是，同一个函数被多次调用，都会创建一个新的上下文。具体的在后面调用栈部分还会详解。</p>
</blockquote>
<blockquote>
<p>3、eval执行上下文：
当使用eval函数的时候，eval代码也会被编译，并创建执行上下文。（可以忽略）</p>
</blockquote>
<h3 data-id="heading-5">4、执行上下文生命周期</h3>
<h4 data-id="heading-6">1、全局上下文</h4>
<p>执行上下文创建分为创建阶段与执行阶段两个阶段，较为难理解应该是创建阶段，我们先说创建阶段。</p>
<p><strong>1、创建阶段</strong></p>
<blockquote>
<p>JS执行上下文的创建阶段主要负责三件事：确定this---创建词法环境组件（LexicalEnvironment）---创建变量环境组件（VariableEnvironment）。如果你有阅读其它关于执行上下文的文章读到这里一定有疑问，执行上下文创建过程不是应该解释this，作用域与变量对象/活动对象才对吗，怎么跟别的地方说的不一样，这里我最后再提醒一次哈，这是ES3版本这样子定义的，这篇文章呢，主要是按ES5版本进行讲解，后面我就不继续解释这个问题喽，如果你想继续了解此版本内容，再给你推荐一个文章（长期关注的一个大佬）：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMjExNzQxMQ%3D%3D%26mid%3D2247485068%26idx%3D1%26sn%3D8a58365c6edc28408ceaf507564cdcc2%26chksm%3D974bb440a03c3d56ee0e5498035006fd9d2a66e77dd88087d85991f802fccd087af587ef8cd2%26mpshare%3D1%26scene%3D1%26srcid%3D0527VffST2KOz7xQlsxNJ8aA%26sharer_sharetime%3D1622072938011%26sharer_shareid%3Dbf7a7143f255060150499be3bd42eb7d%26version%3D3.1.8.3015%26platform%3Dwin%23rd%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzIxMjExNzQxMQ==&mid=2247485068&idx=1&sn=8a58365c6edc28408ceaf507564cdcc2&chksm=974bb440a03c3d56ee0e5498035006fd9d2a66e77dd88087d85991f802fccd087af587ef8cd2&mpshare=1&scene=1&srcid=0527VffST2KOz7xQlsxNJ8aA&sharer_sharetime=1622072938011&sharer_shareid=bf7a7143f255060150499be3bd42eb7d&version=3.1.8.3015&platform=win#rd%E3%80%82" ref="nofollow noopener noreferrer">mp.weixin.qq.com/s?__biz=MzI…</a></p>
</blockquote>
<p><strong>补充解释：</strong></p>
<blockquote>
<p>词法环境是一个包含标识符变量映射的结构，这里的标识符表示变量/函数的名称，变量是对实际对象【包括函数类型对象】或原始值的引用。
变量环境可以说也是词法环境，它具备词法环境所有属性，一样有环境记录与外部环境引入。在ES6中唯一的区别在于词法环境用于存储函数声明与let const声明的变量，而变量环境仅仅存储var声明的变量。</p>
</blockquote>
<p><strong>2、代码执行阶段</strong></p>
<p>​<strong>1、创建阶段</strong></p>
<blockquote>
<p>​创建全局对象（ Window  有了）
​创建 this  ，并让它指向全局对象
​给变量和函数安排内存空间
​默认给变量赋值为 undefined ；将函数声明放入内存
​创建作用域链</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59cdb40356c949319cc95d96d987ed5a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中你也可以看出，变量 a、函数 add 和 addAll 都保存到了全局上下文的变量环境对象中。</p>
<p>或者案例2：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92fa1060a04f463786168cd713859c2f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意点：</strong></p>
<blockquote>
<p>1、在执行上下文创建阶段，函数声明与var声明的变量在创建阶段已经被赋予了一个值，var声明被设置为了undefined，函数被设置为了自身函数，而let const被设置为未初始化。</p>
</blockquote>
<blockquote>
<p>现在你总知道变量提升与函数声明提前是怎么回事了吧，以及为什么let const为什么有暂时性死域，这是因为作用域创建阶段JS引擎对两者初始化赋值不同。</p>
</blockquote>
<p>2、let、const</p>
<p>`let myname= '极客时间'</p>
<p>&#123;</p>
<p>console.log(myname) let myname= '极客邦</p>
<p>'&#125;`</p>
<p>VM171:5 Uncaught SyntaxError: Unexpected identifier</p>
<p>在块作用域内，let声明的变量被提升，但变量只是创建被提升，初始化并没有被提升，在初始化之前使用变量，就会形成一个暂时性死区。
<strong>【拓展】</strong></p>
<blockquote>
<p>var的创建和初始化被提升，赋值不会被提升。
let的创建被提升，初始化和赋值不会被提升。
function的创建、初始化和赋值均会被提升。</p>
</blockquote>
<p><strong>2、可执行代码执行阶段</strong></p>
<p>执行全局上下文中的代码：</p>
<p>代码执行时根据之前的环境记录对应赋值，比如早期var在创建阶段为undefined，如果有值就对应赋值，像let const值为未初始化，如果有值就赋值，无值则赋予undefined。</p>
<pre><code class="copyable">var name = 'xiuyan'
var tel = '123456'
function getMe() &#123;
return &#123;
name: name,
tel: tel
&#125;
&#125;
//  增加了函数调用
getMe()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6efd72b37314a288c33eb0e7e3d2cb7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b6ccb62d0d492cb86be49aa11866b5~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>全局上下文执行流程：</strong></p>
<pre><code class="copyable">var name = 'xiuyan'
var tel = '123456'
function getMe() &#123;
return &#123;
name: name,
tel: tel
&#125;
&#125;
//  增加了函数调用
getMe()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32ca6c923d7d446f9e71df906e5076c7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">2、变量提升(补充说明)</h4>
<p>在执行上下文创建阶段，函数声明与var声明的变量在创建阶段已经被赋予了一个值，var声明被设置为了undefined，函数被设置为了自身函数，而let const被设置为未初始化。</p>
<p>现在你总知道变量提升与函数声明提前是怎么回事了吧，以及为什么let const为什么有暂时性死域，这是因为作用域创建阶段JS引擎对两者初始化赋值不同。</p>
<pre><code class="copyable">showName()
console.log(myname)   ----打印结果是undefined
var myname = '极客时间'
function showName() &#123;
console.log('函数 showName 被执行');
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">let myname= '极客时间'
&#123;
  console.log(myname) 
  let myname= '极客邦'
&#125;
VM232:4 Uncaught ReferenceError: Cannot access 'myname' before initialization
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>var的创建和初始化被提升，赋值不会被提升。
let的创建被提升，初始化和赋值不会被提升。
function的创建、初始化和赋值均会被提升。</p>
</blockquote>
<p>注意点：</p>
<p>下面是关于同名变量和函数的两点处理原则：
1:如果是同名的函数，JavaScript编译阶段会选择最后声明的那个。
2:如果变量和函数同名，那么在编译阶段，变量的声明会被忽略</p>
<h4 data-id="heading-8">3、函数上下文</h4>
<p>在全局上下文中，当执行到函数调用时候，会创建函数上下文</p>
<p>案例1：</p>
<pre><code class="copyable">var name = 'xiuyan'
var tel = '123456'
function getMe() &#123;
return &#123;
name: name,
tel: tel
&#125;
&#125;
//  增加了函数调用
getMe()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当引擎执行到 getMe ()  调用这一行时，首先会进入函数上下文的创建阶段，在这个阶段里，函数上下文的内容如
下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/102a15a0c6984233b53c89db15134774~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>案例2：</p>
<pre><code class="copyable">var a = 2
function add(b,c)&#123;
return b+c
&#125;
function addAll(b,c)&#123;
var d = 10
result = add(b,c)
return a+result+d
&#125;
addAll(3,6)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引擎执行到 addAll(3,6)  调用这一行时，首先会进入函数上下文的创建阶段，在这个阶段里，函数上下文的内容如
下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49363a8b60054ceebea1e5babdfeee0a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>引擎执行到 add(b,c)  调用这一行时，首先会进入函数上下文的创建阶段，在这个阶段里，函数上下文的内容如
下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91fa1ccb21dd4356827dbd795e4bc4e1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">2、调用栈（执行上下文栈）</h2>
<p>学完全局作用域跟函数作用域，大家应该也清楚啦，上下文是有先后顺序的。</p>
<p>在一个JavaScript程序中，如果产生多个执行上下文，JavaScript引擎会以栈的方式来处理它们，这个栈，我们称其为函数调用栈(call stack)。栈底永远都是全局上下文，而栈顶就是当前正在执行的上下文。</p>
<blockquote>
<p>我们看到函数执行完毕后，其对应的执行上下文也随之消失了。这个消失的过程，我们叫它 ”  出栈 “——  没错，在JS  代码的执行过程中，引擎会为我们创建 ”  执行上下文栈 “ （也叫调用栈）。
因为函数上下文可以有许多个，我们不可能保留所有的上下文。当一个函数执行完毕，其对应的上下文必须让出之前所占用的资源。因此上下文的建立和销毁，就对应了一个 ”  入栈 “ 和 ”  出栈 “ 的操作。当我们调用一个函数的时候，就会把它的上下文推入调用栈里，执行完毕后出栈，随后再为新的函数进行入栈操作。</p>
</blockquote>
<p>函数上下文执行流程：</p>
<p>案例：</p>
<pre><code class="copyable">var color = 'blue';

function changeColor() &#123;
    var anotherColor = 'red';

    function swapColors() &#123;
        var tempColor = anotherColor;
        anotherColor = color;
        color = tempColor;
    &#125;

    swapColors();
&#125;

changeColor();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/839258d8b3cd46ddbfe1ec115d007e05~tplv-k3u1fbpfcp-zoom-1.image" alt="preview" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>参考文章：</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000012646203" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000012646203" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
<p><strong>总结：</strong></p>
<p>每调用一个函数，JavaScript 引擎会为其创建执行上下文，并把该执行上下文压入调用栈，然后 JavaScript 引擎开始执行函数代码。</p>
<p>如果在一个函数A中调用啦另外一个函数B，那么JavaScript引擎会为B函数创建执行上下文，并将B函数的执行上下文压入栈顶。</p>
<p>当前函数执行完毕后，JavaScript引擎会将该函数的执行上下文弹出栈。</p>
<p>当分配的调用栈空间被占满时，会引发“栈堆溢出”问题。</p>
<p>栈底永远都是全局上下文，而栈顶就是当前正在执行的上下文。</p>
<p><strong>注意点：</strong></p>
<p>1、调用栈有两个指标，最大栈容量和最大调用深度，满足其中任意一个就会栈溢出，不过
具体多大和多深，这个没有研究过，有知道的朋友，介绍留个言交流一下。</p>
<h2 data-id="heading-10">3、作用域、作用域链</h2>
<h4 data-id="heading-11">1、作用域（scope）</h4>
<p>作用域是指在程序中定义变量的区域，该位置决定了变量的生命周期。通俗地理解，作用域
就是变量与函数的可访问范围，即作用域控制着变量和函数的可见性和生命周期。</p>
<p>在 ES6 之前，ES 的作用域只有两种：全局作用域和函数作用域。</p>
<blockquote>
<p>全局作用域中的对象在代码中的任何地方都能访问，其生命周期伴随着页面的生命周期。
函数作用域就是在函数内部定义的变量或者函数，并且定义的变量或者函数只能在函数内
部被访问。函数执行结束之后，函数内部定义的变量会被销毁。</p>
</blockquote>
<p>看过文章前面部分的同学，应该对var 声明的变量，为什么会有变量提升现象，已经完全可以理解，</p>
<p>这里重点给大家介绍一下const,let声明变量。</p>
<p>let 关键字声明的变量是可以被改变的，而使用 const 声明的变量其值是不可以被改变的。</p>
<p>但不管怎样，两者都可以生成块级作用域。</p>
<blockquote>
<p>函数内部通过 var 声明的变量，在编译阶段全都被存放到变量环境里面了。
通过 let 声明的变量，在编译阶段会被存放到词法环境（Lexical Environment）中。
在函数的作用域内部，通过 let 声明的变量并没有被存放到词法环境中。</p>
</blockquote>
<p>案例：</p>
<pre><code class="copyable">function foo()&#123;
var a = 1
let b = 2
&#123;
let b = 3
var c = 4
let d = 5
console.log(a)
console.log(b)
&#125;
console.log(b)
console.log(c)
console.log(d)
&#125;
foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d31237f2a784bdb839a6d67398b2b8a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>块级作用域就是通过词法环境的栈结构来实现的，而变量提升是通过变量环境来实现，通过这两者的结合，
JavaScript 引擎也就同时支持了变量提升和块级作用域了。（具体的函数执行细节，请看参考文章吧，太晚了，我干不动啦，要困觉啦）</p>
<p><strong>作用域参考文章：</strong></p>
<p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftime.geekbang.org%2Fcolumn%2Farticle%2F126339" target="_blank" rel="nofollow noopener noreferrer" title="https://time.geekbang.org/column/article/126339" ref="nofollow noopener noreferrer">time.geekbang.org/column/arti…</a></p>
<p><strong>注意点：</strong></p>
<p>1、词法环境（LexicalEnvironment）创建 对象环境记录器 ，
它用来定义出现在 全局上下文 中的变量和函数上下文的关系，
（负责处理 let 和 const 定义的变量），是用来登记<code>let</code> <code>const</code> <code>class</code>等变量声明。</p>
<h4 data-id="heading-12">2、作用域链</h4>
<p>在每个执行上下文的变量环境中，都包含了一个外部引用，用来指向外部的执行上下
文，我们把这个外部引用称为outer。</p>
<p>当一段代码使用了一个变量时，JavaScript 引擎首先会在“当前的执行上下文”中查找该
变量，
比如上面那段代码在查找 myName 变量时，如果在当前的变量环境中没有查找到，那么
JavaScript 引擎会继续在 outer 所指向的执行上下文中查找。</p>
<p>案例：</p>
<pre><code class="copyable">function bar() &#123;
console.log(myName)
&#125;
function foo() &#123;
var myName = " 极客邦 "
bar()
&#125;
var myName = " 极客时间 "
foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/394555ab35ae47ccb1a88355129cdf84~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，bar 函数和 foo 函数的 outer 都是指向全局上下文的，这也就意味着如
果在 bar 函数或者 foo 函数中使用了外部变量，那么 JavaScript 引擎会去全局执行上下文
中查找。我们把这个查找的链条就称为作用域链。</p>
<p>看到这个图，有没有感觉疑惑的地方？是不是跟平常的认知有点不一样呢？你还别说，我刚学的时候，我都怀疑是不是作者写错知识点啦，都想开始喷啦，幸好忍住啦，不然小丑原来是我自己，害，菜鸡，是真的难，。。。</p>
<p>要回答这个问题，你还需要知道什么是词法作用域。这是因为在 JavaScript 执行过程中，
其作用域链是由词法作用域决定的。说实话，词法作用域是啥玩意，我之前都没听过，绝了。继续往下看吧，大佬们，容本掌柜，继续道来。</p>
<blockquote>
<p>词法作用域
词法作用域就是指作用域是由代码中函数声明的位置来决定的，所以词法作用域是静态的作
用域，通过它就能够预测代码在执行过程中如何查找标识符。</p>
</blockquote>
<p>JavaScript 作用域链是由词法作用域决定的,词法作用域就是根据代码的位置来决定的，</p>
<p>词法作用域是代码编译阶段就决定好的，和函数是怎么调用的没有关系。</p>
<blockquote>
<p>了解了词法作用域以及 JavaScript 中的作用域链，结合上面这个案例，我们再回过头来看看上面的那个问题：
在开头那段代码中，foo 函数调用了 bar 函数，那为什么 bar 函数的外部引用是全局执行
上下文，而不是 foo 函数的执行上下文?
这是因为根据词法作用域，foo 和 bar 的上级作用域都是全局作用域，所以如果 foo 或者
bar 函数使用了一个它们没有定义的变量，那么它们会到全局作用域去查找。也就是说，词
法作用域是代码阶段就决定好的，和函数是怎么调用的没有关系。</p>
</blockquote>
<h2 data-id="heading-13">4、闭包</h2>
<p>理解了变量环境、词法环境和作用域链等概念，那接下来你再理解什么是 JavaScript 中
的闭包就容易多了。</p>
<h4 data-id="heading-14">1、闭包是什么：</h4>
<p>在 JavaScript 中，根据词法作用域的规则，内部函数总是可以访问其外部函数中声明的变量，当通过调用一个外部函数返回一个内部函数后，即使该外部函数已经执行结束了，但是内部函数引用外部函数的变量依然保存
在内存中，我们就把这些变量的集合称为闭包。比如外部函数是 foo，那么这些变量的集合就称为 foo 函数的闭包。</p>
<p>光看文字，可能之前不咋接触过闭包的同学，容易蒙蔽，还是先找个demo演示看看吧。</p>
<h4 data-id="heading-15">2、闭包案例</h4>
<pre><code class="copyable">function foo() &#123;
var myName = " 极客时间 "
let test1 = 1
const test2 = 2
var innerBar = &#123;
getName:function()&#123;
console.log(test1)
return myName
&#125;,
setName:function(newName)&#123;
myName = newName
&#125;
&#125;
return innerBar
&#125;
var bar = foo()
bar.setName(" 极客邦 ")
bar.getName()
console.log(bar.getName())
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9aafc02a58494441b9bd04e2d97d4f62~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从上面的代码可以看出，innerBar 是一个对象，包含了 getName 和 setName 的两个方
法（通常我们把对象内部的函数称为方法）。你可以看到，这两个方法都是在 foo 函数内
部定义的，并且这两个方法内部都使用了 myName 和 test1 两个变量。</p>
</blockquote>
<blockquote>
<p>根据词法作用域的规则，内部函数 getName 和 setName 总是可以访问它们的外部函数
foo 中的变量，所以当 innerBar 对象返回给全局变量 bar 时，虽然 foo 函数已经执行结
束，但是 getName 和 setName 函数依然可以使用 foo 函数中的变量 myName 和
test1。所以当 foo 函数执行完成之后，其整个调用栈的状态如下图所示：</p>
</blockquote>
<blockquote>
<p>好了，现在我们终于可以给闭包一个正式的定义了。在 JavaScript 中，根据词法作用域的
规则，内部函数总是可以访问其外部函数中声明的变量，当通过调用一个外部函数返回一个
内部函数后，即使该外部函数已经执行结束了，但是内部函数引用外部函数的变量依然保存
在内存中，我们就把这些变量的集合称为闭包。比如外部函数是 foo，那么这些变量的集
合就称为 foo 函数的闭包。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b1826229be4102b6603c8721fb6775~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，setName 的执行上下文中没有 myName 变量，foo 函数的闭包中包含
了变量 myName，所以调用 setName 时，会修改 foo 闭包中的 myName 变量的值。
同样的流程，当调用 bar.getName 的时候，所访问的变量 myName 也是位于 foo 函数闭
包中的。</p>
<h4 data-id="heading-16">3、谷歌浏览器f12查看闭包</h4>
<p>可以通过“开发者工具”来看看闭包的情况，打开 Chrome 的“开发者工具”，在
bar 函数任意地方打上断点，然后刷新页面，可以看到如下内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48fc1fa74492472fac4fedc96eb2bf0d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​开发者工具中的闭包展示</p>
<p>从图中可以看出来，当调用 bar.getName 的时候，右边 Scope 项就体现出了作用域链的情况：Local 就是当前的 getName 函数的作用域，Closure(foo) 是指 foo 函数的闭包，最下面的 Global 就是指全局作用域，从“Local–>Closure(foo)–>Global”就是一个完整的作用域链。
所以说，你以后也可以通过 Scope 来查看实际代码作用域链的情况，这样调试代码也会比较方便。</p>
<h4 data-id="heading-17">4、闭包回收</h4>
<p>闭包是怎么回收的
理解什么是闭包之后，接下来我们再来简单聊聊闭包是什么时候销毁的。因为如果闭包使用
不正确，会很容易造成内存泄漏的，关注闭包是如何回收的能让你正确地使用闭包。
通常，<strong>如果引用闭包的函数是一个全局变量，那么闭包会一直存在直到页面关闭；但如果这</strong>
<strong>个闭包以后不再使用的话，就会造成内存泄漏。</strong>
如果引用闭包的函数是个局部变量，等函数销毁后，在下次 JavaScript 引擎执行垃圾回收
时，判断闭包这块内容如果已经不再被使用了，那么 JavaScript 引擎的垃圾回收器就会回
收这块内存。</p>
<blockquote>
<p>所以在使用闭包的时候，你要尽量注意一个原则：如果该闭包会一直使用，那么它可以作为
全局变量而存在；但如果使用频率不高，而且占用内存又比较大的话，那就尽量让它成为一
个局部变量。</p>
<p>关于闭包回收的问题本文只是做了个简单的介绍，其实闭包是如何回收的还牵涉到了
JavaScript 的垃圾回收机制，而关于垃圾回收，等后续文章再进行整理，详细解释，</p>
</blockquote>
<p>大家可以先自行研究一下。</p>
<h2 data-id="heading-18">5、this</h2>
<p>this是啥，为啥需要this这个关键字，了解一下来龙去脉，可以帮助我们更好的理解this，以及使用它。</p>
<h4 data-id="heading-19">1、为什么需要this关键字</h4>
<p>先来看个案例</p>
<pre><code class="copyable">var bar = &#123;
myName:"time.geekbang.com",
printName: function () &#123;
console.log(myName)
&#125;
&#125;
function foo() &#123;
let myName = " 极客时间 "
return bar.printName
&#125;
let myName = " 极客邦 "
let _printName = foo()
_printName()
bar.printName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信你已经知道了，在 printName 函数里面使用的变量 myName 是属于全局作用域下面
的，所以最终打印出来的值都是“极客邦”。这是因为 JavaScript 语言的作用域链是由词
法作用域决定的，而词法作用域是由代码结构来确定的。</p>
<p>不过按照常理来说，调用bar.printName方法时，该方法内部的变量 myName 应该使用
bar 对象中的，因为它们是一个整体，大多数面向对象语言都是这样设计的。</p>
<blockquote>
<p>所以在对象内部的方法中使用对象内部的属性是一个非常普遍的需求。
但是 JavaScript 的作用域机制并不支持这一点，基于这个需求，
JavaScript 又搞出来另外一套this 机制。</p>
</blockquote>
<blockquote>
<p>在某些函数或者方法的编写中，this可以让我们更加便捷的方式来引用对象，在进行一些API设计时，
代码更加的简洁和易于复用。</p>
</blockquote>
<p>相信现在大家应该比较清楚，为啥需要this啦吧，当然这个只是其中一方面原因，其他的原因，有待大家来补充完善。</p>
<h4 data-id="heading-20">2、this是什么</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49f3258493dd4753977740dad0d40510~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，this 是和执行上下文绑定的，也就是说每个执行上下文中都有一个this。</p>
<blockquote>
<p>不过在讲解之前，希望你能区分清楚作用域链和this是两套不同的系统，它们之间基本没太多联系。在前期明确这点，可以避免你在学习 this 的过程中，和作用域产生一些不必要的关联。</p>
</blockquote>
<h4 data-id="heading-21">2、this分类</h4>
<p>执行上下文主要分为三种——全局执行上下文、函数执行上下文和 eval 执行上下文，所以对应
的 this 也只有这三种——全局执行上下文中的 this、函数中的 this 和 eval 中的 this（忽略）。</p>
<p><strong>1、全局执行上下文中的 this</strong>
首先我们来看看全局执行上下文中的 this 是什么。
你可以在控制台中输入console.log(this)来打印出来全局执行上下文中的 this，最终
输出的是 window 对象。所以你可以得出这样一个结论：全局执行上下文中的 this 是指向
window 对象的。这也是 this 和作用域链的唯一交点，作用域链的最底端包含了 window
对象，全局执行上下文中的 this 也是指向 window 对象。</p>
<p><strong>2、函数执行上下文中的 this</strong></p>
<p>现在你已经知道全局对象中的 this 是指向 window 对象了，那么接下来，我们就来重点分
析函数执行上下文中的 this。还是先看下面这段代码：</p>
<pre><code class="copyable">function foo()&#123;
console.log(this)
&#125;
foo()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在 foo 函数内部打印出来 this 值，执行这段代码，打印出来的也是 window 对象，这
说明在默认情况下调用一个函数，其执行上下文中的 this 也是指向 window 对象的。</p>
<p>3、对象中的this指向</p>
<pre><code class="copyable">var bar = &#123;
myName:"time.geekbang.com",
printName: function () &#123;
console.log(this.myName)  ----time.geekbang.com
&#125;
&#125;
function foo() &#123;
let myName = " 极客时间 "
return bar.printName
&#125;
let myName = " 极客邦 "
let _printName = foo()
_printName()
bar.printName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象bar中，加了this，打印出来的myName就是对象bar中的值，相反，如果不加this，那就指向的是全局上下文中的内容，我感觉有必要，把这个也加上去作为分类介绍一下。可以自己去掉this，测试一下看看。</p>
<p>说了这么多this指向情况，估计你会好奇，那能不能设置执行上下文中的 this 来指向其他对象呢？答案是肯定的。通常情况下，有下面三种方式来设置函数执行上下文中的 this 值。</p>
<h4 data-id="heading-22">4、改变this指向</h4>
<p><strong>1、通过函数的 call 方法设置</strong>
你可以通过函数的call方法来设置函数执行上下文的 this 指向，比如下面这段代码，我们就并没有直接调用 foo 函数，而是调用了 foo 的 call 方法，并将 bar 对象作为 call 方法的参数。</p>
<pre><code class="copyable">let bar = &#123;
myName : " 极客邦 ",
test1 : 1
&#125;
function foo()&#123;
this.myName = " 极客时间 "
&#125;
foo.call(bar)
console.log(bar)
console.log(myName)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行这段代码，然后观察输出结果，你就能发现 foo 函数内部的 this 已经指向了 bar 对
象，因为通过打印 bar 对象，可以看出 bar 的 myName 属性已经由“极客邦”变为“极
客时间”了，同时在全局执行上下文中打印 myName，JavaScript 引擎提示该变量未定
义。
其实除了 call 方法，你还可以使用bind和apply方法来设置函数执行上下文中的 this，它
们在使用上还是有一些区别的，如果感兴趣你可以自行搜索和学习它们的使用方法，这里我
就不再赘述了。</p>
<p><strong>2. 通过对象调用方法设置</strong></p>
<p>要改变函数执行上下文中的 this 指向，除了通过函数的 call 方法来实现外，还可以通过对
象调用的方式，比如下面这段代码：</p>
<pre><code class="copyable">var myObj = &#123;
name : " 极客时间 ",
showThis: function()&#123;
console.log(this)
&#125;
&#125;
myObj.showThis()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这段代码中，我们定义了一个 myObj 对象，该对象是由一个 name 属性和一个
showThis 方法组成的，然后再通过 myObj 对象来调用 showThis 方法。执行这段代码，
你可以看到，最终输出的 this 值是指向 myObj 的。
所以，你可以得出这样的结论：使用对象来调用其内部的一个方法，该方法的 this 是指向
对象本身的。</p>
<p><strong>注意点：</strong></p>
<p>1、在全局环境中调用一个函数，函数内部的 this 指向的是全局变量 window。
通过一个对象来调用其内部的一个方法，该方法的执行上下文中的 this 指向对象本身。</p>
<p><strong>3. 通过构造函数中设置</strong></p>
<pre><code class="copyable">function CreateObj()&#123;
this.name = " 极客时间 "
&#125;
var myObj = new CreateObj()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们就通过 new 关键字构建好了一个新对象，并且构造函数中的 this 其实就是新对象本身。</p>
<p>new的具体细节参考这篇文章：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnew" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<p>this知识点参考文章：</p>
<p>1、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FhYm0JgBI25grNG_2sCRlTA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/hYm0JgBI25grNG_2sCRlTA" ref="nofollow noopener noreferrer">mp.weixin.qq.com/s/hYm0JgBI2…</a></p>
<p>2、<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftime.geekbang.org%2Fcolumn%2Farticle%2F128427" target="_blank" rel="nofollow noopener noreferrer" title="https://time.geekbang.org/column/article/128427" ref="nofollow noopener noreferrer">time.geekbang.org/column/arti…</a></p>
<blockquote>
<p><strong>在整理文章，资料收集的过程中，着实发现每一个知识点都太大，深入下去，都有很多好玩的知识点值得学习，后期会针对这些单独知识点，再出一个JavaScript更细的疑难杂症</strong></p>
</blockquote>
<p>大家有什么想学习或者想讨论的JavaScript疑难杂症，可以给大掌柜留言，一起多多交流，站在前人巨人的肩膀上，大家一起努力学习。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa790686334941aa84f81ddf4fd9c3de~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考文章：</p>
<p>1、前端面试之彻底搞懂this指向
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMjExNzQxMQ%3D%3D%26mid%3D2247485068%26idx%3D1%26sn%3D8a58365c6edc28408ceaf507564cdcc2%26chksm%3D974bb440a03c3d56ee0e5498035006fd9d2a66e77dd88087d85991f802fccd087af587ef8cd2%26mpshare%3D1%26scene%3D1%26srcid%3D0527VffST2KOz7xQlsxNJ8aA%26sharer_sharetime%3D1622072938011%26sharer_shareid%3Dbf7a7143f255060150499be3bd42eb7d%26version%3D3.1.8.3015%26platform%3Dwin%23rd%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s?__biz=MzIxMjExNzQxMQ==&mid=2247485068&idx=1&sn=8a58365c6edc28408ceaf507564cdcc2&chksm=974bb440a03c3d56ee0e5498035006fd9d2a66e77dd88087d85991f802fccd087af587ef8cd2&mpshare=1&scene=1&srcid=0527VffST2KOz7xQlsxNJ8aA&sharer_sharetime=1622072938011&sharer_shareid=bf7a7143f255060150499be3bd42eb7d&version=3.1.8.3015&platform=win#rd%E3%80%82" ref="nofollow noopener noreferrer">mp.weixin.qq.com/s?__biz=MzI…</a></p>
<p>2、JavaScript深入理解之作用域链<a href="https://link.juejin.cn/?target=http%3A%2F%2Fcavszhouyou.top%2FJavaScript%25E6%25B7%25B1%25E5%2585%25A5%25E7%2590%2586%25E8%25A7%25A3%25E4%25B9%258B%25E4%25BD%259C%25E7%2594%25A8%25E5%259F%259F%25E9%2593%25BE.html" target="_blank" rel="nofollow noopener noreferrer" title="http://cavszhouyou.top/JavaScript%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3%E4%B9%8B%E4%BD%9C%E7%94%A8%E5%9F%9F%E9%93%BE.html" ref="nofollow noopener noreferrer">cavszhouyou.top/JavaScript%…</a></p>
<p>3、执行上下文详细图解<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000012646203" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000012646203" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
<p>4、一篇文章看懂JS执行上下文<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fecholun%2Fp%2F11438363.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/echolun/p/11438363.html" ref="nofollow noopener noreferrer">www.cnblogs.com/echolun/p/1…</a></p>
<p>5、 块级作用域：var缺陷以及为什么要引入let和const？<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftime.geekbang.org%2Fcolumn%2Farticle%2F126339" target="_blank" rel="nofollow noopener noreferrer" title="https://time.geekbang.org/column/article/126339" ref="nofollow noopener noreferrer">time.geekbang.org/column/arti…</a></p>
<p>6、new 运算符
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Fnew" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/new" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<p>7、this：从JavaScript执行上下文的视角讲清楚this
<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftime.geekbang.org%2Fcolumn%2Farticle%2F128427" target="_blank" rel="nofollow noopener noreferrer" title="https://time.geekbang.org/column/article/128427" ref="nofollow noopener noreferrer">time.geekbang.org/column/arti…</a></p></div>  
</div>
            