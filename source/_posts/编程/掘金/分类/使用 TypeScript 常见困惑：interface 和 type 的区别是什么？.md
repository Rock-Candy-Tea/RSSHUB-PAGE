
---
title: '使用 TypeScript 常见困惑：interface 和 type 的区别是什么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1970'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:54:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=1970'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flink.juejin.cn%2F%253Ftarget%253Dhttp%25253A%25252F%25252Fwww.gtalent.cn%25252Fexam%25252Finterview%25252FD1OQu4fYp5yjI3q0" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttp%253A%252F%252Fwww.gtalent.cn%252Fexam%252Finterview%252FD1OQu4fYp5yjI3q0" ref="nofollow noopener noreferrer">web前端工程师（高级）</a></strong></p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flink.juejin.cn%2F%253Ftarget%253Dhttp%25253A%25252F%25252Fwww.gtalent.cn%25252Fexam%25252Finterview%25252F49peyJvIznUbdZRL" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttp%253A%252F%252Fwww.gtalent.cn%252Fexam%252Finterview%252F49peyJvIznUbdZRL" ref="nofollow noopener noreferrer">web前端工程师（js）</a></strong></p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flink.juejin.cn%2F%253Ftarget%253Dhttp%25253A%25252F%25252Fwww.gtalent.cn%25252Fexam%25252Finterview%25252FfcaP4W7zBdowtCDi" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttp%253A%252F%252Fwww.gtalent.cn%252Fexam%252Finterview%252FfcaP4W7zBdowtCDi" ref="nofollow noopener noreferrer">高级java开发工程师(微服务/Spring Cloud)</a></strong></p>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Flink.juejin.cn%2F%253Ftarget%253Dhttp%25253A%25252F%25252Fwww.gtalent.cn%25252Fexam%25252Finterview%25252Fg4sRFGjOEQAbt9ZX" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=https%3A//link.juejin.cn/%3Ftarget%3Dhttp%253A%252F%252Fwww.gtalent.cn%252Fexam%252Finterview%252Fg4sRFGjOEQAbt9ZX" ref="nofollow noopener noreferrer">高级python开发工程师</a></strong></p>
<p>当我们使用 TypeScript 时，就会用到 <code>interface</code> 和 <code>type</code>，平时感觉他们用法好像是一样的，没啥区别，都能很好的使用，所以也很少去真正的理解它们之间到底有啥区别。我们开发过经常或这么来定义类型：</p>
<pre><code class="copyable">interface Point &#123;
    x: number;
    y: number;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者这样定义：</p>
<pre><code class="copyable">type Point = &#123;
    x: number;
    y: number;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>interface</code> 和 <code>type</code>之间的差异不仅仅是次要语法声明。那么，今天我们就来看看这两家伙之间存在啥不可告人的秘密。</p>
<h3 data-id="heading-0">类型和类型别名</h3>
<p>TypeScript 有 <code>boolean</code>、<code>number</code>、<code>string</code> 等基本类型。如果我们想声明高级类型，我们就需要使用<strong>类型别名</strong>。</p>
<p>类型别名指的是为类型创建新名称。<strong>需要注意的是</strong>，我们并没有定义一个新类型。使用<code>type</code>关键字可能会让我们觉得是创建一个新类型，但我们只是给一个类型一个新名称。</p>
<p>所以我们所以 type 时，不是在创建新的类别，而是定义类型的一个别名而已。</p>
<h3 data-id="heading-1">接口</h3>
<p>与 <code>type</code>相反，接口仅限于对象类型。它们是描述对象及其属性的一种方式。类型别名声明可用于任何基元类型、联合或交集。<strong>在这方面，接口被限制为对象类型</strong>。</p>
<h3 data-id="heading-2">interface 和 type 的相似之处</h3>
<p>在讨论它们的区别之前，我们先来看看它们的相似之处。</p>
<h4 data-id="heading-3">两者都可以被继承</h4>
<p>interface 和 type 都可以继承。另一个值得注意的是，接口和类型别名并不互斥。类型别名可以继承接口，反之亦然。</p>
<p>对于一个接口，继承另一个接口</p>
<pre><code class="copyable">interface PartialPointX &#123; x: number; &#125;
interface Point extends PartialPointX &#123; y: number; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，继承一个类型</p>
<pre><code class="copyable">type PartialPointX = &#123; x: number; &#125;;
interface Point extends PartialPointX &#123; y: number; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型继承另一个类型：</p>
<pre><code class="copyable">type PartialPointX = &#123; x: number; &#125;;
type Point = PartialPointX & &#123; y: number; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，继承一个接口：</p>
<pre><code class="copyable">interface PartialPointX &#123; x: number; &#125;
type Point = PartialPointX & &#123; y: number; &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">实现</h4>
<p>类可以实现接口以及类型（TS 2.7+）。但是，类不能实现联合类型。</p>
<pre><code class="copyable">interface Point &#123;
 x: number;
 y: number;
&#125;

class SomePoint implements Point &#123;
 x = 1;
 y = 2;
&#125;

type AnotherPoint = &#123;
 x: number;
 y: number;
&#125;;

class SomePoint2 implements AnotherPoint &#123;
 x = 1;
 y = 2;
&#125;

type PartialPoint = &#123; x: number; &#125; | &#123; y: number; &#125;;

// Following will throw an error
class SomePartialPoint implements PartialPoint &#123;
 x = 1;
 y = 2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">interface 和 type 的区别</h3>
<h4 data-id="heading-6">并集和交集类型</h4>
<p>虽然接口可以被扩展和合并，但它们不能以联合和交集的形式组合在一起。类型可以使用联合和交集操作符来形成新的类型。</p>
<pre><code class="copyable">// object
type PartialPointX = &#123; x: number; &#125;;
type PartialPointY = &#123; y: number; &#125;;

// 并集
type PartialPoint = PartialPointX | PartialPointY;

// 交集
type PartialPoint = PartialPointX & PartialPointY;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">声明合并</h4>
<p>TypeScript编译器合并两个或多个具有相同名称的接口。 这不适用于类型。 如果我们尝试创建具有相同名称但不同的属性的两种类型，则TypeScript编译器将抛出错误。</p>
<pre><code class="copyable">// These two declarations become:
// interface Point &#123; x: number; y: number; &#125;
interface Point &#123; x: number; &#125;
interface Point &#123; y: number; &#125;

const point: Point = &#123; x: 1, y: 2 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">元组类型</h4>
<p>元组(键值对)只能通过<code>type</code>关键字进行定义。</p>
<pre><code class="copyable">type Point = [x: number, y: number];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没有办法使用接口声明元组。不过，我们可以在接口内部使用元组</p>
<pre><code class="copyable">interface Point &#123;
  coordinates: [number, number]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">我们应该使用哪一个？</h3>
<p>一般来说，接口和类型都非常相似。</p>
<p>对于库或第三方类型定义中的公共API定义，应使用接口来提供声明合并功能。除此之外，我们喜欢用哪个就用哪个，但是在整个代码库中应该要保持一致性。</p></div>  
</div>
            