
---
title: 'new()和create()的原理，区别和实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3218'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 14:13:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=3218'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">原型，构造函数 ，和实例的关系</h2>
<p>开始探究new()和create()前 先整理下 原型，构造函数 ，和实例的关系</p>
<ul>
<li>实例=new 构造函数()</li>
<li>实例.<strong>prototype</strong> 指向原型</li>
<li>构造函数的.prototype 指向原型;</li>
<li>原型的本质是一个对象</li>
<li>实例.<strong>prototype</strong>===构造函数的.prototype 指向原型;</li>
<li>原型.constructor指向构造函数</li>
<li>实例.constructor也指向构造函数因为实例自己没有此属性,会去找原型的相关属性,也就指向构造函数,</li>
<li>构造函数的prototype在不指向的情况下指向Object,Object的prototype指向null</li>
<li>原型也可能有自己的原型，那么就形成了原型链，实例在查询某个属性时 会沿着原型链逐级向上查找直到找到目标属性（这就是继承）</li>
</ul>
<h2 data-id="heading-1">new</h2>
<h3 data-id="heading-2">new的使用</h3>
<pre><code class="copyable">function A ()&#123;&#125;
const a=new A()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">new的原理</h3>
<ol>
<li>创建一个空对象</li>
<li>空对象的__proto__属性指向构造函数的prototype属性 指向同一个原型</li>
</ol>
<h3 data-id="heading-4">new的实现</h3>
<pre><code class="copyable">const a=&#123;&#125;
a.__proto__=A.proptotype
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">单纯的原型链继承弊端</h3>
<ul>
<li>原型的属性是被所有实例共享的(继承的弊端)，会存在实例篡改属性问题</li>
</ul>
<p>其他的继承方式----待更新</p>
<h2 data-id="heading-6">ceate</h2>
<h3 data-id="heading-7">ceate的使用</h3>
<pre><code class="copyable">const obj=Object.create(func)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">ceate的原理</h3>
<ol>
<li>ceate方法里创建一个对象(构造函数)</li>
<li>对象的 prototype属性指向，ceate方法的人参</li>
<li>返回 该对象的实例</li>
</ol>
<h3 data-id="heading-9">ceate的实现</h3>
<pre><code class="copyable">function create(prpto)&#123;
  function Fn()&#123;&#125;
  Fn.prototype=proto;
  return new Fn()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">new和 ceate的区别</h2>
<ul>
<li>new 实例化的对象原型指向的是构造函数的原型</li>
<li>create生成的对象的原型指向的是 Object.create(proto) 的入参</li>
</ul></div>  
</div>
            