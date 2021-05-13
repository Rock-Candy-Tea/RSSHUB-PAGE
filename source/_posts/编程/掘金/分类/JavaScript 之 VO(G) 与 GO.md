
---
title: 'JavaScript 之 VO(G) 与 GO'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c462e2c0dc2f437184c2431b605cbc4b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 02:16:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c462e2c0dc2f437184c2431b605cbc4b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>EC(G): Execution  Context (Global) 全局执行上下文。代码提交后，在栈内存(ECStack执行环境栈)中形成的全局执行上下文。</p>
<ul>
<li>
<p>VO(G)：Variable Object(Global)全局变量对象</p>
<p>为了可以访问到存放在GO中的属性和方法，浏览器在全局执行上下文EC(G)中，默认声明了一个变量window，存放在VO(G)中，并让window指向GO的地址，后期便可以基于window访问内置的属性和方法。</p>
<ol>
<li>我们经常把window称为全局对象</li>
<li>编写代码时，我们可以省略window   如window.alert() ⇒  alert()；</li>
</ol>
</li>
</ul>
<p>GO：Global  Object 全局对象   全局变量window对应的堆内存地址，用来存储内置的属性和方法。</p>
<p><strong>var/function/let/const在全局执行上下文中的区别：</strong></p>
<ul>
<li>在<strong>全局执行上下文</strong>中，基于<strong>var/function</strong>声明的变量是存储在<strong>GO</strong>中的，相当于给window设置属性；</li>
<li>而基于<strong>let/const</strong>声明的变量是存储在<strong>VO(G)<strong>中的，他们才是根正苗红的</strong>全局变量</strong>。与window没有关系；</li>
<li><strong>没有基于任何关键字修饰/声明的变量</strong>，其实是省略了"window."，核心也是在<strong>GO</strong>中增加一个属性。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c462e2c0dc2f437184c2431b605cbc4b~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于以上：</p>
<ol>
<li>如果是<strong>window.xxx</strong>，直接到<strong>GO</strong>中找即可；</li>
<li>如果是直接<strong>输出一个变量</strong>，则<strong>先去VO(G)<strong>中找，有的话获取的是</strong>全局变量</strong>，如果<strong>没有则到GO</strong>中找，如果有，则是<strong>全局对象属性</strong>，如果<strong>没有则报错</strong>：xxx is not defined。</li>
</ol>
<h2 data-id="heading-0">变量提升机制</h2>
<ol>
<li>
<p>在<strong>当前上下文</strong>中，代码执行之前，浏览器首先会把所有带<strong>var/function</strong>关键字的进行提前<strong>声明或者定义</strong>。</p>
<ol>
<li>var 只声明 不定义</li>
<li>function 既声明又定义   <strong>注意：</strong>
<ol>
<li>函数在哪个执行上下文<strong>创建</strong>，它的<strong>作用域</strong>就是哪个执行上下文；</li>
<li>作用域是函数所处的执行上下文，在函数创建时确定，即其上级上下文；</li>
<li>函数私有执行上下文在函数执行时决定；</li>
<li>函数的声明定义，是<strong>先定义再声明</strong>，即先创建值[堆内存]，再创建变量；</li>
<li>为函数开辟的堆内存中存储了：
<ol>
<li>函数的作用域scope  <函数的执行上下文，函数的上级执行上下文></li>
<li>代码字符串</li>
<li>键值对    name: '函数名'    length : '形参个数'</li>
</ol>
</li>
</ol>
</li>
</ol>
</li>
<li>
<p><strong>let/const/import/class</strong>声明的变量<strong>不存在变量提升</strong>。</p>
</li>
<li>
<p><strong>私有作用域中的变量提升：</strong></p>
<p>函数的底层运行机制：</p>
<p>代码运行到[函数执行]时，形成私有执行上下文EC(FN)，私有变量对象AO(FN)，在函数内代码执行前浏览器做了以下事情：</p>
<ol>
<li>初始化作用域链</li>
<li>初始化this</li>
<li>初始化arguments</li>
<li><strong>形参</strong>私有化并赋值</li>
<li>变量提升</li>
<li>代码执行</li>
<li>默认情况下，函数执行完，所形成的上下文会出栈释放掉</li>
</ol>
<p><strong>闭包</strong>：函数执行，会产生一个全新的私有上下文，保护里面的私有变量，不受外界的干扰，避免了全局变量污染，我们把函数的这种保护机制称之为闭包。</p>
</li>
<li>
<p><strong>推荐使用函数表达式</strong></p>
<ol>
<li><code>functoin fn()&#123;&#125;````var fn = function()&#123;&#125;</code>[函数表达式] 的区别：
<ul>
<li>函数表达式的执行只能在声明后执行，普通函数可以在声明定义前执行，<strong>区别在于变量提升</strong></li>
<li>真实项目推荐使用函数表达式，确保函数执行只能在“创建函数代码”的下面，保证逻辑的严谨性。</li>
</ul>
</li>
</ol>
</li>
<li>
<p><strong>匿名函数具名化[官方推荐规范]</strong>：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123;
    A = <span class="hljs-number">100</span>; <span class="hljs-comment">//无效操作 </span>
    <span class="hljs-built_in">console</span>.log(A); <span class="hljs-comment">//函数本身</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>设置的名字，并不会在所处上下文中进行声明；</li>
<li>在函数执行形成的私有上下文中，会把这个名字作为一个私有变量「存储到AO中」，变量值是当前函数本身「堆内存地址」; 并且默认情况下，对这个变量值进行修改是无效的；</li>
<li>但凡函数内部，这个名字被我们手动的声明过[例如：形参/var/let/const...]，以我们声明的为准。则规则2无效，浏览器将权利移交给我们。</li>
</ol>
<pre><code class="hljs language-jsx copyable" lang="jsx">(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">A</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(A); <span class="hljs-comment">//undefined</span>
    <span class="hljs-keyword">var</span> A = <span class="hljs-number">100</span>;
    <span class="hljs-built_in">console</span>.log(A); <span class="hljs-comment">//100</span>
&#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>匿名函数：自执行函数/函数表达式/回调函数....</p>
<p>匿名函数具名化的作用：</p>
<p>可以<strong>在函数内部基于这个名字访问到这个函数</strong>，这样就可以实现一些不具备的能力，如：递归</p>
<blockquote>
<p>非严格模式下，也可通过arguments.callee访问当前匿名函数，arguments.callee.caller：存储函数在哪执行的，</p>
</blockquote>
<blockquote>
<p>“use strict” //开启JS严格模式，基于webpack打包后，都是严格模式，arguments.callee、arguments.callee.caller在严格模式下不能用</p>
</blockquote>
</li>
<li>
<p><strong>块级上下文 [ES6新增]</strong></p>
<ol>
<li>是在代码执行期间执行的，即碰到&#123;&#125;才形成相应的块级上下文</li>
<li><strong>除函数和对象</strong>的大括号外，如：<strong>判断体、循环体、代码块</strong>，如果在大括号中出现了<strong>let/const/function/class</strong> 等关键词声明变量，则当前大括号会产生一个“块级私有上下文”，它的上级上下文就是其所处的上下文。
<ul>
<li>let/const/funtion 会产生块级上下文，也会受到块级上下文的束缚</li>
<li>var不产生，也不受块级上下文的影响</li>
</ul>
</li>
</ol>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f352f4397174f78aabbed0174e4a116~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
3. 函数在块级上下文中的特殊性【新版本与老版本的不同】</p>
<pre><code class="copyable">    老版本：不会有块级上下文，所以在大括号（除函数和对象外）中出现fuction，还是保持原始的样子，变量提升阶段是声明+定义；

    新版本，为了兼容ES5也可以兼容ES6，则全局下也要声明，私有块级上下文中也要声明。

    1. 出现在“除函数/对象”以外的大括号中的function，在最开始变量提升阶段只声明
    2. 会产生块级上下文，
    3. **遇到函数声明的那串代码时候(分界点：将之前对该函数的值给上级上下文一份，此时该函数的上级上下文变量和该函数的私有变量拥有了同一个值【堆内存地址】，但他们始终是两个变量)**，会向该函数的全局变量指向函数对象地址，以后再对函数私有变量进行赋值，与该函数全局变量无关，只与函数私有变量有关。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9e57f04cdb745c2aa8a0a55ec19b9dc~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
<code>         jsx         &#123;             function foo() &#123;&#125; //**将之前对foo的操作同步给全局一份**             foo = 1;             function foo() &#123;&#125; //**也会将之前对foo的操作同步给全局一份，遇到一次改一次**         &#125;         console.log(foo);// 1        </code></p></div>  
</div>
            