
---
title: 'Vue 3 和 React 16.8 到底能多像'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44f654ce05b42279299f48284026ec2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 23:24:09 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44f654ce05b42279299f48284026ec2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">导读</h1>
<p>注：为行文方便，本文将对 Vue 3 的 composition api 也称为 hooks，也是目前业内比较通俗的说法。</p>
<p>Vue 团队于 2020 年 9 月 18 日晚 11 点半发布了 Vue 3.0 版本。大家最关注的点就是 Vue 也引入了类似 React Hooks 的概念和用法。很多人说二者越来越像了，那么它们到底有多像？哪里像？能像到什么程度？
我想没有比列出代码对比更直观的方式了，毕竟 “Talk is cheap, show me the code.” 才是程序员的风格。</p>
<p>本文将以 <strong>表单提交</strong> 和 <strong>列表展示</strong> 两个典型场景，来对比 Vue 3 和 React16.8+ 的代码实现。React 的代码将只使用 hooks + functional component 的形式展现；Vue 由于支持的形式更丰富，所以会有 hooks + template、hooks + JSX 两个版本，后者将是体现本文主题的关键点。</p>
<h1 data-id="heading-1">场景说明</h1>
<h2 data-id="heading-2">场景一 - Form</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44f654ce05b42279299f48284026ec2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，一个最简单的表单提交场景，主要展示<strong>数据响应式</strong>的实现，具体说明如下：</p>
<ol>
<li>表单有初始值，进入页面后从服务端异步获取，API 为 <code>fetchUserInfo</code></li>
<li>input 和 radio 实时响应用户输入</li>
<li>点击 Submit 按钮，会 alert 出当前表单展示的用户信息</li>
</ol>
<h2 data-id="heading-3">场景二 - Table</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f43de88811104d259917f30afe7402ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图，一个最简单的表格展示场景，主要展示对<strong>数组的处理</strong>以及<strong>表达式</strong>的实现，具体说明如下：</p>
<ol>
<li>数据从后端异步获取，API 为 <code>fetchUserList</code></li>
<li>sex 字段返回值为 <strong>0 或 1</strong>，列表要分别展示为 Female 或 Male</li>
</ol>
<h1 data-id="heading-4">代码实现</h1>
<p>全文的代码将全部采用 TS 实现</p>
<h2 data-id="heading-5">API & Types</h2>
<p>此部分代码为必要的 TS 声明和模拟的后端 API，是所有例子的前置依赖。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// services.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-built_in">enum</span> Sex &#123;
  female,
  male,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> UserInfo &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  sex: Sex;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> fetchUserInfo = (userId: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">Promise</span><UserInfo> =>
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">rev</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> rev(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Zhang san"</span>, <span class="hljs-attr">sex</span>: Sex.male &#125;), <span class="hljs-number">500</span>);
  &#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> updateUserInfo = (params: UserInfo): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">boolean</span>> =>
  <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-literal">true</span>);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> fetchUserList = (): <span class="hljs-built_in">Promise</span><UserInfo[]> =>
  <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">rev</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      rev([
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Zhang san"</span>, <span class="hljs-attr">sex</span>: Sex.male &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Li si"</span>, <span class="hljs-attr">sex</span>: Sex.female &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"Wang wu"</span>, <span class="hljs-attr">sex</span>: Sex.male &#125;,
      ]);
    &#125;, <span class="hljs-number">500</span>);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Vue 3 Hooks + template</h2>
<p>我们先来看下 <code>.vue</code> 单文件组件的经典写法，也就是 template + script + style 的形式。本例只是做了 Vue 3 hooks 的改造，显然这根 React 还不够像，我们只是做个铺垫。</p>
<h3 data-id="heading-7">Form.vue</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"name"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">:checked</span>=<span class="hljs-string">"maleChecked"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"setSex(Sex.male)"</span> /></span>Male
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">:checked</span>=<span class="hljs-string">"femaleChecked"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"setSex(Sex.female)"</span> /></span>Female
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleSubmit"</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onMounted, ref, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; Sex, fetchUserInfo, updateUserInfo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> nameRef = ref(<span class="hljs-string">""</span>);
    <span class="hljs-keyword">const</span> sexRef = ref(Sex.male);

    onMounted(<span class="hljs-function">() =></span> &#123;
      fetchUserInfo(<span class="hljs-string">"id-xxx"</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        nameRef.value = res.name;
        sexRef.value = res.sex;
      &#125;);
    &#125;);

    <span class="hljs-keyword">const</span> handleSubmit = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> params = &#123; <span class="hljs-attr">name</span>: nameRef.value, <span class="hljs-attr">sex</span>: sexRef.value &#125;;
      updateUserInfo(params).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (res) alert(<span class="hljs-built_in">JSON</span>.stringify(params));
      &#125;);
    &#125;;

    <span class="hljs-keyword">const</span> setSex = <span class="hljs-function">(<span class="hljs-params">sex: Sex</span>) =></span> &#123;
      sexRef.value = sex;
    &#125;;

    <span class="hljs-keyword">const</span> maleChecked = computed(<span class="hljs-function">() =></span> sexRef.value === Sex.male);
    <span class="hljs-keyword">const</span> femaleChecked = computed(<span class="hljs-function">() =></span> sexRef.value === Sex.female);

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: nameRef,
      <span class="hljs-attr">sex</span>: sexRef,
      handleSubmit,
      setSex,
      maleChecked,
      femaleChecked,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从以上代码可以看出，理论上在 Vue 3 里，data、methods、computed、生命周期等这些代码，都可以不再出现在实例对象的第一层，而是全部聚合到了 setup 里。正因如此，setup 内的每一行代码都可以自由的调整位置，以达到“根据功能聚合代码”的目的，甚至可以再进一步的抽离出去，形成独立的 hooks。这也是 Vue 团队引入此功能的目的所在。详见官方文档 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fv3.vuejs.org%2Fguide%2Fcomposition-api-introduction.html" target="_blank" rel="nofollow noopener noreferrer" title="https://v3.vuejs.org/guide/composition-api-introduction.html" ref="nofollow noopener noreferrer">Why Composition API?</a>。</p>
<p>另外，请注意 <code>setSex</code>、<code>maleChecked</code>、<code>femaleChecked</code> 的实现，下文会有所优化。回过头来看的话，这部分实际上有些冗余了。</p>
<h3 data-id="heading-8">Table.vue</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">:cellPadding</span>=<span class="hljs-string">"5"</span> <span class="hljs-attr">:cellSpacing</span>=<span class="hljs-string">"5"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tr</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"user in userList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"user.name"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123; user.name &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;&#123; user.sex === 0 ? "Male" : "Female" &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">table</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; onMounted, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; fetchUserList, UserInfo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> userListRef = ref<UserInfo[]>([]);

    onMounted(<span class="hljs-function">() =></span> &#123;
      fetchUserList().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        userListRef.value = res;
      &#125;);
    &#125;);

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">userList</span>: userListRef,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表格场景的代码实现非常简单，但是请注意 sex 转换成 Male/Female 部分的逻辑（template 部分）。我们看到，代码里出现了 <strong>Magic Number</strong>。这是因为 template 中无法结合 TS 导致的，否则完全可以用 <code>Sex.male</code> 这样的代码代替（见下文代码）。</p>
<p>当然，我们也可以把这个表达式的逻辑放到 setup 中，用一个 function 实现（类似 Form 例中的 <code>maleChecked</code> 方式），这样就可以充分利用 TS 的特性让代码变得更可读，但是会比较重，也不太优雅。这个是目前笔者认为 Vue 结合 TS 最尴尬的地方，template 与 TS 几乎无法结合。</p>
<h2 data-id="heading-9">Vue 3 + JSX vs. React 16.8+</h2>
<p>重头戏来了，经过上面的铺垫，我们来看下 Vue3 和 JSX 在一起会起什么样的化学反应。为展示方便，下面的代码进行了格式处理并用图片展示（文末会有代码的文本版），尽量将相同功能对齐，左侧 Vue 右侧 React。下面开始“大家来找茬”：</p>
<h3 data-id="heading-10">Form</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b820f9dbe5942558ac940e58a2175fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">Table</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/437da6b9284d4ca6aaa8a00543e8922c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>像，太像了，真的太像了。起码表面上看起来，它们的相似度能达到 80%。</p>
<blockquote>
<p>本文的例子非常简单，当加入 props、slot、其他生命周期等特性的时候，二者的代码实现还是会有较大差异的。笔者会另起一篇文章写，本文还是聚焦在二者像的部分。</p>
</blockquote>
<h1 data-id="heading-12">思考</h1>
<p>细心的朋友会注意到，文章的标题用的是“能多像”而不是“有多像”。这是因为要想让二者代码很像，Vue 必须使用 JSX 的方式，所以是需要一些主观控制才能达到“像”的目的，不过这已足够说明二者在深层次的设计理念上有绝对的相似之处。笔者无意纠结于谁抄袭谁，谁更优秀的问题，只是想学习和理解其设计理念和思想。不过人毕竟是感情动物，还是会有所偏向，下面就简单说说笔者这几年的思想变化，供大家参考。</p>
<p>不得不说，从 VDOM 到 Hooks，React 团队对整个行业起到了颠覆性的影响。前者催生了前端跨平台的解决方案，后者让前端项目的可维护性提高了一大截，真真让人拍案叫绝。这些理念也很快被整个行业所接受并借鉴。笔者在 React 16.8 之前，更欣赏 Vue 多一些，因为其文档与渐进式的设计理念实在做的太棒了，Vue 的学习曲线要明显比 React 平滑的多，而且全家桶使用也更简单，管理较集中（都是 Vue 团队维护），<code>.vue</code> 单文件写法也对于熟悉模板语法的前端同学比较友好。当时都流行说，React 适合做大型复杂项目，Vue 更适合做一些中小型项目，个人认为这种断言的说服力很有限，根本不疼不痒。</p>
<p>但是 React Hooks 的出现，让 React 的世界只剩下了 functional component 和 hooks 的概念，二者与 TS 的结合毫无阻碍，完美配合。</p>
<blockquote>
<p>与之相对的，老版本的 class component 的方式，实际上会让 TS 的使用在 Class 这里产生断层（主要是 props 的传递）</p>
</blockquote>
<p>这就造成了 hooks + jsx 的收益，明显大于放弃使用 template 所造成的不适，毕竟 template 与 TS 基本算得上是格格不入了。尤大也说过，“对 TS 的支持更友好”，是 Vue 3 的一个重大提升，相信大牛对于这点的认识肯定比笔者要深。就像上文展示的，现在 Vue 可以有多种写法，而且它们是那么的不同，选择多同样意味着容易造成混乱，也许过段时间关于 Vue 3 的最佳实践之类的讨论会成为热点。就笔者而言，还是更倾向于拥抱 JSX + TS，因为这个组合真的能够大大提升项目的可维护性。</p>
<h1 data-id="heading-13">总结</h1>
<p>TS 的出现，让前端代码的可读性、稳定性与可维护性有了显著的提高，可以说是提升前端生产效率的重要工具。以此为前提，前端项目如果能够充分利用 TS，将能获得可观的收益。</p>
<p>React Hooks 的出现，让 React 与 TS 形成了完美的配合。目前来看，Vue3 可以做到类似于 React Class Component + Hooks + TS 的效果，但是还未达到完美契合的程度，从这点来说，Vue 算是落后与 React 一点。不过 template 作为渐进式理念的重要组成部分，有自己的优势，也很难被舍弃，个人臆测，未来 Vue 会面临 template 与 TS 的取舍抉择。当然，大牛或许有两全其美的解决方案，目前的趋势还不够明朗，我们且拭目以待。</p>
<p>最后，作为程序员，务实、好学是必要的品质。希望大家不要受限于“门派之见”，仰望星空，集百家之所长，努力提升自己，才是最明智的选择。</p>
<p><strong>“得其大者可以兼其小，未有学其小而能至其大者也” —— 欧阳修</strong></p>
<h1 data-id="heading-14">引用</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F133819602" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/133819602" ref="nofollow noopener noreferrer">Vue3 究竟好在哪里？（和 React Hook 的详细对比）</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F256308926" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/256308926" ref="nofollow noopener noreferrer">官宣！Vue 3.0 终于正正正式发布了！</a></li>
</ul>
<h1 data-id="heading-15">附录</h1>
<h2 data-id="heading-16">代码文本</h2>
<h3 data-id="heading-17">React Hooks - Form.tsx</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// Form.tsx</span>
<span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Sex, fetchUserInfo, updateUserInfo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;

<span class="hljs-keyword">const</span> Form = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [name, setName] = useState(<span class="hljs-string">""</span>);
  <span class="hljs-keyword">const</span> [sex, setSex] = useState(Sex.male);

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchUserInfo(<span class="hljs-string">"id-xxx"</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      setName(res.name);
      setSex(res.sex);
    &#125;);
  &#125;, []);

  <span class="hljs-keyword">const</span> handleSubmit = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> params = &#123; name, sex &#125;;
    updateUserInfo(params).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (res) alert(<span class="hljs-built_in">JSON</span>.stringify(params));
    &#125;);
  &#125;;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;name&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> setName(e.target.value)&#125; />
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">&#123;sex</span> === <span class="hljs-string">Sex.male&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setSex(Sex.male)&#125; />Male
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">&#123;sex</span> === <span class="hljs-string">Sex.female&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> setSex(Sex.female)&#125; />Female
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleSubmit&#125;</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Form;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">React Hooks - Table.tsx</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// Table.tsx</span>
<span class="hljs-keyword">import</span> React, &#123; useState, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; Sex, UserInfo, fetchUserList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;

<span class="hljs-keyword">const</span> Table = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [userList, setUserList] = useState<UserInfo[]>([]);

  useEffect(<span class="hljs-function">() =></span> &#123;
    fetchUserList().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> setUserList(res));
  &#125;, []);

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">cellPadding</span>=<span class="hljs-string">&#123;5&#125;</span> <span class="hljs-attr">cellSpacing</span>=<span class="hljs-string">&#123;5&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
      &#123;userList.map((&#123; name, sex &#125;) => (
        <span class="hljs-tag"><<span class="hljs-name">tr</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;name&#125;</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;sex === Sex.male ? "Male" : "Female"&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
      ))&#125;
    <span class="hljs-tag"></<span class="hljs-name">table</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Table;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">Vue 3 + JSX - Form.tsx</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// Form.tsx</span>
<span class="hljs-keyword">import</span> &#123; ref, onMounted, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; Sex, fetchUserInfo, updateUserInfo &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;

<span class="hljs-keyword">const</span> Form = defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> nameRef = ref(<span class="hljs-string">""</span>);
    <span class="hljs-keyword">const</span> sexRef = ref(Sex.male);

    onMounted(<span class="hljs-function">() =></span> &#123;
      fetchUserInfo(<span class="hljs-string">"id-xxx"</span>).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        nameRef.value = res.name;
        sexRef.value = res.sex;
      &#125;);
    &#125;);

    <span class="hljs-keyword">const</span> handleSubmit = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> params = &#123; <span class="hljs-attr">name</span>: nameRef.value, <span class="hljs-attr">sex</span>: sexRef.value &#125;;
      updateUserInfo(params).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (res) alert(<span class="hljs-built_in">JSON</span>.stringify(params));
      &#125;);
    &#125;;

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;nameRef.value&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> &#123; nameRef.value = e.target.value; &#125;&#125; />
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">&#123;sexRef.value</span> === <span class="hljs-string">Sex.male&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123; sexRef.value = Sex.male; &#125;&#125; /> Male
          <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">&#123;sexRef.value</span> === <span class="hljs-string">Sex.female&#125;</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123; sexRef.value = Sex.female; &#125;&#125; /> Female
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleSubmit&#125;</span>></span>Submit<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Form;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">Vue 3 + JSX - Table.tsx</h3>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-comment">// Table.tsx</span>
<span class="hljs-keyword">import</span> &#123; ref, onMounted, defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; Sex, UserInfo, fetchUserList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../services"</span>;

<span class="hljs-keyword">const</span> Table = defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> userListRef = ref<UserInfo[]>([]);

    onMounted(<span class="hljs-function">() =></span> &#123;
      fetchUserList().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        userListRef.value = res;
      &#125;);
    &#125;);

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">cellpadding</span>=<span class="hljs-string">&#123;5&#125;</span> <span class="hljs-attr">cellspacing</span>=<span class="hljs-string">&#123;5&#125;</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Name<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">th</span>></span>Sex<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
        &#123;userListRef.value.map((&#123; name, sex &#125;) => (
          <span class="hljs-tag"><<span class="hljs-name">tr</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;name&#125;</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;name&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">td</span>></span>&#123;sex === Sex.male ? "Male" : "Female"&#125;<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
        ))&#125;
      <span class="hljs-tag"></<span class="hljs-name">table</span>></span></span>
    );
  &#125;,
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Table;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            