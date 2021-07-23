
---
title: 'JS 对象基本用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8122'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 11:47:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=8122'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">声明对象的两种语法</h2>
<h4 data-id="heading-1">对象的定义</h4>
<ul>
<li>无序的数据集合</li>
<li>键值对的集合</li>
</ul>
<h4 data-id="heading-2">写法</h4>
<ul>
<li>1.常用的简便写法</li>
</ul>
<p><code>let obj = &#123;'name': 'frank', 'age':18&#125;</code></p>
<ul>
<li>2.正规的写法：let 对象名=new Object(&#123;'键名（属性名）':'键值（属性值）'&#125;)</li>
</ul>
<p><code>let obj = new Object(&#123;'name': 'frank'&#125;)</code></p>
<h4 data-id="heading-3">注意</h4>
<ul>
<li>键名是字符串，不是标识符</li>
<li>引号可以省略，就算引号省略了，键名还是字符串</li>
</ul>
<h4 data-id="heading-4">Object.keys(obj)可以获得名为obj的对象的所有键名（属性名）（key）！</h4>
<h2 data-id="heading-5">如何删除对象的属性</h2>
<ul>
<li>1.delete obj.xxx</li>
<li>2.delete obj['xxx']</li>
</ul>
<p>以上两种写法都可以删除对象obj中名为xxx的属性。</p>
<h4 data-id="heading-6">判断对象中还有没有某个属性名：</h4>
<pre><code class="copyable">'xxx' in obj === ture
'xxx' in obj === false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>xxx是要判断的属性名，obj是对象名。<br>
存在返回true，不存在返回false。</p>
<h4 data-id="heading-7">判断含有属性名，但属性值是不是undefined:</h4>
<pre><code class="copyable">'xxx' in obj && obj.xxx === undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>xxx是要判断的属性名，obj是对象名。<br>
属性值为undefined时返回undefined，否则返回false。</p>
<h2 data-id="heading-8">如何查看对象的属性</h2>
<ul>
<li>查看自身所有属性：<code>Object.keys(obj)</code></li>
<li>查看自身+共有属性：<code>console.dir(obj)</code> 或者 用Object.keys打印出obj._ _ proto_ _</li>
<li>如何判断一个属性是自身的还是共有的<code>obj.hasOwnProperty('XXX')</code></li>
<li>查看某一个属性：<code>obj['name']</code>或者<code>obj.name</code></li>
</ul>
<h2 data-id="heading-9">如何修改或增加对象的属性</h2>
<h4 data-id="heading-10">直接赋值</h4>
<ul>
<li><code>let obj=&#123;'name':'frank'&#125;</code></li>
<li><code>obj.name='frank'</code>其中name是字符串</li>
<li><code>obj['name']='frank'</code></li>
<li><code>obj['na'+'me']='frank'</code></li>
<li><code>let key='name';obj[key]='frank'</code></li>
<li>批量赋值可以用<code>Object.assign(obj,&#123;'age':18,'gender':'man'&#125;)</code>,其中obj是对象名，age键名，18键值</li>
<li></li>
<li>修改共有属性<code>Object.prototype['toString']='xxx'</code></li>
<li>修改隐藏属性<code>let obj = Object.create(common)</code></li>
</ul>
<h2 data-id="heading-11">'name' in obj和obj.hasOwnProperty('name') 的区别</h2>
<ul>
<li><code>'name' in obj</code>查看属性name是否在obj里,但是它无法区分这个属性是自身特有的还是共有的。</li>
<li><code>obj.hasOwnProperty('name')</code>用来检测name是否为obj特有的属性还是共有的属性，如果是特有的返回true，如果是共有的则返回false</li>
</ul></div>  
</div>
            