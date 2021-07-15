
---
title: '06-TypeScript对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e6d321e52440ccaea7a576bb256374~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:09:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e6d321e52440ccaea7a576bb256374~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在各种面向对象的语言中， 如Java， Python， C#等， 都有对象的概念， 有这样一句解释 --- 万物皆对象， 那么对象到底是个什么东西， 怎么就万物皆对象了。 实际上， 对象这个概念非常的抽象， 一个人， 一辆车， 一台电脑都可以成为对象。</p>
<p>对象又是怎样产生的呢？ 类产生对象。 类可以理解成类别的意思， 相当于对象的模版。 类中包含属性和方法。 如手机类中包含手机品牌属性， 颜色属性， 价格属性； 包含打电话的方法。 苹果手机， 小米手机就是手机类的对象。 用代码这样表示</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Phone</span> </span>&#123;
    <span class="hljs-comment">// 属性</span>
    <span class="hljs-attr">brand</span>: <span class="hljs-built_in">string</span>;
    price: <span class="hljs-built_in">number</span>;
    <span class="hljs-comment">// 构造函数</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">brand: <span class="hljs-built_in">string</span>, price: <span class="hljs-built_in">number</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.brand = brand;
        <span class="hljs-built_in">this</span>.price = price;
    &#125;
    <span class="hljs-comment">// 方法</span>
    <span class="hljs-function"><span class="hljs-title">call</span>(<span class="hljs-params">brand: <span class="hljs-built_in">string</span></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;brand&#125;</span>手机可以打电话`</span>);
    &#125;
&#125;
 
<span class="hljs-keyword">let</span> iPhone = <span class="hljs-keyword">new</span> Phone(<span class="hljs-string">"苹果"</span>, <span class="hljs-number">8699</span>); <span class="hljs-comment">// iPhone是类Phone的对象（实例）</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`手机的品牌是：<span class="hljs-subst">$&#123;iPhone.brand&#125;</span>`</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`手机的价格是：<span class="hljs-subst">$&#123;iPhone.price&#125;</span>元`</span>);
iPhone.call(iPhone.brand);

<span class="hljs-keyword">let</span> xiaomi = <span class="hljs-keyword">new</span> Phone(<span class="hljs-string">"小米"</span>, <span class="hljs-number">5699</span>); <span class="hljs-comment">// xiāomi是类Phone的对象（实例）</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`手机的品牌是：<span class="hljs-subst">$&#123;xiaomi.brand&#125;</span>`</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`手机的价格是：<span class="hljs-subst">$&#123;xiaomi.price&#125;</span>元`</span>);
xiaomi.call(xiaomi.brand);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e6d321e52440ccaea7a576bb256374~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            