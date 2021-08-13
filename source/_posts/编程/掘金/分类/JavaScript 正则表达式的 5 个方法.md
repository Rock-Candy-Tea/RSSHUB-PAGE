
---
title: 'JavaScript 正则表达式的 5 个方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5633'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 23:57:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=5633'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>【这是我参与8月更文挑战的第 <strong>13</strong> 天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a>】</p>
<p>现在 JavaScript 非常强大，可以用它做很多事情，移动应用程序、网站、网络应用程序、游戏，甚至可以包括人工智能。JavaScript 生态系统有很多脚本库和框架，可以用它来做很多事情。</p>
<p>除此之外，JavaScript 每年都会有一些新的非常有用功能增加，感谢 ECMAScript 规范，现在有很多方法可以用于 JavaScript 中的不同数据类型。</p>
<p>在本文中，将介绍一些 JavaScript 中的编写正则表达式的常见用法。</p>
<h3 data-id="heading-0">1. match()</h3>
<p><code>match()</code> 与字符串一起使用以检查字符串和正则表达式 <code>regex</code> 之间的匹配，以正则表达式为参数。</p>
<p>语法：</p>
<pre><code class="copyable">str.match(regex);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法返回 3 个可能的值：</p>
<ul>
<li>如果正则表达式包含一个 <code>g</code> 标记，即为全局匹配，它将返回一个包含所有匹配项的数组，没捕获组信息；</li>
<li>如果正则表达式没有 <code>g</code> 标记，它将返回一个包含第一个匹配项和其相关的捕获组的数组；</li>
<li>如果根本没有匹配项，则返回 <code>null</code> 。</li>
</ul>
<blockquote>
<p><code>groups</code>：一个命名捕获组的对象，其键是名称，值为捕获组，如果未定义命名捕获组，则为 <code>undefined</code>。</p>
</blockquote>
<p>带有标记 <code>g</code>  的实例代码：</p>
<pre><code class="copyable">const strText = "Hello China";
const regex = /[A-Z]/g; // 大写字母正则表达式
console.log(strText.match(regex)); // [ 'H', 'C' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有标记 <code>g</code>  的实例代码：</p>
<pre><code class="copyable">const text = 'Hello World';
const regex = /[A-Z]/; //Capital letters regex.
console.log(text.match(regex)); // [ 'H', index: 0, input: 'Hello China', groups: undefined ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当没有匹配的实例代码：</p>
<pre><code class="copyable">const strText = "hello china";
const regex = /[A-Z]/; // 大写字母正则表达式
console.log(strText.match(regex)); // null
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. test()</h3>
<p><code>test()</code> 用于测试指定字符串和正则表达式之间是否匹配，接受一个字符串作为其参数，并根据是否匹配返回 <code>true</code> 或 <code>false</code> 。</p>
<p>假设在下面的字符串 <code>strText</code> 中检测单词 <code>china</code> 是否存在。可以为查找单词创建一个正则表达式并测试该正则表达式和字符串 <code>strText</code> 之间是否匹配。</p>
<pre><code class="copyable">const strText = "hello china";
const regex = /china/;
console.log(regex.test(strText)); // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是没有匹配的实例代码：</p>
<pre><code class="copyable">const strText = "hello China";
const regex = /china/;
console.log(regex.test(strText)); // false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可以看到，大小写是会影响匹配的结果，如果需要忽略大小写，则需要使用标记 <code>i</code>，如下代码：</p>
<pre><code class="copyable">const strText = "hello China";
const regex = /china/i;
console.log(regex.test(strText)); // true
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>请注意，在语法上 <code>.match()</code> 与 <code>.test()</code>  在使用上是 “相反” 的</p>
</blockquote>
<h3 data-id="heading-2">3. search()</h3>
<p>search() 方法是一个字符串方法，可以将其与正则表达式一起使用。可以将正则表达式作为参数传递给它，以在字符串中搜索匹配项。</p>
<p>方法返回第一个匹配项在整个字符串中的位置（<code>索引</code>），如果没有匹配项，则返回  <code>-1</code>。</p>
<p>匹配的实例：</p>
<pre><code class="copyable">const strText = "hello china，i love china";
const regex = /china/;
console.log(strText.search(regex)); // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有匹配的实例：</p>
<pre><code class="copyable">const strText = "hello china，i love china";
const regex = /devpoint/;
console.log(strText.search(regex)); // -1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. replace()</h3>
<p><code>replace()</code> 是在字符串中搜索指定的值或正则表达式并将其替换为另一个值，方法接受两个参数：</p>
<ol>
<li>要搜索的值</li>
<li>要替换的新值</li>
</ol>
<p>方法返回一个包含被替换后的新字符串，<strong>需要注意的是，它不会改变原始字符串，并且只会替换搜索到的第一个值</strong>。</p>
<p>实例代码：</p>
<pre><code class="copyable">const strText = "hello world,i love world";
const regex = /world/;
console.log(strText.replace(regex, "china")); // hello china,i love world
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. replaceAll()</h3>
<p><code>replaceAll()</code> 类似于方法 <code>replace()</code> ，但它允许替换字符串中所有匹配的值或正则表达式。</p>
<p>它接受两个参数：</p>
<ol>
<li>要搜索的值，如果是正则，则必须带上全局标记 <code>g</code></li>
<li>要替换的新值</li>
</ol>
<p>它返回一个包含所有新值的新字符串，同样也不会更改原始字符串。</p>
<p>实例代码：</p>
<pre><code class="copyable">const strText = "hello world,i love world";
const regex = /world/g;
console.log(strText.replaceAll(regex, "china")); // hello china,i love china
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等效于如下代码：</p>
<pre><code class="copyable">const strText = "hello world,i love world";
console.log(strText.replaceAll("world", "china")); // hello china,i love china
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过正则查找替换，在正则表达式中加上全局标记 <code>g</code> , 同样可以替换所有符合正则条件的字符串，如下代码：</p>
</blockquote>
<pre><code class="copyable">const strText = "hello world,i love world";
const regex = /world/g;
console.log(strText.replace(regex, "china")); // hello china,i love china
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">总结</h3>
<p>本文介绍了可以与正则表达式一起使用的常用方法，在项目中常用且有用，如表单验证、密码验证等。</p></div>  
</div>
            