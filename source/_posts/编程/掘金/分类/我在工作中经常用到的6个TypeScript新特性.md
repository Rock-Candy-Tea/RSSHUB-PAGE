
---
title: '我在工作中经常用到的6个TypeScript新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5296987a15457ebfaa014dfb0e9871~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 16:19:49 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5296987a15457ebfaa014dfb0e9871~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>今天来介绍一下 TypeScript 的一些较新的功能和进展，这些是我在日常工作中经常在用的功能。</p>
<h3 data-id="heading-0">在构造函数中直接定义属性</h3>
<p>Typescript 中可以通过构造函数的参数直接定义属性，我们来先看早期的做法：</p>
<pre><code class="copyable">class Note &#123;
  public title: string;
  public content: string;
  private history: string[];
  
  constructor(title: string, content: string, history: string[]) &#123;
    this.title = title;
    this.content = content;
    this.history = history;
    
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>采用 ts 中简写的语法：</p>
<pre><code class="copyable">class Note &#123;
  constructor(
     public title: string, 
     public content: string, 
     private history: string[]
  )&#123;
    // 这里不用在写 this.title = title
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它可能看上去不像是有属性的类，但它确实有，利用的是 Typescript 提供的简写形式 — 用构造函数的参数直接定义属性。</p>
<p>这个简写语法做了很多：</p>
<ul>
<li>声明了一个构造函数参数及其类型</li>
<li>声明了一个同名的公共属性</li>
<li>当我们 new 出该类的一个实例时，把该属性初始化为相应的参数值</li>
</ul>
<h3 data-id="heading-1">空值合并</h3>
<p><code>??</code>其实没啥意思，就是Nullish Coalescing (空值合并)。听起来有点懵，我们直接上代码</p>
<pre><code class="copyable">const i = undefined
const k = i ?? 5
console.log(k) // 5

// 3.9.2编译
const i = undefined;
const k = i !== null && i !== void 0 ? i : 5;
console.log(k); // 5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候你肯定是想说了这样不就完了吗？</p>
<pre><code class="copyable">let k = i || 5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这样也用，但是你不觉得很不严谨吗？ 如果<code>i = 0</code>呢？</p>
<h3 data-id="heading-2">私有类字段</h3>
<p>TypeScript 3.8 将支持 ECMAScript 私有字段，千万别和 TypeScript private 修饰符 混淆。</p>
<p>这是在 TypeScript 中具有私有类字段的类：</p>
<pre><code class="copyable">class Animal &#123;
  #name: string;
  constructor(theName: string) &#123;
    this.#name = theName;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>private</code>关键字之上使用私有类字段的区别在于前者有更好的运行时保证。用<code>private</code>关键字声明的 TypeScript 字段将在编译后的JavaScript代码中成为常规字段。另一方面，私有类字段在编译后的代码中仍然是私有的。</p>
<p>试图在运行时访问私有类字段将导致语法错误。我们也使用浏览器开发工具也检查不了私有类字段。</p>
<p>有了私有类字段，我们终于在JavaScript中得到了真正的隐私。</p>
<h3 data-id="heading-3">命名元组类型(Labeled tuple types)</h3>
<p>命名元组类型适需要 TypeScript 4.0及以上版本才能使用，它极大的改善了我们的开发体验及效率，先来看一个例子:</p>
<pre><code class="copyable">type Address = [string, number]

function setAddress(...args: Address) &#123;
  // some code here
  console.log(args)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们这样定义函数入参后，在使用函数时，编辑器的智能提示只会提示我们参数类型，丢失了对参数含义的描述。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5296987a15457ebfaa014dfb0e9871~tplv-k3u1fbpfcp-watermark.image" alt="01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了改善这一点，我们可以通过 Labeled tuple types，我们可以这样定义参数：</p>
<pre><code class="copyable">type Address = [streetName: string, streetNumber: number]

function setAddress(...args: Address) &#123;
  // some code here
  console.log(args)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c48fc8105b44e66b2262236e02b860a~tplv-k3u1fbpfcp-watermark.image" alt="02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，在调用函数时，我们的参数就获得了相应的语义，这使得代码更加容易维护。</p>
<h3 data-id="heading-4">模板字面量类型</h3>
<p>自 ES6 开始，我们就可以通过模板字面量（Template Literals）的特性，用反引号来书写字符串，而不只是单引号或双引号：</p>
<pre><code class="copyable">const message = `text`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正如 Flavio Copes 所言，模板字面量提供了之前用引号写的字符串所不具备的特性：</p>
<ul>
<li>
<p>定义多行字符串非常方便</p>
</li>
<li>
<p>可以轻松地进行变量和表达式的插值</p>
</li>
<li>
<p>可以用模板标签创建 DSL（Domain Specific Language，领域特定语言）</p>
</li>
</ul>
<p>模板字面量类型和 JavaScript 中的模板字符串语法完全一致，只不过是用在类型定义里面：</p>
<pre><code class="copyable">type topBottom = "top" | "bottom"
type leftRight = "left" | "right"

type Position = `$&#123;topBottom &#125;-$&#123;leftRight &#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b532f45d41542e6b9f52abf5fe4cbb8~tplv-k3u1fbpfcp-watermark.image" alt="03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们定义了一个具体的字面量类型时，TypeScript 会通过拼接内容的方式产生新的字符串字面量类型。</p>
<h3 data-id="heading-5">实用类型</h3>
<p>TypeScript为你提供了一组实用类型，让你在现有类型的基础上构建新的类型。有许多实用类型涵盖了不同的情况，例如选择类型属性来复制，大写字母，或使所有的属性都是可选的。</p>
<p>下面是一个使用 <code>Omit</code>工具的例子，它复制了原始类型的所有属性，除了我们选择不包括的那些。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/965112b574744b7aa54bcd136acbcb56~tplv-k3u1fbpfcp-watermark.image" alt="04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">type User = &#123;
  name: string
  age: number
  location: string
&#125;

type MyUser = Omit<User, 'name'>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这些就是我工作经常使用的一部分，另外一些后面在分享，就这？</p>
<p>~完，我是刷碗智，准备吵鸡吃，我们下期在见。</p>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.fundebug.com%2F%3Futm_source%3Dxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.fundebug.com/?utm_source=xiaozhi" ref="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<h2 data-id="heading-6">交流</h2>
<p>文章每周持续更新，可以微信搜索「 大迁世界 」第一时间阅读和催更（比博客早一到两篇哟），本文 GitHub <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a>  已经收录，整理了很多我的文档，欢迎Star和完善，大家面试可以参照考点复习，另外关注公众号，后台回复<strong>福利</strong>，即可看到福利，你懂的。</p></div>  
</div>
            