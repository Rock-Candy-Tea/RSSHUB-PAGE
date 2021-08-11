
---
title: '「TypeScript」入门进阶(一)✈️'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b06ed302524b4dee96535db269f93b06~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:31:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b06ed302524b4dee96535db269f93b06~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言🎉</h2>
<ul>
<li>虽然之前有学过<code>TypeScript</code>但是平时业务上面都还是用<code>JavaScript</code>来开发导致逐渐对<code>TypeScript</code>生疏了。</li>
<li>借此更文活动的机会再来一起学习一下<code>TypeScript</code>的知识吧。</li>
<li>在之前的文章中我们<code>TypeScript</code>的基础知识过了一遍，是不是发现其实也不会很难呢。</li>
<li>本文也是<code>TypeScript</code>进阶篇的第一篇，关于基础篇可以看我之前分享的文章喔~。</li>
</ul>
<h2 data-id="heading-1">类型别名🚤</h2>
<ul>
<li>基本语法是 [<code>type</code>  <code>名称</code> = <code>类型</code>]</li>
<li>类型别名顾名思义就是给一个类型起了另一个名称，其他地方如果需要用到该类型的时候都可以使用它的别名来代替。</li>
</ul>
<pre><code class="copyable">type otherType=number;
let other:otherType;
other=5;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>编译成<code>JavaScript</code>后：</li>
</ul>
<pre><code class="copyable">var other;
other = 5;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>值得一提的是我们给类型起了别名但并不是新建了一种类型，所以我们要遵循它的原始类型。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b06ed302524b4dee96535db269f93b06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>如果我们将不符合类型的值传给变量则会像上图这样报错。</li>
<li>类型定义对象的时候会和接口很像,甚至可以当成接口来使用。</li>
</ul>
<pre><code class="copyable">type otherObj=&#123;
    name:string
&#125;;
interface sthObj&#123;
    name:string
&#125;;
let obj1:otherObj=&#123;
    name:'掘金'
&#125;;
let obj2:sthObj=&#123;
    name:'小卢'
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这样写是完全没有问题的，那什么时候我们改用别名什么时候接口呢？因为我们的<code>type</code>只是起了别名，所以当我们要给类型拓展的时候就要使用接口了，因为<code>type</code>不可以被继承。类型别名常用于联合类型。</li>
</ul>
<h2 data-id="heading-2">字符串字面量类型⛴️</h2>
<ul>
<li>基本语法是 [<code>type</code>  <code>名称</code> = <code>字符串</code>]</li>
<li>字符串字面量类型就是约束变量为某几个字符串其中的一个，如果出现了其他的字符串则会报错。</li>
</ul>
<pre><code class="copyable">type sthingFruit= "apple" | "banana" | "mango";
let fruit:sthingFruit;
fruit="apple";
fruit="grapes"; //报错
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在上面的例子中我们将<code>sthingFruit</code>约束为只能接受 <code>apple</code> <code>banana</code> <code>mango</code>的一个类型，那么其他变量在使用这个类型的时候就只能选择里面允许的值，像上面给他一个<code>grapes</code>是不可取的。</li>
</ul>
<h2 data-id="heading-3">元组🛳️</h2>
<ul>
<li>在之前基础的学习中我们知道，可以用数组来合并相同类型的数据。</li>
</ul>
<pre><code class="copyable">let fruit:string[]=['apple','banana',"mango"];
let fruit1:string[]=['apple','banana',25]; //报错 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以看到如果给定义了<code>string</code>类型的数组添加<code>number</code>类型的数值，他就会报错<code>不能将类型“number”分配给类型“string”</code>。</li>
<li>在<code>JavaScript</code>中的数组没有这些限制，那有没有一种情况我们<code>TypeScript</code>一个数组中也可以既可以有<code>string</code>类型又有<code>number</code>类型呢？这时候就需要我们的<code>元组</code>出场了。</li>
<li>元组（<code>Tuple</code>）合并了不同类型的对象，我们可以这样书写。</li>
</ul>
<pre><code class="copyable">let fruit:[string,number,string];
fruit=['apple',25,'banana'];
fruit=['apple',25]; //报错
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>我们可以看到虽然元组可以接受不同类型的数值，但是赋值的时候他的格式和数量要跟<code>:</code>定义的类型格式数量一致。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4762edc8da9346ad9d85a0168fbc7bce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在元组中我们可以跟数组一样单一的改变对应的值。</li>
</ul>
<pre><code class="copyable">let fruit:[string,number,string];
fruit=['apple',18,'banana'];
fruit[0]='watermelon';
fruit[1]=20;
fruit[3]=21; //报错 类型不对
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>我们也可以单独拿出值来做操作但是也要严格按照类型的规范。</li>
<li>虽然在赋值的时候需要严格按照格式和数量，但是如果在后续<code>push</code>的时候是可以添加约束的类型的值的。</li>
</ul>
<pre><code class="copyable">let fruit:[string,number];
fruit=['apple',18];
fruit.push('banana');
fruit.push('grapes');
fruit.push('oranges');
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>值得注意的是我们后续如果给元组<code>push</code>的数值必须是之前定义的类型，相当于把类型限制于之前定义的类型的联合类型，正如上面的<code>string</code> <code>number</code>。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ecb7960d278402aa7df30abbcd7edf9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">写在最后👋</h2>
<ul>
<li>本文也算是记录一下<code>TypeScript</code>的学习，接下来我会持续输出<code>TypeScript</code>相关的知识，大家可以一起来学习。</li>
<li>如果您觉得这篇文章有帮助到您的的话不妨<strong>🍉关注+点赞+收藏+评论+转发🍉</strong>支持一下哟~~😛</li>
</ul>
<h2 data-id="heading-5">往期精彩🌅</h2>
<p><a href="https://juejin.cn/post/6993568844191121421" target="_blank" title="https://juejin.cn/post/6993568844191121421">「TypeScript」入门基础(一)🎯</a></p>
<p><a href="https://juejin.cn/post/6993876476068118536" target="_blank" title="https://juejin.cn/post/6993876476068118536">「TypeScript」入门基础(二)🎯</a></p>
<p><a href="https://juejin.cn/post/6994236151942905864" target="_blank" title="https://juejin.cn/post/6994236151942905864">「TypeScript」入门基础(三)🎯</a></p>
<p><a href="https://juejin.cn/post/6994610183439646727" target="_blank" title="https://juejin.cn/post/6994610183439646727">「TypeScript」入门基础(四)🎯</a></p></div>  
</div>
            