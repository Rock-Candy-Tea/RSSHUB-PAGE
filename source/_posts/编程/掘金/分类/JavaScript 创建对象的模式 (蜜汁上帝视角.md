
---
title: 'JavaScript 创建对象的模式 (蜜汁上帝视角'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259ff05ab3234a99a6d11abde77a3fd7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 05:20:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259ff05ab3234a99a6d11abde77a3fd7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这个博客里主要介绍一下JavaScript创建对象的一些模式。想要深入详细了解还是建议大家看看书。</p>
<hr>
<p>说起创建对象，一般来说我应该讲创建女朋友的。可是想了想我就是女的，也没什么特殊爱好，所以我还是不创建女朋友了。行现在开始:older_man:就是:angel:上帝。:older_man:要开始造人了。</p>
<p><strong>我先造一个亚当，再造一个夏娃。</strong> 打印看一下，我已经造成功了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259ff05ab3234a99a6d11abde77a3fd7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>他俩生了孩子，叫该隐和亚伯，<strong>:older_man:继续造该隐和亚伯</strong>，又成功了。</p>
<p>但是你是不是发现问题了，这样就出来了好多重复代码啊。:older_man:要是造60亿人民岂不是累死。所以，我得搞得跟女娲似的，用藤蔓沾了泥土，往地上一甩，泥点点就能成人。所以我开启<strong>工厂模式</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83a2e4fec0ea455195c914858c0df746~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">工厂模式</h1>
<p><strong>工厂模式就是用函数封装，以特定模式创建对象</strong></p>
<p>:older_man:用函数封装了造人对象。</p>
<p>原来造俩人8行代码，现在造俩人8行代码</p>
<p>原来造四人16行代码，现在造四人10行代码。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0244895413dd493d96c890367109a1dc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只造人不够啊，我还得造动物。有条:snake:引诱了夏娃吃苹果，亚伯该隐还养了:sheep:。<strong>我要开始造动物了。</strong></p>
<p>好了现在我已经造成功了，但是问题双来了，虽然我用了三个函数造他们，但是为啥输出出来都是普通object的&#123;&#125;形式？万物平等？:older_man:不同意，万物平等我就都造人了。所以我得把他们区分开。这就用到了<strong>构造函数模式</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da5cabccf89f497bb1ab749d7362c97d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">构造函数模式</h1>
<p><strong>构造函数模式就是用构造函数创建特定类型的对象</strong></p>
<p>构造函数形如：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//声明</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> 函数名(<span class="hljs-params">参数</span>)</span>&#123;

函数体

&#125;

<span class="hljs-comment">// 使用</span>

<span class="hljs-keyword">let</span> 实例 = <span class="hljs-keyword">new</span> 函数名(参数)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我就用构造函数的形式来创建了。发现没，还少了声明对象和返回值呢。</p>
<p>但是问题又来了。这就简单了吗？这不是还有大量重复代码？<code>this.name</code> <code>this.gander</code>所有物种都这样搞岂不是累死？那我只好继续简化啦。这就用到了<strong>原型模式</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39c957098354cf2acb682eca4bc6f98~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，现在让他们叫一声。问题又来了，如果我想让羊也叫，蛇也叫，那岂不是又出现大量一模一样的代码？这个可以用<strong>原型模式</strong>解决。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/608f5338ca934f21a1b7fff5ccf4572b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">原型模式</h1>
<p>我们创建的每一个函数都会有prototype属性，这个属性是一个指针，指向一个对象，这个对象里边包含了各种“由某种特定类型的所有实例”共享的方法和属性。</p>
<blockquote>
<p><strong>实例</strong>就是 <code>let 实例  = new 函数名()</code> 你声明的这个东西就是实例。这是抽象和具体的概念。你的函数就是抽象，你的实例就是具体。</p>
</blockquote>
<p>想了解原型的可以自己看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_36667170%2Farticle%2Fdetails%2F105099064" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_36667170/article/details/105099064" ref="nofollow noopener noreferrer">JavaScript 详细图解原型</a>。</p>
<p>我就不详细解析原型了，我下边直接说方法了。</p>
<p>既然:older_man:想再少写一点代码，那我就直接把这些相同的东西写进原型里。原型链的尽头是Object，我就直接写Object里边吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65eb05d281e0406cba6cff700b186b3d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>只要把相同的方法添加到某一个原型中，只要实例在这条原型链上就可以使用这个方法哦。不用每个函数都声明了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e52df03c5cb34334aeec156af33af196~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那你可能问，为什么你不直接把name和gander也放到原型中去。</p>
<p>可以是可以，但是这样代码量并不会减少啊。因为你要给这些属性赋值，你就要再把它拿出来赋值。</p>
<p>你看嘛。不用更改的方法写到原型里，那函数中就不用写了。但是需要更改的方法，你写道原型里，如果你函数体中不给他赋值也没用哦。所以我们才要<strong>综合使用构造函数模式和原型模式</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60ebfaaac0964af6940665cd59e2556c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">组合使用构造函数模式和原型模式</h1>
<p>这是创建自定义类型最常见的方式。可以将共有的方法和不需要重新赋值的属性写到原型中，而那些特有的属性写到各自的函数体中。</p>
<p>下图中所有生物说的都是‘我是上帝创造的’，这是个不需要改变的属性，因此可以把它加到原型里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea291fb0269d4294b34fe6d868c1c7a9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">动态原型模式</h1>
<p><strong>检查某个方法是否存在，来决定是否需要初始化原型。</strong></p>
<p>比如现在:older_man:给Person这个函数的原型里添加了speak的方法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e55c980aa4b4ebb8e83de33f2b1260e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>:older_man:突然又不想当上帝了。让给你吧。</p>
<p>可是你拿到我的代码之后，也想让他们说“我是XXX”，但是你不知道我里边写没写这个方法。那怎么办，那就用到了<strong>动态原型模式</strong>。</p>
<p>猜猜下边的代码待用之后是输出“我是XXX”还是“哈哈哈我是XXX”？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0d98d837ba84614a0a945a666f088fe~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>答案是：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/671503f45e8b4251acedb2b02a145139~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>红框框就是动态添加原型，判断函数原型中是否有这个方法再决定要不要添加。因为上边我已经写了Person的speak方法，所以下边判断已经有了，就不会添加这个方法了。</p>
<h1 data-id="heading-5">寄生构造函数模式</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f25f18cf4e124c67b39d35464d9fe2e9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种对比一下工厂模式，你就会发现，其实只多了一个new</p>
<h1 data-id="heading-6">稳妥构造函数模式</h1>
<p>稳妥构造函数模式创建对象实例方法不引用this，不使用new操作符。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cc77a59ea474c79bedf910e8dae3332~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>稳妥对象</strong>：是指‘没有公共属性，方法中也不引用this’的对象</p>
</blockquote>
<blockquote>
<p>稳妥对象最适合在一些安全的环境中或者在防止数据被其他应用程序改动时使用。</p>
</blockquote>
<hr>
<p>今天我也精分成功了</p></div>  
</div>
            