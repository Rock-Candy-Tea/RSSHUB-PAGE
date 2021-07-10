
---
title: '手撕JS方法系列：2-重写内置new'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4609'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 19:46:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=4609'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>需求：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">name</span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
&#125;
Dog.prototype.bark = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'wangwang'</span>);
&#125;
Dog.prototype.sayName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'my name is '</span> + <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-comment">/*
let sanmao = new Dog('小黑');
sanmao.sayName();
sanmao.bark();
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">//=>完成你的代码   </span>
&#125;
<span class="hljs-keyword">let</span> sanmao = _new(Dog, <span class="hljs-string">'小黑'</span>);
sanmao.bark(); <span class="hljs-comment">//=>"wangwang"</span>
sanmao.sayName(); <span class="hljs-comment">//=>"my name is 小黑"</span>
<span class="hljs-built_in">console</span>.log(sanmao <span class="hljs-keyword">instanceof</span> Dog); <span class="hljs-comment">//=>true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>思路：了解new做了哪些事</strong></p>
<ol>
<li>让构造函数中的this指向这个实例对象</li>
<li>this.xxx = xxx 都是给实例对象设置私有属性和方法</li>
<li>如果构造函数没有return或者返回的是原始值，则把创建的实例对象返回；若返回的是对象，则以自己返回的为主</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _new = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params">Ctor, ...params</span>) </span>&#123;
    <span class="hljs-comment">// 1.格式校验：函数 & 有原型对象 & 不是Symbol/BigInt</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Ctor !== <span class="hljs-string">"function"</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;Ctor&#125;</span> is not a constructor!`</span>);
    <span class="hljs-keyword">let</span> name = Ctor.name,
        proto = Ctor.prototype,
        obj,
        result;
    <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^(Symbol|BigInt)$/i</span>.test(name) || !proto) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span> is not a constructor!`</span>);
    
    <span class="hljs-comment">// 2.创建当前类的一个实例对象</span>
    obj = <span class="hljs-built_in">Object</span>.create(proto);
    
    <span class="hljs-comment">// 3.把构造函数像普通函数一样执行，但是this需要指向创建的实例对象</span>
    result = Ctor.call(obj, ...params);
    
    <span class="hljs-comment">// 4.看函数的返回值，如果没有写返回值，或者返回的是原始值，我们默认返回实例对象；</span>
    <span class="hljs-comment">// 如果返回的是对象，则以自己返回的为主；</span>
    <span class="hljs-keyword">if</span> (result !== <span class="hljs-literal">null</span> && <span class="hljs-regexp">/^(object|function)$/i</span>.test(<span class="hljs-keyword">typeof</span> result)) <span class="hljs-keyword">return</span> result;
    <span class="hljs-keyword">return</span> obj;
&#125;;
<span class="hljs-keyword">let</span> sanmao = _new(Dog, <span class="hljs-string">'小黑'</span>);
sanmao.bark(); <span class="hljs-comment">//=>"wangwang"</span>
sanmao.sayName(); <span class="hljs-comment">//=>"my name is 小黑"</span>
<span class="hljs-built_in">console</span>.log(sanmao <span class="hljs-keyword">instanceof</span> Dog); <span class="hljs-comment">//=>true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            