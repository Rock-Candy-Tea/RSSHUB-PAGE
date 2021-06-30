
---
title: 'ts中的接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1114'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 05:38:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=1114'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">接口</h1>
<h2 data-id="heading-1">接口的关键字interface</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IStudent &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">no</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">stu: IStudent</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(stu)
&#125;
say(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'hhh'</span>, <span class="hljs-attr">no</span>: <span class="hljs-number">1</span> &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">可选属性</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IStudent &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">no</span>: <span class="hljs-built_in">number</span>
    tag?: <span class="hljs-built_in">string</span> <span class="hljs-comment">//可选属性</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">stu: IStudent</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(stu)
&#125;
say(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'hhh'</span>, <span class="hljs-attr">no</span>: <span class="hljs-number">1</span> &#125;)
say(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'haha'</span>, <span class="hljs-attr">no</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">tag</span>: <span class="hljs-string">'三好学生'</span> &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">只读属性 ,关键字 readonly</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IStudent &#123;
    <span class="hljs-keyword">readonly</span> firtName: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">no</span>: <span class="hljs-built_in">number</span>
    tag?: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params">stu: IStudent</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(stu)
&#125;
<span class="hljs-keyword">let</span> stu1: IStudent = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">no</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">firtName</span>: <span class="hljs-string">'张'</span> &#125;
<span class="hljs-keyword">let</span> stu2: IStudent = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'李四'</span>, <span class="hljs-attr">no</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">tag</span>: <span class="hljs-string">'三好学生'</span>, <span class="hljs-attr">firtName</span>: <span class="hljs-string">'李'</span> &#125;
<span class="hljs-comment">// stu1.firtName = '王'</span>
<span class="hljs-built_in">console</span>.log(stu1.firtName)
say(stu1)
say(stu2)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">用接口声明函数</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> ISay1 &#123;
    (name: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">let</span> say1: ISay1 = <span class="hljs-function">(<span class="hljs-params">str1: <span class="hljs-built_in">string</span></span>) =></span> &#123; <span class="hljs-keyword">return</span> str1 &#125;
<span class="hljs-keyword">let</span> say2: ISay1 = <span class="hljs-function">(<span class="hljs-params">str1: <span class="hljs-built_in">string</span></span>) =></span> &#123; <span class="hljs-keyword">return</span> str1 &#125;
<span class="hljs-comment">// function say1(st1: string): string &#123;</span>
<span class="hljs-comment">//     return st1</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-built_in">console</span>.log(say1(<span class="hljs-string">'say1'</span>), say2(<span class="hljs-string">'say2'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">可索引类型的接口</h2>
<p>声明的数组</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> StringArray &#123;
    [index: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">let</span> myArray: StringArray;
myArray = [<span class="hljs-string">"Bob"</span>, <span class="hljs-string">"Fred"</span>];

<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明的map</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IMap &#123;
    [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">string</span>;
&#125;
<span class="hljs-keyword">let</span> m: IMap = &#123; <span class="hljs-string">"a"</span>: <span class="hljs-string">"a"</span> &#125;
<span class="hljs-built_in">console</span>.log(m)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">类类型,接口对class的约束</h1>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 接口重在约束</span>
<span class="hljs-keyword">interface</span> ILee &#123;
    <span class="hljs-attr">firstname</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Lee</span> <span class="hljs-title">implements</span> <span class="hljs-title">ILee</span> </span>&#123;
    <span class="hljs-attr">firstname</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">let</span> lee = <span class="hljs-keyword">new</span> Lee()
lee.firstname = <span class="hljs-string">'Lee'</span>

<span class="hljs-built_in">console</span>.log(lee)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">接口的继承</h2>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">interface</span> IAnimal &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">interface</span> ICat <span class="hljs-keyword">extends</span> IAnimal &#123;
    say(str: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-keyword">interface</span> IDog <span class="hljs-keyword">extends</span> IAnimal &#123;
    say(str: <span class="hljs-built_in">string</span>, <span class="hljs-attr">s2</span>: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span>
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-title">implements</span> <span class="hljs-title">ICat</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    say(s1: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span> &#123;
        <span class="hljs-keyword">return</span> s1
    &#125;
&#125;
<span class="hljs-comment">// 接口重在签名，也就是约束</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-title">implements</span> <span class="hljs-title">IDog</span> </span>&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    say(s1: <span class="hljs-built_in">string</span>, <span class="hljs-attr">st2</span>: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">string</span> &#123;
        <span class="hljs-keyword">return</span> s1 + st2
    &#125;
&#125;
<span class="hljs-keyword">let</span> cat: ICat = <span class="hljs-keyword">new</span> Cat()
<span class="hljs-built_in">console</span>.log(cat.say(<span class="hljs-string">'cat'</span>))
<span class="hljs-keyword">let</span> dog: IDog = <span class="hljs-keyword">new</span> Dog()
<span class="hljs-built_in">console</span>.log(dog.say(<span class="hljs-string">'dog1'</span>, <span class="hljs-string">'dog2'</span>))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            