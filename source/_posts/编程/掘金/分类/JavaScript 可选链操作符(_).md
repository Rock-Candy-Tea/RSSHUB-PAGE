
---
title: 'JavaScript 可选链操作符(_.)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2182'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 06:30:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=2182'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>可选链操作符( ?. )允许读取位于连接对象链深处的属性的值，而不必明确验证链中的每个引用是否有效。?. 操作符的功能类似于 . 链式操作符，不同之处在于，在引用为空(null 或者 undefined) 的情况下不会引起错误，该表达式短路返回值是 undefined。与函数调用一起使用时，如果给定的函数不存在，则返回 undefined。</p>
<p>当尝试访问可能不存在的对象属性时，可选链操作符将会使表达式更短、更简明。</p>
<h1 data-id="heading-0">一、语法</h1>
<pre><code class="copyable">obj?.prop;
obj?.[expr];
arr?.[index];
func?.(args);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>额，先来简单的使用下：</p>
<pre><code class="copyable">const obj = &#123;
    name: '山呱呱',
    foo: &#123;
      bar: &#123;
        baz: 18,
        fun: ()=>&#123;&#125;
      &#125;,
    &#125;,
    school: &#123;
        students: [&#123;
            name: 'shanguagua'
        &#125;]
    &#125;,
    say() &#123;
        return 'www.shanzhonglei.com'
    &#125;
  &#125;;

  console.log(obj?.foo?.bar?.baz);  // 18

  console.log(obj?.school?.students?.[0]['name']) // shanguagua

  console.log(obj?.say?.()) // www.shanzhonglei.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>操作符会隐式检查对象的属性是否为null或undefined，代码更加优雅简洁。</p>
<pre><code class="copyable">const name = obj?.name;
const name1 = obj === null || obj === undefined ? undefined : obj.name; // 等同于
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">二、使用场景</h1>
<h2 data-id="heading-2">2.1 与函数调用结合</h2>
<pre><code class="copyable">// 若obj有属性method但method不是函数, 则也会报错
const result = obj?.method?.();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.2 处理可选的回调函数</h2>
<pre><code class="copyable">function invoke(fn) &#123;
  if (fn) &#123;
    fn.call(this);
  &#125;
&#125;

// 写法更加简洁
function betterInvoke(fn) &#123;
  fn?.call(this);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2.3 可选链和表达式</h2>
<pre><code class="copyable">const obj = &#123;
    propName: 'name'
&#125;;
console.log(obj?.['prop' + 'Name']); // name
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">2.4 可选链不能用于赋值</h2>
<pre><code class="copyable">const obj = &#123;
    propName: 'name'
&#125;;
obj?.['propName'] = 'new name'; // Syntax Error
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">2.5 访问数组元素</h2>
<pre><code class="copyable">const first = arr?.[0];
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2.6 短路特性</h2>
<p>当可选链左侧为null 或 undefined 时, 后续操作不会执行。</p>
<pre><code class="copyable">const name = a?.b?.c?.d;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但在实际开发中，我们需要一个默认的值，此时就可以使用双问号??操作符。</p>
<pre><code class="copyable">const name = a?.b?.c?.d??'shanguagua';
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            