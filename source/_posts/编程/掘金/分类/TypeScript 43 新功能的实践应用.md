
---
title: 'TypeScript 4.3 新功能的实践应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39af4fe638c48018cf6f42b1df78877~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 03 Jul 2021 23:34:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39af4fe638c48018cf6f42b1df78877~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文通过解决在实际工作中遇到的问题，层层剖析解法，带你了解 TS4.3 的高级特性，一起来看看吧。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39af4fe638c48018cf6f42b1df78877~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>已经成为前端标配的 TypeScript 在 5 月底发布 4.3 版本。作为一个小版本迭代，粗看并没有什么令人惊艳的新功能。但如果你真的有在持续关注 TypeScript，那么其中的一项更新值得重点关注：</p>
<blockquote>
<p>Template String Type Improvements</p>
</blockquote>
<p>为什么值得注意呢？看一下 TS 4.0 以来的三条更新记录：</p>
<blockquote>
<p>4.0 版本新增 Variadic Tuple Types</p>
<p>4.1 版本新增 Template Literal Types</p>
<p>4.3 版本完善 Template Literal Types</p>
</blockquote>
<p>然后我现在告诉你，Tuple Types 和 Template Literal Types 其实是一对关系密切的好哥们。所以，聪明的你是不是已经猜到，既然 TS 在 Tuple Types 和 Template Literal Types 持续发力，那很大概率，现在应该可以用它们来完成一些以前不太可能完成的事情。</p>
<p>而我呢，早在 4 月份的时候就发现了 TS 4.3 将要发布的这个新功能，并且已经在预览版中亲身体验，解决了一个非常有趣的小问题：<strong>如何将对象类型的所有可能的合法路径静态类型化。</strong></p>
<p>下面就让我带你看看 4.3 增强之后的 Template Literal Types 可以解决一个什么样的真实问题吧。</p>
<h2 data-id="heading-0">还原问题现场</h2>
<p>我们团队现在的项目中使用 FinalForm 管理表单状态，但这不是重点，重点是其中一个和 lodash set 方法几乎一模一样的 change 方法，做不到完全的类型安全。这导致我们在写相关的 TS 代码时，只能用稍显丑陋的 as any 逃生。具体示例看 👇 的代码：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> NestedForm = &#123;
  <span class="hljs-attr">name</span>: [<span class="hljs-string">'赵'</span> | <span class="hljs-string">'钱'</span> | <span class="hljs-string">'孙'</span> | <span class="hljs-string">'李'</span>, <span class="hljs-built_in">string</span>];
  age: <span class="hljs-built_in">number</span>;
  articles: &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>;
    sections: <span class="hljs-built_in">string</span>[];
    date: <span class="hljs-built_in">number</span>;
    likes: &#123;
      <span class="hljs-attr">name</span>: [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>];
      age: <span class="hljs-built_in">number</span>;
      &#125;[];
  &#125;[];
&#125;

<span class="hljs-comment">// FinalForm 中的一个常用 API，语义和 lodash 中的 set 几乎一样</span>
<span class="hljs-keyword">interface</span> FormApi<FormValues = Record<string, any>> &#123;
  <span class="hljs-attr">change</span>: <F extends keyof FormValues>(name: F, value?: Partial<FormValues[F]>) => void
&#125;

const form: FormApi<NestedForm> = // 假装有了一个 form 实例

// 基本使用
form.change('age', '20') // 这样是类型安全的

// 可大量的真实使用场景其实类型不安全，但又完全合情合理，所以只能使用 as any 逃生
form.change('name.0', '刘')
form.change('articles.0.title', 'some string')
form.change('articles.0.sections.2', 'some string')

// 项目中逃生代码
<Select
  placeholder="请选择类型"
  onChange=&#123;Kind => &#123;
    // 清空其他字段, 只保留 Kind
    form.change(`$&#123;field&#125;.Env.$&#123;i&#125;` as any, &#123; Kind &#125;);
  &#125;&#125;
>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以问题就是：<strong>我们能让类似的方法完全的类型安全吗？</strong></p>
<p>答案我也不藏着掖着了：<strong>解决此类问题需要 4.3 增强之后的 Template Literal Types 和 4.0 版本新增 Variadic Tuple Types，再加上一些其它早就有的高级特性。</strong></p>
<p>看到这些新增和高级字眼，妥妥的一道高阶 TS 面试题 👀 有木有。而我确实也能向你保证，如果接下来的内容，你能做到既知其然，又知其所以然，TS 这关你稳过。</p>
<h2 data-id="heading-1">解决方案拆解，由浅入深</h2>
<h3 data-id="heading-2">第一步：<strong>核心技术支撑</strong></h3>
<ul>
<li>
<p>很多时候，解决方案往往已经<strong>藏在问题</strong>中</p>
<ul>
<li>
<p>change 方法类型安全的部分是对象最外层的 <strong>key：</strong></p>
<ul>
<li><code>name</code></li>
<li><code>age</code></li>
<li><code>articles</code></li>
</ul>
</li>
<li>
<p>类型不安全的部分是对象其它的嵌套路径：</p>
<ul>
<li><code>name.0</code></li>
<li><code>name.1</code></li>
<li><code>articles.0.likes.0.age</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>我们的目标其实很清晰了：<strong>得到对象的全部可能路径</strong>。也许这依然有些模糊，但如果如果我换个说法，你或许就明白了：给你一颗二叉树，问题是从根节点出发，所有可能的路径。</p>
<p>但是这些和 Template Literal Types 有什么关系吗？！当然有，而且非常有。我们都知道 <code>articles.0.likes.0.age</code> 是字符串，但是它更是 template string type。也正是它，可以让我们在类型层面表示出一个对象的全部嵌套子路径。</p>
<h3 data-id="heading-3">第二步：Template Literal Types 搭配 Variadic Tuple Types 显奇效</h3>
<p>这一步不要求你能全部看懂，先有个大致的概念和感觉，先让你知道，Template Literal Types 搭配 Variadic Tuple Types，再用上一些泛型技巧，可以稳稳的拿到对象的全部嵌套子路径。后面会详细介绍如何用泛型求解对象的全部嵌套子路径。</p>
<ul>
<li>
<p>核心操作</p>
<ul>
<li>
<p>join</p>
<ul>
<li>['articles', number] => <code>articles.$&#123;number&#125;</code></li>
</ul>
</li>
</ul>
</li>
</ul>

<ul>
<li>
<p>split</p>
<ul>
<li><code>articles.$&#123;number&#125;</code> => '['articles', number]</li>
</ul>
</li>
<li>
<p>详细操作</p>
<ul>
<li>
<ul>
<li>
<p>&#123; name: &#123; firstName: string, secondName: string &#125;, hobby: string[] &#125;</p>
</li>
<li>
<p>每一个路径都是一个 tuple，所有路径就是所有 tuple 的联合 👇</p>
</li>
<li>
<p>['name'] | [hobby] | ['name', 'firstName'] | ['name', 'secondName'] | ['hobby', number]</p>
</li>
<li>
<p>tuple 可以轻松转为 template string type 👇</p>
</li>
<li>
<p><code>name</code> | <code>hobby</code> | <code>name.firstName</code> | <code>name. secondName</code> | <code>hobby.$&#123;number&#125;</code></p>
</li>
<li>
<p>然后就是如何根据 path 得到 path 对应的 value 的类型 👇</p>
<ul>
<li>给定 <code>name.firstName</code> 可以知道对应的 value 类型是 string</li>
<li>给定 <code>hobby.$&#123;number&#125;</code> 可以知道对应的 value 类型是 string</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>结论：template string type 与 tuple type 可以等价转换</p>
</li>
</ul>
<h3 data-id="heading-4">第三步：你可能不了解<strong>的 TS 高级特性</strong></h3>
<p>在具体详解泛型函数之前，本节想要先介绍一些你可能不了解 TS 高级特性，如果你非常有自信，可以略过此节，直接去看后面的泛型函数，如果发现看不懂，回头再看此节也不迟。</p>
<h4 data-id="heading-5">1.  你可能不了解的 TS 类型系统</h4>
<p>我们知道 TS 最核心的功能就是一套静态类型系统，但你真的懂 TS 类型系统吗？让我问你一个问题测试一下：<strong>TS 的类型是值的集合吗？</strong></p>
<p>这是一个非常有趣的问题，正确答案是：编程语言中的类型，<strong>除了一个特例之外</strong>，确实都是值的集合。但因为特例的存在，我们就不能将编程语言中的类型视为值的集合。这个特例在 TS 中叫 <strong>never</strong>，并无对应的值，<strong>用于表示代码会崩溃退出或陷入死循环</strong>。并且，never 是所有类型的子类型，这意味着你写的任何看似被静态类型保护着的安全无忧的函数，实际运行时也都有可能崩溃或死循环。很无奈，这种没人喜欢的可能性是静态类型系统允许的合法行为。所以，静态类型也不是万能的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eef77eb8e02745d38b8c7443e9b8ea0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2.  <em>Conditional types</em></h4>
<blockquote>
<p>At the heart of most useful programs, we have to make decisions based on input.</p>
</blockquote>
<blockquote>
<p><em>Conditional types</em> help describe the relation between the types of inputs and outputs.</p>
</blockquote>
<p>条件类型的引入，是 TS 泛型开始发光发热的基础。我们都知道，编程不可能离开用条件分支做决定，任何实际编程项目中，都随处可见 if else。</p>
<p>TS 泛型中最普通的条件分支是这个样子的:</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">SomeType <span class="hljs-keyword">extends</span> OtherType ? TrueType : FalseType;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以基于条件分支做一些有用事情。比如判断一个类型是不是数组类型，如果是，就返回数组的元素类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Flatten<T> = T <span class="hljs-keyword">extends</span> unknown[] ? T[<span class="hljs-built_in">number</span>] : T;

<span class="hljs-comment">// Extracts out the element type.</span>
<span class="hljs-keyword">type</span> Str = Flatten<<span class="hljs-built_in">string</span>[]>;
<span class="hljs-comment">//   string</span>

<span class="hljs-comment">// Leaves the type alone.</span>
<span class="hljs-keyword">type</span> Num = Flatten<<span class="hljs-built_in">number</span>>;
<span class="hljs-comment">//   number</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">Distributive Conditional Types</h5>
<blockquote>
<p>When conditional types act on <strong>a generic type</strong>, they become <strong><em>distributive</em></strong> when given <strong>a union type</strong>.</p>
</blockquote>
<p>编程除了用分支做决定外，还离不开循环，毕竟一个个手写是完全不现实的，TS 泛型函数并没有常规意义上的 for 或 while 循环，但却有 Distributive Conditional Types，其作用非常类似数组的 map 方法，只不过是作用对象是 union 类型而已。具体表现可以直接看下面的图示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d724a2b6dbc44b399c3c28f8645f8b4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">3.  Inferring Within Conditional Types</h4>
<p>关于条件类型还有一个不可缺失的高阶特性：infer 推断。TS 的 infer 能力可以让我们使用声明式的编程方法从一个复杂复合类型中精准提取出我们感兴趣的那部分。</p>
<blockquote>
<p>Here, we used the <code>infer</code> keyword to <strong>declaratively</strong> introduce a new generic type variable named <code>Item</code> instead of <strong>specifying how to retrieve</strong> the element type of <code>T</code> within the true branch.</p>
</blockquote>
<p>例如上面提取数组元素类型的泛型可以用 infer 实现如下，看上去是不是更简洁省劲一些呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Flatten<Type> = Type <span class="hljs-keyword">extends</span> <span class="hljs-built_in">Array</span><infer Item> ? Item : Type;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">4.  元组 tuple 和模版字符串类型 template string type 的递归操作</h4>
<p>这一小节之前的内容都只算热身，这一小节的递归泛型是本文核心。解决方案拆解的第一步已经指出核心技术支撑是 Variadic Tuple Types 和 Template Literal Types。这一小节将在条件泛型和 infer 的基础上引入 tuple 和 template string 的递归操作。</p>
<p>Tuple 就是 length 固定，每一个元素类型也固定的 Array，如下面代码所示，Test1 是一个 tuple，length 固定为 4，每一个元素类型也固定。JoinTupleToTemplateStringType 是一个泛型函数，可以将一个 Tuple 转换为 Template Literal Types，作用到 Test1 上得到的结果是 <code>names.$&#123;number&#125;.firstName.lastName</code>。具体到 JoinTupleToTemplateStringType 的实现，除了条件类型和 infer 的使用，我们还使用了一个威力巨大的 TS 泛型特性：递归。如果对算法略有了解，会知道任何算法操作的核心是分支和循环，而循环又何递归完全等价，意思是任何用循环实现的算法，理论上都可以用递归实现，反之亦然。在目前主流编程语言中，绝大部分都是以循环为主，甚至很多人可能听过一些「不要写递归」之类的说法。但在 TS 泛型层面，我们只能使用递归和条件来实现一些有趣的泛型函数。下面的代码我加了详细的注释，顺着慢慢看，别害怕，就一定能看懂。因为递归有一个特点，写起来可能不容易，但阅读的时候往往要容易很多（前提是单个逻辑完整且不存在嵌套的递归）。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Test1 = [<span class="hljs-string">'names'</span>, <span class="hljs-built_in">number</span>, <span class="hljs-string">'firstName'</span>, <span class="hljs-string">'lastName'</span>];
<span class="hljs-comment">// 假设需要处理的 Tuple 元素类型只会是字符串或 number</span>
<span class="hljs-comment">// 做这个假设的原因是，对象 object 的 key 一般来说，只会是 string 或 number</span>
<span class="hljs-keyword">type</span> JoinTupleToTemplateStringType<T> = T <span class="hljs-keyword">extends</span> [infer Single] <span class="hljs-comment">// 此处是递归基，用于判断 T 是否已经是最简单的只有一个元素的 Tuple</span>
  ? Single <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> <span class="hljs-comment">// 如果是递归基，则提取出 Single 的具体类型</span>
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;Single&#125;</span>`</span>
    : <span class="hljs-built_in">never</span>
  <span class="hljs-comment">// 如果还未到递归基，则继续递归</span>
  : T <span class="hljs-keyword">extends</span> [infer First, ...infer RestTuple] <span class="hljs-comment">// 完全类似 JS 数组解构</span>
  ? First <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;First&#125;</span>.<span class="hljs-subst">$&#123;JoinTupleToTemplateStringType<RestTuple>&#125;</span>`</span> <span class="hljs-comment">// 递归操作</span>
    : <span class="hljs-built_in">never</span>
  : <span class="hljs-built_in">never</span>;
<span class="hljs-keyword">type</span> TestJoinTupleToTemplateStringType = JoinTupleToTemplateStringType<Test1>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的递归操作里，是把 Tuple 转换成 Template Literal Type，下面这个递归泛型相反，是把一个 Template Literal Type 转换成 Tuple。代码也加了详细注释，别害怕，只要慢慢看，就一定能看懂。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> Test2 = <span class="hljs-string">`names.<span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>.firstName.lastName.<span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>`</span>;
<span class="hljs-keyword">type</span> SplitTemplateStringTypeToTuple<T> =
  T <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;infer First&#125;</span>.<span class="hljs-subst">$&#123;infer Rest&#125;</span>`</span>
    <span class="hljs-comment">// 此分支表示需要继续递归</span>
    ? First <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>`</span>
      ? [<span class="hljs-built_in">number</span>, ...SplitTemplateStringTypeToTuple<Rest>] <span class="hljs-comment">// 完全类似 JS 数组构造</span>
      : [First, ...SplitTemplateStringTypeToTuple<Rest>]
    <span class="hljs-comment">// 此分支表示抵达递归基，递归基不是 nubmer 就是 string</span>
    : T <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>`</span>
    ? [<span class="hljs-built_in">number</span>]
    : [T];
<span class="hljs-keyword">type</span> TestSplitTemplateStringTypeToTuple = SplitTemplateStringTypeToTuple<Test2>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">最后一步：求解对象全部嵌套子路径的<strong>递归泛型</strong></h3>
<p>终于到了最后一步，真正的解决方案，一个求解对象全部嵌套子路径的递归泛型 AllPathsOf。AllPathsOf 并不复杂，由两个嵌套泛型构成，这两个嵌套泛型分别只有七八行，加起来十五行，是不是还行？所以问题最关键的一步是想到先求出 TuplePaths，再铺平。其中铺平这一步我们之前已经展示过，就是用一个递归泛型把一个 Tuple 转换成 Template Literal Type。所以问题只剩下一个：如何把对象的所有子路径提取并表示为 Tuple Union。RecursivelyTuplePaths 本身也不复杂，下面代码中有详细注释，别害怕，慢慢看，一定能看懂。</p>
<p>剩下就是的 ValueMatchingPath，看代码好像比 AllPathsOf 还复杂一点，但由于只是附加功能，此处不详细介绍，感兴趣的可以看代码，相信经过前面几轮递归泛型的洗礼，这个稍微长一点的也不成问题。</p>
<pre><code class="hljs language-TypeScript copyable" lang="TypeScript"> <span class="hljs-comment">//</span>
 <span class="hljs-comment">// 支持的环境：TS 4.3+</span>
 <span class="hljs-comment">//</span>

 <span class="hljs-comment">/** 获取嵌套对象的全部子路径 */</span>
<span class="hljs-keyword">type</span> AllPathsOf<NestedObj> = <span class="hljs-built_in">object</span> <span class="hljs-keyword">extends</span> NestedObj
  ? <span class="hljs-built_in">never</span>
  <span class="hljs-comment">// 先把全部子路径组织成 tuple union，再把每一个 tuple 展平为 Template Literal Type</span>
  : FlattenPathTuples<RecursivelyTuplePaths<NestedObj>>;

 <span class="hljs-comment">/** 给定子路径和嵌套对象，获取子路径对应的 value 类型 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> ValueMatchingPath<NestedObj, Path <span class="hljs-keyword">extends</span> AllPathsOf<NestedObj>> =
  <span class="hljs-built_in">string</span> <span class="hljs-keyword">extends</span> Path
    ? <span class="hljs-built_in">any</span>
    : <span class="hljs-built_in">object</span> <span class="hljs-keyword">extends</span> NestedObj
    ? <span class="hljs-built_in">any</span>
    : NestedObj <span class="hljs-keyword">extends</span> <span class="hljs-keyword">readonly</span> (infer SingleValue)[] <span class="hljs-comment">// Array 情况</span>
    ? Path <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">string</span>&#125;</span>.<span class="hljs-subst">$&#123;infer NextPath&#125;</span>`</span>
      ? NextPath <span class="hljs-keyword">extends</span> AllPathsOf<NestedObj[<span class="hljs-built_in">number</span>]> <span class="hljs-comment">// Path 有嵌套情况，继续递归</span>
        ? ValueMatchingPath<NestedObj[<span class="hljs-built_in">number</span>], NextPath>
        : <span class="hljs-built_in">never</span>
      : SingleValue <span class="hljs-comment">// Path 无嵌套情况，数组的 item 类型就是目标结果</span>
    : Path <span class="hljs-keyword">extends</span> keyof NestedObj <span class="hljs-comment">// Record 情况</span>
    ? NestedObj[Path] <span class="hljs-comment">// Path 是 Record 的 key 之一，则可直接返回目标结果</span>
    : Path <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;infer Key&#125;</span>.<span class="hljs-subst">$&#123;infer NextPath&#125;</span>`</span> <span class="hljs-comment">// 否则继续递归</span>
    ? Key <span class="hljs-keyword">extends</span> keyof NestedObj
      ? NextPath <span class="hljs-keyword">extends</span> AllPathsOf<NestedObj[Key]> <span class="hljs-comment">// 通过两层判断进入递归</span>
        ? ValueMatchingPath<NestedObj[Key], NextPath>
        : <span class="hljs-built_in">never</span>
      : <span class="hljs-built_in">never</span>
    : <span class="hljs-built_in">never</span>;

 <span class="hljs-comment">/**
 * Recursively convert objects to tuples, like
 * `&#123; name: &#123; first: string &#125; &#125;` -> `['name'] | ['name', 'first']`
 */</span>
<span class="hljs-keyword">type</span> RecursivelyTuplePaths<NestedObj> = NestedObj <span class="hljs-keyword">extends</span> (infer ItemValue)[] <span class="hljs-comment">// Array 情况</span>
  <span class="hljs-comment">// Array 情况需要返回一个 number，然后继续递归</span>
  ? [<span class="hljs-built_in">number</span>] | [<span class="hljs-built_in">number</span>, ...RecursivelyTuplePaths<ItemValue>] <span class="hljs-comment">// 完全类似 JS 数组构造方法</span>
  : NestedObj <span class="hljs-keyword">extends</span> Record<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>> <span class="hljs-comment">// Record 情况</span>
  ?
      <span class="hljs-comment">// record 情况需要返回 record 最外层的 key，然后继续递归</span>
      | [keyof NestedObj]
      | &#123;
          [Key <span class="hljs-keyword">in</span> keyof NestedObj]: [Key, ...RecursivelyTuplePaths<NestedObj[Key]>];
        &#125;[Extract<keyof NestedObj, <span class="hljs-built_in">string</span>>]
        <span class="hljs-comment">// 此处稍微有些复杂，但做的事其实就是构造一个对象，value 是我们想要的 tuple</span>
        <span class="hljs-comment">// 最后再将 value 提取出来</span>
  <span class="hljs-comment">// 既不是数组又不是 record 时，表示遇到了基本类型，递归结束，返回空 tuple。</span>
  : [];

 <span class="hljs-comment">/**
 * Flatten tuples created by RecursivelyTupleKeys into a union of paths, like:
 * `['name'] | ['name', 'first' ] -> 'name' | 'name.first'`
 */</span>
<span class="hljs-keyword">type</span> FlattenPathTuples<PathTuple <span class="hljs-keyword">extends</span> unknown[]> = PathTuple <span class="hljs-keyword">extends</span> []
  ? <span class="hljs-built_in">never</span>
  : PathTuple <span class="hljs-keyword">extends</span> [infer SinglePath] <span class="hljs-comment">// 注意，[string] 是 Tuple</span>
  ? SinglePath <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> <span class="hljs-comment">// 通过条件判断提取 Path 类型</span>
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;SinglePath&#125;</span>`</span>
    : <span class="hljs-built_in">never</span>
  : PathTuple <span class="hljs-keyword">extends</span> [infer PrefixPath, ...infer RestTuple] <span class="hljs-comment">// 是不是和数组解构的语法很像？</span>
  ? PrefixPath <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span> <span class="hljs-comment">// 通过条件判断继续递归</span>
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;PrefixPath&#125;</span>.<span class="hljs-subst">$&#123;FlattenPathTuples<Extract<RestTuple, (<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>)[]>>&#125;</span>`</span>
    : <span class="hljs-built_in">never</span>
  : <span class="hljs-built_in">string</span>;

 <span class="hljs-comment">/**
 * 借助 TS 4.3 的新能力(template string type 增强)改造 FormApi interface 中的 change 方法，可用性几乎完美
 **/</span>
<span class="hljs-keyword">interface</span> FormApi<FormValues = Record<string, any>> &#123;
  <span class="hljs-attr">change</span>: <Path extends AllPathsOf<FormValues>>(
    name: Path,
    value?: Partial<ValueMatchingPath<FormValues, Path>>
  ) => void;
&#125;

 // 演示用的嵌套 Form 类型
interface NestedForm &#123;
  name: ['赵' | '钱' | '孙' | '李', string];
  age: number;
  articles: &#123;
    title: string;
    sections: string[];
    date: number;
    likes: &#123;
      name: [string, string];
      age: number;
    &#125;[];
  &#125;[];
&#125;

 // 假装有了一个 NestedForm 类型表单实例的 change 方法
const change: FormApi<NestedForm>['change'] = (name, value) => &#123;
  console.log(name, value);
&#125;;

 // 👇 尽情尝试
let index = 0;
change(`articles.0.likes.$&#123;index&#125;.age`, 10);
change(`name.$&#123;index&#125;`, '刘'); // 其实此处依然不够安全，可以想想怎么更安全 🤔

 /** 提取出来的全部子路径，放在这里直观展示一下 */
type AllPathsOfNestedForm =
  | keyof NestedForm
  | `name.$&#123;number&#125;`
  | `articles.$&#123;number&#125;`
  | `articles.$&#123;number&#125;.title`
  | `articles.$&#123;number&#125;.sections`
  | `articles.$&#123;number&#125;.date`
  | `articles.$&#123;number&#125;.likes`
  | `articles.$&#123;number&#125;.sections.$&#123;number&#125;`
  | `articles.$&#123;number&#125;.likes.$&#123;number&#125;`
  | `articles.$&#123;number&#125;.likes.$&#123;number&#125;.name.$&#123;number&#125;`
  | `articles.$&#123;number&#125;.likes.$&#123;number&#125;.age`
  | `articles.$&#123;number&#125;.likes.$&#123;number&#125;.name`;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">最最后一步：<strong>使用尾递归技术优化泛型函数的性能</strong></h3>
<p>最最后一步是个 bonus，额外的优化。可以看到前面的 AllPathsOf 是个运行复杂度不低的递归。这应该是递归的通病，也有一些朋友因为这个不喜欢递归。但其实递归的这种问题是可以通过技术手段规避掉的。这个技术手段就是尾递归。</p>
<p>下面我们用经典的 fibonacci 数列来切实感受一下递归、尾递归、循环的区别：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"> <span class="hljs-comment">// 递归版 fibonacci，性能捉急，简直不可容忍</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibRecursive</span>(<span class="hljs-params">n: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> n <= <span class="hljs-number">1</span> ? n : fibRecursive(n - <span class="hljs-number">1</span>) + fibRecursive(n - <span class="hljs-number">2</span>);
&#125;

 <span class="hljs-comment">// 尾递归版 fibonacci，化腐朽为神奇，性能飙升</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibTailRecursive</span>(<span class="hljs-params">n: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fib</span>(<span class="hljs-params">a: <span class="hljs-built_in">number</span>, b: <span class="hljs-built_in">number</span>, n: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
    <span class="hljs-keyword">return</span> n === <span class="hljs-number">0</span> ? a : fib(b, a + b, n - <span class="hljs-number">1</span>);
  &#125;
  <span class="hljs-keyword">return</span> fib(<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, n);
&#125;

 <span class="hljs-comment">// 循环版 fibonacci，好像和尾递归版异曲同工？</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fibLoop</span>(<span class="hljs-params">n: <span class="hljs-built_in">number</span></span>) </span>&#123;
  <span class="hljs-keyword">let</span> [a, b] = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>];
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
    [a, b] = [b, a + b];
  &#125;
  <span class="hljs-keyword">return</span> a;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是的，尾递归的性能在时间复杂度上和循环一样一样的。</p>
<p>下面看看尾递归如何在 TS 泛型中使用：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> OneLevelPathOf<T> = keyof T & (<span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>)
<span class="hljs-keyword">type</span> PathForHint<T> = OneLevelPathOf<T>;

<span class="hljs-comment">// P 参数是一个状态容器，用于承载每一步的递归结果，并最终帮我们实现尾递归</span>
<span class="hljs-keyword">type</span> PathOf<T, K <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span>, P <span class="hljs-keyword">extends</span> <span class="hljs-built_in">string</span> = <span class="hljs-string">''</span>> =
  K <span class="hljs-keyword">extends</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;infer U&#125;</span>.<span class="hljs-subst">$&#123;infer V&#125;</span>`</span>
    ? U <span class="hljs-keyword">extends</span> keyof T  <span class="hljs-comment">// Record</span>
      ? PathOf<T[U], V, <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;U&#125;</span>.`</span>>
      : T <span class="hljs-keyword">extends</span> unknown[]  <span class="hljs-comment">// Array</span>
      ? PathOf<T[<span class="hljs-built_in">number</span>], V, <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>.`</span>>
      : <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;PathForHint<T>&#125;</span>`</span>  <span class="hljs-comment">// 走到此分支，表示参数有误，提示用户正确的参数</span>
    : K <span class="hljs-keyword">extends</span> keyof T
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;K&#125;</span>`</span>
    : T <span class="hljs-keyword">extends</span> unknown[]
    ? <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;<span class="hljs-built_in">number</span>&#125;</span>`</span>
    : <span class="hljs-string">`<span class="hljs-subst">$&#123;P&#125;</span><span class="hljs-subst">$&#123;PathForHint<T>&#125;</span>`</span>;  <span class="hljs-comment">// 走到此分支，表示参数有误，提示用户正确的参数</span>

 <span class="hljs-comment">/**
 * 使用尾递归泛型改造 FormApi interface 中的 change 方法，提升性能
 * */</span>
<span class="hljs-keyword">interface</span> FormApi<FormValues = Record<string, any>> &#123;
  <span class="hljs-attr">change</span>: <Path extends string>(
    // 此处按需判断给定的 name 参数是否是 FormValues 的子路径
    // 编译性能会有明显提升
    name: PathOf<FormValues, Path>,
    value?: Partial<ValueMatchingPath<FormValues, Path>>
  ) => void;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">结语</h2>
<p>TS 4.3 Template Literal Types 实践到这里就结束了。这些略有复杂但逻辑清晰的递归泛型理解起来肯定有一些难度，如果实在看不懂，也没关系。后面可以慢慢来。但想要真正掌握 TS，这个程度的递归泛型是必须要掌握的，所以本文的确还是有一些价值的 👀 😊</p>
<h2 data-id="heading-13">参考链接</h2>
<p><strong><a href="https://github.com/microsoft/TypeScript/issues/20423" target="_blank" rel="nofollow noopener noreferrer">github.com/microsoft/T…</a></strong></p></div>  
</div>
            