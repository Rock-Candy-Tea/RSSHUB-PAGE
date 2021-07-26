
---
title: 'Typescript 边学边练'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=726'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 18:57:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=726'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>你是否曾经：</p>
<ol>
<li>看了各种TS文档，写起来还是似懂非懂；</li>
<li>接触了一些TS关键字，用起来不太熟练，缺乏明确的理论参考；</li>
<li>TS写着写着降级到了JS；</li>
<li>类型在不知道什么地方就断了层，再也接不上了；</li>
</ol>
<p>基于我们踩坑TS的过程，总结了这篇文档。通过边学边练，从问题到解答到知识点，带你体验类型体操的快乐，并把类型体操应用在日常开发中。</p>
</blockquote>
<ul>
<li>适合对象：“掌握JS，看过TS的，打算加强理解的前端同学”</li>
<li>看完收获：“掌握TS的若干核心知识点；体会类型体操的快乐”</li>
<li>食用姿势：
<ul>
<li>按题不定期食用（每个题都有涉及到相关知识点）</li>
<li>食用顺序：关键词 -> 题目要求 -> 知识点 -> 解题 -> 答题链接 -> 参考答案 -> 参考JS -> 知识点</li>
<li>场景和解答仅供参考，并不是“TS完备”的答案</li>
</ul>
</li>
</ul>
<h2 data-id="heading-0">题目汇总</h2>


















































































<table><thead><tr><th>序号</th><th>标题</th><th>难度指数</th><th>关键词</th><th>题目摘要</th></tr></thead><tbody><tr><td>1.</td><td><a href="https://juejin.cn/post/6981286316998656008" target="_blank" title="https://juejin.cn/post/6981286316998656008">Extract</a></td><td>🌟</td><td><code>generics</code>、<code>union</code>、<code>extends</code></td><td>从某联合类型中选出“和其他类型相交”一部分</td></tr><tr><td>2.</td><td><a href="https://juejin.cn/post/6986176614367248392" target="_blank" title="https://juejin.cn/post/6986176614367248392">Lookup</a></td><td>🌟🌟</td><td><code>generics</code>、<code>union</code>、<code>extends</code></td><td>从某联合类型中选出“满足特定条件的”一部分</td></tr><tr><td>3.</td><td><a href="https://juejin.cn/post/6986181848116396063" target="_blank" title="https://juejin.cn/post/6986181848116396063">Chainable Option</a></td><td>🌟🌟</td><td><code>generics</code>、<code>recursive</code></td><td>使用递归使类型满足链式调用</td></tr><tr><td>4.</td><td><a href="https://juejin.cn/post/6986606043283324942" target="_blank" title="https://juejin.cn/post/6986606043283324942">SubType</a></td><td>🌟🌟</td><td><code>keyof</code></td><td>给对象做merge操作</td></tr><tr><td>5.</td><td><a href="https://juejin.cn/post/6987001375938838542" target="_blank" title="https://juejin.cn/post/6987001375938838542">Change Argument</a></td><td>🌟🌟🌟</td><td><code>infer</code>、<code>ReturnType</code>、<code>Parameters</code></td><td>操作函数的参数和返回值的类型</td></tr><tr><td>6.</td><td><a href="https://juejin.cn/post/6987002391212392462" target="_blank" title="https://juejin.cn/post/6987002391212392462">Underscore</a></td><td>🌟🌟🌟</td><td><code>Template Literal Types</code>、<code>recursive</code></td><td>下划线字符串转驼峰式</td></tr><tr><td>7.</td><td><a href="https://juejin.cn/post/6987585311228297230" target="_blank" title="https://juejin.cn/post/6987585311228297230">EventEmitter</a></td><td>🌟🌟🌟🌟</td><td><code>generics</code>、<code>function overload</code>、<code>Intersection</code></td><td>通过泛型解决函数参数间的相互依赖</td></tr><tr><td>8.</td><td><a href="https://juejin.cn/post/6987586892153765902" target="_blank" title="https://juejin.cn/post/6987586892153765902">Permutation</a></td><td>🌟🌟🌟🌟</td><td><code>union</code>、<code>extends</code>、<code>never</code></td><td>全排列问题</td></tr><tr><td>9.</td><td><a href="https://juejin.cn/post/6987590161735368718" target="_blank" title="https://juejin.cn/post/6987590161735368718">Simple Vue</a></td><td>🌟🌟🌟🌟🌟</td><td><code>this</code></td><td>模拟一个Vue的this操作</td></tr><tr><td>10.</td><td><a href="https://juejin.cn/post/6987596107866079269" target="_blank" title="https://juejin.cn/post/6987596107866079269">Union To Tuple</a></td><td>🌟🌟🌟🌟🌟</td><td><code>function overload</code>、<code>Intersection</code></td><td>无序联合类型转有序tuple</td></tr></tbody></table>
<h2 data-id="heading-1">参考链接</h2>
<ol>
<li>类型分发：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-2-8.html%23distributive-conditional-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-8.html#distributive-conditional-types" ref="nofollow noopener noreferrer">Documentation - TypeScript 2.8</a></li>
<li>泛型：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Fgenerics.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/generics.html" ref="nofollow noopener noreferrer">Documentation - Generics</a></li>
<li>递归类型：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-3-7.html%23more-recursive-type-aliases" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#more-recursive-type-aliases" ref="nofollow noopener noreferrer">Documentation - TypeScript 3.7</a></li>
<li>函数中的泛型：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Ffunctions.html%23generic-functions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/functions.html#generic-functions" ref="nofollow noopener noreferrer">Documentation - More on Functions</a></li>
<li>keyof关键字：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-2-1.html%23keyof-and-lookup-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-1.html#keyof-and-lookup-types" ref="nofollow noopener noreferrer">Documentation - TypeScript 2.1</a></li>
<li>this类型：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Futility-types.html%23thistypetype" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/utility-types.html#thistypetype" ref="nofollow noopener noreferrer">Documentation - Utility Types</a></li>
<li>infer关键字：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjkchao.github.io%2Ftypescript-book-chinese%2Ftips%2Finfer.html%23%25E4%25BB%258B%25E7%25BB%258D" target="_blank" rel="nofollow noopener noreferrer" title="https://jkchao.github.io/typescript-book-chinese/tips/infer.html#%E4%BB%8B%E7%BB%8D" ref="nofollow noopener noreferrer">infer | 深入理解 TypeScript</a></li>
<li>Rest/Spread Parameters:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-3-0.html%23tuples-in-rest-parameters-and-spread-expressions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#tuples-in-rest-parameters-and-spread-expressions" ref="nofollow noopener noreferrer">Documentation - TypeScript 3.0</a></li>
<li>模板字符串：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Frelease-notes%2Ftypescript-4-1.html%23template-literal-types" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html#template-literal-types" ref="nofollow noopener noreferrer">Documentation - TypeScript 4.1</a></li>
<li>字符串部分内置类型：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2F2%2Ftemplate-literal-types.html%23uppercasestringtype" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html#uppercasestringtype" ref="nofollow noopener noreferrer">Documentation - Template Literal Types</a></li>
<li>never判断：</li>
</ol>
<pre><code class="copyable">- [Conditional Types - Checking extends never](https://github.com/microsoft/TypeScript/issues/23182);
- <https://github.com/type-challenges/type-challenges/issues/614>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="12">
<li>Dependent Type:</li>
</ol>
<pre><code class="copyable">- [TypeScript 类型技巧 - 多参数类型约束](https://zhuanlan.zhihu.com/p/95828198)；
- [Typescript Tips: 动态重载实现廉价版dependent type](https://zhuanlan.zhihu.com/p/95829351)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="13">
<li>关于交叉类型和函数重载：</li>
</ol>
<pre><code class="copyable">- [TypeScript union function types](https://stackoverflow.com/questions/58629426/typescript-union-function-types)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="14">
<li>关于TS图灵完备：<a href="https://juejin.cn/post/6927088564194770951" target="_blank" title="https://juejin.cn/post/6927088564194770951">证明 JS 和 TS 类型编程是图灵完备的</a></li>
</ol>
<p>欢迎关注「 字节前端 ByteFE 」</p>
<p>简历投递联系邮箱「<a href="https://link.juejin.cn/?target=mailto%3Atech%40bytedance.com" target="_blank" title="mailto:tech@bytedance.com" ref="nofollow noopener noreferrer">tech@bytedance.com</a>」</p></div>  
</div>
            