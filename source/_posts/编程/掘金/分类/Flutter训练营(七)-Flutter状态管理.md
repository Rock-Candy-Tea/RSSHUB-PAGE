
---
title: 'Flutter训练营(七)-Flutter状态管理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08bf0b54e64c4318affa0ff96bdb3b45~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 06:02:57 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08bf0b54e64c4318affa0ff96bdb3b45~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>Flutter是Google开发的一套全新的跨平台、开源UI框架，支持iOS、Android系统开发，并且是未来新操作系统Fuchsia的默认开发套件，同时也是当下最流行的跨端解决方案。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在弄清楚如何使用 各个状态管理库 之前，我们首先需要清楚地知道为什么我的应用需要状态管理。</p>
<p>当开发的应用足够简单，Flutter 作为一个声明式框架，你或许只需要将数据映射成视图就可以了。你可能并不需要状态管理，但是随着功能的增加，你的应用程序将会有几十个甚至上百个状态。</p>
<p>随着应用需要共享多处统一状态时，我们很难再清楚的测试维护我们的状态，因为它看上去实在是太复杂了！而且还会有多个页面共享同一个状态，例如当你进入一个文章点赞，退出到外部缩略展示的时候，外部也需要显示点赞数，这时候就需要同步这两个状态。</p>
<p>Flutter 实际上在一开始就为我们提供了一种状态管理方式 — StatefulWidget。然而我们发现它仅适合用于在单个 Widget 内部维护其状态。当我们需要使用跨组件的状态时，StatefulWidget 将不再是一个好的选择。</p>
<p>State 属于某一个特定的 StatefulWidget，在多个 Widget 之间进行交流的时候，虽然你可以使用 callback 解决，但是当嵌套足够深的话，很容易就增大代码耦合度。</p>
<p>这时候，我们便迫切的需要一个架构来帮助我们理清这些关系，因此，各大状态管理框架应运而生。本文主要介绍2种：官方推荐的Provider、阿里团队的 <code>Fish-Redux</code></p>
<h2 data-id="heading-1">一、状态管理</h2>
<p>了解过前端的同学应该对Vue、React的状态管理不陌生，我之前的文章也有详细比较过，常见的状态管理有Vuex、Flux、Redux、MobX、Bloc、Stamen等等。但是对于新生代的Flutter，之前还没有完全符合Flutter的状态管理库，之前介绍过Redux是一门JS库，Redux 是一个函数式的数据管理的框架，不仅仅可以用于React，还可以应用于其他框架和平台，特点是、可预测、集中式、易调试、灵活性的数据管理的框架，所有对数据的增删改查等操作都由 Redux 来集中负责。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08bf0b54e64c4318affa0ff96bdb3b45~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是对于Flutter来说，Redux 的优点同时也是缺点，Redux 核心仅仅关心数据管理，不关心具体什么场景来使用它。所以在Flutter中使用 Redux 中将面临两个具体问题：Redux 的集中和 Component 的分治之间的矛盾；Redux 的 Reducer 需要一层层手动组装，带来的繁琐性和易错性。</p>
<p>就在今天（2019年3月5号），闲鱼宣布在 GitHub 上开源 Fish Redux，从此Flutter有了真正意义上的完善的状态管理框架-Fish Redux。</p>
<h2 data-id="heading-2">二、旧-Flutter-provide</h2>
<p>上面说到Fish Redux 算是Flutter真正意义上完善的状态管理框架，原因是之前确实也有状态管理-Flutter-provide。（官方地址 <a href="https://github.com/google/flutter-provide%EF%BC%89" target="_blank" rel="nofollow noopener noreferrer">github.com/google/flut…</a></p>
<p>Provide 和 Scoped_model一样，也是借助了InheritWidget，将共享状态放到顶层MaterialApp之上。底层部件通过Provier获取该状态，并通过混合ChangeNotifier通知依赖于该状态的组件刷新。</p>
<p>举个例子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c78e1cafedd64f33bedb07ced3cbb6c1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这两个页面都同时依赖于counter 和 switcher两个不同的状态。并且一个页面改变状态之后另外一个页面状态也随之改变。</p>
<h4 data-id="heading-3">1.添加依赖</h4>
<p>在pubspec.yaml中添加Provide的依赖。</p>
<pre><code class="hljs language-dart copyable" lang="dart">dependencies:
  provide: ^<span class="hljs-number">1.0</span><span class="hljs-number">.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">2.创建Model</h4>
<p>这里实际上它承担了State的职责，但是为了和官方的State区分所以叫做model。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Counter</span> <span class="hljs-title">with</span> <span class="hljs-title">ChangeNotifier</span></span>&#123;
  <span class="hljs-built_in">int</span> value = <span class="hljs-number">0</span>;

  increment()&#123;
    value++;
    notifyListeners();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们可以看到，数据和操作数据的方法都在model中，我们可以很清晰的把业务分离出来。对比Scoped_model可以发现，Provide模式中model不再需要继承Model类，只需要实现Listenable，我们这里混入ChangeNotifier，可以不用管理听众。通过 notifyListeners 我们可以通知听众刷新。</p>
<h4 data-id="heading-5">3.将状态放入顶层</h4>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-keyword">var</span> counter = Counter();
  <span class="hljs-keyword">var</span> providers = Providers();

<span class="hljs-comment">//将counter对象添加进providers</span>
  providers.provide(Provider.value(counter));

  runApp(
    ProviderNode(
        child: MyApp(), 
        providers: providers),
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ProviderNode 封装了 InheritWidget，并且提供了一个 providers 容器用于放置状态。providers 内部通过 Map> 来储存 provider，在存放的时候你可以通过传入ProviderScope("name") 来指定key。Provider.value 将 counter 包装成了_ValueProvider。并在它的内部提供了 StreamController 从而实现对数据进行流式操作。</p>
<h4 data-id="heading-6">4.获取状态</h4>
<p>同样的Provide也提供了两种获取State的方法。我们先来介绍第一种，通过Provide小部件获取。</p>
<pre><code class="hljs language-dart copyable" lang="dart">Provide(
  builder: (context, child, counter) &#123;
     <span class="hljs-keyword">return</span> Text(
        <span class="hljs-string">'<span class="hljs-subst">$&#123;counter.value&#125;</span>'</span>,
        style: Theme.of(context).textTheme.display1,
      );
   &#125;,
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次通知数据刷新时，builder将会重新构建这个小部件。builder方法接收三个参数，这里主要介绍第二个和第三个。第二个参数child：假如这个小部件足够复杂，内部有一些小部件是不会改变的，那么我们可以将这部分小部件写在Provide的child属性中，让builder不再重复创建这些小部件，以提升性能。第三个参数counter：这个参数代表了我们获取的顶层providers中的状态。</p>
<p><code>scope</code>：通过指定ProviderScope获取该键所对应的状态。在需要使用多个相同类型状态的时候使用。</p>
<p>第二种获取方式：Provide.value(context)final currentCounter = Provide.value(context)；这种方式实际上调用了 context.inheritFromWidgetOfExactType 找到顶层的 _InheritedProviders 来获取到顶层 providers 中的状态。</p>
<hr>
<h4 data-id="heading-7">如何组织多个状态</h4>
<p>和 scoped_model 不同的是，provide 模式中你可以轻松组织多个状态。只需要将状态provide 进 provider 中就可以了。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">void</span> main() &#123;
  <span class="hljs-keyword">var</span> counter = Counter();
  <span class="hljs-keyword">var</span> switcher = Switcher();

  <span class="hljs-keyword">var</span> providers = Providers();

  providers
    ..provide(Provider.value(counter))
    ..provide(Provider.value(switcher));

  runApp(
    ProviderNode(
        child: MyApp(), 
        providers: providers)
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">获取数据流</h4>
<p>在将 counter 添加进 providers 的过程中进行了一次包装。我们刚才通过分析源码知道了这个操作能够让我们处理流式数据。通过 Provide.stream(context) 就能获取数据流。</p>
<pre><code class="hljs language-dart copyable" lang="dart">StreamBuilder(
   initialData: currentCounter,
   stream: Provide.stream(context)
       .where((counter) => counter.value % <span class="hljs-number">2</span> == <span class="hljs-number">0</span>),
   builder: (context, snapshot) =>
       Text(<span class="hljs-string">'Last even value: <span class="hljs-subst">$&#123;snapshot.data.value&#125;</span>'</span>)),
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">三、新-Fish Redux</h2>
<p>Fish Redux 是闲鱼团队基于 Redux 做的一次量身改良，通过 Redux 做集中化的可观察的数据管理。FR 是一个基于 Redux 数据管理的组装式 flutter 应用框架， 特别适用于构建中大型的复杂应用，对于传统 Redux 在使用层面上的两大缺点做了重大改良，具体做法是：首先规定一个组件需要定义一个数据（Struct）和一个 Reducer，同时组件之间存在着父依赖子的关系。通过这层依赖关系去解决了 集中 和 分治 之间的矛盾，而对 Reducer 的手动层层 Combine 变成由框架自动完成，使之简化了使用 Redux 的困难，同时也得到了理想的集中的效果和分治的代码。</p>
<pre><code class="hljs language-dart copyable" lang="dart">sample_page
- State
- Action
- Reducer
- Store
- Middleware
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个组件页面目录结构可以是这样设计，好处是这些概念与 ReduxJS 是一致的，可以保留Redux 的优势。Fish Redux 最显著的特征是函数式的编程模型、可预测的状态管理、可插拔的组件体系、最佳的性能表现。它的特点是配置式组装。一方面我们将一个大的页面，对视图和数据层层拆解为互相独立的 Component|Adapter，上层负责组装，下层负责实现；另一方面将Component|Adapter 拆分为 View，Reducer，Effect 等相互独立的上下文无关函数。</p>
<p>Fish Redux 的灵感主要来自于 Redux， Elm， Dva 这样的优秀框架。所以用闲鱼Flutter团队自己的话来说，Fish Redux 站在巨人的肩膀上，将集中，分治，复用，隔离做的更进一步。</p>
<h2 data-id="heading-10">四、FR源码解读</h2>
<h3 data-id="heading-11">1. Action</h3>
<p>Action 包含两个字段</p>
<ul>
<li>
<p>type</p>
</li>
<li>
<p>payload</p>
</li>
</ul>
<p>推荐的写法是为一个组件或适配器创建一个 action.dart 文件，包含两个类</p>
<ul>
<li>
<p>为 type 字段起一个枚举类</p>
</li>
<li>
<p>为 Action 的创建起一个 ActionCreator 类，这样利于约束 payload 的类型。</p>
</li>
<li>
<p>Effect 接受处理的 Action，以 on&#123; Verb &#125; 命名</p>
</li>
<li>
<p>Reducer 接受处理的 Action，以 &#123; verb &#125; 命名</p>
</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">enum</span> MessageAction &#123;
    onShare,
    shared,
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MessageActionCreator</span> </span>&#123;
    <span class="hljs-keyword">static</span> Action onShare(<span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Object</span>> payload) &#123;
        <span class="hljs-keyword">return</span> Action(MessageAction.onShare, payload: payload);
    &#125;

    <span class="hljs-keyword">static</span> Action shared() &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> Action(MessageAction.shared);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-12">2. Adapter</h3>
<p>我们在基础 Component 的概念外，额外增加了一种组件化的抽象 Adapter。它的目标是解决 Component 模型在 ListView 的场景下的 3 个问题：</p>
<ul>
<li>
<p>1）将一个"Big-Cell"放在 ListView 里，无法享受 ListView 代码的性能优化。</p>
</li>
<li>
<p>2）Component 无法区分 appear|disappear 和 init|dispose 事件。</p>
</li>
<li>
<p>3）Effect 的生命周期和 View 的耦合，在 ListView 的有些场景下不符合直观的预期。</p>
</li>
</ul>
<p>一个 Adapter 和 Component 几乎都是一致的，除了以下几点：</p>
<ul>
<li>
<p>Component 生成一个 Widget，Adapter 生成一个 ListAdapter，ListAdapter 有能力生成一组 Widget。</p>
</li>
<li>
<p>不具体生成 Widget，而是一个 ListAdapter，能非常大的提升页面帧率和流畅度。</p>
</li>
<li>
<p>Effect-Lifecycle-Promote</p>
</li>
<li>
<p>Component 的 Effect 是跟着 Widget 的生命周期走的，Adapter 的 Effect 是跟着上一级的 Widget 的生命周期走。</p>
</li>
<li>
<p>Effect 提升，极大的解除了业务逻辑和视图生命的耦合，即使它的展示还未出现，的其他模块依然能通过 dispatch-api，调用它的能力。</p>
</li>
<li>
<p>appear|disappear 的通知</p>
</li>
<li>
<p>由于 Effect 生命周期的提升，我们就能更加精细的区分 init|dispose 和 appear 或disappear。而这在 Component 的模型中是无法区分的。</p>
</li>
<li>
<p>Reducer is long-lived, Effect is medium-lived, View is short-lived.</p>
</li>
</ul>
<h3 data-id="heading-13">3. Auto-Dispose</h3>
<p>它是一个非常简易管理生命周期对象的方式。一个 auto-dispose 对象可以自我主动释放，或者在它 follow 的 托管对象释放的时候，释放。在 Effect 中使用的 Context，以及 HigherEffect 中的 EffectPart，都是 auto-dispose 对象。所以我们可以方便的将自定义的需要做生命周期管理的对象托管给它们。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ItemWidgetBindingObserver</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">WidgetsBindingObserver</span>
    <span class="hljs-title">with</span> <span class="hljs-title">AutoDispose</span> </span>&#123;
  ItemWidgetBindingObserver() : <span class="hljs-keyword">super</span>() &#123;
    WidgetsBinding.instance.addObserver(<span class="hljs-keyword">this</span>);
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> didChangeAppLifecycleState(AppLifecycleState state) &#123;
    <span class="hljs-keyword">if</span> (AppConfig.flutterBinding.framesEnabled &&
        state == AppLifecycleState.resumed) &#123;
      AppConfig.flutterBinding.performReassemble();
    &#125;
  &#125;

  <span class="hljs-meta">@override</span>
  <span class="hljs-keyword">void</span> dispose() &#123;
    <span class="hljs-keyword">super</span>.dispose();
    WidgetsBinding.instance.removeObserver(<span class="hljs-keyword">this</span>);
  &#125;
&#125;

<span class="hljs-keyword">void</span> _init(Action action, Context<ItemPageContainerState> ctx) &#123;
    <span class="hljs-keyword">final</span> ItemWidgetBindingObserver observer = ItemWidgetBindingObserver();
    observer.follow(ctx);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-14">4. Connector</h3>
<p>它表达了如何从一个大数据中读取小数据，同时对小数据的修改如何同步给大数据，这样的数据连接关系。它是将一个集中式的 Reducer，可以由多层次多模块的小 Reducer 自动拼装的关键。它大大降低了我们使用 Redux 的复杂度。我们不再关系组装过程，我们关系核心的什么动作促使数据怎么变化。它使用在配置 Dependencies 中，在配置中我们就固化了大组件和小组件之间的连接关系(数据管道)，所以在我们使用小组件的时候是不需要传入任何动态参数的。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DetialState</span> </span>&#123;
    Profile profile;
    <span class="hljs-built_in">String</span> message;
&#125;

Connector<DetialState, <span class="hljs-built_in">String</span>> messageConnector() &#123;
    <span class="hljs-keyword">return</span> Connector<DetialState, <span class="hljs-built_in">String</span>>(
        <span class="hljs-keyword">get</span>: (DetialState state) => state.message,
        <span class="hljs-keyword">set</span>: (DetialState state, <span class="hljs-built_in">String</span> message) => state.message = message,
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-15">5. Component</h3>
<p>组件是对视图展现和逻辑功能的封装。</p>
<p>面向当下，从 Redux 的视角看，我们对组件分为状态修改的功能(Reducer)和其他。面向未来，从 UI-Automation 的视角看，我们对组件分为展现表达和其他。结合上面两个视角，于是我们得到了，View、 Effect、Reducer 三部分，称之为组件的三要素，分别负责了组件的展示、非修改数据的行为、修改数据的操作。我们以显式配置的方式来完成大组件所依赖的小组件、适配器的注册，这份依赖配置称之为 Dependencies。</p>
<p>所以有了这个公式Component = View + Effect(可选) + Reducer(可选) + Dependencies ( 可选 )</p>
<h5 data-id="heading-16">分治：从组件的角度：</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd625044a3734122b2a61a64a4678ebf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-17">集中：从 Store 的角度：</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/192f6d8fac244ce3a429ba7512d23d64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h3 data-id="heading-18">6. CustomAdapter</h3>
<p>对大 Cell 的自定义实现，要素和 Component 类似，不一样的地方是 Adapter 的视图部分返回的是一个 ListAdapter。</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CommentAdapter</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Adapter</span><<span class="hljs-title">CommentState</span>> </span>&#123;
    CommentAdapter()
        : <span class="hljs-keyword">super</span>(
            adapter: buildCommentAdapter,
            effect: buildCommentEffect(),
            reducer: buildCommentReducer(),
        );
&#125;

ListAdapter buildCommentAdapter(CommentState state, Dispatch dispatch, ViewService service) &#123;
    <span class="hljs-keyword">final</span> <span class="hljs-built_in">List</span><IndexedWidgetBuilder> builders = Collections.compact(<IndexedWidgetBuilder>[]
    ..add((BuildContext buildContext, <span class="hljs-built_in">int</span> index) =>
        _buildDetailCommentHeader(state, dispatch, service))
    ..addAll(_buildCommentViewList(state, dispatch, service))
    ..add(isEmpty(state.commentListRes?.items)
        ? (BuildContext buildContext, <span class="hljs-built_in">int</span> index) =>
            _buildDetailCommentEmpty(state.itemInfo, dispatch)
        : <span class="hljs-keyword">null</span>)
    ..add(state.commentListRes?.getHasMore() == <span class="hljs-keyword">true</span>
        ? (BuildContext buildContext, <span class="hljs-built_in">int</span> index) => _buildLoadMore(dispatch)
        : <span class="hljs-keyword">null</span>));
    <span class="hljs-keyword">return</span> ListAdapter(
    (BuildContext buildContext, <span class="hljs-built_in">int</span> index) =>
        builders[index](buildContext, index),
    builders.length,
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-19">7. Dependencies</h3>
<p>Dependencies 是一个表达组件之间依赖关系的结构。它接收两个字段</p>
<ul>
<li>
<p><code>slots</code></p>
</li>
<li>
<p><code>string</code></p>
</li>
</ul>
<p>它主要包含三方面的信息</p>
<ul>
<li>
<p><code>slots</code>，组件依赖的插槽。</p>
</li>
<li>
<p><code>adapter</code>，组件依赖的具体适配器（用来构建高性能的 ListView）。</p>
</li>
<li>
<p><code>Dependent</code> 是 subComponent 或 subAdapter + connector 的组合。</p>
</li>
<li>
<p>一个 组件的 Reducer 由 Component 自身配置的 Reducer 和它的 Dependencies 下的所有子 Reducers 自动复合而成。</p>
</li>
</ul>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-comment">// register in component</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ItemComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ItemComponent</span><<span class="hljs-title">ItemState</span>> </span>&#123;
  ItemComponent()
      : <span class="hljs-keyword">super</span>(
          view: buildItemView,
          reducer: buildItemReducer(),
          dependencies: Dependencies<ItemState>(
            slots: <<span class="hljs-built_in">String</span>, Dependent<ItemState>>&#123;
              <span class="hljs-string">'appBar'</span>: AppBarComponent().asDependent(AppBarConnector()),
              <span class="hljs-string">'body'</span>: ItemBodyComponent().asDependent(ItemBodyConnector()),
              <span class="hljs-string">'ad_ball'</span>: ADBallComponent().asDependent(ADBallConnector()),
              <span class="hljs-string">'bottomBar'</span>: BottomBarComponent().asDependent(BottomBarConnector()),
            &#125;,
          ),
        );
&#125;

<span class="hljs-comment">// call in view</span>
Widget buildItemView(ItemState state, Dispatch dispatch, ViewService service) &#123;
  <span class="hljs-keyword">return</span> Scaffold(
      body: Stack(
        children: <Widget>[
          service.buildComponent(<span class="hljs-string">'body'</span>),
          service.buildComponent(<span class="hljs-string">'ad_ball'</span>),
          Positioned(
            child: service.buildComponent(<span class="hljs-string">'bottomBar'</span>),
            left: <span class="hljs-number">0.0</span>,
            bottom: <span class="hljs-number">0.0</span>,
            right: <span class="hljs-number">0.0</span>,
            height: <span class="hljs-number">100.0</span>,
          ),
        ],
      ),
      appBar: AppbarPreferSize(child: service.buildComponent(<span class="hljs-string">'appBar'</span>)));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-20">8. Dependent</h3>
<p>Dependent = connector+ subComponent | subAdapter 的组合，它表达了小组件|小适配器是如何连接到 Component 的。</p>
<hr>
<h3 data-id="heading-21">9. Directory</h3>
<p>推荐的目录结构会是这样：</p>
<pre><code class="hljs language-dart copyable" lang="dart">sample_page
    -- action.dart
    -- page.dart
    -- view.dart
    -- effect.dart
    -- reducer.dart
    -- state.dart
    components
        sample_component
        -- action.dart
        -- component.dart
        -- view.dart
        -- effect.dart
        -- reducer.dart
        -- state.dart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上层负责组装，下层负责实现。</p>
<h2 data-id="heading-22">五、Fish Redux的优化</h2>
<p>Redux 是一个专注于状态管理的框架；Fish Redux 是基于 Redux 做状态管理的应用框架；应用框架不仅仅要解决状态管理的问题，还要解决分治，通信，数据驱动，解耦等等问题。</p>
<p>Redux 通过使用者手动组织代码的形式来完成从小的 Reducer 到主 Reducer 的合并过程；Fish Redux 通过显式的表达组件之间的依赖关系，由框架自动完成从细力度的 Reducer 到主 Reducer 的合并过程；</p>
<p>Fish Redux 提供了一个 Adapter 的抽象组件模型，在基础的组件模型以外，Fish Redux 提供了一个 Adapter 抽象模型，用来解决在 ListView 上大 Cell 的性能问题。通过上层抽象，可以得到了逻辑上的 ScrollView，性能上的 ListView。</p>
<h2 data-id="heading-23">六、MobX库</h2>
<p>相信当大家开始用 Flutter 后，大多数项目都是在 Flutter 中编写的。终究有一天会遇到 setState() 这座大山，想逃都逃不掉。它会同时处理很多类，带着一大堆动态数据，让代码变得丑陋不堪，写起来也像蜗牛一样慢；而且它会严重拖累应用程序的性能，因为你得不停从头至尾重建小部件树，哪怕变量值稍微改变一下也得折腾一次。</p>
<p>前面介绍了Flutter-provide、Fish Redux这两种状态管理库，对Fish Redux感兴趣的同学可以参考我之前的分析文章：Fish-Redux 的设计原则（上篇）Fish-Redux 的设计原则（下篇）。
今天介绍一下MobX 。。。嗯？？？ 这不是前端react常用的状态管理 mobX，对，又是它，它现在也推出了MobX Flutter。MobX 是一个广受好评的库，它融入函数响应式编程（TFRP）原则简化了状态管理，使其容易扩展。</p>
<h2 data-id="heading-24">参考文献</h2>
<p>阿里巴巴 fish-redux 地址：<a href="https://github.com/alibaba/fish-redux" target="_blank" rel="nofollow noopener noreferrer">github.com/alibaba/fis…</a></p>
<p>MobX Flutter : <a href="https://pub.dev/packages/mobx" target="_blank" rel="nofollow noopener noreferrer">pub.dev/packages/mo…</a></p></div>  
</div>
            