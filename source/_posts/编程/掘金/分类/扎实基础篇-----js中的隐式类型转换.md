
---
title: '扎实基础篇-----js中的隐式类型转换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4764'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 06:47:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=4764'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>；</p>
<h2 data-id="heading-0">前言</h2>
<p>在上一篇文章<a href="https://juejin.cn/post/6992174698234658852" target="_blank" title="https://juejin.cn/post/6992174698234658852">关于类型</a>中，主要介绍了js里关于类型你可能会忽略的小细节。还不了解的小伙伴可以去学习一下。</p>
<p>这篇文章主要来大家一起规整一下，JS中的隐式类型转换。</p>
<h2 data-id="heading-1">正文</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span> == <span class="hljs-string">'1'</span>; <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们使用在日常业务开发中，我们经常会碰到需要类型转换的问题，像上面这样使用<code>==</code>进行等式的判断，就会先进行隐式类型转换，转换为同一类型后再做比较了。</p>
<h3 data-id="heading-2">基础数据类型相比较</h3>
<p>那么隐式类型转换大概有多少情况呢，可以看以下题目思考一下。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'123'</span> == <span class="hljs-number">123</span>;
<span class="hljs-literal">null</span> == <span class="hljs-literal">undefined</span>;
<span class="hljs-literal">null</span> == <span class="hljs-literal">false</span>;
<span class="hljs-string">'0'</span> == <span class="hljs-literal">true</span>;
<span class="hljs-string">'1'</span> == <span class="hljs-literal">true</span>;
[] == <span class="hljs-literal">false</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面这几个情况，相信你一定不陌生，你所维护的项(lao)目(dai)中(ma)相信见到过这些身影，下面请跟随我一起来完成这几道题目吧。</p>
<ul>
<li><code>'123' == 123</code> 结果为<strong>true</strong>，两个被比较的值如果为<code>String</code>和<code>Number</code>类型，那么就会先将字符串转换为number再进行比较，即<code>123 == 123</code> => <code>true</code>;</li>
<li><code>null == undefined</code> 结果为<strong>true</strong>，<code>undefined</code>及<code>null</code>这两个值只有与<code>undefined</code>、<code>null</code>进行比较时才会返回<code>true</code>，其他情况都返回<code>false</code>;</li>
<li><code>null == false</code> 结果为<strong>false</strong>，这直接应用上一条规则即可，因为比较的值不为<code>undefined</code>或<code>null</code>;</li>
<li><code>'0' == true</code> 结果为<strong>false</strong>，被比较的值中有一个值为<code>Boolean</code>类型，则被比较的值都会转为数字再进行比较，即<code>'0' == 1</code> => <code>0 == 1</code> => <code>false</code>；</li>
<li><code>'1' == true</code> 结果为<strong>true</strong>，同上一条规则，即<code>'1' == 1</code> => <code>1 == 1</code> => <code>true</code>;</li>
<li><code>[] == false</code> 结果为<strong>true</strong>，被比较的值中有一个值为<code>Boolean</code>类型，转为数字再进行比较，即<code>0 == 0</code> => <code>true</code>；</li>
</ul>
<p>了解了这些规则，试着再看一下这几个题目，是不是很简单了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">''</span> == <span class="hljs-literal">null</span>; <span class="hljs-comment">// false 因为和null比较的不是`undefined`及`null`</span>
<span class="hljs-string">''</span> == <span class="hljs-number">0</span>; <span class="hljs-comment">// true 字符串和数字都转为数字比较</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">引用数据类型相比较</h3>
<p>除了基础数据类型，这些还有一种复杂情况，题目如下</p>
<pre><code class="hljs language-js copyable" lang="js">[] == <span class="hljs-string">''</span>;
[] == <span class="hljs-number">0</span>;
[<span class="hljs-number">2</span>] == <span class="hljs-literal">true</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里涉及到了引用<code>Object</code>类型与<code>string</code>、<code>number</code>、<code>object</code>比较，当对象类型和原始类型做相等比较时，对象类型会依照<code>ToPrimitive</code>规则转换为原始类型</p>
<blockquote>
<p><code>ToPrimitive</code>指对象类型类型(如:对象、数组)转换为原始类型的操作。</p>
</blockquote>
<p><code>ToPrimitive</code>规则简单说就是先查找对象的<code>valueOf</code>方法，如果有返回值，那么<code>ToPrimitive</code>的值就是这个值</p>
<p>如果<code>valueOf</code>不存在或者返回的不是原始类型的，那就继续尝试调用对象的<code>toString</code>方法，同样的如果有返回值，那么<code>ToPrimitive</code>的值就是这个值</p>
<p>如果<code>valueOf</code>和<code>toString</code>方法都没有返回原始类型的值，就会抛出异常。</p>
<p>来看根据这个规则再看一下题目</p>
<ul>
<li><code>[] == ''</code> 结果为<strong>true</strong>，<code>[].valueOf() 结果为[]</code> => <code>[].toString() 结果为 ''</code> => <code>'' == ''</code> => <code>true</code>;</li>
<li><code>[] == 0</code> 结果为<strong>true</strong>，<code>[].valueOf() 结果为[]</code> => <code>[].toString() 结果为 ''</code> => <code>'' == 0</code> => <code>true</code>;</li>
<li><code>[2] == true</code> 结果为<strong>false</strong>，<code>[2].valueOf() 结果为[2]</code> => <code>[2].toString() 结果为 '2'</code> => <code>'2' == true</code> => <code>2 == 1</code> => <code>false</code>;</li>
</ul>
<h2 data-id="heading-4">结论</h2>
<p>相信通过今天的讲解，你对隐式类型转换有了更深的理解，熟悉之后你再维护旧项目代码，发现<code>==</code>的判断后肯定就能够更得心应手了。</p>
<p>什么？新项目不行吗？新项目就用<code>===</code>以及强制类型转换吧，这不比记这么多规则香吗？但强制类型转换也有一些需要你记住的规则，感兴趣的小伙伴可以先点个关注，明天我再与你分享<strong>强制类型转换</strong>。</p>
<h2 data-id="heading-5">结语</h2>
<p>前端漫漫长途，我们都在路上，希望可以和小伙伴们一起交流，一起进步。持续更新ing.....</p></div>  
</div>
            