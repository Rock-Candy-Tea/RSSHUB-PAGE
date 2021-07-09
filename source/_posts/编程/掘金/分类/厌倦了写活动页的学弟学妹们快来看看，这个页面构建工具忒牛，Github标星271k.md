
---
title: '厌倦了写活动页的学弟学妹们快来看看，这个页面构建工具忒牛，Github标星27.1k'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc07aec52fa4a65a073b7db8909c210~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 01:36:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc07aec52fa4a65a073b7db8909c210~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbc07aec52fa4a65a073b7db8909c210~tplv-k3u1fbpfcp-watermark.image" alt="CSDN首图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你经常接触一些公司的活动页，可能会经常头疼以下问题：这些项目周期短，需求频繁，迭代快，技术要求不高，成长空间也小。但是我们还是马不停蹄的赶着产品提来的一个个需求，随着公司规模的增加，我们不可能无限制的增加人手不断地重复着这些活动。这里我就不具体介绍一些有的没的的一些概念了，因为要介绍的概念实在太多了，作为一个前端的我们，直接上代码撸就好了！！！！</p>
<h3 data-id="heading-0">目标</h3>
<p>我们的目标是实现一个页面制作后台，在后台中我们可以对页面进行 组件选择 --> 布局样式调整 --> 发布上线 --> 编辑修改这样的流程操作。</p>
<h3 data-id="heading-1">架构设计</h3>
<p>首先是要能提供组件给用户进行选择，那么我们需要一个组件库，然后需要对选择的组件进行布局样式调整，所以我们需要一个页面编辑后台接着我们需要将编辑产出的数据渲染成真实的页面，所以我们需要一个<code>node</code> 服务和用于填充的 <code>template</code> 模板。发布上线，这个直接对接各个公司内部的发布系统就好了，这里我们不做过多阐述。最后的编辑修改功能也就是针对配置的修改，所以我们需要一个数据库，这里我选择的是用了<code>mysql</code>。当然你也可以顺便做做权限管理，页面管理....等等之类的活。啰嗦了这么长，我们来画个图，了解下大概的流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33d1e85e9e8941cba57ab27cc4ced3bf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">组件的实现</h2>
<p>首先我们来实现组件这一部分，因为组件关联着后台编辑的预览和最后发布的使用。组件设计我们应该尽量保持组件的对外一致性，这样在进行渲染的时候，我们可以提供一个统一的对外数据接口。这里我们的技术选型是基于 <code>Vue</code> 的，所以下面的代码部分也主要是基于 Vue 的，但是万变不离其宗，其他语言也类似。</p>
<p>根据上图，我们的组件是会被一个个拆分单独发布到 <code>npm</code> 仓库的，为什么这么设计呢？其实之前也考虑过设计成一个组件库，所有组件都包含在一个组件库内，这样只需要发布一个组件库包，用的时候按需加载就好了。后来在实践的过程中发现这样并不合适协同开发，其他前端如果想贡献组件，接入的改造成本也很大。</p>
<p>举个chestnut：小明在业务中写了个Button组件，这个组件经常会被其他项目复用，他想把这个组件贡献到我们的系统中，被模板使用，如果是一个组件库的话，他首先得拉取我们组件库的代码，然后按照组件库的规范格式进行提交。这样一来，偷懒的小明可能就不太愿意这么干，最爽的方法当然是在本地构建一个npm库，开发选用的是用 <code>TypeScript</code> 还是其他的我们不关心，选用的 <code>CSS</code> 预处理器我们也不关心，甚至编码规范的 <code>ESLint </code>我们也不关心。最后只需通过编译后的文件即可。这样就避免了一个组件库的约束。依托于NPM完善的发布/拉取，以及版本控制机制，可以让我们少做一些额外的工作，也可以快速的把平台搭建起来。</p>
<p>说了这么多，代码呢？，我们以一个Button为例，我们对外提供这样的形式组件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"data.style.container"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"w_button_container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"data.style.btn"</span>></span> &#123;&#123;data.context&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'WButton'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;&#125;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>可以看到我们只对外暴露了一个props，这样做法的好处是可以统一组件对外暴露的数据，组件内部爱怎么玩怎么玩。注意，这里我们也可以引入一些第三方组件库，比如mint-ui之类的。</p>
</blockquote>
<h3 data-id="heading-3">后台编辑的实现</h3>
<p>在写代码前，我们先考虑一下需要实现哪些功能：</p>
<p>1.一个属性编辑区，提供给使用者编辑组件内部 <code>props</code> 的功能</p>
<p>2.一个组件选择区，提供使用者选择需要的组件</p>
<p>3.一个组件预览区，提供使用者拖拽排序页面预览的功能</p>
<h3 data-id="heading-4">编辑区的实现</h3>
<p>按照顺序，我们先来实现组件的属性编辑功能。我们要考虑，一个组件暴露出哪些可配置的信息。这些可配置的信息如何同步到后台编辑区，让使用者进行编辑，一个按钮的可配置信息可能是这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad501e50265f4361b815846f644822cc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果把这些配置全部写在后台库里面，根据当前选择的组件加载不同的配置，维护起来会相当麻烦，而且随着组件数量的增加，也会变得臃肿，所以我们可以将这些配置存储在服务端，后台只需要根据存储的规则进行解析便可，举个例子，我们其实可以存储这样的编辑配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  &#123;
    <span class="hljs-string">"blockName"</span>: <span class="hljs-string">"按钮布局设置"</span>, 
    <span class="hljs-string">"settings"</span>: &#123;
      <span class="hljs-string">"src"</span>: &#123;
        <span class="hljs-string">"type"</span>: <span class="hljs-string">"input"</span>,  
        <span class="hljs-string">"require"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-string">"label"</span>: <span class="hljs-string">"按钮文案"</span>
      &#125;
    &#125;
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在编辑后台，通过接口请求到这些配置，便可以进行规则渲染：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 根据类型，选择创建对应的组件
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;VNode&#125;</span> <span class="hljs-variable">vm</span></span>
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;any&#125;</span></span>
 */</span>
createEditorElement (vm: VNode) &#123;
  <span class="hljs-keyword">let</span> dom = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">switch</span> (vm.config.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'align'</span>:
      dom = <span class="hljs-built_in">this</span>.createAlignElement(vm)
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'select'</span>:
      dom = <span class="hljs-built_in">this</span>.createSelectElement(vm)
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'actions'</span>:
      dom = <span class="hljs-built_in">this</span>.createActionElement(vm)
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">'vue-editor'</span>:
      dom = <span class="hljs-built_in">this</span>.createVueEditor(vm)
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">default</span>:
      dom = <span class="hljs-built_in">this</span>.createBasicElement(vm)
  &#125;
  <span class="hljs-keyword">return</span> dom
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">组件选择区</h3>
<p>首先我们需要考虑的是，组件怎么进行注册？因为组件被用户选用的时候，我们是需要渲染该组件的，所以我们可以提供一段 node 脚本来遍历所需组件，进行组件的安装注册：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义渲染模板和路径</span>
<span class="hljs-keyword">var</span> OUTPUT_PATH = path.join(__dirname, <span class="hljs-string">'../packages/index.js'</span>);
<span class="hljs-built_in">console</span>.log(chalk.yellow(<span class="hljs-string">'正在生成包引用文件...'</span>))
<span class="hljs-keyword">var</span> INSTALL_COMPONENT_TEMPLATE = <span class="hljs-string">'    &#123;&#123;name&#125;&#125;'</span>;
<span class="hljs-keyword">var</span> IMPORT_TEMPLATE = <span class="hljs-string">'import &#123;&#123;componentName&#125;&#125; from \'&#123;&#123;name&#125;&#125;\''</span>;
<span class="hljs-keyword">var</span> MAIN_TEMPLATE = <span class="hljs-string">`/* Automatic generated by './compiler/build-entry.js' */

&#123;&#123;include&#125;&#125;

const components = [
&#123;&#123;install&#125;&#125;
]

const install = function(Vue) &#123;
    components.map((component) => &#123;
        Vue.component(component.name, component)
    &#125;)
&#125;

/* istanbul ignore if */
if (typeof window !== 'undefined' && window.Vue) &#123;
    install(window.Vue)
&#125;

export &#123;
    install,
    &#123;&#123;list&#125;&#125;
&#125;
`</span>;
<span class="hljs-comment">// 渲染引用文件</span>
<span class="hljs-keyword">var</span> template = render(MAIN_TEMPLATE, &#123;
  <span class="hljs-attr">include</span>: includeComponentTemplate.join(endOfLine),
  <span class="hljs-attr">install</span>: installTemplate.join(<span class="hljs-string">`,<span class="hljs-subst">$&#123;endOfLine&#125;</span>`</span>),
  <span class="hljs-attr">version</span>: process.env.VERSION || <span class="hljs-built_in">require</span>(<span class="hljs-string">'../package.json'</span>).version,
  <span class="hljs-attr">list</span>: listTemplate.join(<span class="hljs-string">`,<span class="hljs-subst">$&#123;endOfLine&#125;</span>`</span>)
&#125;);

<span class="hljs-comment">// 写入引用</span>
fs.writeFileSync(OUTPUT_PATH, template);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>最后渲染出来的文件大概是这样：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> WButton <span class="hljs-keyword">from</span> <span class="hljs-string">'w-button'</span>
<span class="hljs-keyword">const</span> components = [
    WButton
]
<span class="hljs-keyword">const</span> install = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Vue</span>) </span>&#123;
    components.map(<span class="hljs-function">(<span class="hljs-params">component</span>) =></span> &#123;
        Vue.component(component.name, component)
    &#125;)
&#125;
<span class="hljs-comment">/* istanbul ignore if */</span>
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span> && <span class="hljs-built_in">window</span>.Vue) &#123;
    install(<span class="hljs-built_in">window</span>.Vue)
&#125;
<span class="hljs-keyword">export</span> &#123;
    install,
    WButton
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个也是组件库的通用写法，所以这里的思想就是把发布到 npm 上的组件，进行聚合，聚合成一个组件包引用，我们在后台编辑的时候，是需要全量引入的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> W_UI <span class="hljs-keyword">from</span> <span class="hljs-string">'../../packages'</span>

Vue.use(W_UI)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们组件便注册完了，组件选择区，主要是提供组件的可选项，我们可以遍历组件，提供一个个 List 让用户选择，当然如果我们每个组件如果只提供一个组件名，用户可能并不知道组件长什么样，所以我们最好可以提供一下组件长什么样的缩略图。这里我们可以在组件发布的时候，也通过 node 脚本进行。这里要实现的代码比较多，我就大致说一下过程，因为也不是核心逻辑，可有可无，只能说有了体验上会好一点：</p>
<blockquote>
<p>1.用户启用 dev-server 进行代码编写测试</p>
<p>2.server 脚本使用 Chrome 工具 puppeteer，调整页面到手机端模式， 进行当前 dev-server 截图。</p>
<p>3.生成截图文件，上传到node服务，关联组件</p>
</blockquote>
<p>这样，就可以在加载组件选择区的时候，为组件附上缩略图。</p>
<h3 data-id="heading-6">组件预览区</h3>
<p>当用户在选择区选择了组件，我们需要展示在预览区域，那么我们怎么知道用户选择了哪些组件呢？总不能提前全部把组件写入渲染区域，通过v-if来判断选择吧？当然没有这么蠢，Vue 已经提供了动态组件的功能了：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> 
   <span class="hljs-attr">:class</span>=<span class="hljs-string">"[index===currentEditor ? 'active' : '']"</span> 
   <span class="hljs-attr">:is</span>=<span class="hljs-string">"select.name"</span> 
   <span class="hljs-attr">:data</span>=<span class="hljs-string">"select.data"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么我们不用缩略图代替真实组件？一方面生成的缩略图尺寸存在问题，另一方面，我们需要编辑的联动性，就是编辑区的编辑需要及时的反馈给用户。</p>
<h3 data-id="heading-7">额外的问题</h3>
<p>说了这么多，貌似一切都很顺利，但是这样在实践的时候，发现了存在一个明显的问题就是：我们中间的预览区域其实就是为了尽可能模拟移动端页面效果。但是如果我们加入了一些包含类似 <code>position: fixed</code> 样式的组件，会发现样式上就出现了明显的问题。典型的比如<code>Dialog Loading</code> 等。所以我们参考了 m-ui组件库的设计，将中间预览操作容器展示为一个iframe。将iframe大小调整为<code>375 * 667</code>，模拟 <code>iPhone 6</code> 的手机端。这样就不会存在样式问题了。可是这样又出现了另一个难点，那就是左侧的编辑数据如何及时的反应到<code>iframe</code>中？没错，就是<code>postMessgae</code>，大致思路如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e57d4c852fe4f918e9cdf1daf81d480~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
利用 <code>vuex</code> 做数据存储池，所有的变化，通过 <code>postMessgae</code>进行同步，这样我们只用确保数据池中的数据变化，便可以映射到渲染层的变化。比如，我们在预览区进行了组件选择和拖拽排序，那么我们只需通过<code>vuex</code>出发同步信息便可：😊</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// action.ts</span>
<span class="hljs-keyword">const</span> action = &#123;
  setCurrentPage (&#123;commit, state&#125;, <span class="hljs-attr">page</span>: number) &#123;
      <span class="hljs-comment">// 更新当前store</span>
      commit(<span class="hljs-string">'setCurrentPage'</span>,page)
      <span class="hljs-comment">// 对应postMessage</span>
      helper.postMsgToChild(&#123;<span class="hljs-attr">type</span>: <span class="hljs-string">'syncState'</span>, <span class="hljs-attr">value</span>: state&#125;)
    &#125;,
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">Template 模板的实现</h3>
<p>模板的设计实现，我参考了 <code>Vue-cli 2.x</code> 版本的思想，把这里的模板，存在了对应的 git 仓库中。当用户需要进行页面构建的时候，直接从 git 仓库中拉取对应的模板即可。当然拉取完，也会缓存一份在本地，以后渲染，直接从本地缓存中读取即可。我们现在把中心放在模板的格式和规范上。模板我们采用什么样的语法无所谓，这里我才用了和 <code>Vue-cli</code> 一样的Handlerbars 引擎。这里直接上我们模板的设计：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pg-index"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;backgroundColor: '&#123;&#123;bgColor&#125;&#125;'&#125;"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main-container"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;
        backgroundColor: '&#123;&#123;bgColor&#125;&#125;',
        backgroundImage: '&#123;&#123;bgImage&#125;&#125;' ? 'url(&#123;&#123;bgImage&#125;&#125;)' : null,
        backgroundSize: '&#123;&#123;bgSize&#125;&#125;',
        backgroundRepeat: 'no-repeat'
      &#125;"</span>></span>
        &#123;&#123;#components&#125;&#125;
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cp-module-editor &#123;&#123;className&#125;&#125; &#123;&#123;data.className&#125;&#125;"</span>></span>
            <&#123;&#123;name&#125;&#125; class="temp-component" :data="&#123;&#123;tostring data&#125;&#125;" data-type="&#123;&#123;upcasefirst name&#125;&#125;"></&#123;&#123;name&#125;&#125;>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        &#123;&#123;/components&#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
    </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">noRepeatCpsName</span>&#125;&#125;</span><span class="xml">
  import </span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">upcasefirst</span> this&#125;&#125;</span><span class="xml"> from '</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">this</span>&#125;&#125;</span><span class="xml">'
    </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">noRepeatCpsName</span>&#125;&#125;</span><span class="xml">
export default &#123;
  name: '</span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">upcasefirst</span> repoName&#125;&#125;</span><span class="xml">',
  components: &#123;
    </span><span class="hljs-template-tag">&#123;&#123;#<span class="hljs-name">noRepeatCpsName</span>&#125;&#125;</span><span class="xml">
      </span><span class="hljs-template-variable">&#123;&#123;<span class="hljs-name">upcasefirst</span> this&#125;&#125;</span><span class="xml">,
    </span><span class="hljs-template-tag">&#123;&#123;/<span class="hljs-name">noRepeatCpsName</span>&#125;&#125;</span><span class="xml">
  &#125;
&#125;
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>为了简化逻辑，我们把模板都设计成流式布局，所有组件一个个堆叠往下顺序排列。这个文件便是我们<code>vue-webpack-simple</code>的模板中的App.vue。我们对其进行了改写。这样在数据填充万，便可以渲染出一个 Vue 单文件。这里我只举着一个例子，我们还可以实现多页模板等等复杂的模板，根据需求拉取不同的模板即可。</p>
</blockquote>
<h3 data-id="heading-9">Node 渲染服务</h3>
<p>当后台提交渲染请求的时候，我们的 node 服务所做的工作主要是：</p>
<ul>
<li>拉取对应模板</li>
<li>渲染数据</li>
<li>编译</li>
</ul>
<p>拉取也就是去指定仓库中通过 <code>download-git-repo</code> 插件进行拉取模板。编译其实也就是通过 <code>metalsmith</code> 静态模板生成器把模板作为输入，数据作为填充，按照 <code>handlebars</code> 的语法进行规则渲染。最后产出 <code>build</code> 构建好的目录。在这一步，我们之前所需的组件，会被渲染进 package.json 文件。我们来看一下核心代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这里就像一个管道，以数据入口为生成源，通过renderTemplateFiles编译产出到目标目录</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">build</span>(<span class="hljs-params">data, temp_dest, source, dest, cb</span>) </span>&#123;
  <span class="hljs-keyword">let</span> metalsmith = Metalsmith(temp_dest)
    .use(renderTemplateFiles(data))
    .source(source)
    .destination(dest)
    .clean(<span class="hljs-literal">false</span>)

  <span class="hljs-keyword">return</span> metalsmith.build(<span class="hljs-function">(<span class="hljs-params">error, files</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (error) <span class="hljs-built_in">console</span>.log(error);
    <span class="hljs-keyword">let</span> f = <span class="hljs-built_in">Object</span>.keys(files)
      .filter(<span class="hljs-function"><span class="hljs-params">o</span> =></span> fs.existsSync(path.join(dest, o)))
      .map(<span class="hljs-function"><span class="hljs-params">o</span> =></span> path.join(dest, o))
    cb(error, f)
  &#125;)
&#125;


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderTemplateFiles</span>(<span class="hljs-params">data</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">files</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.keys(files).forEach(<span class="hljs-function">(<span class="hljs-params">fileName</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> file = files[fileName]
      <span class="hljs-comment">// 渲染方法</span>
      file.contents = Handlebars.compile(file.contents.toString())(data)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们得到的是一个 Vue 项目，此时还不能直接跑在浏览器端，这里就涉及到当前发布系统所支持的形式了。怎么说？如果你的公司发布系统需要在线编译，那么你可以把源文件直接上传到git仓库，触发仓库的 WebHook 让发布系统替你发掉这个项目即可。如果你们的发布系统是需要你编译后提交编译文件进行发布的，那么你可以通过 node 命令，进行本地构建，产出 HTML，CSS，JS。直接提交给发布系统即可。到这里，我们的任务就差不多了~具体的核心实心大多已经阐述清楚，如果实现当中有什么问题和不妥，也欢迎一起探讨交流！！</p>
<h3 data-id="heading-10">💬总结</h3>
<p>实现这样一套页面构建系统，其实我这里简化了很多东西，旨在给大家提供一种思路。另外，其实我们的页面全部在服务端构建的时候产出，我们可以再服务端这一层做很多工作，比如页面的性能优化，因为页面数据我们全部都有，我们也可以做页面的预渲染，骨架屏，ssr，编译时优化等等。而且我们也可以对产出的活动页做数据分析~有很多想象的空间。</p>
<h3 data-id="heading-11">热文推荐：</h3>
<ul>
<li><a href="https://juejin.cn/post/6976902669151518751" target="_blank" title="https://juejin.cn/post/6976902669151518751">95页字节跳动内部前端学习笔记，完整版开放下载</a></li>
<li><a href="https://juejin.cn/post/6974346715801321485" target="_blank" title="https://juejin.cn/post/6974346715801321485">《vue/vue3.0面试突击版》来啦！GitHub 上标星 35k，帮你成功上岸！</a></li>
<li><a href="https://juejin.cn/post/6971793002368876575" target="_blank" title="https://juejin.cn/post/6971793002368876575">自学总结：非科班转前端拿到字节跳动 offer？</a></li>
<li><a href="https://juejin.cn/post/6963636611649110023" target="_blank" title="https://juejin.cn/post/6963636611649110023">前端面试篇，没有项目经验怎么应对面试呢？全方面</a></li>
<li><a href="https://juejin.cn/post/6959049853003366430" target="_blank" title="https://juejin.cn/post/6959049853003366430">字节、百度我的前端春招面经（4轮技术面）</a></li>
</ul>
<blockquote>
<p><strong>📢欢迎点赞 👍  收藏 ⭐ 留言 📝 如有错误敬请指正！家人们记得三连哦</strong></p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/427a20dede6b43b0ba5a7cb97215d72d~tplv-k3u1fbpfcp-watermark.image" alt="7fa25d67gy1flunihsbgjg20a90acx6q.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            