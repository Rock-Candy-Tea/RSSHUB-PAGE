
---
title: 'javascript面向对象（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbab62b12ed54cc2b20e21eee6ddcb6c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 20:24:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbab62b12ed54cc2b20e21eee6ddcb6c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">对象</h2>
<blockquote>
<p>1.面向对象中一个对象就是一个独立的功能块，但页面上同一个功能可能会有多处使用</p>
</blockquote>
<p>2.类：把功能相似的代码归为一个类，当需要使用该功能时，通过类来生成相应的功能对象</p>
<h2 data-id="heading-1">工厂模式</h2>
<blockquote>
<p>最常用的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 工厂模式</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HRBP</span>(<span class="hljs-params">name,gender</span>)</span>&#123;
            <span class="hljs-keyword">return</span>&#123;
                name,
                gender,
                <span class="hljs-function"><span class="hljs-title">jobA</span>(<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'公司经营计划'</span>);
                &#125;,
                <span class="hljs-function"><span class="hljs-title">jobB</span>(<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'人事调动'</span>);
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">let</span> 张三 = HRBP(<span class="hljs-string">'rose'</span>,<span class="hljs-string">'女'</span>)
        <span class="hljs-built_in">console</span>.log(张三);
        张三.jobA()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">new运算符</h2>
<blockquote>
<p>new运算符专属于函数
new 运算：根据函数中的代码操作，实例化一个对象</p>
<blockquote>
<ol>
<li>new 函数，默认情况下会返回一个对象</li>
<li>new 运算时，函数中的 this 会指向实例化之后 对象</li>
<li>new 运算时，会直接执行函数，可以不加()，除非需要传参</li>
</ol>
</blockquote>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HRBP</span>(<span class="hljs-params">name,gender</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.gender = gender;
        <span class="hljs-built_in">this</span>.jobA=<span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'公司经营计划'</span>);
        &#125;
    &#125;         
    <span class="hljs-keyword">let</span> 李四 = <span class="hljs-keyword">new</span> HRBP(<span class="hljs-string">'李四'</span>,<span class="hljs-string">'男'</span>) <span class="hljs-comment">//如果不需要参数的话可以不加()</span>
    
    <span class="hljs-built_in">console</span>.log(李四);
    李四.jobA()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">原型、原型链</h2>
<blockquote>
<p>prototype 原型 (原型对象，类的原型)
==在工厂模式中当我们在定义不同的实例化对象并调用jobA函数时，每次都会重新创建实例化对象里面的jobA函数，这样就会造成性能问题==</p>
<blockquote>
<p>而在<code>JavaScript中</code>，每当定义一个函数数据类型(普通函数、类)时候，都会天生自带一个<code>prototype</code>属性，这个属性指向函数的<code>原型对象</code>。原型对象就相当于一个公共的区域，所有同一个类的实例化对象都可以访问到这个原型对象，<code>所以</code>我们可以将对象中共有的内容，统一设置到原型对象中。</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 原型</span>
<span class="hljs-comment">/*
function HRBP(name,gender)&#123;
            this.name = name;
            this.gender = gender;
            this.jobA=()=>&#123;
            console.log('公司经营计划');
        &#125;
    &#125;         
    let 李四 = new HRBP('李四','男');
    let 张三 = new HRBP('张三','男');
    console.log(李四.jobA === 张三.jobA);  //false
    */</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HRBP</span>(<span class="hljs-params">name,gender</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.name = name;
            <span class="hljs-built_in">this</span>.gender = gender;
    &#125;         
    HRBP.prototype.jobA=<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'公司经营计划'</span>);
    &#125;
    <span class="hljs-keyword">let</span> 李四 = <span class="hljs-keyword">new</span> HRBP(<span class="hljs-string">'李四'</span>,<span class="hljs-string">'男'</span>);
    <span class="hljs-keyword">let</span> 张三 = <span class="hljs-keyword">new</span> HRBP(<span class="hljs-string">'张三'</span>,<span class="hljs-string">'男'</span>);
    <span class="hljs-built_in">console</span>.log(李四.jobA === 张三.jobA);  <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>原型链：对象的<code>__proto__ </code>属性，在__proto__ 属性中，存储的时其构造函数的原型对象的引用地址。</p>
<blockquote>
<p>当我们调用对象的某个属性或方法时，在对象自身找不到就会去找对象的<code>__proto__</code>属性，然后通过 <code>__proto__ </code>访问到其构造函数的原型链。直到找到<code>Object</code>对象的原型，Object对象的原型没有原型，如果在Object原型中依然没有找到，则返回undefined。</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">Object</span>.prototype.jobC = <span class="hljs-function">()=></span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'支付薪水'</span>);
   &#125;
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">HRBP</span>(<span class="hljs-params">name,gender</span>)</span>&#123;
           <span class="hljs-built_in">this</span>.name = name;
           <span class="hljs-built_in">this</span>.gender = gender;
   &#125;         
   HRBP.prototype.jobA=<span class="hljs-function">()=></span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'公司经营计划'</span>);
   &#125;
   <span class="hljs-keyword">let</span> 李四 = <span class="hljs-keyword">new</span> HRBP(<span class="hljs-string">'李四'</span>,<span class="hljs-string">'男'</span>);
   <span class="hljs-keyword">let</span> 张三 = <span class="hljs-keyword">new</span> HRBP(<span class="hljs-string">'张三'</span>,<span class="hljs-string">'男'</span>);
   <span class="hljs-built_in">console</span>.log(李四.jobA === 张三.jobA);  <span class="hljs-comment">//true</span>
   张三.jobC();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">原型与原型链图片：</h2>
<p>==原型：==
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbab62b12ed54cc2b20e21eee6ddcb6c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
==原型链==
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f98d205b92c6491197bbf7b630ce4019~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文为博主原创文章，不得用于商业用途，转载请注明出处，谢谢。
本文链接：<a href="https://blog.csdn.net/zxhzm_life/article/details/118299700" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/zxhzm_life/…</a></p></div>  
</div>
            