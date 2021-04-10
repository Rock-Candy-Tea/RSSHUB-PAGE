
---
title: 'new 操作符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5997'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 01:56:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=5997'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<h3 data-id="heading-0">new 操作符做的事情</h3>
<ol>
<li>创建了一个全新的对象。</li>
<li>将对象链接到这个函数的 prototype 对象上。</li>
<li>执行构造函数，并将 this 绑定到新创建的对象上。</li>
<li>判断构造函数执行返回的结果是否是引用数据类型，若是则返回构造函数执行的结果，否则返回创建的对象。</li>
</ol>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myNew</span>(<span class="hljs-params">Constructor, ...args</span>) </span>&#123;
    <span class="hljs-comment">// console.log(Constructor);</span>
    <span class="hljs-comment">// Constructor 输出结果</span>
    <span class="hljs-comment">// ƒ Test() &#123; </span>
    <span class="hljs-comment">//      console.log('被执行的函数。'); </span>
    <span class="hljs-comment">//      return '返回被执行的函数。'; </span>
    <span class="hljs-comment">// &#125;;</span>

    <span class="hljs-comment">// console.log(args);</span>
    <span class="hljs-comment">// args 输出结果</span>
    <span class="hljs-comment">// [1, "JavaScript", "辛弃疾", &#123;…&#125;, Array(3)]</span>
    <span class="hljs-comment">// console.log(args[3]);</span>
    <span class="hljs-comment">// args[3] 输出结果</span>
    <span class="hljs-comment">// &#123;sname: "杨万里", number: 3, web: "vue"&#125;</span>
    <span class="hljs-comment">// console.log(args[4]);</span>
    <span class="hljs-comment">// [5, "uniApp", "范仲淹"]</span>

    <span class="hljs-comment">// 判断 Constructor 参数是否是函数</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Constructor !== <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'Constructor.apply is not a function'</span>;
    &#125;;

    <span class="hljs-comment">// 1、创建了一个全新的对象。</span>
    <span class="hljs-keyword">let</span> newObject = &#123;&#125;;

    <span class="hljs-comment">// 2、将对象链接到这个函数的 prototype 对象上。</span>
    newObject.__proto__ = Constructor.prototype;

    <span class="hljs-comment">// 此处是把 1 / 2 步结合到一起</span>
    <span class="hljs-comment">// const newObject = Object.create(Constructor.prototype);</span>

    <span class="hljs-comment">// 3、执行构造函数，</span>
    <span class="hljs-comment">// 并将 this 绑定到新创建的对象上。</span>
    <span class="hljs-keyword">let</span> result = Constructor.apply(newObject, args);

    <span class="hljs-comment">// 4. 判断构造函数执行返回的结果是否是引用数据类型，</span>
    <span class="hljs-comment">// 若是则返回构造函数执行的结果，</span>
    <span class="hljs-comment">// 否则返回创建的对象。</span>
    <span class="hljs-keyword">return</span> result != <span class="hljs-literal">undefined</span> && result != <span class="hljs-literal">null</span> ? result : newObject;
&#125;;

<span class="hljs-comment">// 需要被 new 的函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">NewTest</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'被执行的函数。'</span>); <span class="hljs-comment">// 被执行的函数。</span>
    <span class="hljs-keyword">return</span> <span class="hljs-string">'返回被执行的函数。'</span>;
&#125;;

<span class="hljs-comment">// 定义参数</span>
<span class="hljs-keyword">let</span> dataObj = &#123;
    <span class="hljs-attr">sname</span>: <span class="hljs-string">'杨万里'</span>,
    <span class="hljs-attr">number</span>: <span class="hljs-number">3</span>,
    <span class="hljs-attr">web</span>: <span class="hljs-string">'vue'</span>
&#125;;
<span class="hljs-keyword">let</span> dataArray = [<span class="hljs-number">5</span>, <span class="hljs-string">'uniApp'</span>, <span class="hljs-string">'范仲淹'</span>];

<span class="hljs-comment">// 执行 myNew 函数</span>
<span class="hljs-keyword">let</span> test = myNew(NewTest, <span class="hljs-number">1</span>, <span class="hljs-string">'JavaScript'</span>, <span class="hljs-string">'辛弃疾'</span>, dataObj, dataArray);
<span class="hljs-built_in">console</span>.log(test); <span class="hljs-comment">// 返回被执行的函数。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-1">1、new 的原理是什么？</h3>
<p>new 操作符做的事情。</p>
</blockquote>
<blockquote>
<h3 data-id="heading-2">2、通过 new 的方式创建对象和通过字面量创建对象有什么区别？</h3>
<p>对象都是通过 new 产生。function Foo() &#123;&#125;，function 是语法糖，内部等同于 new Function() 。let object = &#123; number: 1 &#125; ，使用字面量创建对象，内部也是使用了 new Object() 。对于创建一个对象来说，更推荐使用字面量的方式创建对象。因为使用 new Object() 的方式创建对象，需要通过作用域链一层层找到 Object ，如果使用字面量的方式就没有这个问题。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            