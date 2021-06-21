
---
title: 'Quill基本使用和配置 - DevUI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 15:34:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下文章和本文相关，也许你也会喜欢：</p>
<p><a href="https://juejin.cn/post/6844904073620094990" target="_blank">《现代富文本编辑器Quill的模块化机制》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p>
<p><a href="https://juejin.cn/post/6844904145145741326" target="_blank">《现代富文本编辑器Quill的内容渲染机制》</a></p>
<h1 data-id="heading-0">引言</h1>
<p>之前在HWEB大前端技术分享会上给大家分享过 <a href="https://juejin.cn/post/6966993945973194765" target="_blank">Quill 的一些实践</a>，不过由于时间关系只讲了个大概，后续打算深入浅出地对 Quill 做一个详细的介绍。</p>
<p>这个系列打算从实践的角度去讲 Quill 富文本编辑器，先从 Quill 的基本使用开始吧！</p>
<h1 data-id="heading-1">极简方式使用 Quill</h1>
<p>快速开始三部曲：</p>
<ul>
<li>安装</li>
<li>引入</li>
<li>使用</li>
</ul>
<pre><code class="copyable">// 安装
npm i quill
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><div id="editor"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 引入
import Quill from 'quill';

// 使用
const quill = new Quill('#editor');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然我们已经初始化了 Quill 实例，但是在页面中却什么也看不到。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5b777a31c864e689acca905fd2c72d5~tplv-k3u1fbpfcp-watermark.image" alt="极简Quill.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然看上去什么也没有，但是我们点击空白处，会发现有一个光标，并且可以输入内容，并给内容增加格式（由于没有工具栏，只能通过 Quill 快捷键<code>Ctrl+B</code>增加格式），以下是动画效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7ea853563b04012b4072c928611344a~tplv-k3u1fbpfcp-watermark.image" alt="快速开始.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然只是一个极简版的富文本编辑器，不过加上边框和按钮，就是一个基础版的掘金评论框（还差插入表情和图片）😜</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd6fd2a04fe04a5b981ee77a35f328d7~tplv-k3u1fbpfcp-watermark.image" alt="基础版掘金评论框.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是使用 Quill 最简单的方式。</p>
<h1 data-id="heading-2">加一些配置选项吧</h1>
<h2 data-id="heading-3">配置编辑器容器元素 container</h2>
<p>Quill 类一共有两个参数，第一个参数是必选的编辑器容器元素<code>container</code>，可以是一个CSS选择器，比如前面的<code>#editor</code>，也可以是一个DOM元素，比如：</p>
<pre><code class="copyable">const container = document.getElementById('editor');
// const container = document.querySelector('#editor');
// const container = $('#editor').get(0);
const quill = new Quill(container);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果容器里面已经有一些 HTML 元素，那么初始化 Quill 的时候，那些元素也会渲染出来，比如：</p>
<pre><code class="copyable"><div id="editor">
  <p>DevUI：面向企业中后台的前端开源解决方案</p>
  <h2>宗旨与法则</h2>
  <p>规范的组件化的目的不是为了限制创造，而是为了创造者更确定、科学、高效。所有行为决策的价值归依是产品业务。产品业务永远比组件化本身更重要，业务第一。</p>
  <p>规范不是绝对、教条、冷漠、强制的，实际工作中总会有新增需求、存优化空间、情感化设计需求超出一般通用规范。保持克制的同时，允许基于强烈业务需求的规范突破；之后如果有足够的理由迭代出组件，那么就进行组件深化。</p>
  <h2>设计语言</h2>
  <p>DevUI的价值观奠定了 DevCloud品牌的基础。它是 DevCloud 的设计师们思考、工作的产物，反映了 DevCloud 的产品文化、设计理念和对客户的承诺。DevUI的这些价值观贯穿于所有产品和面向客户的沟通和内容中。同时，它是 DevUI 设计原则的源头，为具体的设计方法提供启发和指引。</p>
  <p>DevUI倡导<code>沉浸</code>、<code>灵活</code>、<code>致简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。</p>
  <h2>致简</h2>
  <p>DevUI坚持以用户为中心去进行设计，注重直观可达性，把服务示例化以帮助用户快速融入到使用中去。同时， DevUI提供大量的快捷键，简化使用的流程、提高操作效率。</p>
  <h2>沉浸</h2>
  <p>DevUI的沉浸式体验包括人的感官体验和认知体验，当用户的个人技能与面对的挑战互相匹配，并且长时间处在稳定状态时，用户达到心流状态并且不易被外界因素所干扰。</p>
  <p>在产品设计中，DevUI专注在降低用户在完成任务目标时的认知阻力中。为此，DevUI同时提供多种不同的切换页面的途径，包括面包屑、快捷键、按钮和链接等，方便用户随时快速、连续地切换页面，到达自己所需的页面，使用户处于流畅的体验中，减轻寻找信息的焦虑感。</p>
  <h2>灵活</h2>
  <p>DevUI提供超过60个独立原子级组件，可以自由组合，像搭积木一样，用小组件搭建出符合自身产品需要的分子级组件，进而搭建出自己的业务系统。</p>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染出来的编辑器效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/942041b440f24567b6ab3c08831d6961~tplv-k3u1fbpfcp-watermark.image" alt="渲染初始HTML.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">配置选项 options</h2>
<p>第二个参数是可选的配置选项<code>options</code>，options是一个JSON对象，比如我们想给我们的编辑器增加一个主题，使它不再那么单调。</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow'
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外需要引入该主题对应的样式：</p>
<pre><code class="copyable">@import 'quill/dist/quill.snow.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们看到编辑器已经有一个工具栏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ebd136c701460195f8048bbee25036~tplv-k3u1fbpfcp-watermark.image" alt="snow主题.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且可以通过工具栏对编辑器的内容进行操作，比如给<code>DevUI</code>增加一个超链接：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/148df13ff4a040c2adbab515916a76a3~tplv-k3u1fbpfcp-watermark.image" alt="配置snow主题.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了<code>snow</code>主题，Quill 还内置了一个<code>bubble</code>气泡主题，配置方式和<code>snow</code>主题一样：</p>
<ul>
<li>引入主题样式</li>
<li>在options里配置主题</li>
</ul>
<pre><code class="copyable">// 引入bubble主题样式
@import 'quill/dist/quill.bubble.css';
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'bubble' // 配置 bubble 主题
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f9a8b3520dd4cebb9b97f4954798cef~tplv-k3u1fbpfcp-watermark.image" alt="bubble主题.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>bubble主题没有显性的工具栏，它会在你选中编辑器中的文本时，在选中文本的下方显示一个气泡工具栏，从而对文本进行格式化操作，比如给选中的段落增加引用格式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf8b5bb2961b4da8b9be24d9accd69c8~tplv-k3u1fbpfcp-watermark.image" alt="bubble主题.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">更多配置选项</h1>
<p>Quill 不仅仅可以配置主题，options一共支持8个配置选项：</p>
<ul>
<li>bounds 编辑器内浮框的边界</li>
<li>debug debug级别</li>
<li>formats 格式白名单</li>
<li>modules 模块</li>
<li>placeholder 占位文本</li>
<li>readOnly 只读模式</li>
<li>scrollingContainer 滚动容器</li>
<li>theme 主题</li>
</ul>
<h2 data-id="heading-6">formats 格式白名单</h2>
<p>这个配置项非常有用，比如刚刚提到的掘金评论框，我们发现评论框里只能插入纯文本，其他格式都不允许，即使时粘贴进来的格式化文本也会变成纯文本。</p>
<p>在 Quill 里很容易实现，只需要配置<code>formats</code>为空数组即可。</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  formats: []
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里的<code>formats</code>格式白名单，控制的是内容实际的格式，和设置格式的渠道无关，比如<code>formats</code>设置为空，那么无论是：</p>
<ul>
<li>通过工具栏设置格式</li>
<li>还是通过快捷键（比如<code>Ctrl+B</code>）设置格式</li>
<li>抑或是粘贴带格式的文本</li>
</ul>
<p>都是无法设置格式的。</p>
<p>如果我们想保留一部分格式，比如只保留<code>粗体</code>和<code>列表</code>两种格式：</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  formats: [ 'bold', 'list' ]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Quill 一共支持<code>11</code>种行内格式：</p>
<ul>
<li>background</li>
<li>bold</li>
<li>color</li>
<li>font</li>
<li>code</li>
<li>italic</li>
<li>link</li>
<li>size</li>
<li>strike</li>
<li>script</li>
<li>underline</li>
</ul>
<p><code>7</code>种块级格式：</p>
<ul>
<li>blockquote</li>
<li>header</li>
<li>indent</li>
<li>list</li>
<li>align</li>
<li>direction</li>
<li>code-block</li>
</ul>
<p><code>3</code>种嵌入格式：</p>
<ul>
<li>formula</li>
<li>image</li>
<li>video</li>
</ul>
<p>不配置<code>formats</code>选项，会默认支持所有的<code>21</code>种格式。</p>
<h2 data-id="heading-7">placeholder 占位文本</h2>
<p>我们发现掘金的评论框在没有输入内容时，会有一个<code>输入评论...</code>的占位文本。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be448f34fc24aa593b410431b38330d~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这可以很容易地通过配置<code>placeholder</code>选项实现。</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  formats: [],
  placeholder: '输入评论...',
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b903796469984ef99f8ae2d1277a2bcd~tplv-k3u1fbpfcp-watermark.image" alt="placeholder.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">readOnly 只读模式</h2>
<p>通过配置<code>readOnly</code>可以实现：</p>
<blockquote>
<p>初始状态编辑器是阅读态，不可以编辑，可以通过点击<code>编辑</code>按钮让编辑器变成编辑态。</p>
</blockquote>
<p>由于掘金的评论框不支持编辑，就不拿它举例子。</p>
<p>以 <a href="https://www.huaweicloud.com/devcloud/" target="_blank" rel="nofollow noopener noreferrer">DevCloud</a> 看板项目的评论框为例，初始状态下评论是不可编辑的，点击<code>编辑</code>按钮，变成可编辑状态，并且显示工具栏、保存按钮等元素，点击保存按钮，新增的内容被保存，编辑器变成只读态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72743b1bc50f4e4c8e2473df4d37c40b~tplv-k3u1fbpfcp-watermark.image" alt="readOnly.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">modules 模块配置</h2>
<p>这个配置项放在最后并不代表它不重要，恰恰相反，这是 Quill 中<code>最重量级</code>也是<code>最常用</code>的配置。</p>
<p>在之前的文章中，给大家介绍过 <a href="https://juejin.cn/post/6844904073620094990" target="_blank">Quill 的模块化机制</a>，这个配置项就是用来配置 Quill 的模块的。</p>
<p>在<a href="https://juejin.cn/post/6844904073620094990" target="_blank">Quill的模块化机制</a>一文中，我们提到</p>
<p>Quill 一共有6个内置模块：</p>
<ul>
<li>Clipboard 粘贴版</li>
<li>History 操作历史</li>
<li>Keyboard 键盘事件</li>
<li>Syntax 语法高亮</li>
<li>Toolbar 工具栏</li>
<li>Uploader 文件上传</li>
</ul>
<p>每个模块的用途详见<a href="https://juejin.cn/post/6844904073620094990#heading-3" target="_blank">Quill内置模块</a>章节。</p>
<p><code>modules</code>选项可以用来配置这些模块。</p>
<h3 data-id="heading-10">配置 toolbar 模块</h3>
<p>Quill 默认只在工具栏中显示一部分格式化按钮，里面没有插入图片的按钮，我们可以通过配置<code>toolbar</code>模块来增加。</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  modules: &#123;
    toolbar: [
      // 默认的
      [&#123; header: [1, 2, 3, false] &#125;],
      ['bold', 'italic', 'underline', 'link'],
      [&#123; list: 'ordered'&#125;, &#123; list: 'bullet' &#125;],
      ['clean'],
      
       // 新增的
      ['image']
    ]
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9077626cc9b447c851662c69babaa73~tplv-k3u1fbpfcp-watermark.image" alt="插入图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想做一个掘金这样的富文本编辑器，也非常简单。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a870552642b84c06be4dc761fe2f8bbd~tplv-k3u1fbpfcp-watermark.image" alt="掘金富文本.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>掘金的富文本编辑器主要包含以下工具栏按钮：</p>
<ul>
<li>加粗</li>
<li>斜体</li>
<li>下划线</li>
<li>一级/二级标题</li>
<li>引用</li>
<li>代码块</li>
<li>行内代码</li>
<li>无序列表</li>
<li>有序列表</li>
<li>超链接</li>
<li>插入图片</li>
</ul>
<p>使用 Quill 实现，需要这样配置<code>toolbar</code>模块。</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  modules: &#123;
    toolbar: [
      'bold', 'italic', 'underline', 
      &#123; header: 1 &#125;, &#123; header: 2 &#125;,
      'blockquote', 'code-block', 'code', 'link',
      &#123; list: 'ordered'&#125;, &#123; list: 'bullet' &#125;,
      'image',
    ]
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍微修改下样式，就能做出一个和掘金富文本编辑器差不多的富文本编辑器啦，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab209110c32b45c1964a272529d73b66~tplv-k3u1fbpfcp-watermark.image" alt="掘金编辑器效果.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是和掘金实际的富文本编辑器的对比图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d053e81616824172984c582f256f6b5f~tplv-k3u1fbpfcp-watermark.image" alt="对比图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对比以上效果对比图，除了工具栏的 icon 使用的是掘金 Markdown 编辑器的 icon 之外，其他几乎是一样的。</p>
<h3 data-id="heading-11">配置 keyboard 模块</h3>
<p>除了工具栏模块，我们还可以配置别的模块，比如快捷键模块<code>keyboard</code>，<code>keyboard</code>模块默认支持很多快捷键，比如：</p>
<ul>
<li>加粗的快捷键是<code>Ctrl+B</code>；</li>
<li>超链接的快捷键是<code>Ctrl+K</code>;</li>
<li>撤销/回退的快捷键是<code>Ctrl+Z/Y</code>。</li>
</ul>
<p>但它不支持删除线的快捷键，如果我们想定制删除线的快捷键，假设是<code>Ctrl+Shift+S</code>，可以这样配置：</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  modules: &#123;
    toolbar: [
      // 默认的
      [&#123; header: [1, 2, 3, false] &#125;],
      ['bold', 'italic', 'underline', 'link'],
      [&#123; list: 'ordered'&#125;, &#123; list: 'bullet' &#125;],
      ['clean'],
      ['image']
    ],
    
    // 新增的
    keyboard: &#123;
      bindings: &#123;
        strike: &#123;
          key: 'S',
          ctrlKey: true,
          shiftKey: true,
          handler: function(range, context) &#123;
            // 获取当前光标所在文本的格式
            const format = this.quill.getFormat(range);
            // 增加/取消删除线
            this.quill.format('strike', !format.strike);
          &#125;
        &#125;,
      &#125;
    &#125;,
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">配置 history 模块</h3>
<p>Quill 内置的<code>history</code>模块，每隔<code>1s</code>会记录一次操作历史，并放入历史操作栈（最大100）中，便于撤销/回退操作。</p>
<p>如果我们不想记录得那么频繁，想<code>2s</code>记录一次，另外我们想增加操作栈的大小，最大记录200次操作历史，可以这样配置：</p>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  modules: &#123;
    toolbar: [
      // 默认的
      [&#123; header: [1, 2, 3, false] &#125;],
      ['bold', 'italic', 'underline', 'link'],
      [&#123; list: 'ordered'&#125;, &#123; list: 'bullet' &#125;],
      ['clean'],
      ['image']
    ],
    keyboard: &#123;
      bindings: &#123;
        strike: &#123;
          key: 'S',
          ctrlKey: true,
          shiftKey: true,
          handler: function(range, context) &#123;
            // 获取当前光标所在文本的格式
            const format = this.quill.getFormat(range);
            // 增加/取消删除线
            this.quill.format('strike', !format.strike);
          &#125;
        &#125;,
      &#125;
    &#125;,
    
    // 新增的
    history: &#123;
      delay: 2000, // 2s记录一次操作历史
      maxStack: 200, // 最大记录200次操作历史
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">小结</h1>
<p>本文主要介绍了 Quill 的基本用法，以及如何通过 options 选项配置 Quill。</p>
<p>后续将介绍更多关于 Quill 的实践，关注 DevUI 不迷路🦌。</p>
<p>欢迎加DevUI小助手微信：devui-official，一起讨论Angular技术和前端技术。</p>
<p>欢迎关注我们<a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://github.com/devcloudfe/ng-devui" target="_blank" rel="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://devui.design/admin/" target="_blank" rel="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-14">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6973792387231383566" target="_blank">《Angular Schematics在DevUI Admin中的实践》</a></p>
<p><a href="https://juejin.cn/post/6844904073620094990" target="_blank">《现代富文本编辑器Quill的模块化机制》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p></div>  
</div>
            