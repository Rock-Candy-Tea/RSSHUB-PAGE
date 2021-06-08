
---
title: 'Javascript复习第五天'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c2d8900d9247c1b3ce69f270ba6b02~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 17:44:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c2d8900d9247c1b3ce69f270ba6b02~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>这是我参与更文挑战的第6天，活动详情查看：</code><a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">原型</h3>
<p>每一个函数都有一个prototype属性，它的值是一个对象</p>
<p>对于普通函数来说， 它的作用不大</p>
<p>但是对于构造函数，作用：实例共享方法</p>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">People</span>(<span class="hljs-params">name, age, sex</span>) </span>&#123;
<span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.age = age;
<span class="hljs-built_in">this</span>.sex = sex;
&#125;

<span class="hljs-comment">// 其实我们使用布兰达艾奇为我们提供的People.prototype属性添加方法，并且也不需要在函数中定义函数名</span>
People.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"你好"</span>);
&#125;

<span class="hljs-comment">// 实例化对象</span>
<span class="hljs-keyword">var</span> xiaoming = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"小明"</span>, <span class="hljs-number">12</span>, <span class="hljs-string">"男"</span>);
<span class="hljs-keyword">var</span> xiaohong = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"小红"</span>, <span class="hljs-number">12</span>, <span class="hljs-string">"女"</span>);
xiaoming.say();
xiaohong.say();


<span class="hljs-built_in">console</span>.log(xiaoming.say === xiaohong.say);
<span class="hljs-comment">// 原型的作用: 实例共享方法</span>
<span class="hljs-comment">// 构造函数的方法要写在原型上</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">hasOwnProperty</h4>
<p>该方法是检测某个方法是否在构造函数中</p>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义一个构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">People</span>(<span class="hljs-params">name, age, sex</span>) </span>&#123;
<span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.age = age;
<span class="hljs-built_in">this</span>.sex = sex;
<span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"你好"</span>);
&#125;
&#125;

<span class="hljs-comment">// 方法写在原型上</span>
People.prototype.intro = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"大家好, 我今年"</span> + <span class="hljs-built_in">this</span>.age + <span class="hljs-string">"岁了"</span>);
&#125;


<span class="hljs-comment">// 实例化对象</span>
<span class="hljs-keyword">var</span> xiaoming = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"小明"</span>, <span class="hljs-number">12</span>, <span class="hljs-string">"男"</span>);
<span class="hljs-keyword">var</span> xiaohong = <span class="hljs-keyword">new</span> People(<span class="hljs-string">"小红"</span>, <span class="hljs-number">12</span>, <span class="hljs-string">"女"</span>);
xiaoming.say();
xiaoming.intro();
xiaohong.say();
xiaohong.intro();

<span class="hljs-comment">// 同样是方法， 如何区别方法是在构造函数中还是在原型上？</span>
<span class="hljs-built_in">console</span>.log(xiaoming.hasOwnProperty(<span class="hljs-string">"say"</span>) ? <span class="hljs-string">"say在身上"</span> : <span class="hljs-string">"say不在身上"</span>);
<span class="hljs-built_in">console</span>.log(xiaohong.hasOwnProperty(<span class="hljs-string">"intro"</span>) ? <span class="hljs-string">"intro在身上"</span> : <span class="hljs-string">"intro不在身上"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">安全类</h3>
<p>定义: 无论外部如何调用类， 得到的都是一个类的实例化对象</p>
<p>解决问题： 有些程序员，不使用new来调用构造函数，可能导致代码出现一些问题</p>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">People</span>(<span class="hljs-params">name, age, sex</span>) </span>&#123;
<span class="hljs-comment">// 判断this指向谁，从而决定代码如何执行</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> === <span class="hljs-built_in">window</span>) &#123;
        <span class="hljs-comment">// 说明没有使用new来调用，而是当做普通函数来调用，如果一个普通函数中想要返回内容，需要使用return</span>
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> People(name, age, sex);
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-comment">// 说明使用new 来调用函数 </span>
<span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.age = age;
<span class="hljs-built_in">this</span>.sex = sex;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">继承</h3>
<p>子类继承父类的属性和方法</p>
<p>继承分为三种：</p>
<p>1 类式继承</p>
<p>2 构造函数式继承</p>
<p>3 组合式继承</p>
<h4 data-id="heading-4">类式继承</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">People</span>(<span class="hljs-params"></span>) </span>&#123;
&#125;
People.prototype.sayHello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-comment">// 定义子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Student</span>(<span class="hljs-params"></span>) </span>&#123;
&#125;
<span class="hljs-comment">// 继承</span>
Student.prototype = <span class="hljs-keyword">new</span> People();
<span class="hljs-comment">// 注意补回constructor属性</span>
Student.prototype.constructor = Student;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">构造函数式继承</h4>
<p>注：其实跟继承没关系</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义父类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">People</span>(<span class="hljs-params">name, age, sex</span>) </span>&#123;
   <span class="hljs-built_in">this</span>.name = name;
   <span class="hljs-built_in">this</span>.age = age;
   This.sex = sex;
&#125;
People.prototype.sayHello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-comment">// 定义子类</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Student</span>(<span class="hljs-params">name, age, sex, grade</span>) </span>&#123;
   People.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
   <span class="hljs-comment">// 新属性的继承代码一定要放在下方</span>
 <span class="hljs-built_in">this</span>.grade = grade;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">组合式继承</h4>
<p>构造函数式继承 + 类式继承</p>
<h4 data-id="heading-7">instanceof</h4>
<p>该关键字用于判定某一个对象是否是某一个构造函数的实例</p>
<p>使用方式：</p>
<pre><code class="hljs language-js copyable" lang="js">对象  <span class="hljs-keyword">instanceof</span> 构造函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">内置构造函数</h3>
<h4 data-id="heading-9">内置构造函数的分类</h4>
<p>ECMAScript核心语法添加的内置构造函数：</p>
<pre><code class="copyable">Object、 Array、 Function、 String、 Number、 Boolean、 RegExp、 Date、 Error
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Function</h4>
<p>该构造函数用于定义函数</p>
<p>使用方式：</p>
<p>接受任意个字符串参数，除了最后一个都是形参</p>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fun = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"return a + b"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出fun:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c2d8900d9247c1b3ce69f270ba6b02~tplv-k3u1fbpfcp-watermark.image" alt="图片14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>等价方式1：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> fun = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等价方式2：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params"></span>) </span>&#123;
   <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>特点： 如果使用new Function得到的函数， 通过函数.name 得到的anonymous</p>
<p>如果使用函数声明式或者函数表达式打点调用name得到的是变量名称</p>
<pre><code class="hljs language-js copyable" lang="js">函数有一个length属性，表示的是函数在定义的时候形参的个数
argument.length，表示的是函数在执行的时候实参的个数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">RegExp</h4>
<p>该构造函数用于定义正则表达式</p>
<p>使用方式：接受两个参数</p>
<p>第一个参数：字符串，定义正则表达式的表达体</p>
<p>第二个参数： 字符串，正则表达式的修饰符 i、 g、 m</p>
<p>举例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// RegExp</span>
<span class="hljs-keyword">var</span> reg = <span class="hljs-regexp">/\s/g</span>;
<span class="hljs-keyword">var</span> reg1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"\\s"</span>, <span class="hljs-string">"g"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注： 因位字符串中也有转义字符，所以在使用构造函数定义表达式的时候，要多转义一次。</p></div>  
</div>
            