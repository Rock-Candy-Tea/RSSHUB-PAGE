
---
title: '【Flutter 基础】 视图布局（二）List Widget'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6482c87975e34d7baea23ee146b9971a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 01:54:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6482c87975e34d7baea23ee146b9971a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第6天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><em>注：本文从个人公众号（岛前屿端）中迁移重新发布</em></p>
<blockquote>
<p>Flutter 是谷歌的移动 UI 框架，可以从单个代码库快速的为移动端(iOS & Android)、Web、桌面端、嵌入式设备上构建高质量的原生用户界面和应用程序。</p>
</blockquote>
<hr>
<ul>
<li>前置阅读：<a href="https://juejin.cn/post/6978712721600544804/" target="_blank">【Flutter 基础】 视图布局（一）基本概念</a></li>
</ul>
<p>在 Flutter 视图布局（一）中文章结束时留下了一个问题，大家有尝试去实现吗？</p>
<p>如果大家认真看文章的话，这并不是很难的东西。</p>
<p>当然如果有配合 <strong>github</strong> 项目的代码来看的话，一定会发现我也已经将实现好的代码也更新上去了，可以作为实现参考。</p>
<p>好，那么我们就废话不多说，这次我们就来说道说道 <strong>ListBody</strong> 和 <strong>ListView</strong> 这两个常用的布局 <strong>List Widget</strong>。</p>
<p>在此之前我们还是要说说 Flutter 的包管理方式，因为这是开发中必不可少的绕不开的一部分。</p>
<h2 data-id="heading-0">包管理方式</h2>
<p>在 MyApp 项目目录下有个 <strong>pubspec.yaml</strong> 文件，这个文件主要是 Flutter 用于<strong>管理外部依赖项</strong>。</p>
<blockquote>
<p>YAML 是一个<strong>标记性语言</strong>，它<strong>对大小写敏感</strong>，由于不像其他类型文件的数据格式拥有明显的<strong>父、子级标记</strong>而是默认使用空格缩进 <em>（2个空格）</em> 代表层级，比如用 “- ” <em>（中划线+空格）</em> 来表示列表。</p>
</blockquote>
<p>当然，在默认的文件中也有<strong>示例说明</strong>，这就需要你自己去打开文件看一看啦。</p>
<p>在默认的文件情况下我们可以看到一级分类由以下类型组成。现在我们从上到下来分别解释一下这些东西到底是干什么的：</p>
<ol>
<li>name 项目名称</li>
<li>description 简介</li>
<li>version 版本号</li>
<li>environment 环境，表示 SDK 版本</li>
<li>dependencies 依赖项</li>
<li>dev_dependencies 开发依赖项</li>
<li>flutter 所需资源文件引入</li>
</ol>
<p>然后现在我们先在 <strong>dependencies</strong> 中加入 <code>english_words</code>，这个英文单词的包主要是用于后续的例子中，可以先考虑引入。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">english_words:</span> <span class="hljs-string">^3.1.0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在添加完新的依赖包后，当你进行保存时 VS Code 会<strong>自动进行依赖包的更新和下载</strong>，还是比较方便的，就<strong>不需要手动进行更新命令</strong>了。</p>
<p>当然也可以手动执行命令（最终作用是相同的）</p>
<pre><code class="hljs language-shell copyable" lang="shell">flutter packages get
<span class="hljs-meta">#</span><span class="bash"> or</span>
flutter pub get
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，接下来我们可以说说 ListBody 和 ListView 了</p>
<h2 data-id="heading-1">ListBody</h2>
<p>我们先来看看 ListBody 的源码部分</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6482c87975e34d7baea23ee146b9971a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListBody 源码部分）</em></p>
<p>这不看都不知道，相比 <strong>Row、Column</strong> 来说简直是太简单了：</p>
<ul>
<li>Axis mainAxis 主轴，默认垂直方向，即 y 轴</li>
<li>bool reverse 是否反向/颠倒顺序的</li>
<li>List<Widget> children 子元素列表 Widget 类型</li>
</ul>
<p>都看到这了，才 <strong>三个属性</strong> ，那还等什么？当然是上手就干啊！</p>
<p><em>（我的嘴角微微上翘，手指在键盘上噼里啪啦一通乱舞……）</em></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c899af0ea7f84daaa52222f6cc797523~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我的内心毫无波澜甚至还有些想笑</p>
<p>看着代码完成了，也没有明显报错，这很OK，召唤控制台 - 输入 - <em><a href="https://juejin.cn/post/6968657797391056909#heading-3" target="_blank">R 命令</a></em></p>
<p><em>兴奋的等待……</em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6bf520c06245f9b3cbaf702643545f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>发生了什么？</p>
<p>这是怎么回事？发生了什么事？！</p>
<p><strong>冷静一下不要慌，让我们来看看源码。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd23a0ed1d71435382708d246060e82f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListBody 源码注释部分）</em></p>
<p>看完之后发现，原来 <strong>ListBody</strong> 是一个可以设定轴方向的 <strong>多子元素列表</strong>，但是需要一个可以<strong>强制范围的容器</strong>来装载它。而且这是一个很少不能够直接使用的 Widget，如果需要的话应该<strong>优先选择 ListView</strong>，因为它有相同的布局方式以及提供了滚动行为。</p>
<p>（摸着下巴若有所思）OK，那我们就来把他放在 ListView 下。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df31da69a6f4e77b52b697ea05ba4a1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListBody 放在 ListView 下）</em></p>
<p>这样就没什么问题了！</p>
<h2 data-id="heading-2">ListView</h2>
<p>关于 ListView 还是要先认真看下源码，这次可不能那么鲁莽。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d203267968834ed0a889bbb0bb00788f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListView 源码部分）</em></p>
<p>仔细一看，这属性还挺多。不着急，那我们分别都来看一看。</p>
<ul>
<li>Axis scrollDirection 滚动的方向，即轴方向，Axis.vertical 垂直方向 和 Axis.horizontal 水平方向，默认为垂直方向</li>
<li>bool reverse 是否反向/颠倒顺序的，默认为 false，如为 true 则 垂直方向从底部开始，水平方向从右边开始</li>
<li>bool primary 是否是主主要的滚动 Widget，默认为 false， 如果为 true 则 controller 必须为 null</li>
<li>bool shrinkWrap 是否收缩滚动视图</li>
<li>EdgeInsetsGeometry padding 顾名思义填充的内边距</li>
<li>ScrollController controller 滚动事件，与 primary 互斥</li>
<li>ScrollPhysics physics 滚动的行为方式</li>
<li>bool addAutomaticKeepAlives</li>
<li>bool addRepaintBoundaries</li>
<li>bool addSemanticIndexes</li>
<li>double cacheExtent</li>
<li>int semanticChildCount</li>
<li>DragStartBehaviordragStartBehavior</li>
<li>List<Widget> children 子元素列表 Widget 类型</li>
</ul>
<h3 data-id="heading-3">reverse</h3>
<p>reverse 就是将列表的渲染方式是否是反向，垂直方向从底部开始，水平方向从右边开始。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f1031f5703c4cc995868b85b7f13b77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（reverse 反向渲染/颠倒列表）</em></p>
<h3 data-id="heading-4">controller</h3>
<p>关于滚动事件，如果真要说的话，那么篇幅就太长了，所以这里暂时不讲，后续会将一些 Widget 的事件 整理出来。</p>
<p>如果各位少侠小伙伴们有兴趣的，可以先看看这个滚动事件参考：</p>
<p><a href="https://book.flutterchina.club/chapter6/scroll_controller.html" target="_blank" rel="nofollow noopener noreferrer">book.flutterchina.club/chapter6/sc…</a></p>
<p><a href="https://api.flutter.dev/flutter/widgets/ScrollView/controller.html" target="_blank" rel="nofollow noopener noreferrer">api.flutter.dev/flutter/wid…</a></p>
<p>primary 与 controller 互斥，当 controller 定义了事件且 <strong>primary</strong> 为 <strong>true</strong> 时 则会 喜提满屏红。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a77553d8fd54655bbb4db00f6b86992~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（primary 与 controller 互斥）</em></p>
<p>在源码中有这样一段：</p>
<blockquote>
<p>如果 primary 为 true 则 controller 必须为 null，controller 滚动事件，与 primary 互斥。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ae151b349044f0b9e5d0b44ded96c5e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<em>（源码）</em></p>
<h3 data-id="heading-5">addAutomaticKeepAlives</h3>
<p>是否将子项都装在 <strong>AutomaticKeepAlive</strong> 中，默认为 <strong>true</strong>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24692875ad494ef38d932e7213a50a06~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<em>（addAutomaticKeepAlives 源码部分说明）</em></p>
<p>简单来说（翻译一下），<strong>通常列表是懒惰的</strong>，将子元素装在 <strong>AutomaticKeepAlive</strong> 中，以便其<strong>子级元素可以使用 KeepAliveNotification 来保留状态</strong>，否则它们在屏幕外将被回收。</p>
<p>如果需要<strong>手动维护</strong>子元素的子级元素那么就必须 <strong>禁用此功能（false）</strong> （以及 <strong>addRepaintBoundaries</strong> 设为 <strong>false</strong>）。</p>
<p>再简单来说，就是<strong>子元素可以超出屏幕之外还继续保留</strong>，但是这个状态的保留<strong>由框架负责</strong>。如果你需要自己决定如何保留子元素的状态，那么就<strong>把 addAutomaticKeepAlives 和 addRepaintBoundaries 关了自己写去吧（Flutter 可不伺候你）</strong>。</p>
<h3 data-id="heading-6">addRepaintBoundaries</h3>
<p>是否将子项都装在 <strong>RepaintBoundary</strong> 中，默认为 <strong>true</strong>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f6ef835ce0447f495e075f139359f12~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<em>（addRepaintBoundaries 源码部分说明）</em></p>
<p>简单来说（翻译一下），通常在可滚动列表的容器中子项都会被装在<strong>重绘边界</strong>之内，以便列表<strong>在滚动时不需要将它们进行重绘</strong>。如果是简单的子项内容 <strong>（纯色块或者短文本）</strong> ，则关闭 <strong>addRepaintBoundaries（false）</strong> 让其<strong>重绘子项</strong>可能会更有效率。</p>
<p>简单来说，不能再简单了，请少侠们自己思考。</p>
<h3 data-id="heading-7">addSemanticIndexes</h3>
<p>是否将子项都装在 <strong>IndexedSemantics</strong> 中，默认依然为 <strong>true</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27625158501f49e992a09c376804a4c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（addSemanticIndexes 源码部分说明）</em></p>
<h3 data-id="heading-8">cacheExtent</h3>
<p>在视图可见区域之外有一个区域 <strong>（即垂直是上下部分，水平是左右部分）</strong> ，用于缓存滚动即进入可见区域的子元素。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab9a02d05f54a3792b945390c606175~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>进入此缓存区域的子项在即使<strong>未在可见视图内也是可见的</strong>，即是进入可见区域后就会被布局渲染，cacheExtent 主要是用于<strong>描述该区域所延伸的大小</strong>。</p>
<h2 data-id="heading-9">physics</h2>
<p>physics 主要是 滚动的物理效果</p>
<ul>
<li><strong>ClampingScrollPhysics</strong> 默认的钳位效果</li>
<li><strong>BouncingScrollPhysics</strong> 回弹的物理效果</li>
<li><strong>FixedExtentScrollPhysics</strong> 拨轮式的物理效果</li>
<li><strong>AlwaysScrollableScrollPhysics</strong> 始终可以滚动效果</li>
<li><strong>NeverScrollableScrollPhysics</strong> 禁止滚动效果</li>
</ul>
<p><strong>AlwaysScrollableScrollPhysics</strong> 和 <strong>NeverScrollableScrollPhysics</strong> 就不用演示效果了，毕竟这个意思和 CSS 中 <em>overflow 的 scroll 和 hidden</em> 一个意思。</p>
<h3 data-id="heading-10">ClampingScrollPhysics</h3>
<p><strong>ClampingScrollPhysics</strong> 我也不知道为什么要用 <strong>Clamping</strong>，可能是<strong>像钳子一样拥有最大张合度吧</strong>。在默认情况下，如果<strong>列表子元素不足以超出可视范围</strong>则不会产生可滚动行为。如<strong>超出可视范围</strong>则到达列表尽头时会停留并有<strong>水波样式</strong>出现。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f11318f16ab2495da97709fe3d083c18~tplv-k3u1fbpfcp-watermark.image" alt="640.gif" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ClampingScrollPhysics 的滚动效果）</em></p>
<h3 data-id="heading-11">BouncingScrollPhysics</h3>
<p><strong>BouncingScrollPhysics</strong> 的话就是大家都熟悉的<strong>回弹效果</strong>了，当操作列表<strong>到达可视范围尽头时还可以继续超出一定的空间</strong>，当失去焦点后回到尽头的位置，这样就能给予用户一个<strong>良好的使用体验</strong>。一般来说都会在下拉刷新上拉加载这样的场景里使用。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce55f88da3324bf8ab4d5eeb69c68884~tplv-k3u1fbpfcp-watermark.image" alt="640 (1).gif" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（BouncingScrollPhysics 的滚动效果）</em></p>
<h3 data-id="heading-12">BouncingScrollPhysics</h3>
<p>BouncingScrollPhysics 的滚动效果</p>
<p>FixedExtentScrollPhysics 是类似拨轮的效果，怎么说呢，这个用文字还真不好描述效果，看一张实物图大概就能理解了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0057438c5584e30a81e64abd0911c49~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>拨轮日期印章（图片来自网络）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be2c6c69fdac4b3d915e788778514214~tplv-k3u1fbpfcp-watermark.image" alt="640 (2).gif" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（FixedExtentScrollPhysics 的滚动效果）</em></p>
<h2 data-id="heading-13">无限滚动例子</h2>
<p>以上就是 ListView 属性的使用说明了，但是你可能会问了</p>
<blockquote>
<p>哎呀，这些<strong>子元素你写那么多不现实啊</strong>，真正使用到的时候肯定都是<strong>按需生成</strong>的，不然如果有很多子元素不可能都 copy paste 一遍吧？</p>
</blockquote>
<p>很好，我很佩服你提问的勇气！不过没关系，Flutter 当然也知道这个问题，那么我们就来看看它有哪些相关的方法可以使用。</p>
<p>不用多说，我们还是来先看源码。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eee0c58a55e4dcebc8e06a19f28bce8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListView 源码注释说明）</em></p>
<p>源码中说到 ListView 有4中设置子元素的方式：</p>
<ul>
<li>List<Widget></li>
<li>ListView.builder</li>
<li>ListView.separated</li>
<li>ListView.custom</li>
</ul>
<p>第一种 <strong>List<Widget></strong> 就不用多说了，我们常用的<strong>直接写在列表里</strong>的方式。另外的三种方式就需要我们编码去实现了。</p>
<p>需要编码的三个构造函数都拥有相同的属性这也是最常用的属性：</p>
<ul>
<li>padding 每个元素的边距</li>
<li>itemCount 元素的数量，默认为 null 即无限</li>
<li>itemBuilder 接受一个回调函数 参数为：BuildContext context, int index</li>
</ul>
<h3 data-id="heading-14">ListView.builder</h3>
<p>首先还是要翻译一下源码里是怎么解释这个方法的：</p>
<blockquote>
<p>使用了 <strong>indexedWidgetBuilder</strong> 它可以按需生成子元素，此构造函数适用于列表需要<strong>大量或者无限子元素生成</strong>，因为其调用了<strong>元素生成器</strong>，所以<strong>仅在实际可视范围</strong>中显示。</p>
</blockquote>
<p>Ok，那我们就来看看代码是如何实现的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a30912b731d45339b7c08596469ee07~tplv-k3u1fbpfcp-watermark.image" alt="640 (3).gif" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListView.builder 实现动态生成子元素）</em></p>
<p>当 <strong>itemCount</strong> 设置为 <strong>null</strong> 时就可以实现无限下拉列表。少侠们可以在代码中尝试修改一下看看效果。</p>
<h3 data-id="heading-15">ListView.separated</h3>
<p>首先还是要翻译一下源码里是怎么解释这方法的：</p>
<blockquote>
<p>使用了两个 <strong>indexedWidgetBuilder</strong> 来处理子元素，itembuilder 是<strong>按需生成子元素</strong>，<strong>separatorbuilder</strong> 是根据子元素来生成<strong>子元素之间的分隔符元素</strong>。此构造函数只能<strong>适用于子级数量确定的</strong>列表视图。</p>
</blockquote>
<p>Ok，那我们就来看看代码是如何实现的。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9dc6844e9e14d5bbf0effda6cd332a4~tplv-k3u1fbpfcp-watermark.image" alt="640 (4).gif" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（ListView.builder 实现动态生成子元素）</em></p>
<p>其实 <strong>separated</strong> 和 <strong>builder</strong> 差别并不大，这里我只做了<strong>简单的修改就实现了分割线</strong>。</p>
<h3 data-id="heading-16">ListView.custom</h3>
<p>没错还是要翻译一下源码里是怎么解释这方法的：</p>
<blockquote>
<p>构造函数接受一个 <strong>sliverChildDelegate</strong>，它提供<strong>自定义子模型</strong>其他方面的功能。例如：<strong>sliverchildDelegate</strong> 可以控制用于<strong>估计实际不可见子级大小的算法</strong>。</p>
</blockquote>
<p><strong>ListView.custom</strong> 要实现起来的话较为麻烦，但还是可以简单实现一下。</p>
<p>主要实现方式有 <strong>SliverChildListDelegate</strong> 列表方式 和 <strong>SliverChildBuilderDelegate</strong> 编码方式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7835add2145f4e87812cdd3ce5307a16~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（SliverChildListDelegate 列表方式实现）</em></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4679268991ad447eb5693f8e7d05500d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
<em>（SliverChildBuilderDelegate 编码方式实现）</em></p>
<p>最终效果的话，少侠们，可以自己更新修改代码尝试哟。</p>
<hr>
<h2 data-id="heading-17">最后</h2>
<p><strong>ListView Widget</strong> 的内容其实并不难，<strong>列表的使用都有对应的场景</strong>，只要熟悉了列表的<strong>渲染特征</strong>后，碰见相应的场景自然就不用纠结到底使用哪一个更合适了。其中的难点还是在于 <strong>ListView.custom</strong> 的实现上，他需要你<strong>自己去实现列表相关的所有东西</strong>：<code>监听滚动</code>、<code>渲染子元素的方式</code>、<code>销毁子元素</code>等等。</p>
<h2 data-id="heading-18">最后总结</h2>
<p>Flutter 基本上为你考虑了一些相关场景使用的实现，所以可以很方便的使用这些内容，但是考虑过细自然也就会觉得需要了解的内容就过多。</p>
<p>就单单从“列表”来看，大致和其他语言的实现是相似的，了解其中常用的属性即可正常使用。</p>
<p>配合文章一同食用的代码已同步更新到 Github 地址：<a href="https://github.com/linxsbox/myapp.git" target="_blank" rel="nofollow noopener noreferrer">github.com/linxsbox/my…</a></p>
<ul>
<li>前置阅读：<a href="https://juejin.cn/post/6978712721600544804/" target="_blank">【Flutter 基础】 视图布局（一）基本概念</a></li>
</ul>
<h2 data-id="heading-19">参考</h2>
<ul>
<li><strong>《Flutter实战》：<a href="https://book.flutterchina.club/chapter6/scroll_controller.html" target="_blank" rel="nofollow noopener noreferrer">book.flutterchina.club/chapter6/sc…</a></strong></li>
<li><strong>Flutter 官网 API：<a href="https://api.flutter.dev/flutter/widgets/ScrollView/controller.html" target="_blank" rel="nofollow noopener noreferrer">api.flutter.dev/flutter/wid…</a></strong></li>
</ul></div>  
</div>
            