
---
title: '疯了吧！这帮人居然用 Go 写_前端_？（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2470'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 02:54:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=2470'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者 ｜ 郑嘉涛（羣青）
来源｜<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FCOPlMcmbuVsWoW7yS2zPHw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/COPlMcmbuVsWoW7yS2zPHw" ref="nofollow noopener noreferrer">尔达 Erda 公众号</a>
​</p>
<h1 data-id="heading-0">前言</h1>
<p>​</p>
<p>上篇我们讲了故事发生的背景，也简单阐述了组件及协议的设想：
​</p>
<blockquote>
<p>一、丰富的通用组件库。</p>
</blockquote>
<p>二、组件渲染能力，将业务组件渲染成通用组件。
三、协议渲染能力，以处理复杂交互。</p>
<p>​</p>
<p>以及这种开发模式带来的好处：
​</p>
<blockquote>
<p>这样的设计初衷旨在大量减少前端工作，尤其是前后端对接方面，甚至可以认为对接是“反转”的，体现在两个层面：接口定义的反转和开发时序的变化。</p>
</blockquote>
<p>​</p>
<p>如果你对我们的设计思路还不够了解，可以先阅读上篇：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MDYzNTAxMw%3D%3D%26mid%3D2247484634%26idx%3D1%26sn%3Def4faeae7d2690a0bbfb96e05ae350ee%26chksm%3Dce222e30f955a7269b88e91f9446fc4192081e10a7c03000b668e2da6e2ae64f76f4e6a5351e%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg2MDYzNTAxMw==&mid=2247484634&idx=1&sn=ef4faeae7d2690a0bbfb96e05ae350ee&chksm=ce222e30f955a7269b88e91f9446fc4192081e10a7c03000b668e2da6e2ae64f76f4e6a5351e&scene=21#wechat_redirect" ref="nofollow noopener noreferrer">《疯了吧！这帮人居然用 Go 写“前端”？（一）》</a>。
​</p>
<p>本篇我将更细致地介绍组件渲染和协议渲染，以及如何通过这两种渲染做到前端彻底不关注业务。
​</p>
<p>当然最后你会发现是否 REST 并非重要，重要的是合理的切分关注点，而框架只是运用切分的帮助手段。
​</p>
<h1 data-id="heading-1">组件渲染</h1>
<p>具体而言，针对一个通用组件，如何完成业务逻辑？</p>
<p>比如说下面同样的一个卡片组件（Card），它由通用的元素构成和呈现：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">cardComp:</span>
  <span class="hljs-attr">props:</span>
    <span class="hljs-attr">titleIcon:</span> <span class="hljs-string">bug-icon</span>
    <span class="hljs-attr">title:</span> <span class="hljs-string">Title</span>
    <span class="hljs-attr">subContent:</span> <span class="hljs-string">Sub</span> <span class="hljs-string">Content</span>
    <span class="hljs-attr">description:</span> <span class="hljs-string">Description</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，通过不同的 props，可以渲染出不同的场景。
​</p>
<h2 data-id="heading-2">场景 1：需求卡片</h2>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">kanbanCardComp:</span>
  <span class="hljs-attr">props:</span>
    <span class="hljs-attr">titleIcon:</span> <span class="hljs-string">requirement-icon</span>
    <span class="hljs-attr">title:</span> <span class="hljs-string">一个简单的需求</span>
    <span class="hljs-attr">subContent:</span> <span class="hljs-string">完成容器扩容不抖动</span>
    <span class="hljs-attr">description:</span> <span class="hljs-string">需要存储记录用户的扩容改动，通过调用内部封装的</span> <span class="hljs-string">k8s</span> <span class="hljs-string">接口以实现。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">场景 2：打包任务卡片</h2>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">taskCardComp:</span>
  <span class="hljs-attr">props:</span>
    <span class="hljs-attr">titleIcon:</span> <span class="hljs-string">flow-task-icon</span>
    <span class="hljs-attr">title:</span> <span class="hljs-string">buildpack</span> <span class="hljs-string">(java)</span>
    <span class="hljs-attr">subContent:</span> <span class="hljs-string">✅</span> <span class="hljs-string">success</span>
    <span class="hljs-attr">description:</span> <span class="hljs-string">time</span> <span class="hljs-number">02</span><span class="hljs-string">:09,</span> <span class="hljs-string">begin</span> <span class="hljs-string">at</span> <span class="hljs-number">10</span><span class="hljs-string">:21</span> <span class="hljs-string">am</span> <span class="hljs-string">...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于后端来说，只需要遵循通用组件的数据定义，根据组件渲染器的规则，实现渲染方法即可（需要强调的是，后端不需要知道 UI 的长相，后端面对的始终是数据）。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">Render</span><span class="hljs-params">(ctx Context, c *Comp)</span> <span class="hljs-title">error</span></span> &#123;
  <span class="hljs-comment">// 1. query db or internal service</span>
  <span class="hljs-comment">// 2. construct comp</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在交互方面，我们也需要通用组件定义所有的操作，操作（operation）可以认为是交互的影响或者说结果。举个例子，其实查询渲染就是最基础的一种操作；而对于需求卡片来说，点击查看详情，右上角的删除、编辑等都是操作：</p>
<p>不过在通用组件层面，无需感知业务，定义的都是通用的 click, menu-list 等操作，由业务组件实现具体的业务。</p>
<p>前端在呈现层表述的交互（比如悬浮、点击、释放等），最终都会对应到通用组件定义的操作，而操作即是一次标准的组件渲染请求。可以这么思考：假设页面已经呈现在用户面前了，用户通过鼠标（也可能是触摸板）触发的浏览器交互事件，都由前端“呈现器”翻译成组件操作（operation），比如说删除操作，一旦执行操作组件便会触发重新渲染。
​</p>
<p>下面的伪代码表述了操作在渲染中的体现：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-comment">// 伪代码，精简了数据结构和条件判断</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">Render</span><span class="hljs-params">(ctx Context, c *Comp, ops <span class="hljs-keyword">string</span>)</span> <span class="hljs-title">error</span></span> &#123;
  <span class="hljs-keyword">if</span> ops != <span class="hljs-string">"view"</span> &#123;
    doOps()
  &#125;
  <span class="hljs-comment">// continue render (aka re-render)</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">nil</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是缺了点什么？没错，后端也无法凭空变出一个卡片。组件渲染必须要有输入的部分，可能是用户直接或者间接的输入。比如用户说：“我想要看 id=42 的需求卡片”，这就是直接的输入，一般会在 url 上体现。另一种情况则是间接的输入：“我想要看 status = DONE 的所有需求卡片“，那么针对某一张需求卡片而言，它所需的 id，是从另一个组件 - 需求列表中获得的。</p>
<p>具体这个数据怎么在组件间绑定，我们会在后续章节（协议渲染）中详细阐述。现在只需要知道，对于单个组件的渲染（也就是业务组件）而言，我们规范了开发者只需要定义组件渲染必要的输入。这是一个很有吸引力的做法，通过参数屏蔽外界逻辑，能够有效地做到高内聚和低耦合。</p>
<p>当然有输入就有输出（要知道数据绑定肯定是把一个组件的输出绑定在另一个组件的输入）。当然交互其有状态的特性（在协议渲染中会详细阐述），我们最终让输入输出合并在一个 <code>state</code> 中体现，仍然是需求卡片的例子：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">kanbanCardComp:</span>
  <span class="hljs-attr">props:</span>
    <span class="hljs-attr">titleIcon:</span> <span class="hljs-string">requirement-icon</span>
    <span class="hljs-attr">title:</span> <span class="hljs-string">一个简单的需求</span>
    <span class="hljs-attr">subContent:</span> <span class="hljs-string">完成容器扩容不抖动</span>
    <span class="hljs-attr">description:</span> <span class="hljs-string">需要存储记录用户的扩容改动，通过调用内部封装的</span> <span class="hljs-string">k8s</span> <span class="hljs-string">接口以实现。</span>
  <span class="hljs-attr">state:</span>
    <span class="hljs-attr">ticketId:</span> <span class="hljs-number">42</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后一张大图来总结一下组件的渲染过程：</p>
<h1 data-id="heading-4">协议渲染</h1>
<p>这里我们需要引申一个实际的问题，以 web ui 为例：当用户访问一个页面时，这个页面并非只有一个组件，比如事项看板页面，就有诸如过滤器、看板甬道、事项卡片、类型切换器等多个组件。</p>
<p>并且，有个头疼的问题：组件之间显然是有联动的。比如过滤器的过滤条件控制了看板甬道的列表结果。
传统的 web 开发，这些联动肯定是由前端代码来实现的。但如果前端来实现这些联动关系，显然就需要深度理解和参与业务了，这与我们整个设计思路是违背的。</p>
<p>这里需要我们有个清晰的认知：在实际的场景中，绝不是标准化单个组件的结构后，前后端就能彻底分离的。换言之，仅将结构的定义由后端转移到前端，只达成了一半：在静态层面解耦了前后端。</p>
<p>而另一半，需要我们将组件间联动、对组件的操作、操作导致重新渲染等，也能由渲染器进行合适处理，也就是在动态层面解耦前后端。</p>
<p>在讲组件渲染的时候我们刻意留了一个悬念：为了保持组件的高内聚低耦合，我们将组件需要的所有输入都参数化，并将输入和输出参数合称为“状态”（state）。那如何将参数、状态串联起来，完成整个页面的逻辑呢？</p>
<p>想想其实也很简单，我们需要有一个协议去规范定义这些依赖关系和传递方式，详见如下形式。</p>
<p>protocol.yaml：
​</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-string">//</span> <span class="hljs-string">组件初始值</span>
<span class="hljs-attr">component:</span>
  <span class="hljs-attr">kanbanCardComp:</span>
  <span class="hljs-attr">state:</span>
      <span class="hljs-string">//</span> <span class="hljs-attr">ticketId:</span> <span class="hljs-string">??</span>
    <span class="hljs-attr">operations:</span>
      <span class="hljs-attr">click:</span>
        <span class="hljs-attr">reload:</span> <span class="hljs-literal">true</span>
  <span class="hljs-attr">ticketDetailDrawerComp:</span>
    <span class="hljs-attr">state:</span>
      <span class="hljs-attr">visible:</span> <span class="hljs-literal">false</span>
      <span class="hljs-string">//</span> <span class="hljs-attr">ticketId:</span> <span class="hljs-string">??</span>
    <span class="hljs-attr">operations:</span>
      <span class="hljs-attr">close:</span>
        <span class="hljs-attr">reload:</span> <span class="hljs-literal">true</span>
<span class="hljs-string">//</span> <span class="hljs-string">渲染过程</span>
<span class="hljs-attr">rendering:</span>
  <span class="hljs-attr">__Trigger__:</span>
    <span class="hljs-attr">kanbanCardComp:</span>
      <span class="hljs-attr">operations:</span>
        <span class="hljs-attr">click:</span> <span class="hljs-string">set</span> <span class="hljs-string">ticketDetailDrawerComp.state.visible</span> <span class="hljs-string">=</span> <span class="hljs-literal">true</span>
    <span class="hljs-attr">ticketDetailDrawerComp:</span>
      <span class="hljs-attr">operations:</span>
        <span class="hljs-attr">close:</span> <span class="hljs-string">set</span> <span class="hljs-string">ticketDetailDrawerComp.state.visible</span> <span class="hljs-string">=</span> <span class="hljs-literal">false</span>
  <span class="hljs-attr">__Default__:</span>
    <span class="hljs-attr">kanbanCardComp:</span>
      <span class="hljs-attr">state:</span>
        <span class="hljs-attr">ticketId:</span> &#123;&#123; <span class="hljs-string">url.path.2</span> &#125;&#125;
    <span class="hljs-attr">ticketDetailDrawerComp:</span>
      <span class="hljs-attr">state:</span>
        <span class="hljs-attr">ticketId:</span> &#123;&#123; <span class="hljs-string">kanbanCardComp.state.ticketId</span> &#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在进行协议渲染时，<strong>首先</strong>执行 <code>__Trigger__</code> 部分，操作类型的渲染会临时性地修改部分组件的状态；<strong>其次</strong>执行 <code>__Default__</code> 部分，进行组件之间的数据绑定；<strong>最后</strong>会进行单个业务组件的渲染，这部分在第一篇文章中已经详细阐述。</p>
<p>不过最终需要将这个协议渲染之后给到前端，因为 <code>rendering</code> 不过只是过程数据，最终需要转化成平凡的值。以这个例子而言，（假设用户进行了卡片的 click 操作）协议最终渲染成：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">component:</span>
  <span class="hljs-attr">kanbanCardComp:</span>
    <span class="hljs-attr">props:</span>
      <span class="hljs-string">//</span> <span class="hljs-string">后端组件基于</span> <span class="hljs-string">ticketId=42</span> <span class="hljs-string">渲染出的具体数据</span>
      <span class="hljs-attr">titleIcon:</span> <span class="hljs-string">requirement-icon</span>
      <span class="hljs-attr">title:</span> <span class="hljs-string">一个简单的需求</span>
      <span class="hljs-attr">subContent:</span> <span class="hljs-string">完成容器扩容不抖动</span>
      <span class="hljs-attr">description:</span> <span class="hljs-string">需要存储记录用户的扩容改动，通过调用内部封装的</span> <span class="hljs-string">k8s</span> <span class="hljs-string">接口以实现。</span>
  <span class="hljs-attr">state:</span>
      <span class="hljs-attr">ticketId:</span> <span class="hljs-number">42</span>
    <span class="hljs-attr">operations:</span>
      <span class="hljs-attr">click:</span>
        <span class="hljs-attr">reload:</span> <span class="hljs-literal">true</span>
  <span class="hljs-attr">ticketDetailDrawerComp:</span>
    <span class="hljs-attr">props:</span>
      <span class="hljs-string">//</span> <span class="hljs-string">后端组件基于</span> <span class="hljs-string">ticketId=42</span> <span class="hljs-string">渲染出的具体数据</span>
      <span class="hljs-string">...</span>
    <span class="hljs-attr">state:</span>
      <span class="hljs-attr">visible:</span> <span class="hljs-literal">true</span>
      <span class="hljs-attr">ticketId:</span> <span class="hljs-number">42</span>
    <span class="hljs-attr">operations:</span>
      <span class="hljs-attr">close:</span>
        <span class="hljs-attr">reload:</span> <span class="hljs-literal">true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得强调的一点是，前端不需要知道组件之间的联动。所有的联动，都通过重新渲染来实现。这意味着，每次操作，会导致重新渲染这个协议。而从内部来说，则是先进行操作的落实（比如删除、更新），即调用确定的接口执行操作，然后进行场景的重新渲染。
​</p>
<p>简单的说就是前端每次发生操作，只要告诉后端我操作了什么（operation），后端执行操作之后立刻刷新页面，当然实际的流程会稍微复杂。</p>
<p>从上图中我们可以看到，每次的操作是非常“短视”的，尤其是前端可以说只需要“告诉”后端做了什么操作，别的一概无需知晓。那么就会有人问了：如果某次操作需要传递数据怎么办？比如传统的对接方式，如果要删除一个资源，前端就必须传入后端资源的 ID。那就需要讲到协议必须要有的一个特性：状态。</p>
<p>RESTful API 是无状态的，但是业务逻辑需要有先后顺序，势必就需要存在状态。传统的做法是由前端维系这个状态，尤其是 SPA 更是将所有的状态都维系在内存。
​</p>
<p>举个例子，比如一个编辑表单，首先打开表单之后，前端需要调用后端接口传入资源 ID 取得数据，并将数据 copy 进表单进行渲染；当保存按钮 click 触发时，需要取得表单中当前值，并调用后端 save 接口进行保存。</p>
<p>我们知道，当前端不关心业务时，状态的维系也随之破碎。这个状态必须要下沉到和渲染同一个位置，准确的说是协议渲染这一层（因为组件单体我们刻意设计成内聚和无状态）。</p>
<p>如何做到状态的下移呢？其实也非常简单，我们知道一个事实，那就是操作之前必定渲染（也就是只有访问了页面才能在页面上点击）。我们只需要在渲染的时候提前预判之后操作所需要的全部数据，提前内置在协议中；而前端在执行操作时，将协议以及操作的对象等信息悉数上报即可。当组件渲染器接收到这个协议的时候，是可以拿到所有需要的参数的（因为本来就是我自己为自己准备的），此时执行完操作后，就开启下一个预判，并重新渲染协议给予前端进行界面呈现。</p>
<p>下面的例子中，可以看到当用户进入第一页（currentPageNo = 1）时，我们早已料到用户会进行下一页（next）操作，就已经把这个操作所需要的参数（pageNo = 2）置于协议之中了；随后用户针对组件 <code>paginationBar</code> 进行了一次操作 <code>next</code>，操作处理时便能拿到所需数据。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">components:</span>
  <span class="hljs-attr">paginationBar:</span>
    <span class="hljs-attr">state:</span>
      <span class="hljs-attr">currentPageNo:</span> <span class="hljs-number">1</span>
    <span class="hljs-attr">operations:</span>
      <span class="hljs-attr">next:</span>
        <span class="hljs-attr">reload:</span> <span class="hljs-literal">true</span>
        <span class="hljs-attr">meta:</span>
          <span class="hljs-attr">pageNo:</span> <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所谓的“早已想到”并非难事，因为各个业务组件中会定义此业务组件实现了通用组件的那些操作，我们要求在定义这些操作的时候，必须要定义这些操作所必须要的外界传入参数（之所以说外界，是因为有些业务参数在组件内部就可以自行处理，而无需依赖外部组件，比如 state 或者 props 的数据信息已经充足）。</p>
<p>最后针对呈现而言，还需要补充组件之间的层级关系，最终形成一个树形的关系，为了布局也需要填充一些“无意义”的组件像 Container、LRContainer 等：</p>
<p>不过这些都是静态的数据，可以直接放入协议，也无需渲染：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">hierarchy:</span>
  <span class="hljs-attr">root:</span> <span class="hljs-string">ticketManage</span>
  <span class="hljs-attr">structure:</span>
    <span class="hljs-attr">ticketManage:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">head</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">ticketKanban</span>
    <span class="hljs-attr">head:</span>
      <span class="hljs-attr">left:</span> <span class="hljs-string">ticketFilter</span>
      <span class="hljs-attr">right:</span> <span class="hljs-string">ticketViewGroup</span>

<span class="hljs-attr">components:</span>
  <span class="hljs-attr">ticketManage:</span>
    <span class="hljs-attr">type:</span> <span class="hljs-string">Container</span>
  <span class="hljs-attr">head:</span>
    <span class="hljs-attr">type:</span> <span class="hljs-string">LRContainer</span>
  <span class="hljs-string">...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">暂时告一段落</h1>
<p>我们通过组件渲染、协议渲染以及一个通用组件库完成了彻底的前后端分离。不过我们在实践中发现，很多时候彻底的前后端分离会带来一定的困难，这也是我们将认为协议承载的是场景而非页面。</p>
<p>如果是彻底的前后端分离，那势必整个页面甚至整个网站就应该是一个协议，因为只要跳出协议或者说页面间切换，就会有业务含义。但真实情况是，如果一个协议中有太多的组件需要编排，这个复杂编排对于开发者而言是非常繁琐的，并且这个复杂性带来的损失完全淹没彻底前后端分离带来的优势。</p>
<p>从务实角度出发，我们更应该实践“关注点分离”而非是彻底的“前后端分离”。在设计组件以及协议时，我们总是问自己：</p>
<ul>
<li>前端关注什么？</li>
<li>后端关注什么？</li>
<li>框架/协议应该关注什么？</li>
</ul>
<p>最终我们框架选择和传统对接方式共存的形式，并且能够友好地互相操作。
​</p>
<p>比如前端在呈现一个组件的时候，可以选择“偷偷”调用一些 RESTful API 来完成特定的事情，也可以在一个页面中“拼凑“多个协议进行联动等等。</p>
<p>我们也发现，当大量业务逻辑能够从前端下沉到后端时，前端呈现层的逻辑将变得非常简单（数量有限的组件）。我们意外获得了多端支持能力，比如可以实现 CLI 的呈现层，也可以实现 IDE 插件的呈现层等等。</p>
<p>当然我们现在并没有实现这些，不过相信如果是聪明的你，实现这个不难吧～</p>
<p>目前 Erda 的所有代码均已开源，真挚的希望你也能够参与进来！
​</p>
<ul>
<li><strong>Erda Github 地址：</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ferda-project%2Ferda" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/erda-project/erda" ref="nofollow noopener noreferrer"><em>https://github.com/erda-project/erda</em></a></li>
<li><strong>Erda Cloud 官网：</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.erda.cloud%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.erda.cloud/" ref="nofollow noopener noreferrer"><em>https://www.erda.cloud/</em></a></li>
</ul></div>  
</div>
            