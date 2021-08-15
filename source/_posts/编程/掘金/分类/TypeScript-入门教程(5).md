
---
title: 'TypeScript-入门教程(5)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1936'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 22:56:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1936'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">函数类型</h2>
<p><em>函数是 JavaScript 中的一等公民</em></p>
<h3 data-id="heading-1">1.函数声明</h3>
<p>JavaScript中两种常见的定义函数的方式：函数声明和函数表达</p>
<pre><code class="copyable">// 函数声明（Function Declaration）
function sum(x, y) &#123;
    return x + y;
&#125;

// 函数表达式（Function Expression）
let mySum = function (x, y) &#123;
    return x + y;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在TypeScript中函数如果有输入和输出，那么则要对其输入和输出的值进行约束，函数声明定义的较为简单：</p>
<pre><code class="copyable">function sum(x:number,y:number):number&#123;
   return x+y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中我们限制了传入的x,y的参数必须为Number类型的数值，同时我们返回值的类型也必须是Number类型。
<em>注意：输入多余的（或者少于要求的）参数，是不被允许的</em></p>
<h3 data-id="heading-2">2.函数表达式</h3>
<p>如果我们用函数表达式定义一个函数，可能是这样的：</p>
<pre><code class="copyable">let mySum=function(x:number,y:number):number&#123;
  return x+y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是可以通过编译的，不过事实上，我们只是给等号右边的匿名函数进行了类型定义，而等号左边的 <code>mySum</code>，是通过赋值操作进行类型推论而推断出来的。所以应该修改为这样：</p>
<pre><code class="copyable">let mySum: (x: number, y: number) => number = function (x: number, y: number): number &#123;
    return x + y;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意不要混淆了 TypeScript 中的 <code>=></code> 和 ES6 中的 <code>=></code>。</p>
<p>在 TypeScript 的类型定义中，<code>=></code> 用来表示函数的定义，左边是输入类型，需要用括号括起来，右边是输出类型。</p>
<p>在 ES6 中，<code>=></code> 叫做箭头函数，应用十分广泛.</p>
<h3 data-id="heading-3">3.用接口定义函数的形状</h3>
<p>我们也可以使用接口的方式来定义一个函数需要符合的形状：</p>
<pre><code class="copyable">interface SearchFunc &#123;
    (s1: string, s2: string): boolean;
&#125;

let mySearch: SearchFunc;
mySearch = function(s1: string, s2: string) &#123;
    return s1.search(s2) !== -1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口SearchFunc中定义了参数的类型以及返回值的类型。</p>
<h3 data-id="heading-4">4.可选参数</h3>
<p>我们指导参数多传或者是少传都是不被允许的，那么我们就可以设置可选参数，用<code>?</code>来表示：</p>
<pre><code class="copyable">function getName(n1:string,n2?:string):string&#123;
   if(n2)&#123;
      return n1+n2;
    &#125;else&#123;
       return n1;
    &#125;
&#125;
getName("Tom","Jack"); //TomJack
getName(undefined,"James") //James
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>注意：可选参数必须是在必须参数的后面，换句话说，可选参数后面不允许再出现必需参数了</em></p>
<pre><code class="copyable">function getName(n1?:string,n2:string):string&#123;
   if(n1)&#123;
      return n1+n2;
    &#125;else&#123;
       return n2;
    &#125;
&#125;
getName("Tom","Jack"); //TomJack
getName(undefined,"James") //error
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5.参数默认值</h3>
<p>在 ES6 中，我们允许给函数的参数添加默认值，<strong>TypeScript 会将添加了默认值的参数识别为可选参数</strong>：</p>
<pre><code class="copyable">function setName(n1:string,n2:string="Harden"):string&#123;
     return n1+n2;
&#125;
setName("Kobe","Bryant")// KobeBryant
setName(undefined,"James") // JamesHarden
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时就不受<em><strong>可选参数必须接在必需参数后面</strong></em>的限制了：</p>
<pre><code class="copyable">function setName(n1:string="Paul",n2:string):string&#123;
     return n1+n2;
&#125;
setName("Lerbon","James")// LerbonJames
setName(undefined,"James") // PaulJames
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            