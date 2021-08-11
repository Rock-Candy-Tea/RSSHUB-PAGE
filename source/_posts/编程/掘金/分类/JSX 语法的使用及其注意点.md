
---
title: 'JSX 语法的使用及其注意点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: ''
author: 掘金
comments: false
date: Tue, 10 Aug 2021 19:25:31 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>在使用react开发项目的时候，基本都会使用到JSX 语法，它的主要特点就是，凡是使用 到JavaScript 的值的地方，都可以插入这种类似 HTML 的语法。
React 使用 JSX 来替代常规的 JavaScript。</p>
<p>JSX 是一个看起来很像 XML 的 JavaScript 语法扩展。</p>
<p>我们不需要一定使用 JSX，但它有以下优点：</p>
<ul>
<li>JSX 执行更快，因为它在编译为 JavaScript 代码后进行了优化。</li>
<li>它是类型安全的，在编译过程中就能发现错误。</li>
<li>使用 JSX 编写模板更加简单快速。</li>
</ul>
<pre><code class="copyable">const lut= <h1>love u, tiantian!</h1>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种看起来可能有些奇怪的标签语法既不是字符串也不是 HTML。它被称为 JSX， 一种 JavaScript 的语法扩展。</p>
<p>我们知道元素是构成 React 应用的最小单位，JSX 就是用来声明 React 当中的元素。</p>
<p>与浏览器的 DOM 元素不同，React 当中的元素事实上是普通的对象，React DOM 可以确保 浏览器 DOM 的数据内容与 React 元素保持一致。</p>
<p>要将 React 元素渲染到根 DOM 节点中，我们通过把它们都传递给 ReactDOM.render() 的方法来将其渲染到页面上：</p>
<pre><code class="copyable">var myDivEle = <div className="lut">这是一个jsx</div>; 
ReactDOM.render(myDivEle, document.getElementById('name'));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以在 JSX 中使用 JavaScript 表达式。表达式写在花括号  <strong>&#123;&#125;</strong>  中。实例如下：</p>
<pre><code class="copyable">var myDivEle = <div> <h1>&#123;520+1314&#125;</h1> </div>; 
ReactDOM.render( myDivEle, document.getElementById('name') );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用的时候需要有两个注意的点：</p>
<ul>
<li>所有 HTML 标签必须是闭合的，如果写成<code><h1>love</code>就会报错。如果是那种没有闭合语法的标签，必须在标签尾部加上斜杠，比如<code><img src="" /></code>。</li>
<li>任何 JSX 表达式，顶层只能有一个标签，也就是说只能有一个根元素。下面的写法会报错。</li>
<li>由于 JSX 就是 JavaScript，一些标识符像 <code>class</code> 和 <code>for</code> 不建议作为 XML 属性名。作为替代，React DOM 使用 <code>className</code>和 <code>htmlFor</code> 来做对应的属性。</li>
</ul>
<pre><code class="copyable">// 报错，因为根元素的位置有两个并列的<h1>标签
const lut= <h1>tiantian</h1><h1>520</h1>;

// 不报错，在其外在包裹一个div，就不会报错，因为只允许有一个根元素
const lut= <div><h1>tiantian</h1><h1>520</h1></div>;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            