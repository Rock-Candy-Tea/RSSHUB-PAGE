
---
title: 'umi+qiankun+gitsubmodel 完成项目微前端重构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbebadc83e7e40ed812c690dd1481115~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 19:19:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbebadc83e7e40ed812c690dd1481115~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">写在前面</h1>
<p>本次例子是简化版的真实项目，从零到一，包括最后的nginx配置都有。并且配上效果图，至于文件目录结构，因为和umi官网命令搭建的一样就不会贴出来了。主应用，子应用全都是用umi进行开发，没有和网上大部分例子一样嵌套了vue等其他框架。全程使用了umi全家桶开发，cv大法，若想了解微前端更多原理之类的，网上很多讲解，这里不涉及，因为本人也是一知半解。只会使用，不会搭建构造。</p>
<h1 data-id="heading-1">项目背景</h1>
<p>公司有个C端项目，简单概括就是一个基础商城，会售卖给很多个甲方，同时会根据甲方的要求进行特殊化处理。比如每个甲方的登录方式不一样，首页布局不一样等等。项目之前的处理方式是利用git分支功能做管理，一个甲方一个分支。但这样会出现不好维护的情况，比如共有的代码出现了一个问题，我需要修改其他分支并且重新打包，这样非常不友好。并且随着业务的越来越庞大，功能模块越来越多，里面好几个业务都可以当作是一个项目来进行开发了。这时候微前端这几个字就走进了我的眼球，并且决定对项目进行重构。</p>
<h1 data-id="heading-2">开始工作</h1>
<p>经过搜索，我把目光锁定了qiankun,并且使用umi开发，别问，问就是底层原理不会，而<a href="https://umijs.org/plugins/plugin-qiankun" target="_blank" rel="nofollow noopener noreferrer">umi刚好有qiankun</a>一条龙服务。具体参考文档。跟着文档，一步步生成了两个项目，main和home,main就是主应用，相当于一个容器，用于登录和通用的基础应用。而home顾名思义就是首页，相当于一个子应用。如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbebadc83e7e40ed812c690dd1481115~tplv-k3u1fbpfcp-watermark.image" alt="X89RV&#125;E9%(M2FCR&#125;E3VJRJQ.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2a1d15431144db2bb5373c7543a4809~tplv-k3u1fbpfcp-watermark.image" alt="`KZ_OQM)EMMQ_L7$63EOT.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后根据文档所写，安装qiankun 两个应用都要：</p>
<pre><code class="hljs language-js copyable" lang="js">yarn add  @umijs/plugin-qiankun
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>main/.umirc.ts 下的 defineConfig 增加</em></p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 注册主应用</span>
  <span class="hljs-attr">qiankun</span>: &#123;
    <span class="hljs-attr">master</span>: &#123;&#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>home/.umirc.ts 下的defineConfig增加</em></p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 注册子应用</span>
  <span class="hljs-attr">qiankun</span>: &#123;
    <span class="hljs-attr">slave</span>: &#123;&#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>main/src/app.ts的配置加上：</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> qiankun = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">apps</span>: [
      &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>, <span class="hljs-comment">// 唯一 id </span>
        <span class="hljs-attr">entry</span>: <span class="hljs-string">'//xxx.xxx.xx.xxx:8000'</span>, <span class="hljs-comment">// home的运行地址  </span>
      &#125;,
      <span class="hljs-comment">// 若有多个子应用往下增加</span>
    ],
    <span class="hljs-attr">lifeCycles</span>: &#123;
      <span class="hljs-attr">afterMount</span>: <span class="hljs-function">(<span class="hljs-params">props: any</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'qiankun---'</span>, props)
      &#125;,
    &#125;,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过这一波操作，再次重启项目发现竟然ok，如下截图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6335b8c0a95846719e848233839a0f8f~tplv-k3u1fbpfcp-watermark.image" alt=")&#123;6H4$GD&#125;@%`[(A]&#125;D$$BK7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这我心里只有两个字，芜湖~但是！但是！但是！到这里还没完，因为真正用于开发上线还有几个问题：</p>
<ol>
<li>如何隔离</li>
<li>如何数据传递</li>
<li>怎么在子应用跳转主应用的路由，比如子应用/home 要跳去/mine 页面（mine属于父级应用路由）</li>
<li>如何使用公共的组件，方法等</li>
<li>怎么打包通过正式的url访问</li>
</ol>
<h3 data-id="heading-3">如何隔离</h3>
<p>这点其实很好办，官网本身有给出沙盒api，而且再不济就不要用重名咯~（半开玩笑）</p>
<h3 data-id="heading-4">如何数据传递</h3>
<p>这点也很好解决，官网也有例子，但不得不吐槽一下，使用官网的例子，主应用注册不能写在.umirc.ts，需写在app.ts里（按照我上面的配置就好），不多说，上代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main  app.ts</span>
<span class="hljs-keyword">import</span> &#123; history &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useQiankunStateForSlave</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [qiankunGlobalState, setQiankunGlobalState] = useState<any>(&#123;
    <span class="hljs-attr">masterHistory</span>: history,
    <span class="hljs-attr">test</span>:<span class="hljs-string">'hello'</span>,
  &#125;)
  <span class="hljs-comment">// 可以挂载到window下  这里需要注意，如果window获取，修改内容时需要及时修改window</span>
  <span class="hljs-built_in">window</span>.masterHistory = history
  <span class="hljs-built_in">window</span>.qiankunGlobalState = qiankunGlobalState
  <span class="hljs-keyword">return</span> &#123;
    qiankunGlobalState,
    setQiankunGlobalState,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候不管主应用还是子应用，都可以使用useModel获取qiankunGlobalState，并且通过setQiankunGlobalState来对数据进行更新，修改等</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 主/子应用的test.tsx  不一定test.tsx哈，哪里想用就去哪里</span>
<span class="hljs-keyword">import</span> &#123; IRouteComponentProps, useModel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>
<span class="hljs-keyword">import</span> React, &#123; useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Text</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; setQiankunGlobalState, qiankunGlobalState &#125; = useModel(
    <span class="hljs-string">'@@qiankunStateForSlave'</span>,
  )
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'qiankunGlobalState'</span>, qiankunGlobalState)
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      setQiankunGlobalState(&#123;
        ...qiankunGlobalState,
        <span class="hljs-attr">userName</span>: <span class="hljs-string">'我是js'</span>,
      &#125;)
    &#125;, <span class="hljs-number">2000</span>)
  &#125;, [])
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里一部分涨的帅/漂亮的同志就会说，怎么我ts一使用window.xxx就会报红线呀</p>
<p>这时候需要在目录下增加window.d.ts 名字任意哈，.d.ts结尾即可。内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// window.d.ts</span>
<span class="hljs-keyword">import</span> &#123; History &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'umi'</span>

declare <span class="hljs-built_in">global</span> &#123;
  interface Window &#123;
    <span class="hljs-attr">masterHistory</span>: History
    <span class="hljs-attr">qiankunGlobalState</span>: &#123;
      <span class="hljs-attr">projectName</span>: string
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">如何维护公共的组件，方法</h3>
<p>一开始我是想到npm这种方式，但是开发阶段各种改很不方便，于是后面使用了git submodel，创建一个libs的项目进行管理维护。</p>
<ol>
<li>首先创建一个libs文件，里面存放各种公用的方法，组件，图片等，并且同步到gitlab上</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97f1ff27b4dc47f194540adad5dfbe22~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.各应用到src下关联该模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main  home src目录</span>
git submodule add 项目git地址/libs.git  src/
<span class="hljs-comment">// 执行完后会发现目录下多了个.gitmodules,并且src下有libs的文件了，这时候不管是哪个应用，都可以对libs进行开发维护，而libs维护和普通项目git一样。 记得libs切换到分支再进行开发！！！因为一开始默认是某次提交</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">怎么打包，通过正式的url访问</h3>
<p>我司是用k8s进行项目打包的，经百度在ci文件加上以下配置：</p>
<pre><code class="hljs language-js copyable" lang="js">.gitlab-ci.ymi文件
<span class="hljs-attr">variables</span>:
  GIT_SUBMODULE_STRATEGY: recursive # 拉取 Submodule 内容
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正当我兴致勃勃准备开瓶82年的旺仔牛奶庆祝的时候，发现后台打包显示报错，报错信息如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e99300ca18a4a33b9a3f628ab2a72fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过报错信息大体得知，下载失败，但是为什么失败呢，怎么成功呢，我一脸懵逼，百度查了好久好久都没有答案，自己也折腾了无数遍，换账号，ssh等等都没折腾成功，后来想起，<a href="https://docs.gitlab.com/ee/ci/git_submodules.html" target="_blank" rel="nofollow noopener noreferrer">git submodule gitlab</a>介绍中的配置于是我屁颠屁的修改.gitmodules里的url路径为相对路径,果然成功了！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1ed14dacfc4eb695bba351afaac1b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">nginx配置</h3>
<p>这里的配置各项目大同小异，具体根据实际来即可。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df0386ec77ae49e9979a12ef5d61b829~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置完后兴致勃勃的打开，效果不错</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b9db688b6c54022a9192f4f2582e551~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后打包成功后，记得修改以下app.ts里的entry值，目前我是配合cross-env配置了本地开发环境local、测试环境dev、生产环境prod，分别对应不同的url。这样就方便多了。到这里还有两个小问题目前暂未解决,</p>
<h3 data-id="heading-8">未解决的小问题</h3>
<ol>
<li>主应用的路由不能动态生成，每有一个页面，需要手动到.umirc.ts的router里增加，挺不方便的</li>
<li>.gitmodules打包时候需要用相对路径，这样的话本地初始化开发就不太方便了</li>
</ol>
<p>若有知道的大神希望告诉下解决方案。</p>
<h3 data-id="heading-9">总结</h3>
<p>到这里可能会有疑问，<em>怎么在子应用跳转主应用的路由</em> 这个问题还没解决呀。对于这个问题一些细心的朋友就发现了，我把 main 的 history 当作参数传进了 qiankunGlobalState ，那么只要在子应用调用 qiankunGlobalState.masterHistory 这个方法就可以跳转main组件的路由，其他子应用路由同理。</p>
<p>总体来说开发还是相对顺滑的，果然是前人栽树后人乘凉。不得不佩服开发这些框架的大佬们真的强。目前我花费最多时间就是公共模块的维护与开发，总体打包，以及nginx配置那一块。但是目前来说，对于移动端项目，网上好像没有微前端例子公布。我这个真实的项目目前也在最后开发阶段，准备进入提测环节，并未真正发布使用，所以微前端合适不合适移动端，暂时未知，发布投入使用后，我会抽空再总结一下。</p>
<p>另外本人是个离开了百度、谷歌就活不下去的cv菜鸡，写的不好不对的地方欢迎指正~</p>
<h1 data-id="heading-10">感谢大家！</h1></div>  
</div>
            