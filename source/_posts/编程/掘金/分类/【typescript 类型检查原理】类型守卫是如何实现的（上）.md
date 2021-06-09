
---
title: '【typescript 类型检查原理】类型守卫是如何实现的（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd0c0f4204b4b71966ab6e02ff66044~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 07:10:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd0c0f4204b4b71966ab6e02ff66044~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第8天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
</blockquote>
<p>这是【类型检查的实现原理】系列文章的第三篇，前两篇分别讲了基础类型、泛型、高级类型还有 override 的实现原理：</p>
<p><a href="https://juejin.cn/post/6959882656548913188" target="_blank">基于 babel 手写 ts type checker</a></p>
<p><a href="https://juejin.cn/post/6970289328929013767" target="_blank">【typescript 类型检查原理】override 是如何实现的</a></p>
<p>这一节我们来理一下类型守卫的实现原理，因为内容比较多，分为上下两篇，上篇讲实现思路，下篇是代码实现。</p>
<h2 data-id="heading-0">什么是类型守卫</h2>
<p>javascript 的类型代表了一种可能性，表示可能占用的内存大小、可能调用的方法等。typescript 的类型包含了 javascript 的类型，并且对可以对类型做交集、并集、各种推导，最终产生准确的类型。typescript 的类型的推导也是一种可能性的推导，目标是得出的类型更准确的描述具体的变量类型。</p>
<p>精准就意味着要做一些类型的可能性的缩小，各种类型编程的目的都是产生更小更准确的类型，类型守卫也是这个目的。</p>
<p>类型推导是使得整个类型变得更小更准确，而类型守卫则是当类型进入某个分支的时候，暂时性的变得更小更精确，使得类型检查更准确。</p>
<p>比如下面的代码，整体类型是 string| number，这是一个联合类型，当 a 进入 if 分支的时候，类型明显只可能是 string，别的情况进不来，这时候可以做进一步的类型缩小，这就叫做类型守卫。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params">a: <span class="hljs-built_in">string</span>| <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> a === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> a.toLocaleLowerCase();
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> a.toFixed(<span class="hljs-number">1</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>类型守卫的目的就是让整体的类型在一些确定的条件下暂时性的变得更小更精确。这种条件包括 typeof、instanceOf、in、===、!==、==、!=。</strong></p>
<p>为什么这些条件下可以缩小类型呢？因为能够进入这些分支，那么变量显然只可能是改种类型，所以类型的可能性自然可以做进一步的缩小。</p>
<p>比如 in 操作符触发的类型守卫：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbd0c0f4204b4b71966ab6e02ff66044~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>=== 判断触发的类型守卫：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e05d4dfc9e246739da4a4af369d4bc5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同理 instanceof 等也是一样，只要是进入能够确定具体类型的分支，那么类型就可以做缩小。</p>
<p>在 ts 4.3 中，泛型的类型缩小也做了支持（之前只能通过类型断言来缩小类型）。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/090b8d6690394d4ebb4dcb533134fb5d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>类型缩小是自动的类型断言，当有的时候类型缩小或者类型推导都不行的时候，就用 as 手动类型断言。</strong></p>
<h2 data-id="heading-1">实现思路分析</h2>
<p>我们知道了类型缩小是在在进入条件分支的时候，对类型检查用的类型做暂时性的缩小，那么实现的时候自然就是在 if、switch 的分支的检查时，对类型做一些处理。</p>
<p>ts 的类型检查是先通过解析配置文件的 includes、exclues、files 等，结合 lib、types、typeRoots 的配置来确定要做检查的所有文件，然后对每个文件依次进行递归下降的类型检查。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d70e030237fa4de8bea86bebc2b0598a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当检查到 if、switch 的节点的时候，我们只需要判断 test 部分是否是一个 BinaryExpression，并且 operator 是 in、===、!==、instanceOf 等情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/626e356fc6cb430f83a8a91ad826a461~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据 operator 的不同分别做不同的判断：</p>
<ul>
<li>in： 判断 left 是否是 right 变量的类型的一个属性，如果是，对类型做缩小</li>
<li>instanceof：判断 left 的类型是否是 right 变量的类型的子类型，如果是，对类型做缩小</li>
<li>=== / !==: 分为包含 typeof 和不包含 typeof 两种：
<ul>
<li>不包含 typeof： 判断 left 和 right 是否相等，如果是，把类型缩小到具体的字面量类型。</li>
<li>包含 typeof：如果两边有一边是 typeof 的 UnaryExpression，则取类型之后再做比较，如果是，把类型缩小到具体的类型</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">总结</h2>
<p>typscript 的高级类型的推导的目的就是缩小可能性范围，让类型更精确。有的时候，在进入一些分支的时候，类型就确定了，这时候就可以暂时性的对类型做范围的缩小，这叫做类型守卫。</p>
<p>触发条件有 in、instanceof、typeof、===、!== 等能够让类型更准确的判断。</p>
<p>类型守卫相当于自动的类型断言，当类型守卫搞不定的时候，就手动用类型断言 as 来缩小类型。</p>
<p>我们梳理了实现类型守卫的思路，就是遇到条件语句 IfStatement、SwitchStatement 的时候，对 test 部分做判断，如果包含 in、instanceof、typeof 等，做相应的类型处理，之后再进行类型检查。</p>
<p>这一篇希望能帮你理清对类型守卫的认识，并且有实现的思路，下一篇我们来做具体的代码实现。</p></div>  
</div>
            