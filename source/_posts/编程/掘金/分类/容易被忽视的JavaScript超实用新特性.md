
---
title: '容易被忽视的JavaScript超实用新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5de3a9b6d6c04fe3b742cd2453ad488d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 01:30:01 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5de3a9b6d6c04fe3b742cd2453ad488d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5de3a9b6d6c04fe3b742cd2453ad488d~tplv-k3u1fbpfcp-watermark.image" alt="js图片.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">容易被忽视的JavaScript超实用新特性</h1>
<p><strong>这是我参与新手入门的第1篇文章</strong></p>
<h2 data-id="heading-1">一.可选链操作符( ?. )</h2>
<p>你可能碰到过这样的情形：当需要访问嵌套在对象内部好几层的属性时，可能会得到这种错误Cannot read property 'xx' of undefined,然后你就要修改你的代码来处理属性链中每一个可能的undefined对象，比如：</p>
<pre><code class="copyable">let nestedProp = obj.first && obj.first.second;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了避免报错，在访问obj.first.second之前，要保证 obj.first 的值既不是 null，也不是 undefined。如果只是直接访问 obj.first.second，而不对 obj.first 进行校验，则有可能抛出错误。</p>
<p>有了可选链操作符（?.），在访问 obj.first.second 之前，不再需要明确地校验 obj.first 的状态，再并用短路计算获取最终结果：</p>
<pre><code class="copyable">let nestedProp = obj.first?.second;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过使用 ?. 操作符取代 . 操作符，JavaScript 会在尝试访问 obj.first.second 之前，先隐式地检查并确定 obj.first 既不是 null 也不是 undefined。如果obj.first 是 null 或者 undefined，表达式将会短路计算直接返回 undefined</p>
<h2 data-id="heading-2">二.空值合并操作符（??）</h2>
<p>我们在开发过程中，经常会遇到这样场景：变量如果是空值，则就使用默认值，我们是这样实现的：</p>
<pre><code class="copyable">let c = a ? a : b // 方式1 
let c = a || b // 方式2 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种方式有个明显的弊端，由于 || 是一个布尔逻辑运算符，左侧的操作数会被强制转换成布尔值用于求值。任何假值（0， ''， NaN， null， undefined）都不会被返回。这导致如果你使用0，''或NaN作为有效值，就会出现不可预料的后果。比如：</p>
<pre><code class="copyable">let count = 0;
let text = "";

let qty = count || 42;
let message = text || "hi!";
console.log(qty);     // 42，而不是 0
console.log(message); // "hi!"，而不是 ""
<span class="copy-code-btn">复制代码</span></code></pre>
<p>空值合并操作符可以避免这种陷阱，其只在第一个操作数为null 或 undefined 时（而不是其它假值）返回第二个操作数：</p>
<pre><code class="copyable">let c = a ?? b; 
// 等价于let c = a !== undefined && a !== null ? a : b; 

const x = null; 
const y = x ?? 500; 
console.log(y); // 500 
const n = 0 
const m = n ?? 9000; 
console.log(m) // 0 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">三.类的私有属性（#）</h2>
<p>最新提案之一是在类中添加私有属性的方法。我们将使用 # 符号表示类的私有属性。这样就不需要使用闭包来隐藏不想暴露给外界的私有属性。</p>
<pre><code class="copyable">class Counter &#123; 
#x = 0; 
​ 
#increment() &#123; 
  this.#x++; 
&#125; 
​ 
onClick() &#123; 
  this.#increment(); 
&#125; 
&#125; 
​ 
const c = new Counter(); 
c.onClick(); // 正常 
c.#increment(); // 报错
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">为什么引用属性时需要符号#？</h4>
<p>1.我们需要允许公有属性和私有属性同名，因此不能采用过去的传统方式去访问一个私有属性。</p>
<p>2.在 JavaScript 中可以采用 this.field 或者 this['field'] 的方式引用公有属性。而由于私有属性是静态的（不能动态添加），它不能支持第二种引用方式。这可能会导致语法上的混乱。</p>
<p>3.会承担额外的检查“代价”。</p>
<p>总之，我们需要使用符号#来标识私有属性，而使用其它方式会造成不可预期的行为和结果，并带来巨大的性能问题。</p>
<p>私有属性对语言来说是一个非常好的补充。</p></div>  
</div>
            