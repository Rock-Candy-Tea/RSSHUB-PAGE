
---
title: 'es6中的import和export'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3488'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 03:51:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=3488'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">export</h1>
<p>export有两种导出模式，export 和export default(一个模块中只能有一个default)</p>
<h2 data-id="heading-1">导出变量</h2>
<p>export 后边可以是一个变量声明表达式或者是一个&#123;&#125;里边包含变量名，但是不能直接输出一个变量，
export default 后边可以直接跟一个常量或者变量，但是不能跟声明表达式</p>
<pre><code class="copyable">export var a = 1 //正确

const age = 100
export &#123; age &#125; //正确

export age //错误

export default age //正确

export default 50 //正确

export default var name='abc ' //错误



<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">导出函数</h2>
<p>export和export都可以直接导出函数声明语句，但是export后边不能跟匿名函数，如果直接导出函数名export 需要用&#123;&#125;包裹</p>
<pre><code class="copyable">//正确
 export default function test () &#123;
  console.log('test function')
&#125;
   //正确
 export  function test2 () &#123;
  console.log('test function')
&#125;
//错误
 export  function  () &#123;
  console.log('test function')
&#125;
 //正确
 export default function  () &#123;
  console.log('test function')
&#125;

function test3()&#123;
 console.log('test3 function')
&#125;

//正确
expor &#123;test3&#125;
//正确
export default test3
错误
export  test3


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">使用 as别名导出</h2>
<pre><code class="copyable">let a = 100

export &#123;a as age &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">import</h1>
<ul>
<li>对于使用export default 导出的，倒入时不需要使用&#123;&#125;,且名字可以任意定义</li>
<li>对于使用export 导出的，必须使用&#123;&#125;倒入，且名字必须一致</li>
<li>可以使用通配符* 方式全部导入 (import * as obj from '../a.js')</li>
</ul>
<pre><code class="copyable">//对于export default 导出的

import myFn from './a.js'

//对于使用export 导出的

import &#123;test1,test2&#125; from './a.js'



<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">按需加载</h1>
<p>采用回调函数的方式，所有的引入直接在回调中</p>
<pre><code class="copyable">   document.onclick = function() &#123;
      import('./a.js').then(data => &#123;
        console.log(data)
      &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">总结</h1>
<p>这种模块化写法到底有什么优点呢，我们为什么要用呢？</p>
<ul>
<li>防止作用域污染</li>
<li>提高代码的复用性</li>
<li>维护成本降低</li>
</ul></div>  
</div>
            