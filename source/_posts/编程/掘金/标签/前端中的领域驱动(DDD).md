
---
title: '前端中的领域驱动(DDD)'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4d2380d7b6445e1a7adcd8c5b44a126~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 02:00:16 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4d2380d7b6445e1a7adcd8c5b44a126~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>随着我们解决的场景越来越专业化和复杂化，大型SPA应用的流行，前端承担的职责越来越多。很容易导致迭代着迭代着发现代码改不动了。最后只能新起炉灶，重新开发。归根到底在于 <code>复杂度的失控</code> ，此时就需要一些理念来指导开发。</p>
<h3 data-id="heading-0">背景：</h3>
<p>为什么迭代越来越难？原因在于：</p>
<ul>
<li>
<p>问题域本身错综复杂</p>
<ul>
<li>软件本身是为了管理复杂度，我们现在面对的问题域错综复杂。为了创建真正好用的软件，开发者必须有一整套与之相关的知识体系</li>
</ul>
</li>
<li>
<p>技术模型与领域模型不匹配</p>
<ul>
<li>一般我们很容易抽象出一个独立的类、函数来放通用逻辑，这个通用类、函数只有技术维度上的通用。技术维度上的通用 <code>很容易被业务摧毁</code> 。需求上的变动或者膨胀，技术维度的通用很容易被摧毁。根本原因就是我们设计的 <code>技术模型</code> 与 <code>领域模型</code> 不匹配。于是每次需求的改动，映射到技术模型的改动可能就是极大的工作量。甚至根本改不动，在业务压力很大的时候，我们只能告诉产品经理，这个可以做，但是我们需要2个月。结局很可能就是需求方的妥协，牺牲用户的利益。导致产品越来越难用。</li>
</ul>
</li>
<li>
<p>知识的丢失</p>
<ul>
<li>任何项目都会丢失知识，外包出去的系统可能只交回了代码，知识没有传递回来。离职了，转岗了，一旦出于某种原因人们没有口头传递知识，知识就丢失了。</li>
</ul>
</li>
</ul>
<p>上这三个问题归根到底，就是我们没有在前端代码里把我们业务描述清楚。我们很多情况下是 <code>视图驱动</code> ，而不是 <code>业务驱动</code> 。很多时候只关心页面长什么样子，发了什么请求拿了什么数据。于是在业务概念上每个人理解的深度都不同。解这个问题可能采用新的领域驱动设计的开发方式会比较合适。</p>
<h3 data-id="heading-1">什么是领域驱动设计？</h3>
<blockquote>
<p>在维基百科中定义：领域驱动设计是一种由 <strong>域模型</strong> 来驱动着系统设计的思想，不是通过存储数据词典(DB表字段、ESMapper字段等等)来驱动系统设计。 <strong>领域模型是对业务模型的抽象，</strong> <strong>DDD</strong> <strong>是把业务模型翻译成系统架构设计的一种方式。</strong></p>
</blockquote>
<h4 data-id="heading-2">DDD中的模型</h4>
<p>Model与传统的POJO(DTO、DO、DAO)类等对比，都是一个类中有属性、属性有Get/Set方法，并且做传输对象。
Model与传统MVC三层架构层的业务逻辑层中的Service对比，都是处理业务行为(Action)层。
<strong>模型（Model）承载着业务的属性和具体的行为，是业务表达的方式、是</strong> <strong>DDD</strong> <strong>的内核。是一个类中有属性、属性有Get/Set方法，并且业务的行为（Action）操作也是在模型类中（充血模型）即做业务逻辑处理，又做数据传输对象，模型分为Entity、Value Object、Service这三种类型。</strong>
前面说的都是服务端术语。
简单来说，将业务概念优先于代码库的其它分类类型（例如，按文件类型分组）。这意味着，你应该基于你主要的业务领域（“问题”）及其子领域（问题的细分部分）来组织你的代码。例如，在电子商务领域，我们有产品目录、客户、订单、库存等子领域。
虽然DDD概念来自面向对象编程，依赖于类及其关系，但其核心理念可以很容易地应用到其它范式。</p>
<h3 data-id="heading-3">前端应用领域模型（来自： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fmayiprototeam%2Fgfyt69%2Foq14ia" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/mayiprototeam/gfyt69/oq14ia" ref="nofollow noopener noreferrer">前端开发-领域驱动设计 · 语雀</a> ）</h3>
<p>领域模型很多情况下都是由后端同学建立的，前端同学如何指导开发呢？</p>
<ul>
<li>
<p>理解后端领域模型</p>
<ul>
<li>弄清他们的模块划分，我们可以直接借鉴他们的模型，这样也可以保证前后端对于业务模型的理解一致。</li>
</ul>
</li>
<li>
<p>建立前端领域模型</p>
</li>
<li>
<p>分离领域层</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4d2380d7b6445e1a7adcd8c5b44a126~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>强调的是领域层的建设一定不是两个页面同时发了个请求，于是把这个请求抽出来，给与一个领域的名字。他一定被 <code>提前建立好</code> 的。在开始进行前端设计之前就被设计出来的一层。
我们要将所有页面组件与模块内的业务行为都抽离出来，放在合适的领域模块中。只要是业务行为， <code>一定有一个领域模块可以落</code> 。如果不行就是领域模型设计的不合理。
驱动领域层分离的目的并不是页面被复用，这一点在 <code>思想上</code> 一定要转化过来。领域层并不是因为被多个地方复用而被抽离。它被抽离的原因是：</p>
<ul>
<li>
<p>领域层是 <code>稳定</code> 的（页面以及与页面绑定的模块都是不稳定的）</p>
</li>
<li>
<p>领域层是 <code>解耦</code> 的（页面是会耦合的，页面的数据会来自多个接口，多个领域）</p>
</li>
<li>
<p>领域层具有 <code>极高复杂度</code> ，值得单独管理(view层处理页面渲染以及页面逻辑控制，复杂度已经够高，领域层解耦可以轻view层。 <code>view层尽可能轻量</code> 是我们架构师cnfi主推的思路)</p>
</li>
<li>
<p>领域层 <code>以层为单位</code> 是可以被 <code>复用</code> 的（你的代码可能会抛弃某个技术体系，从vue转成react，或者可能会推出一个移动版，在这些情况下，领域层这一层都是可以直接复用）</p>
</li>
<li>
<p>为了领域模型的持续 <code>衍进</code> (模型存在的目的是让人们聚焦，聚焦的好处是加强了前端团队对于业务的理解，思考业务的过程才能让业务前进)</p>
</li>
<li>
<p>主导接口约定</p>
</li>
</ul>
<p>接口约定尽量由 <code>前端主导</code> ，毕竟接口是给前端使用，前端来设计接口比较合理。</p>
<ul>
<li>开发中注意业务含义</li>
</ul>
<p>在类，方法，模块命名时要直指 <code>业务核心</code> ，保持与领域模型的一致。</p>
<ul>
<li>实时同步</li>
</ul>
<p>确保团队内部所有同学都要熟悉系统的模型。尤其是对于要熟悉并修改代码的新同学，先向他们分享我们系统的领域模型之后再介绍技术架构。工作开展的重点的不同会导致编程世界观的不同。这样子会让新同学养成习惯，在进行技术决断之前先判断是否符合现有的模型。不断的思考模型，才能够帮助我们业务成长。</p>
<h3 data-id="heading-4">在 react 中领域驱动设计？</h3>
<p>按照业务划分好模块，组织结构，视图与逻辑分离，一般来说：src目录下应该只含有 assets，pages，layouts，app 四个。</p>
<ul>
<li>
<p>按功能划分文件夹，每个功能只能包含以下四种文件：Xxx.less, Xxx.tsx, useXxx.ts，useXxx.spec.ts , 采用嵌套结构组织，同时，结合 hooks 来做到相关状态逻辑收敛与复用</p>
</li>
<li>
<p>一个文件夹包含该领域内所有逻辑（视图，样式，测试，状态，接口），禁止将逻辑放置于文件夹以外</p>
</li>
<li>
<p>如果需要由其他功能调用，利用控制反转（依赖注入）SOA 进行组合</p>
</li>
</ul>
<p>以上，也符合最小依赖，高内聚的原则，在 React 实践DDD，关键就是用好 hooks ！</p>
<p><code>DDD</code> 可以说是整个软件开发架构设计的趋势，前端中微服务实现其实也是依赖以此，把大的项目拆成相对独立的微应用，这就是划分为一个个的域。</p>
<h3 data-id="heading-5">参考</h3>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yuque.com%2Fmayiprototeam%2Fgfyt69%2Foq14ia" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yuque.com/mayiprototeam/gfyt69/oq14ia" ref="nofollow noopener noreferrer">www.yuque.com/mayiprotote…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.infoq.cn%2Farticle%2Fa7ee4z1qu95xbpktsugt" target="_blank" rel="nofollow noopener noreferrer" title="https://www.infoq.cn/article/a7ee4z1qu95xbpktsugt" ref="nofollow noopener noreferrer">www.infoq.cn/article/a7e…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.allegro.tech%2F2020%2F05%2Fhexagonal-architecture-by-example.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.allegro.tech/2020/05/hexagonal-architecture-by-example.html" ref="nofollow noopener noreferrer">Hexagonal Architecture by example - a hands-on introduction</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjishuin.proginn.com%2Fp%2F763bfbd5e926" target="_blank" rel="nofollow noopener noreferrer" title="https://jishuin.proginn.com/p/763bfbd5e926" ref="nofollow noopener noreferrer">jishuin.proginn.com/p/763bfbd5e…</a></p>
</li>
</ol></div>  
</div>
            