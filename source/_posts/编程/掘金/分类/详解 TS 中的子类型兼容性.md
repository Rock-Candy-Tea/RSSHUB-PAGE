
---
title: '详解 TS 中的子类型兼容性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2531e47feff34569ad6d730fb9fcaed7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sun, 18 Sep 2022 01:47:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2531e47feff34569ad6d730fb9fcaed7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#2c3e50;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;font-weight:600;margin-top:35px;margin-bottom:8px;padding-bottom:5px&#125;.markdown-body h1 :before,.markdown-body h2 :before,.markdown-body h3 :before,.markdown-body h4 :before,.markdown-body h5 :before,.markdown-body h6 :before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:8px;margin-top:50px;font-size:24px;border-bottom:1px solid #eaecef&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #eaecef;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;font-weight:400;background-color:rgba(27,31,35,.05);color:#476582;margin:0;font-size:.85em;border-radius:3px;font-size:.87em;padding:.165em .5em&#125;.markdown-body code,.markdown-body pre&#123;font-family:source-code-pro,Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.6;padding:20px 24px;background-color:#282c34;border-radius:6px&#125;.markdown-body pre>code&#123;font-size:14px;padding:0;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff&#125;.markdown-body a&#123;text-decoration:none;color:#3eaf7c;font-weight:500&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#42b983;border-bottom:1px solid #42b983&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;margin:16px 0;border-collapse:collapse&#125;.markdown-body thead&#123;background:#f6f6f6;background:#3eaf7c;color:#000;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body td,.markdown-body th&#123;border:1px solid #dfe2e5;padding:10px 16px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;font-size:14px;padding:6px 23px;margin:22px 0;border-left:6px solid #42b983;background-color:#f3f5f7;font-weight:400&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body p,.markdown-body ul&#123;line-height:1.7&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" target="_blank" title="https://s.juejin.cn/ds/jooSN7t">点击查看活动详情</a></p>
<h2 data-id="heading-0">简介</h2>
<p>在写 TypeScript 代码时经常遇到类型检查不通过的问题，这些问题根据编译器给出的错误提示以及修改建议多数可以快速修复。本文讲解的内容是编译器进行类型检查时的兼容性相关检查规则，这些规则在 TypeScript 语言背后默默发挥作用。不了解这些规则的话，在遇到兼容性报错只会根据错误提示来修复，若清楚了编译器的子类型赋值兼容性、赋值兼容性等规则，则可以及早规避相关代码错误。</p>
<p>就是说，本文讲的内容是 TypeScript 类型系统的内部工作方式与原理，掌握之后可以做到 <strong>“在编码时将代码在你的大脑里面运行一遍，不用依赖于编译器的类型检查”</strong> 。</p>
<h2 data-id="heading-1">赋值兼容性与子类型兼容性</h2>
<p>在进行赋值、函数调用时传递参数，TypeScript 会对变量进行类型兼容性检查，若类型兼容性检查通过，则说明满足赋值兼容性要求。</p>
<p>一般情况下，若满足子类型兼容性，则一定满足赋值兼容性；然而，满足赋值兼容性，并不一定满足子类型兼容性。</p>
<h3 data-id="heading-2">赋值兼容性特例</h3>
<p>下面三种情况下，满足赋值兼容性，但是不满足子类型兼容性。</p>
<ul>
<li><code>any</code> 类型 下例中变量 <code>t</code> 为 <code>T</code> 类型，<code>any</code> 类型的变量 <code>a</code> 赋值给变量 <code>t</code> 不会导致类型错误，满足赋值兼容性。<code>any</code> 类型为[[顶端类型]]，顶端类型是所有类型的超类型，不是 <code>T</code> 的子类型。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> T &#123;
 <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">let</span> <span class="hljs-attr">t</span>: T
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> <span class="hljs-attr">a</span>: <span class="hljs-built_in">any</span>
t = a
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数字枚举类型 下例中变量 <code>a</code> 为 <code>number</code> 类型，变量 <code>e</code> 为枚举类型 <code>E</code> 赋值给 <code>a</code> 不会导致类型错误，满足赋值兼容性。这里 <code>number</code> 类型能够赋值给数字枚举类型，但是 <code>number</code> 类型却不是数字枚举类型的子类型，不满足子类型兼容性。</li>
</ul>
<pre><code class="hljs language-ini copyable" lang="ini">enum E &#123;
 A,
 B,
 C
&#125;
let <span class="hljs-attr">a</span> = <span class="hljs-number">5</span>
declare let e: E
<span class="hljs-attr">e</span> = a
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>带有可选属性的对象类型 下例中 <code>S</code> 类型能够赋值给 <code>T</code> 类型，满足赋值兼容性，但是 <code>S</code> 类型并不是 <code>T</code> 类型的子类型。因为按照子类型兼容性的要求，若 <code>T</code> 类型上所有的属性（包括可选属性）在 <code>S</code> 类型上都能找到，才算 <code>S</code> 是 <code>T</code> 的子类型，这里 <code>S</code> 上没有 <code>T</code> 上存在的可选属性 <code>b</code>，所以不满足子类型兼容性。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> T &#123;
 <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>;
 b?: <span class="hljs-built_in">string</span>;
&#125;

<span class="hljs-keyword">interface</span> S &#123;
    <span class="hljs-attr">a</span>: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">let</span> <span class="hljs-attr">t</span>: T
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">let</span> <span class="hljs-attr">s</span>: S
t = s
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">子类型与赋值类型差异的原因</h3>
<p>既然上面三种情况不满足子类型兼容性，那为什么 TypeScript 又允许其满足赋值兼容性呢？</p>
<p><strong>情况一：any 类型</strong></p>
<p>any 类型是[[顶端类型]]，根据类型论的解释：顶端类型是所有类型的超类型，确实不会是任何类型的子类型。这属于 TypeScript 类型系统的特例，目的应该是<strong>确保现有的 js 代码在向 ts 代码转移时更容易，可以非常快速的通过 any 类型来绕过 TypeScript 中子类型兼容性限制</strong>。</p>
<p>比如：现有一份功能都已实现的 js 代码，给所有变量 any 类型，基本就可以直接变为 ts 代码，同时类型兼容性还不报错。不过这样一来，TypeScript 也就变成了 <code>AnyScript</code> 了: )。</p>
<p><strong>情况二：数字枚举类型</strong></p>
<p>其实，数字枚举类型被编译为 js 后，在运行时的值就是 <code>number</code> 类型，见下图。之所以，允许 <code>number</code> 类型被赋值给数字枚举类型，也是基于向现有代码兼容的考虑。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2531e47feff34569ad6d730fb9fcaed7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>情况三：带有可选属性的对象类型</strong></p>
<p>TypeScript 中的可选属性修饰符从类型的角度来看其实是给该属性值类型联合了一个 <code>undefined</code> 类型，而 js 中访问对象上不存在的属性和属性值为 <code>undefined</code> 都会得到 <code>undefined</code> 值。在 js 中多数情况下不使用 <code>hasOwnProperty</code> 方法来判断对象的属性是否存在，是没法区分属性不存在还是属性值为 <code>undefined</code>。</p>
<p>TypeScript 的类型系统是在编译时检查的，编译后的代码不存在类型相关代码，所以<strong>为了与现有 js 代码兼容</strong>保留了带有可选属性的对象类型赋值兼容性。就是编译后代码赋值不影响代码执行，但是带有可选属性的对象类型在进行子类型关系检查时是不通过的。</p>
<h2 data-id="heading-4">子类型兼容性</h2>
<p>据面向对象程序设计中[[里氏替换原则]]描述，程序中任何使用了超（父）类型的地方都可以使用其子类型进行替换。TypeScript 中的子类型兼容性体现的就是这一原则，而这也正是<a href="https://juejin.cn/post/7144654082777546765#%E5%A4%9A%E6%80%81" title="#%E5%A4%9A%E6%80%81">多态</a>。</p>
<h3 data-id="heading-5">多态</h3>
<p>多态在类型论中指的是：相同的消息在发送给不同对象时，系统可以根据对象类型不同，分别引发对应类型的方法。</p>
<p>例如，电脑给打印机发出打印消息，彩色打印机和黑白打印机分别执行打印方法，各自打印出彩色照片和黑白照片。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64e21793221947008b288b2fd6ebcd37~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，如果把“打印”这个消息发送给到非打印机设备，比如键盘，那么会怎样呢？</p>
<p>当然是不能执行打印方法，不能正常打印出照片的。那系统是怎么知道键盘不能接受打印消息呢？这就涉及到子类型兼容性了，不能执行打印方法的键盘相当于与打印机不兼容。</p>
<p>在 java 语言中打印机相当于是一个接口，描述了打印机所具备的基本功能（方法），不同类型打印机必须实现了打印机这个接口才是与打印机兼容的。</p>
<p>在 TypeScript 中，也存在基于接口实现的子类型兼容性判断，由于要与 js 语言兼容以及 js 语法特性的历史原因，TypeScript 又对子类型兼容检查制定了更详细的规则。</p>
<h3 data-id="heading-6">符号约定</h3>
<p>子类型兼容性形容的是子类型与超类型的关系（为了便于描述，后文也称作<strong>子类型关系</strong>），这里把这个关系用符号进行一下约定，便于描述。</p>
<p>若类型 <code>S</code> 是类型 <code>T</code> 的子类型，则用符号表示为：</p>
<pre><code class="hljs language-r copyable" lang="r">S <span class="hljs-operator"><</span><span class="hljs-operator">:</span> <span class="hljs-built_in">T</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>任意类型都是自身的子类型和超类型，称为<strong>自反性</strong>，用符号表示为：</p>
<pre><code class="hljs language-ruby copyable" lang="ruby">S <: S 且 S <span class="hljs-symbol">:></span> S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像类的继承一样，子类型与超类型关系具有<strong>传递性</strong>，用符号表示为：</p>
<pre><code class="hljs language-r copyable" lang="r">若
R <span class="hljs-operator"><</span><span class="hljs-operator">:</span> S <span class="hljs-operator"><</span><span class="hljs-operator">:</span> <span class="hljs-built_in">T</span>
则
R <span class="hljs-operator"><</span><span class="hljs-operator">:</span> <span class="hljs-built_in">T</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">基本类型</h3>
<p>基本类型主要包括原始类型、顶端类型、尾端类型，其子类型关系总结如下：</p>
<ol>
<li>
<p>never <: undefined <: null <: [原始类型] number bigint boolean string symbol <: [顶端类型] any unknown</p>
</li>
<li>
<p>字面量类型 <: 相应的原始类型</p>
<ol>
<li>true <: boolean</li>
<li>'a' <: string</li>
<li>0 <: number</li>
<li>0n <: bigint</li>
<li>Symbol() <: symbol</li>
</ol>
</li>
<li>
<p>枚举类型 <: number</p>
</li>
</ol>
<p>用图表示如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db9935798cc0486da68819d414630791~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="TS子类型兼容性1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f16aec807004763a965880259eb917b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="TS子类型兼容性2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">函数类型</h3>
<p>函数类型子类型关系的比较不同于上面简单类型的子类型关系比较，因为函数类型由参数类型、返回值类型构成。</p>
<h4 data-id="heading-9">函数参数数量</h4>
<p>TypeScript 在检查函数子类型关系时，编译器将先检查函数参数数量，具体检查规则如下。</p>
<ul>
<li>规则一：如果 <code>S</code> 是 <code>T</code> 的子类型，即：<code>S <: T</code>，则 <code>S</code> 中所有必选参数必须能够在 <code>T</code> 中找到对应的参数，即 <code>S</code> 中必选参数的个数不能多于 <code>T</code> 中的参数个数。</li>
</ul>
<p>注意：这一点和对象类型的子类型关系刚好相反，后文会讲到。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>规则二：如果 <code>S</code> 是 <code>T</code> 的子类型，即：<code>S <: T</code>，则 <code>T</code> 中的可选参数会计入参数总数，不区分可选参数还是必选参数。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">x?: <span class="hljs-built_in">number</span>, y?: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>规则三：<code>T</code> 中的剩余参数会被当做无穷多个可选参数并计入参数总数，这相当于不进行参数个数检查，因为 <code>S</code> 的参数个数不可能比无穷多还多。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">...x: <span class="hljs-built_in">number</span>[]</span>) =></span> <span class="hljs-built_in">void</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>规则四：子类型 <code>S</code> 中的可选参数不计入参数总数，即 <code>S</code> 中可以存在多余的可选参数。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b?: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>规则五：子类型 <code>S</code> 中的剩余参数不计入参数总数。</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, ...b: <span class="hljs-built_in">number</span>[]</span>) =></span> <span class="hljs-built_in">void</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">void</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">函数参数类型</h4>
<p>TypeScript 检查完函数数量后继续检查函数参数类型，分为两种检查模式：<strong>非严格函数类型检查模式（默认模式）</strong> 、<strong>严格函数类型检查模式</strong>，可以通过 <code>--strictFunctionTypes</code> 编译选项来配置。</p>
<p><strong>非严格函数类型检查模式</strong> 该模式下函数参数类型与函数类型是<strong>双变关系</strong>（双变关系是[[变型]]关系之一）。若函数类型 S 是函数类型 T 的子类型，那么 S 的参数类型必须是 T 中对应参数类型的子类型或者超类型，即只要函数对应位置参数满足子类型关系即可，与子类型关系的方向无关。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 非严格函数类检查</span>
<span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-number">0</span> | <span class="hljs-number">1</span></span>) =></span> <span class="hljs-built_in">number</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">b: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里参数 <code>a</code> 是 <code>b</code> 的子类型，参数 <code>b</code> 是 <code>a</code> 的超类型，因此 S 是 T 的子类型。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dc76cc2e66b4dd1aba235ec809c5165~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Sep-12-2022 00-33-14 1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>严格函数类型检查模式</strong> 该模式下函数参数类型与函数类型是<strong>逆变关系</strong>。若函数类型 S 是函数类型 T 的子类型，那么 S 的参数类型必须是 T 中参数的超类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 严格函数类检查</span>
<span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">b: <span class="hljs-number">0</span> | <span class="hljs-number">1</span></span>) =></span> <span class="hljs-built_in">number</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里参数 <code>a</code> 是 <code>b</code> 的超类型， S 是 T 的子类型，下图用不正确的类型验证并开启严格函数类型检查会报错。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/278e5f1978fe45fea46a4cab80b7a5be~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Sep-12-2022 00-39-00.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">函数返回值类型</h4>
<p>在<strong>非严格函数类型检查模式</strong>和<strong>严格函数类型检查模式</strong>下，函数返回值类型与函数类型始终是<strong>协变关系</strong>。若函数类型 S 是函数类型 T 的子类型，那么 S 的返回值类型必须是 T 返回值类型的子类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-number">0</span>;
<span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">b: <span class="hljs-number">0</span> | <span class="hljs-number">1</span></span>) =></span> <span class="hljs-built_in">number</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里参数 <code>a</code> 是参数 <code>b</code> 的超类型，满足 S 是 T 子类型的函数参数数量及类型条件要求，同时 S 的返回值类型是字面量 <code>0</code> 是 <code>number</code> 类型的子类型。若将 S、T 的返回值类型反过来，则破坏了<strong>协变关系</strong>，导致类型报错，见下图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ea5fc5a05b442a795949059bc00d75e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Sep-12-2022 01-09-45.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">函数重载</h4>
<p>若 S 是 T 的子类型，并且 T 存在函数重载，则 T 的每一个函数重载都能在 S 的函数重载中找到对应的子类型；S 中找到的子类型可以重复使用，就是说 S 的函数重载签名数量可以少于 T 的。</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">S</span> </span>&#123;
    (a: <span class="hljs-keyword">string</span>): <span class="hljs-string">'a'</span>
    (a: <span class="hljs-keyword">string</span>, b: <span class="hljs-keyword">boolean</span>): <span class="hljs-keyword">string</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">T</span> </span>&#123;
    (a: <span class="hljs-keyword">string</span>, b?: <span class="hljs-keyword">boolean</span>): <span class="hljs-keyword">string</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码 S 是 T 的子类型的分析过程如下：</p>
<ol>
<li>T 上具有一个函数重载 <code>(a: string, b?: boolean): string</code> （简称重载 T1），于是去 S 上找对应的函数重载</li>
<li>S 上的函数重载 <code>(a: string): 'a'</code> （简称重载 S1） 和上一步的函数重载按照函数类型的子类型兼容性规则判断兼容性</li>
<li>T1 的参数数量为 2，S1 的参数数量为 1，满足数量要求</li>
<li>S1 的参数类型是 T1 的参数类型的子类型（都是 <code>string</code> 类型，具有<strong>自反性</strong>），满足参数类型要求</li>
<li>S1 返回值类型是 T1 返回值类型的子类型（字符串字面量是 <code>string</code> 类型的子类型），满足返回值类型要求。若修改 S1 的返回值类型将导致不兼容，产生下图报错</li>
<li>这里 TypeScript 编译器根据 S 的函数重载顺序判断 T1 所有重载在找到了对应重载，不再继续往下判断 S 上的另一个重载（但是我们还是继续分析 S 上的另一个重载）</li>
<li>S 上存在另一个重载 <code>(a: string, b: boolean): string</code> （简称 S2），与 T1 按照函数类型的子类型兼容性规则进行判断</li>
<li>T1 的参数数量为 2，S2 的参数数量为 2，满足数量要求</li>
<li>T1、S2 的参数 a 满足类型要求，T1 的参数 b 类型为 <code>boolean | undefined</code> ，S2 的参数 b 类型为 <code>boolean</code> 不满足子类型要求</li>
<li>重载 S2 与重载 T1 不兼容</li>
</ol>
<p>子类型函数重载返回值不兼容导致报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69f1faaa7b114e2e802643cd73e4401b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>子类型函数重载参数类型不兼容导致报错</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ded1297de28475884cc5d4103043d90~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">对象类型</h3>
<p>对象类型是有零个或多个基本类型、函数类型成员组成，比较对象类型的子类型关系时需要分别比较每一个类型成员子类型关系。</p>
<h4 data-id="heading-14">结构化子类型</h4>
<p>TypeScript 中对象类型间的子类型关系取决于对象的结构，对象类型的名称不影响其子类型关系，这一特性叫做[[结构化子类型]]，也可以通俗地理解为[[鸭式辨型]]。</p>
<p>这里类型 S、T 名称不同，但是具有相同成员类型，S 是 T 的子类型，同时 T 也是 S 的子类型，即S、T 满足子类型关系。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1161051a0d194074a80c8a5f58de5b59~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">属性成员类型</h4>
<ul>
<li>若对象类型 S 是对象类型 T 的子类型，则对于 T 中的每一个属性成员 M，都能够在 S 中找到一个同名的属性 N，满足 N 是 M 的子类型。也就是说 S 必须包含 T 中的所有属性成员，T 的属性成员个数不能多于 S 的。该关系也可以简单记为：<strong>协变</strong>。</li>
<li>另外，对象类型 T 中的必选属性成员在 S 中也必须是必选属性成员。</li>
</ul>
<p>这里 S 包含 T 中所有属性成员，满足子类型兼容性</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e30d6b64e8242c5b32d0d072974ce88~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里 T 的必选属性 y 在 S 中不是必选属性，不满足子类型兼容性</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc05e993c804345bd7d71bcdba197e3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">调用签名与构造签名</h4>
<ul>
<li>若对象类型 S 是对象类型 T 的子类型，则对象类型 T 中每一个调用签名 M 都能在对象类型 S 中找到一个调用签名 N，满足 N 是 M 的子类型。该关系也可以简单记为：<strong>协变</strong>。</li>
<li>构造签名的子类型判断规则和调用签名相同，也就是说对象类型的子类型必须包含其超类型的调用签名或构造签名，同时调用签名或构造签名还要满足子类型要求。</li>
</ul>
<h4 data-id="heading-17">字符串索引签名</h4>
<p>若对象类型 S 是对象类型 T 的子类型，如果 T 中存在字符串索引签名（对象类型只能存在一个字符串签名），则 S 中也应该存在字符串索引签名，并且 S 中的字符串索引签名是 T 中字符串索引签名的子类型。该关系也可以简单记为：<strong>协变</strong>。</p>
<h4 data-id="heading-18">数值索引签名</h4>
<p>若对象类型 S 是对象类型 T 的子类型，如果 T 中存在数值索引签名（对象类型只能存在一个数值索引签名），则 S 中也应该存在<strong>数值索引签名或字符串索引签名</strong>，并且是 T 中数值索引签名的子类型。该关系也可以简单记为：<strong>协变</strong>。</p>
<p>若对象类型、接口中同时存在数字索引签名和字符串索引签名时，数值索引签名必须能够赋值给字符串索引签名，因为在 JavaScript 中，对象的属性名只能为字符串或 Symbol，数组的数值索引最终也会被转为字符串索引。<strong>因此，数值索引签名表示的集合是字符串索引签名表示的集合的子集。</strong></p>
<p>所以，与上面字符串索引签名的区别在于，与 T 中对应的可以是数值索引签名或字符串索引签名，相当于把子类型索引签名将类型放宽了，可以和函数类型参数类型的放宽类比。</p>
<h4 data-id="heading-19">类实例类型</h4>
<ul>
<li>在判断两个类之前的子类型关系时，仅检查类的实例成员类型，不检查类的静态成员类型、构造函数类型。</li>
</ul>
<p>这里类 S、T 的构造函数类型不同，类 S 的实例成员类型满足子类型关系（根据对象类型的属性成员类型判规则检查子类型关系），所以 S 是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb61e6c29c294cfbb38b11b48031842b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里修改类 S 的属性 x 的类型，导致类型 S 的实例成员类型子类型关系检查不通过，S 不是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39fec4aa779945d0a5b3938688865f9e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>对于类的私有成员、受保护成员，检查子类型关系时要求其来自于同一个类，即两个类必须存在集成关系。</li>
</ul>
<p>这里类 S 的成员 x 位受保护成员，S 并非继承自 T，故 S 不是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd9731363f64463db7902a295a3a27b2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里 T1 具有私有成员 x，同时 T1 继承自 T，故 T1 是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2bedb9916dc423eb0e3f50604c4ab16~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-20">泛型</h3>
<p><strong>泛型</strong>可以理解为：<strong>类似于函数形参在被函数调用时传入的实参替换</strong>，泛型分为泛型对象类型、泛型函数类型。</p>
<h4 data-id="heading-21">泛型对象类型</h4>
<p>泛型对象类型包含：泛型接口、泛型类、泛型类型别名，TypeScript 在检查其子类型关系时泛型的类型参数不参与，泛型对象的结果对象类型参与。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> <span class="hljs-title class_">Event</span><T> &#123;&#125;
<span class="hljs-keyword">type</span> T = <span class="hljs-title class_">Event</span><<span class="hljs-built_in">string</span>>
<span class="hljs-keyword">type</span> S = <span class="hljs-title class_">Event</span><<span class="hljs-built_in">number</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 <code>Event<T></code> 为泛型接口，其结果类型为[[空对象类型字面量]] <code>&#123;&#125;</code> ，S、T 的类型为泛型接口的结果类型，也为[[空对象类型字面量]] <code>&#123;&#125;</code> 。根据上面<a href="https://juejin.cn/post/7144654082777546765#%E5%AF%B9%E8%B1%A1%E7%B1%BB%E5%9E%8B" title="#%E5%AF%B9%E8%B1%A1%E7%B1%BB%E5%9E%8B">对象类型</a>分析可知，两个空对象类型字面量互相是子类型，即：S 是 T 的子类型，T 也是 S 的子类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> <span class="hljs-title class_">Event</span><T> &#123;
 <span class="hljs-attr">data</span>: T
&#125;
<span class="hljs-keyword">type</span> T = <span class="hljs-title class_">Event</span><<span class="hljs-built_in">string</span>>
<span class="hljs-keyword">type</span> S = <span class="hljs-title class_">Event</span><<span class="hljs-built_in">number</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里类型别名 T 的类型为泛型接口 <code>Event<string></code> 的结果类型，为 <code>&#123; data: string &#125;</code> 类型，称作类型 R1；类型别名 S 的类型为泛型接口 <code>Event<number></code> 的结果类型，为 <code>&#123; data: number &#125;</code> 类型，称作类型 R2。根据<a href="https://juejin.cn/post/7144654082777546765#%E5%AF%B9%E8%B1%A1%E7%B1%BB%E5%9E%8B" title="#%E5%AF%B9%E8%B1%A1%E7%B1%BB%E5%9E%8B">对象类型</a>的子类型关系判断规则可知，R2 上的 number 类型的属性 data 不是 R1 上 string 类型的属性 data 的子类型，故 S 不是 T 的子类型；同理，T 也不是 S 的子类型。</p>
<p>上述代码在 TypeScript 中验证见下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b408e2710b14a0cb3ecd5f6ef196c8b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">泛型函数类型</h4>
<p>与<a href="https://juejin.cn/post/7144654082777546765#%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0%E7%B1%BB%E5%9E%8B" title="#%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0%E7%B1%BB%E5%9E%8B">函数参数类型检查</a>相似，编译器在检查泛型函数类型是也有<strong>非严格泛型函数类型检查</strong>、<strong>严格泛型函数类型检查</strong>两种检查模式，可以通过 <code>--noStrictGenericChecks</code> 编译选项来配置。</p>
<p><strong>非严格泛型函数类型检查</strong> 编译器将所有泛型参数类型替换为 any 类型，然后再按照<a href="https://juejin.cn/post/7144654082777546765#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B" title="#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B">函数类型</a>的子类型关系检查规则来检查子类型兼容性。</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">T</span> = <<span class="hljs-selector-tag">U</span>, <span class="hljs-selector-tag">V</span>>(<span class="hljs-attribute">a</span>: U, <span class="hljs-attribute">b</span>: V) => <span class="hljs-selector-attr">[U, V]</span>
<span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">S</span> = <<span class="hljs-selector-tag">W</span>>(<span class="hljs-attribute">a</span>: W, <span class="hljs-attribute">b</span>: W) => <span class="hljs-selector-attr">[W, W]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码，在非严格泛型函数类型检查模式下，编译器检查步骤如下：</p>
<ol>
<li>替换所有泛型参数为 any 类型</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">any</span>, b: <span class="hljs-built_in">any</span></span>) =></span> [<span class="hljs-built_in">any</span>, <span class="hljs-built_in">any</span>]
<span class="hljs-keyword">type</span> S = <span class="hljs-function">(<span class="hljs-params">a: <span class="hljs-built_in">any</span>, b: <span class="hljs-built_in">any</span></span>) =></span> [<span class="hljs-built_in">any</span>, <span class="hljs-built_in">any</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将泛型参数替换成了具体的类型 any，所以不再是泛型函数签名，去掉泛型参数并成为了普通函数签名。 2. 根据<a href="https://juejin.cn/post/7144654082777546765#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B" title="#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B">函数类型</a>的子类型判断规则依次检查两个函数类型的参数数量、参数类型、返回值类型，这里两个函数签名类型完全相同符合函数类型的子类型关系要求 3. 得出检查结果：S 是 T 子类型，T 也是 S 的子类型</p>
<p><strong>严格泛型函数类型检查</strong> 在严格泛型函数类型检查模式下，编译器不再使用 any 类型替换泛型参数，而是先通过类型推断来统一两个泛型函数的类型参数，再确定两者的子类型关系。</p>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">T</span> = <<span class="hljs-selector-tag">U</span>, <span class="hljs-selector-tag">V</span>>(<span class="hljs-attribute">a</span>: U, <span class="hljs-attribute">b</span>: V) => <span class="hljs-selector-attr">[U, V]</span>
<span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">S</span> = <<span class="hljs-selector-tag">W</span>>(<span class="hljs-attribute">a</span>: W, <span class="hljs-attribute">b</span>: W) => <span class="hljs-selector-attr">[W, W]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假设要检查 T 是否是 S 的子类型，编译器处理步骤如下：</p>
<ol>
<li>尝试使用 S 的类型来推断 T 的类型，得出 T 的参数类型 U、V 都为 W 类型</li>
<li>根据推断将 T 的泛型实例化</li>
</ol>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">T</span> = <<span class="hljs-selector-tag">W</span>>(<span class="hljs-attribute">a</span>: W, <span class="hljs-attribute">b</span>: W) => <span class="hljs-selector-attr">[W, W]</span>
<span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">S</span> = <<span class="hljs-selector-tag">W</span>>(<span class="hljs-attribute">a</span>: W, <span class="hljs-attribute">b</span>: W) => <span class="hljs-selector-attr">[W, W]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>比较泛型实例化后两者的子类型关系，这里两者的类型完全相同</li>
<li>得出结论：T 是 S 的子类型</li>
</ol>
<p><strong>那这里是否能确定 S 是 T 的子类型呢？答案是不能的，因为要确定 S 是 T 的子类型需要反过来使用 T 的类型来推断 S 的类型，具体过程见下面分析。</strong></p>
<p>要检查 S 是否是 T 的子类型，编译器处理步骤如下：</p>
<ol>
<li>尝试使用 T 的类型来推断 S 的类型，得出 S 的参数类型 W 为联合类型 <code>U | V</code></li>
<li>根据推断将 S 的泛型实例化</li>
</ol>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">T</span> = <<span class="hljs-selector-tag">U</span>, <span class="hljs-selector-tag">V</span>>(<span class="hljs-attribute">a</span>: U, <span class="hljs-attribute">b</span>: V) => <span class="hljs-selector-attr">[U, V]</span>
<span class="hljs-selector-tag">type</span> <span class="hljs-selector-tag">S</span> = <<span class="hljs-selector-tag">U</span>, <span class="hljs-selector-tag">V</span>>(<span class="hljs-attribute">a</span>: U | V, <span class="hljs-attribute">b</span>: U | V) => <span class="hljs-selector-attr">[U | V, U | V]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>比较泛型实例化后两者的子类型关系，这里需要判断类型 S 是否是类型 T 的子类型</li>
<li>根据<a href="https://juejin.cn/post/7144654082777546765#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B" title="#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B">函数类型</a>的子类型判断规则依次检查函数参数数量、参数类型、返回值类型，参数数量是满足要求的，但是参数类型、返回值类型不满足函数子类型要求</li>
</ol>
<blockquote>
<p>这里判断 <code>U | V</code> 是否是 U 的超类型（非严格函数类型检查模式）、或是否具有子类型关系（严格函数类型检查模式）时，需要知道联合类型的子类型判断规则，见下文说明。</p>
</blockquote>
<ol start="3">
<li>得出结论：S 不是 T 的子类型</li>
</ol>
<p>这里 S 不是 T 的子类型验证见下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/963a0b56ac0848bb935e286522541933~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/144cd7c85be44ab1a6eb26f76ae4eb36~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">联合类型</h3>
<p>联合类型由若干成员类型构成，检查联合类型时需要考虑各个成员类型的子类型关系。检查规则为：若 S 的所有成员类型都是类型 T 的子类型，则 S 是 T 的子类型，也是[[联合类型]]中<strong>交集</strong>的概念。</p>
<p>这里 S 的成员类型 <code>0</code>、<code>1</code> 都是 T 的子类型，所以 S 也是 T 的子类型。</p>
<pre><code class="hljs language-ini copyable" lang="ini">type <span class="hljs-attr">T</span> = number
type <span class="hljs-attr">S</span> = <span class="hljs-number">0</span> | <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 S 的成员类型 <code>string</code> 不是 T 的子类型，所以 S 不是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4f7f01f19894ef5bb27cb82f812c998~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里 S 和 T 都是联合类型，S 的成员类型 <code>1</code> 和 <code>a</code> 都是 <code>number | string</code> 的子类型，所以 S 是 T 的子类型。</p>
<pre><code class="hljs language-ini copyable" lang="ini">type <span class="hljs-attr">T</span> = number | string
type <span class="hljs-attr">S</span> = <span class="hljs-number">1</span> | <span class="hljs-string">'a'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>联合类型 <code>number</code> | <code>string</code> 表示类型是 <code>number</code> <code>string</code> 类型之一，而字面量类型 <code>1</code> 是 <code>number</code> 类型的子类型，所以 <code>1</code> 是 <code>number | string</code> 的子类型，<code>a</code> 是 <code>number | string</code> 的子类型的推导同样。</p>
</blockquote>
<h3 data-id="heading-24">交叉类型</h3>
<p>交叉类型由若干成员类型构成，检查交叉类型时需要考虑各个成员类型的子类型关系。检查规则为：若 S 至少有一个成员类型是类型 T 的子类型，则 S 是 T 的子类型，也是[[交叉类型]]中<strong>并集</strong>的概念。</p>
<p>这里 S 的成员类型 <code>number</code> 是 T 的子类型，所以 S 是 T 的子类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> T = <span class="hljs-built_in">number</span>
<span class="hljs-keyword">type</span> S = <span class="hljs-built_in">number</span> & <span class="hljs-built_in">string</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 S 的所有成员类型都不是 T 的子类型，所以 S 不是 T 的子类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96cf143b6d534e2eb1c2cc59b9292f8b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里 S 的成员类型都不是 T 的子类型，但是 S 却是 T 的子类型，因为 S 的结果类型为 <code>never</code> 类型，而 <code>never</code> 为[[尾端类型]]是所有类型的子类型。</p>
<pre><code class="hljs language-ini copyable" lang="ini">type <span class="hljs-attr">T</span> = number
type <span class="hljs-attr">S</span> = <span class="hljs-string">'a'</span> & <span class="hljs-string">'b'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>S 的结果类型为 <code>never</code> 类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9906cdf3199a47beb3df15bfaba806e1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">一些疑难点</h2>
<h3 data-id="heading-26">函数的子类型兼容性描述的是函数，而多态描述的是对象，两者相同？</h3>
<p>在上文中<a href="https://juejin.cn/post/7144654082777546765#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B" title="#%E5%87%BD%E6%95%B0%E7%B1%BB%E5%9E%8B">函数类型</a>提到使用子类型替换超类型这一原则就是多态，为何函数的子类型关系也能用多态来解释？</p>
<blockquote>
<p>据面向对象程序设计中[[里氏替换原则]]描述，程序中任何使用了超（父）类型的地方都可以使用其子类型进行替换。TypeScript 中的子类型兼容性体现的就是这一原则，而这也正是<a href="https://juejin.cn/post/7144654082777546765#%E5%A4%9A%E6%80%81" title="#%E5%A4%9A%E6%80%81">多态</a>。</p>
</blockquote>
<p><strong>解答如下：</strong></p>
<p>在 js 中函数也是对象，TypeScript 中将其类型描述为具有调用签名的对象，详细可见[[函数签名]]。所以，函数的子类型关系也属于对象类型的子类型关系，也算是多态。</p></div>  
</div>
            