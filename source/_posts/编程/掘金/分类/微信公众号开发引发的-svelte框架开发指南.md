
---
title: '微信公众号开发引发的-svelte框架开发指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed1b922a8f04d8c9f02b19a94fe58c0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:48:10 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed1b922a8f04d8c9f02b19a94fe58c0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近开发了企业微信嵌入H5项目，本来打算用prettier-vue3开发的，demo测试的时候发现不兼容proxy，企业微信用的webview嵌入的浏览器内核是chrome 53,且现在最新版本的企业微信嵌入的内核还是50多，这就是三年前的版本，官方不更新，求人不如自力更生，所以想其他办法，本来业务不多，用vue或者react有点大材小用，偶得一框架Svelte，发现很适合我们的场景。</p>
<blockquote>
<p>思考：凡是这种对兼容性要求高的，最好用原生js写，如果项目大，一定用框架提前考虑好兼容性，和解决方案。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bed1b922a8f04d8c9f02b19a94fe58c0~tplv-k3u1fbpfcp-watermark.image" alt="4856cb45f1d6e250956aaafc6817b2e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74237f14e9a74f4cb91a19a58f5a91b2~tplv-k3u1fbpfcp-watermark.image" alt="c845bf3ee87526e510c66acef3f8508.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6273e3a064834c93a05a02d0b574f86a~tplv-k3u1fbpfcp-watermark.image" alt="73cbc27262dc6819a0c03471507a655.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>企业微信开发的同学慎重开发</p>
</blockquote>
<h2 data-id="heading-1">Svelte ——  No Runtime 无运行时代码 的框架</h2>
<h3 data-id="heading-2">打包体积更小</h3>
<p>Vue和React是基于运行时的框架，打包出来的代码都会包含它自身的runtime代码。 而Svelte的做法则是在编译时减少运行时的代码， 尽量减小打包后代码中包含的runtime代码。而且像上面介绍的他不基于Virtual Dom，因此Svelte打包后的代码体积相比其他框架的小许多。</p>
<p>下面是<code>Jacek Schae</code>大神的统计，使用市面上主流的框架，来编写同样的 Realword 应用的体积：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee474ff16b9a4bd6b6cdd558026f73ed~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见Svelte构建的应用体积很小吗，有绝对的优势。但是这这比较是片面的</p>
<p>其实对于 Svelte 这个包大小这个问题，其实很早之前在 Svelte Github 中也对 React 和 Svelte 进行了广泛的讨论。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a11fd4deea9a4984a2f9f8d12f20d228~tplv-k3u1fbpfcp-watermark.image" alt="Inflection Point" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Svelte 确实有一个阈值会使得它在一定程度后让体积大小没有了优势，但是在一般情况下，只要不是特别复杂的中后台管理应用，Svelte 应当会比其他框架体积小。</p>
<p>在一些 H5 游戏中，如果你想要获得 React/Vue 数据驱动的方式编写应用，但是你又不想要引入他们这么大的运行时，确实来说是一个非常不错的方案。</p>
<p>或者嵌入到其他应用的的移动端网页，有一个初步的估计大约比使用 React 减少 30 - 50% 的体积，具体的数值因为还没迁移完无法给出完整的数据。还有一点，非运行时的框架，对于首屏的渲染也是有一个极大的帮助，你可以将首屏组件进行拆分，非运行时的首屏组件其实是非常小的，这对移动端来说非常的友好，因为毕竟使用 SSR 对应服务端还是有一定的压力要求的。</p>
<h3 data-id="heading-3">更少的代码量</h3>
<p>Svelte中的写法设计的更人性化，相比其他框架可以在开发中只需更少的代码。 在Svelte官网它们中举了个例子，当声明一个组件状态时：</p>
<p>这是React的代码</p>
<pre><code class="copyable">const [count, setCount] = useState(0);

function increment() &#123;
  setCount(count + 1);
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是Svelte的代码</p>
<pre><code class="copyable">let count = 0;

function increment() &#123;
  count += 1;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相比React简洁了许多，而且感觉就像我们平时写的JavaScript一样，更方便阅读。</p>
<h3 data-id="heading-4">无Virtual Dom</h3>
<p>我们都知道Vue，React中都使用到了Virtual Dom来对Dom进行更新。Virtual Dom会把页面Dom变为树结构的数据存在内存中，每次修改组件中的状态时，会生成一个新的Virtual Dom与旧的Virtual Dom进行对比生成一个补丁，用diff 计算出更新哪些dom。等到真正修改完毕时在去更新真实的dom节点。当然框架中的Virtual Dom要比我说的实现的复杂的多。</p>
<p>而<code>svelte</code>dom 是把数据和真实dom之间的映射关系，在编译的时候就通过AST等算出来，保存在<code>p</code>函数中，Svelte修改更新Dom节点使用了纯JavaScrip实现不依赖任何框架。 因为不依赖Virtual Dom因此初始化和更新时工作都小了许多，从而使页面启动和运行都会更加迅速。</p>
<h3 data-id="heading-5">响应式</h3>
<p>Svelte它也为我们实现了像Vue那样的状态响应式，当某个状态修改状态时组件就会进行更新。这可以让我们更好的封装组件。而且写法就和正常声明变量一样，但是Svelte会在编译时为你自动注入响应式代码。</p>
<pre><code class="copyable">count += 1;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Svelte在编译时，当编译时自动加上响应式代码</p>
<pre><code class="copyable">count += 1; $$invalidate('count', count);
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Hight-Performance ——高性能</h3>
<p>在<code>Virtual Dom</code>已经是前端框架标配的今天， Svelte 声称自己是没有<code>Virtual Dom</code>加持的， 怎么还能保证高性能呢？</p>
<h4 data-id="heading-7">性能测评</h4>
<p>Jacek Schae 在《A RealWorld Comparison of Front-End Frameworks with Benchmarks》中用主流的前端框架来编写 RealWorld 应用，使用 Chrome 的Lighthouse Audit测试性能，得出数据是<strong>Svelte 略逊于Vue, 但好于 React。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a9e17204bd846069f92824c6ec2ae4a~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是很惊奇？另外一个前端框架性能对比的项目也给出了同样的答案：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkrausest%2Fjs-framework-benchmark%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/krausest/js-framework-benchmark%E3%80%82" ref="nofollow noopener noreferrer">github.com/krausest/js…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b856783c4dc49cdb077a4245f698a0e~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么 Svelte 性能还不错，至少没有我们预期的那么糟糕？我们接下来会在原理那一小结来介绍。</p>
<h2 data-id="heading-8">Svelte 劣势</h2>
<p>说完了 Svelte 的优势，我们也要考虑到 Svelte 的劣势。</p>
<h4 data-id="heading-9">和Vue， React框架的对比</h4>
<p>在构建大型前端项目时，我们在选择框架的时候就需要考虑更多的事情。Svelte 目前尚处在起步阶段，对于大型项目必要的<strong>单元测试</strong>并没有完整的方案。目前在大型应用中使用 Svelte , 需要谨慎评。</p>









































<table><thead><tr><th>类目</th><th>Svelte</th><th>Vue</th><th>React</th></tr></thead><tbody><tr><td>UI 组件库</td><td>Material design ( 坦率的说，不好用 )</td><td>Element UI / AntD</td><td>AntD / Material design</td></tr><tr><td>状态管理</td><td>官网自带</td><td>Vuex</td><td>Redux/MobX</td></tr><tr><td>路由</td><td>Svelte-router</td><td>Vue-router</td><td>React-router</td></tr><tr><td>服务端渲染</td><td>支持</td><td>支持</td><td>支持</td></tr><tr><td>测试工具</td><td>官方网站没有相关内容</td><td>@vue/test-utils</td><td>Jest</td></tr></tbody></table>
<p>我们在用 Svelte 开发公司级别中大型项目时，也发现了其他的一些主要注意的点</p>
<ul>
<li>没有像AntD那样成熟的UI库。比如说需求方想加一个toast提示，或者弹窗，pm：”很简单的，不用出UI稿，就直接用之前的样式好啦~“</li>
</ul>
<p>但是 Svelte 需要从0开始 ”抄“ 出来一个toast或者弹窗组件出来，可能会带来额外的开发量和做好加班的准备。</p>
<ul>
<li>Svelte 原生不支持预处理器，比如说<code>less</code>/<code>scss</code>，需要自己单独的配置 webpack loader。</li>
<li>Svelte 原生脚手架没有目录划分</li>
<li>暂时不支持typescript，虽然官方说了会支持, 但是不知道什么时候.</li>
</ul>
<p>还需要注意的一点是，React / Vue等框架自带的<code>runtime</code>虽然会增加首屏加载的<code>bundle.js</code>，可是当项目变得越来越大的时候，框架的<code>runtime</code>在<code>bundle.js</code>里面占据的比例也会越来越小，这个时候我们就得考虑一下是不是存在一个Svelte生成的代码大于React和Vue生成的代码的阈值了。</p>
<h2 data-id="heading-10">svelte 用来开发官网的模板</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fzhangdulin%2Fsvelte-vite-template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/zhangdulin/svelte-vite-template" ref="nofollow noopener noreferrer">开发官网的模板</a></p>
<h2 data-id="heading-11">教程和体验地址</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FLearn%2FTools_and_testing%2FClient-side_JavaScript_frameworks%2FSvelte_getting_started" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Svelte_getting_started" ref="nofollow noopener noreferrer">svelte mdn</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsveltejs%2Fsvelte" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sveltejs/svelte" ref="nofollow noopener noreferrer">svelte github</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsvelte.dev%2Fexamples%23context-api" target="_blank" rel="nofollow noopener noreferrer" title="https://svelte.dev/examples#context-api" ref="nofollow noopener noreferrer">svelte 在线体验地址</a></p>
<h2 data-id="heading-12">svelte 框架</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsveltematerialui.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sveltematerialui.cn/" ref="nofollow noopener noreferrer">中文Material UI</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsveltematerialui.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://sveltematerialui.com/" ref="nofollow noopener noreferrer">英文Material UI</a></p>
<ul>
<li><a href="https://juejin.cn/post/6944355557495013412" target="_blank" title="https://juejin.cn/post/6944355557495013412">参考文档</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FFCy903Rh6837MBDYLwYYIg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/FCy903Rh6837MBDYLwYYIg" ref="nofollow noopener noreferrer">参考文档</a></li>
</ul></div>  
</div>
            