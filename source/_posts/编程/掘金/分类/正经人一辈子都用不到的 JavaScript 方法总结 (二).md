
---
title: '正经人一辈子都用不到的 JavaScript 方法总结 (二)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/711131d038674529945b2f4530d26b4d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 05:38:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/711131d038674529945b2f4530d26b4d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>现在有这样一个需求：用一个对象存储某学生的各科成绩，要求每次只能改变科目分数，不能再添加或者删除科目。</p>
<p>分析一下，这个需求其实就是需要创建一个固定属性的对象，其属性不可增删，但属性值可更改。</p>
<p>有些同学可能就这么开始了：</p>
<ul>
<li>首先，定义一个符合要求的对象：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 声明成绩存储对象</span>
<span class="hljs-keyword">let</span> reportObj = &#123;&#125;;
<span class="hljs-comment">// 给成绩存储对象添加科目，并设置科目属性不可增删，但科目成绩可修改</span>
<span class="hljs-built_in">Object</span>.defineProperties(reportObj, &#123;
    <span class="hljs-attr">ChineseMark</span>: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-number">60</span>
    &#125;,
    <span class="hljs-attr">EnglishMark</span>: &#123;
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">value</span>: <span class="hljs-number">60</span>
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>然后写入成绩：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 存入科目成绩</span>
reportObj.ChineseMark = <span class="hljs-number">99</span>;
reportObj.EnglishMark = <span class="hljs-number">95</span>;
<span class="hljs-built_in">console</span>.log(reportObj);  <span class="hljs-comment">// &#123;ChineseMark: 99, EnglishMark: 95&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除属性来试试：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">delete</span> reportObj.ChineseMark;  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(reportObj);  <span class="hljs-comment">// &#123;ChineseMark: 99, EnglishMark: 95&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>貌似确实符合条件了，那么再试试增加属性吧：</p>
<pre><code class="hljs language-js copyable" lang="js">reportObj.PhysicsMark = <span class="hljs-number">100</span>;
<span class="hljs-built_in">console</span>.log(reportObj);  <span class="hljs-comment">// &#123;ChineseMark: 99, EnglishMark: 95, PhysicsMark: 100&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咋回事，怎么突然就不太符合要求了呢？<code>Object.defineProperties()</code> 只能精确控制所增添的属性的特质，但如果给对象添加属性的话，它就无力控制了。</p>
<p>今天我们就用简单的接口方法来实现一下这幺蛾子需求  ︿(￣︶￣)︿</p>
<h2 data-id="heading-1">Object.seal()</h2>
<h3 data-id="heading-2">描述</h3>
<p>seal 如果作动词，那它的解释就是“密封”：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/711131d038674529945b2f4530d26b4d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825210254120" loading="lazy" referrerpolicy="no-referrer"></p>
<p>见名知意，<code>Object.seal()</code> 方法就是用来“密封”一个对象的，它阻止对象添加新属性，并将对象所有的现有属性标记为不可配置。当前属性的值只要原来是可写的就可以改变。</p>
<h3 data-id="heading-3">作用</h3>
<p>通常，一个对象是可扩展的（可以添加新的属性）。</p>
<p>密封一个对象会让这个对象变的不能添加新属性，且所有已有属性会变的不可配置。属性不可配置的效果就是属性变的不可删除，以及一个数据属性不能被重新定义成为访问器属性，或者反之。但属性的值仍然可以修改。</p>
<p>尝试删除一个密封对象的属性或者将某个密封对象的属性从数据属性转换成访问器属性，结果会静默失败或抛出 TypeError（在严格模式 中最常见的，但不唯一）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> object1 = &#123;
    <span class="hljs-attr">property1</span>: <span class="hljs-number">42</span>
&#125;;

<span class="hljs-built_in">Object</span>.seal(object1);
object1.property1 = <span class="hljs-number">33</span>;
<span class="hljs-built_in">console</span>.log(object1.property1);
<span class="hljs-comment">// expected output: 33</span>

<span class="hljs-keyword">delete</span> object1.property1; <span class="hljs-comment">// cannot delete when sealed</span>
<span class="hljs-built_in">console</span>.log(object1.property1);
<span class="hljs-comment">// expected output: 33</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结起来，<code>Object.seal()</code> 其实就是做了以下事情：</p>
<ul>
<li>设置Object.preventExtension()，禁止添加新属性(绝对存在)</li>
<li>设置configurable为false，禁止配置(绝对存在)</li>
<li>禁止更改访问器属性(getter和setter)</li>
</ul>
<h3 data-id="heading-4">语法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.seal(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">参数</h3>
<p>参数 obj 代表将要被密封的对象。</p>
<h3 data-id="heading-6">返回值</h3>
<p>被密封的对象。</p>
<h2 data-id="heading-7">实现需求</h2>
<p>既然有这么好用的方法，那我们当然要好好利用一番啦，终于可以完美实现文章开头的需求了：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 声明成绩存储对象及其属性</span>
<span class="hljs-keyword">let</span> reportObj = &#123;   
    <span class="hljs-attr">ChineseMark</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">EnglishMark</span>: <span class="hljs-number">60</span>
&#125;;
<span class="hljs-comment">// 密封成绩对象</span>
<span class="hljs-keyword">let</span> sealedReportObj = <span class="hljs-built_in">Object</span>.seal(reportObj);
<span class="hljs-comment">// 更改科目分数</span>
sealedReportObj.ChineseMark = <span class="hljs-number">99</span>;
sealedReportObj.EnglishMark = <span class="hljs-number">97</span>;
<span class="hljs-built_in">console</span>.log(sealedReportObj); <span class="hljs-comment">// &#123;"ChineseMark": 99, "EnglishMark": 97&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 增加属性</span>
sealedReportObj.PhysicsMark = <span class="hljs-number">100</span>;
<span class="hljs-built_in">console</span>.log(sealedReportObj); <span class="hljs-comment">// &#123;"ChineseMark": 99, "EnglishMark": 97&#125;</span>

<span class="hljs-comment">// 删除属性</span>
<span class="hljs-keyword">delete</span> sealedReportObj.ChineseMark; <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(sealedReportObj); <span class="hljs-comment">// &#123;"ChineseMark": 99, "EnglishMark": 97&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到对象的属性确实是增删不了了，算是简单实现了需求吧。</p>
<h2 data-id="heading-8">扩展</h2>
<p>如果要判断一个对象是否“密封”，我们可以使用 <code>Object.isSealed()</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.isSealed(sealedReportObj); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Object.freeze()</h2>
<p>看到这里，可能很多同学都想起了 <code>Object.freeze()</code> 方法，它的作用是用来冻结一个对象。实际作用就是字面意思：冻结一个对象，使其属性和属性值都不可更改。用来实现这个需求显然是不合适的。</p>
<h3 data-id="heading-10">共同点</h3>
<p><code>Object.seal()</code> 和 <code>Object.freeze()</code> 有以下共同点：</p>
<ul>
<li>作用的对象变得不可扩展，这意味着不能再添加新属性。</li>
<li>作用的对象中的每个元素都变得不可配置，这意味着不能删除属性。</li>
<li>如果在 ‘use strict’ 模式下使用，这两个方法都可能抛出错误。</li>
</ul>
<h3 data-id="heading-11">不同点</h3>
<p><code>Object.seal()</code> 能让你修改属性的值，但 <code>Object.freeze()</code> 不能。</p>
<h2 data-id="heading-12">总结</h2>
<p>以上就是关于 <code>Object.seal()</code> 方法的一些简单介绍和应用，以及它和 <code>Object.freeze()</code> 的异同点，希望能对大家有所帮助。</p>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote>
<p>参考文档：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Fseal" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/seal" ref="nofollow noopener noreferrer">Object.seal()</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2Ffreeze" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze" ref="nofollow noopener noreferrer">Object.freeze()</a></p></div>  
</div>
            