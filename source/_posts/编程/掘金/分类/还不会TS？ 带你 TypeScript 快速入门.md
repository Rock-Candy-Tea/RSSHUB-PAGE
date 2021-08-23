
---
title: '还不会TS？ 带你 TypeScript 快速入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41ea8b9ef5f1447a8a247fb03764c170~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 18:04:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41ea8b9ef5f1447a8a247fb03764c170~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言</p>
</blockquote>
<p>TS 现在使用地越来越多，学计算机的就得不断的学习，才能更好的追逐这个时代，这是小浪以前学习TS时候的总结，能快速的帮助大家入门 TS，这里列举不是很全列举一些常用的，但是能满足平时的需求，具体的可以看官方的文档哈，这里只是简单的入门，希望能够帮助到大家</p>
<blockquote>
<p>往期精彩：</p>
<p><a href="https://juejin.cn/post/6994337441314242590" target="_blank" title="https://juejin.cn/post/6994337441314242590">快速上手Vuex 到 手写简易 Vuex</a></p>
<p><a href="https://juejin.cn/post/6990582632270528525" target="_blank" title="https://juejin.cn/post/6990582632270528525">从了解到深入虚拟DOM和实现diff算法</a></p>
<p><a href="https://juejin.cn/post/6989106100582744072" target="_blank" title="https://juejin.cn/post/6989106100582744072">手写一个简易vue响应式带你了解响应式原理</a></p>
<p><a href="https://juejin.cn/post/6988316779818778631" target="_blank" title="https://juejin.cn/post/6988316779818778631">从使用到自己实现简单Vue Router看这个就行了</a></p>
<p><a href="https://juejin.cn/post/6983934602196811789" target="_blank" title="https://juejin.cn/post/6983934602196811789">前端面试必不可少的基础知识，虽然少但是你不能不知道</a></p>
</blockquote>
<h2 data-id="heading-0">1.安装</h2>
<p><code>TS</code> 的优点和缺点就不一一赘述了，下面直接进入正题</p>
<blockquote>
<p>进行全局安装</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.原始数据类型</h2>
<p>掘金代码高亮我觉得和主题有冲突，这里代码代码都是比较简单，我就直接截图了哈</p>
<blockquote>
<p>我们在变量后面添加  <code>: 类型</code> 就可以规定数据的类型，设置其他类型就会报错</p>
<p>我们这里先来了解下基础的类型</p>
</blockquote>
<h3 data-id="heading-2">1.字符串 <code>string</code></h3>
<blockquote>
<p>双引号（<code>"</code>）或单引号（<code>'</code>）表示字符串</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41ea8b9ef5f1447a8a247fb03764c170~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809093951818" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.数字 <code>number</code></h3>
<blockquote>
<p>支持 十/十六/二/八 进制</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55a20a97c3b6463ca7e278c7330620da~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809094238590" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3.布尔 <code>boolean</code></h3>
<blockquote>
<p>只能是 <code>true</code>/<code>false</code></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68898b41d2a248aa9c6b6afa39fe8bad~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809094357439" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">4.<code>undefined</code></h3>
<blockquote>
<p>用处不是很大</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4adbd43b75849fc9d01b4a6008e9da7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809094430315" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">5.<code>null</code></h3>
<blockquote>
<p>用处不是很大</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16172c44cf944880b314d28b20470663~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809094458172" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">6.空 <code>void</code></h3>
<blockquote>
<p>没有任何类型，函数的没用返回值的使用 <code>void</code> ,返回值为空（ <code>undefined</code> ）</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/534b91390cb1492bbc462b152d5682d7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210810194819203" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">7.任意类型 <code>any</code></h3>
<blockquote>
<p>这里当类型不确定的时候，就可以使用 <code>any</code> 任意类型，不到万不得已不使用</p>
<p><code>Unknow</code> 类型和 <code>any</code> 一样可以容纳任意类型比 <code>any</code> 安全</p>
<p>平时用的不多，就不介绍了</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdbd6793bacc4e9da6c199f3a312469f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809094624551" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">7.字面量</h3>
<blockquote>
<p>定义什么就只能赋值什么</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/678078f02de34b5fb5c56bd9eb06ca9c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809154738126" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1d0fb316f0248bf872054508e89de4f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809154921672" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">3.复杂类型</h2>
<h3 data-id="heading-11">1.数组 <code>array</code></h3>
<blockquote>
<p>设置数组的类型 比如这个例子 <code>true</code> 这个就会报错，不属于<code>number</code>，数组的元素必须是规定好的类型 其他类型同理</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/689ff60c586342f9b8789a4e67eabf73~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808213454745" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">2.元组 <code>tuple</code></h3>
<blockquote>
<p>学习过 <code>Python</code> 的同学应该不太陌生，其实可以把它看做一个数组，可以声明多个类型的数组，这样就能插入多个数据类型的数据，就是长度固定的数组</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cc91183e9954989b20f51d3a94d01f3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808214401857" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">3.接口 <code>interface</code></h3>
<blockquote>
<p>它能很方便的帮我们定义 <code>Ojbect</code> 类型，它是非常的灵活可以描述对象的各种类型</p>
</blockquote>
<p>与 <code>java</code> 的 <code>interface</code> 有些区别，下面简单了看下，具体的下面有介绍</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af7ba1b2e9a2457ca6838804c421dd97~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808215444817" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在 <code>interface</code> 属性中添加 <code>？</code>可以<strong>省略</strong></p>
</blockquote>
<p>下面我们给 <code>height</code> 添加 <code>?</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c096e986c2ad491280a6679cecadb753~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808215805574" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>readonly</code> 不可改变的，定义完后就不能修改，是不是和 <code>const</code> 有点像，不过 <code>const</code> 是针对变量， <code>readonly</code> 是针对属性</p>
</blockquote>
<p>下面我们把 <code>id</code> 添加上 <code>readonly</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25cd6d6c64b14e21996955f12f45b33c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808220259826" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">4.函数 <code>funtion</code></h3>
<blockquote>
<p>我们要规定函数的 <strong>输入类型</strong> 和 <strong>返回类型</strong></p>
<p>在<strong>形参后面</strong>接冒号声明 形参的类型，在 <code>()后面</code>冒号声明 返回值类型</p>
</blockquote>
<p>传入多余的参数会报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63e8e40c28bc46bc9921e922820f1126~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808221913660" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们也可以为函数添加<strong>可选参数</strong> 这里用 <code>?</code> 即可，这样我们就可以调用两个参数或者三个参数不报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faa3922132a24f9fba068c2c82019387~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808221628843" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可选参数之后不能再加规定类型的形参</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cabe6ec6e988433ebb31d567865ef40b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808222057869" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以把它添加个 <code>？</code>变为可选参数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f52ec760d2e1416daa2fdd2fad66866d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808222200172" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了上面这种声明式写法还有一种表达式写法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1083fbd7400e4e12a755bc472050e818~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808222347710" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>有了上面的了解后我们来说下 <strong>定义函数类型</strong> 的变量</p>
</blockquote>
<p>这里这个函数还是上面那个</p>
<p>我们定义<code>mysum</code> 指定它 的类型 来接收 我们上面定义的函数</p>
<p><code>()</code> 里面是输入的形参的 类型</p>
<p><code>=></code> 代表是 <strong>返回值</strong> 的类型</p>
<p><code>:</code> 后面的都是声明类型，和代码逻辑没有什么关系</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c6a8e940be4b32af49d561abf47f4c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808223036183" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们刚才说了 <code>interface</code> 可以描述各种类型，那么我们用 <code>interface</code> 来描述下函数类型</p>
</blockquote>
<p>注意一点 之前用的 <code>=></code> 来表示返回值类型</p>
<p>这里是在 <code>()</code>后 <code>: 返回值类型</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43b0ca286db34783b0d0609b8083fbbd~tplv-k3u1fbpfcp-watermark.image" alt="image-20210808223626451" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">5.联合类型 <code>union types</code></h3>
<blockquote>
<p>但对于一个变量的类型可能是几种类型的时候我们可以使用 <code>any</code> ，但是 <code>any</code> 的范围是不是有点大了，不到<strong>万不得已</strong>不使用，</p>
<p>我们如果知道是其中的哪几种类型的话，我们就可以使用 <strong>联合类型</strong> 用 <code>|</code> 分隔</p>
</blockquote>
<p>比如下面的例子，<code>haha</code> 可能是 <code>number</code> 或者 <code>string</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0c6c42d49bf415290f1e4bf5be2263b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809090557218" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意</strong>：在没有赋值之前，只能访问<strong>共同的方法、属性</strong>，比如下面的例子,<code>number</code> 没有<code>length</code> 属性</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/200ea90d1743410c9234f98644aa7238~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809091710353" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">6.对象 <code>object</code></h3>
<blockquote>
<p>我们 直接 <code>let a: object;</code> 是不是没有什么意义，因为 <code>js</code> 中对象太多了。。</p>
</blockquote>
<p>我们可以这样来用</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8656e57cf2984664a4de36aa97e764f8~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809113126137" loading="lazy" referrerpolicy="no-referrer"></p>
<p>属性必须在类型 <code>&#123; name: string; age: number; &#125;</code> 中</p>
<h2 data-id="heading-17">4.断言 <code>type inference</code></h2>
<blockquote>
<p>当在上面联合类型的变量传入的时候，我们声明了这个类型为 <code>number | string</code> 它不能不能调用 <code>length</code> 方法</p>
<p>机器没法判断这个类型，但是我们比机器更了解这个类型，我们人为可以指定类型 <code>string</code> 这里我们就可以用到 <strong>类型断言</strong></p>
</blockquote>
<h3 data-id="heading-18">1.我们就用 <code>as</code> 来进行断言</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/763c3ce74ada44f98a4fd99b12e2ce02~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809093348502" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">2.还有一种写法 <code><类型></code> 两者的功能都是一样的</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f334abbe81545dd8830b65ad21a7bb0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809093854727" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">5.类型守卫 <code>type guard</code></h2>
<blockquote>
<p>遇到联合类型的时候，使用 类型守卫可以 缩小范围</p>
</blockquote>
<p>实现以下和上面一样的方法</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4682cf9bc4ae407abd342a06a211bda4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809101137657" loading="lazy" referrerpolicy="no-referrer"></p>
<p>类型守卫 除了 <code>typeof</code> 之外 ，还有 <code>instanceof</code>、 <code>in</code></p>
<h2 data-id="heading-21">6.类 <code>class</code></h2>
<p>在 <code>ES6</code> 中就有 类的概念了，在 <code>TS</code> 中对类添加一些功能，这里只说下几个常用的</p>
<blockquote>
<p>先写个基础的 类</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4b2d90218ed46cbad97df2377f99170~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809115531683" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们先来说下 3个访问修饰符</p>
</blockquote>
<p><code>Public</code>:修饰的属性或方法是共有的 在 <strong>任何地方</strong> 都能访问</p>
<p><code>Private</code>:修饰的属性或方法是私有的 只有 <strong>本类</strong> 中访问</p>
<p><code>Protected</code>:修饰的属性或方法是受保护的 在 <strong>本类</strong> 和 <strong>子类中</strong> 能够访问</p>
<p>比如指定父类中 <code>money</code> 访问权限为 <code>private</code> ,只能在 <code>Parent</code> 访问，子类访问会出错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2c9b4551ad74c868d8f0ac0207bc4b2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809121311868" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以设置访问权限为 <code>protected</code> ，这样子类就能访问</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fbf27f0252a40dc996c6d9c7d6c4bf9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809121140659" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>静态属性 <code>static</code></p>
</blockquote>
<p>上面的 <code>name</code> <code>money</code> 这两个属性都是通过 实例 去访问的</p>
<p>使用 <code>static</code> 修饰的属性是通过 类 去访问，是每个实例共有的</p>
<p>同样 <code>static</code> 可以修饰 方法，用 <code>static</code> 修饰的方法称为 类方法，可以使用类直接调用</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1b4ced0010547dd8f6e1aa9218a001e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809121921373" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>只读 <code>readonly</code></p>
</blockquote>
<p>我们给属性添加上 <code>readonly</code> 就能保证该属性<strong>只读</strong>，<strong>不能修改</strong>，如果存在 <code>static</code> 修饰符，写在其后</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/262d1bbd34a24c2cb01a7b94e39450b6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809122359082" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>抽象类 <code>abstract</code></p>
</blockquote>
<p><code>TS</code> 新增的抽象类，还是简单说下概念吧，我们写一个类的时候，不希望直接使用该类创建实例**（不能被new）**那么我们把它设置为抽象类，让它不能被实例化</p>
<p>只能被继承</p>
<p>在 <code>class</code> 前面 添加 <code>abstract</code> 修饰符，</p>
<p>在抽象类中 可以写 <strong>抽象方法</strong> ，抽象类没有方法体</p>
<p>举个例子：一个动物的抽象类，有个叫的方法，不可能 每个动物的叫声一样吧，我们可以把它设置为抽象方法，具体功能子类进行实现（该怎么叫就由子类来写）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88c739a6e6854eab9ac07c5ec02bb356~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809124627979" loading="lazy" referrerpolicy="no-referrer"></p>
<p>属性的封装和 <code>java</code> 一样，这里就不说了...</p>
<h2 data-id="heading-22">7.接口 <code>interface</code></h2>
<blockquote>
<p>为什么会出现接口</p>
</blockquote>
<p>为了解决 继承 的困境(一个类只能继承另一个类不能实现多继承)</p>
<p>还有一种情况，<strong>人</strong>能够洗衣服，<strong>洗衣机</strong>也能洗衣服，洗衣机和人找不到一个共同的父类，我们可以把洗衣服这个功能抽离出来写成接口，<strong>人</strong> 和 <strong>洗衣机</strong> 去实现这个接口就行</p>
<blockquote>
<p>我们可以用 <code>implements</code> 来实现接口</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fa2ff70b50464b94b89b08797eae53~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809130103041" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>接口可以多实现</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cd58b7a85bd4d1a9b6bc26ff7e188a9~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809130403175" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>接口之前可以继承</p>
</blockquote>
<p>下面这个例子接口继承了另一个接口，这样人类只需实现一个接口就行</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f273eeece14d24be94b6131b84d977~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809130537563" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">8.枚举 <code>enum</code></h2>
<blockquote>
<p>常量是在项目中经常使用，虽然 <code>const</code> 可以声明常量，但是有的常量取值是在一个范围里的，这里我们就需要使用 <code>enum</code> 来进行处理</p>
</blockquote>
<h3 data-id="heading-24">1.数字枚举</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63548257df9d4b21bae08e82b5799450~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809132958670" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>可以修改枚举中的初始值</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38e0a36b9d8145deba2e99edbe329911~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809133132496" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">2.字符串枚举</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be606dacb6ad4cbd8c6f72421222dfb6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809133851968" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">3.常量枚举</h3>
<p>在 <code>enum</code> 前面添加一个 <code>const</code> 即可，它提高了性能</p>
<p>为什么这么说呢，我就把上面字符串枚举编译成 <code>js</code> 例子，和 常量枚举编译 贴出来对比一下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26a0909e7ab940ae9dc280e3407d96ac~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809135017124" loading="lazy" referrerpolicy="no-referrer"></p>
<p>常量枚举直接找出 <code>Week.Tuesday</code> 上面一截都没了</p>
<h2 data-id="heading-27">9.泛型</h2>
<blockquote>
<p>泛型就像一个占位符一个变量，在使用的时候我们可以将定义好的类型像参数一样传入，原封不动的输出</p>
</blockquote>
<p>比如这个例子我们就想返回一个值，在这里我写死是 <code>number</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b1314d6d7704533bc7faa49c1a81fba~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809140308402" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在实际中，未必就是 <code>number</code>，我们就可以通过泛型来解决，定义好的类型传入进去，返回什么类型出来</p>
<blockquote>
<p>泛型简单介绍</p>
</blockquote>
<p>这里 <code>T</code> 是相当于一个占位符,在方法(变量，接口....等等)后面添加 <code><T></code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d74cce6b3334748a7fac4123d5682ac~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809140625111" loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是看起来这么简单，其实还真是</p>
<p>然后我在使用 getValue这个方法的时候 只需要在 <strong>实参</strong> 规定好类型，编译器它也不笨，能够知道我们的参数类型，并将它们赋值给 <code>T</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f32f6b469fbf42888e7161cd3831df05~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809141357325" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>多个参数</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d526a01bd72840b99b9563aa289a972f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809141619617" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在使用的时候，聪明的就判断出 传入的类型，并修改了 <code>T</code>,<code>U</code>，真的很方便</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e322ee42d054492db39710761cda5f57~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809141716507" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们可以使用 <code>interface</code> 来约束 泛型</p>
</blockquote>
<p>在 <code>T</code> 后面 <code>extends Ilen</code>  ，定义 <code>Ilen</code> 里面代码表示，<code>T</code> 必须要有 <code>length</code> 属性</p>
<p>这样在 方法里面调用  <code>params.length</code> 就不会报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffcaa4d26f164af690b0a3ec35687bd2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809151050324" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在 <strong>类</strong>使用泛型</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b956da6a7f504af2baaafa45be79a88c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809152239297" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在 <strong>接口</strong> 使用泛型</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ba740d5d0d144f3b97581d308271fae~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809152813026" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>在 <strong>数组</strong> 使用泛型</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf14ea4ef16b42d3bf21186fb1245119~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809153225159" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实泛型还有很多很多使用方法，这里就简单地入门下</p>
<h2 data-id="heading-28">10.类型别名</h2>
<blockquote>
<p>使用 <code>type</code> 给类型取别名</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/023c42358ecb40e995422df4febe9067~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809154354725" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">11.交叉类型</h2>
<blockquote>
<p>用 <code>&</code> 进行连接</p>
</blockquote>
<p>把类型都组合起来，变量赋值必须满足 交叉类型</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d117a98220c64842b191bfd52bc87b0a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809155259634" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-30">结语：</h2>
<blockquote>
<p>这篇文章是小浪3月多学TS时做的总结，写的不全面写的都是一些经常用到的，全面的话还得写很多很多。。。官方的文档 yyds ，不过大家可以通过这篇文章进行快速入门，，其实小浪用了TS一段时间了，感觉就是有些泛型写的很复杂，规范性很强，很多第三方库隐藏的类型搞不清楚，刚写的完全看不懂，每次写一个东西都要想着去定义类型，恨不得把电脑砸了...开玩笑的，还是得耐心</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31f26491f7948689a2919d10e902e4a~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考资料：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Fdocs%2Fhandbook%2Fbasic-types.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/docs/handbook/basic-types.html" ref="nofollow noopener noreferrer">TS官方文档</a></p></div>  
</div>
            