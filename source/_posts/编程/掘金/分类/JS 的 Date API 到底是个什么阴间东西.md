
---
title: 'JS 的 Date API 到底是个什么阴间东西'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdd045f0576f46f2a3316a1a186177cb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:58:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdd045f0576f46f2a3316a1a186177cb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKieSun%2Ffucking-frontend" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KieSun/fucking-frontend" ref="nofollow noopener noreferrer">前端进阶学习资料、十五万字面试指南</a></p>
</blockquote>
<p><code>Date</code> API 大家肯定都有用过，虽然更多时候关于日期的处理都交给了 dayjs 或者 moment。</p>
<p>但我们肯定免不了去直接使用原生 API，这时候你可能会免不了爆一句粗口「什么阴间玩意？」，接下来我们来看看到底这个 API 不好用到哪里去。</p>
<p>首先我们先了解下 <code>Date</code> 支持哪些类型的传参：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(value);
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(dateString);
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(year, monthIndex [, day [, hours [, minutes [, seconds [, milliseconds]]]]]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解完参数类型，就直接用起来咯：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdd045f0576f46f2a3316a1a186177cb~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午10.07.36" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没啥毛病，符合预期，不传参就获取当前系统时间。</p>
<p>那么我们换种写法，传入字符串呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4ea93d0a154202b1e4673936605f2a~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午10.10.36" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小小的脑袋充满了问号，明明我传入同样的日期，无非格式变了一下，为啥输出的内容却完全不一样？</p>
<p>笔者这里解释下，当我们输入第一种格式时，内部会帮我们解析成当前时区所对应的协调世界时（UTC），也就是零点加八小时。</p>
<p>而当我们输入第二种格式时，内部会帮我们解析成当前时区的零点。</p>
<p>到这里其实笔者已经有点懵逼了，不踩过这种坑鬼知道会有这样的不同。</p>
<p>你以为这样就结束了？天真了，我们再来看这种写法：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d531b916c68749b2a6f4013a19f206a9~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午10.24.46" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好家伙，我这传的明明是七月份，咋的给我解析成八月份了？？？</p>
<p>这看起来是个 Bug，实际上算是一个老传统，在很久之前的编程语言里确实以 0 开头作为某些时间的起始位：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7ef20b879cd47a0a677e26850430048~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午10.29.50" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上内容大家可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinux.die.net%2Fman%2F3%2Flocaltime" target="_blank" rel="nofollow noopener noreferrer" title="https://linux.die.net/man/3/localtime" ref="nofollow noopener noreferrer">Linux</a> 的文档中阅读到。</p>
<p>文章到这里还没有结束，咱们再来换个写法看看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5a4c5f4e1fa4b309037f8fef0922d26~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午9.56.32" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这第一个写法笔者还能理解一点，毕竟年份从 1900 年开始计数，但是为啥换成数组的写法你就给我变成了 2032 年啊！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7478d4d5e1184e8ebb57f479d11acf7f~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>笔者这里也就不考古了，反正打死不这样写就行了。</p>
<p>那么多坑，心累了，以后就只用 <code>new Date()</code> 吧，但其实单用这个你说不定也能踩到一个坑。</p>
<p>举个场景，我们在服务端给接口 <code>setCookie</code> 的时候都会设置一个 <code>expires</code> 字段代表这个 Cookie 的有效时间，此时如果你的 <code>expires</code> 字段是以 <code>new Date()</code> 生成的话，千万记得要做一次转换。</p>
<p>比如说我们利用 <code>new Date()</code> 获取了一个时间，大家可以看到输出是带有中文的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6277b03d89704cd8a871b157267116d6~tplv-k3u1fbpfcp-zoom-1.image" alt="截屏2021-07-28下午10.07.36" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时如果你把这个时间去做 <code>setCookie</code> 的话，服务端就会报一个 <code>TypeError</code> 的错误：<code>invalid character in header content ["set-cookie"]</code>，这是因为我们设置的值里存在中文。</p>
<p>因此我们需要对这个时间做一次转换得到一个不包含中文的时间字符串。</p>
<p>讲了那么多，难道原生 API 真的没救了？只能全用库了么？这倒也不是，TS39 也知道如此阴间的 API 不好用，因此搞了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-temporal" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-temporal" ref="nofollow noopener noreferrer">proposal-temporal</a> 这个提案来解决问题，算是融合了目前日期处理库的功能。</p>
<p>但是等这个提案兼容大部分浏览器也不知道什么时候呢，还是继续 dayjs 吧。</p>
<blockquote>
<p>作者：yck</p>
<p>仓库：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FKieSun" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/KieSun" ref="nofollow noopener noreferrer">Github</a></p>
<p>公众号：<a href="https://user-gold-cdn.xitu.io/2019/12/22/16f2e3314a431c20?w=900&h=500&f=jpeg&s=148695" target="_blank" title="https://user-gold-cdn.xitu.io/2019/12/22/16f2e3314a431c20?w=900&h=500&f=jpeg&s=148695">前端真好玩</a></p>
<p>特别声明：原创不易，未经授权不得转载或抄袭，如需转载可联系笔者授权</p>
</blockquote></div>  
</div>
            