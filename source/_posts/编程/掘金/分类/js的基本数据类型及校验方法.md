
---
title: 'js的基本数据类型及校验方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3195'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 18:51:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=3195'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今早的地铁看了一个很基础的js面试题，结果悲剧了。。。
那就从头来理一下js的基础吧。</p>
<p>1、js的数据类型</p>
<p>原始类型---保存栈中、赋值是复制变量值</p>
<pre><code class="copyable">null  undefined number  string  boolean  symbol bigint

//symbol是es6新增的数据类型，目的是为了防止属性名的冲突，保证对象中每一个属性名都是独一无二的。
// bigint表示任意大的整数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象类型（引用类型）---保存堆中、赋值是复制引用地址</p>
<pre><code class="copyable">function  array  RegExp Date  Math  Error Set  Map 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、关于检验数据类型的方法</p>
<p><strong>typeof</strong></p>
<p><code>用来判断除了null以外的原始类型的数据，它判断的null是个字符串，但是它可以用来判断对象类型中的function</code></p>
<p><strong>instanceof</strong></p>
<p><code>用它来判断对象类型</code></p>
<p><strong>Object.prototype.toString.call()</strong></p>
<p><code>既可以检测原始数据类型又可以检测对象类型，举个例子</code></p>
<p><code>Object.prototype.toString.call(function()&#123;&#125;)</code> // [object Function]</p>
<p>3、那么在实际的代码中我们需要一个校验数据类型的函数怎么封装一个呢？</p>
<pre><code class="copyable">function checkDataType(obj)&#123;
    const dataType = typeof obj
    if(dataType !== 'object')&#123;
        return dataType
    &#125;
    return Object.prototype.toString.call(obj).slice(8, -1).toLowerCase()
&#125;
console.log(checkDataType('qinggugu')) // string
console.log(checkDataType(1)) // number
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单整理一下，以上校验方法不够完整，欢迎指正补充，感谢~</p></div>  
</div>
            