
---
title: 'Quill富文本编辑器的实践 - DevUI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 07:36:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">引言</h1>
<p>富文本编辑器大概是最复杂、使用场景却极广的组件了。</p>
<p>可以说富文本编辑器让Web数据录入充满了无限的想象空间，如果只有文本框、下拉框这些纯文本的数据录入组件，那么Web的数据录入能力将极大地受限。我们将无法在网页上插入图片、视频这些富文本内容，更无法插入自定义的内容。</p>
<p>富文本编辑器让Web内容编辑变得更轻松、更高效，我们几乎可以在富文本编辑器中插入任何你想插入的内容，图片、视频、超链接、公式、代码块，都不在话下，甚至还可以插入表格、PPT、思维导图，甚至3D模型这种超复杂的自定义内容。</p>
<p>富文本编辑器的场景在Web上也是随处可见，写文章、写评论、意见反馈、录需求单，都需要使用到富文本。</p>
<p>本文结合DevUI团队在富文本组件中的实践，从使用场景、技术选型，再到对Quill的扩展，以及Quill的基本原理，跟大家分享Quill富文本编辑器的那些事儿。</p>
<p>本文主要由以下部分组成：</p>
<ol>
<li>富文本编辑器的使用场景</li>
<li>技术选型</li>
<li>我们为什么选择Quill</li>
<li>如何扩展Quill</li>
<li>Quill基本原理</li>
</ol>
<p>以下内容来自<code>Kagol</code>在<code>华为 HWEB 大前端技术分享会</code>上的演讲。</p>
<h1 data-id="heading-1">富文本编辑器的使用场景</h1>
<ul>
<li>博客文章</li>
<li>Wiki词条</li>
<li>工作项描述</li>
<li>测试用例步骤</li>
<li>反馈意见</li>
<li>评论</li>
<li>…</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34a2a27cfc6a48e59b6fc0a676d9de83~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e19cc1b4f2da4d2295ddf1cfb6f20784~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55d3fcb3feb44f25b263a0825ffdb0dd~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">技术选型</h1>
<p>我们的需求：</p>
<ul>
<li>开源协议友好</li>
<li>Angular框架或框架无关</li>
<li>灵活可扩展</li>
<li>支持插入/编辑表格和图片</li>
<li>插件丰富，生态好</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70e970928367413eb0bec664b725fd91~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c13d57ad02e4027a93fb4658920e2c6~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">选型分析</h2>
<ul>
<li>首先排除官方不维护的<code>UEditor</code></li>
<li>然后排除React框架专属的<code>Draft.js</code>和<code>Slate</code></li>
<li>接着排除开源协议不友好的<code>CKEditor</code></li>
<li>由于我们的业务场景丰富，需要富文本插入/编辑表格的功能，所以还需要排除不支持表格的<code>Trix</code>，弱支持表格的<code>Etherpad</code>和<code>Prosemirror</code>，以及表格功能收费的<code>TinyMCE</code></li>
<li>最后只剩下<code>Quill</code>和<code>wangEditor</code>两款编辑器可选，<code>wangEditor</code>的扩展性和生态不如<code>Quill</code>，所以最终选择<code>Quill</code>作为富文本组件的基座</li>
</ul>
<h1 data-id="heading-4">为什么选择Quill？</h1>
<ul>
<li>BSD协议，商业友好</li>
<li>文档详细，上手快</li>
<li>API驱动，扩展性好</li>
<li>插件丰富，生态好</li>
</ul>
<h2 data-id="heading-5">文档详细</h2>
<p>Document：<a href="https://quilljs.com/" target="_blank" rel="nofollow noopener noreferrer">quilljs.com/</a></p>
<p>介绍Quill的API：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91a03923913c4a0fb53ad67588b9a048~tplv-k3u1fbpfcp-watermark.image" alt="1622088667748.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>介绍如何扩展Quill：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eecd9f47b8e4c9596ca55cff440e0bf~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">上手快</h2>
<ul>
<li>安装Quill：<code>npm i quill</code></li>
<li>引入样式：<code>@import 'quill/dist/quill.snow.css';</code></li>
<li>引入Quill：<code>import Quill from 'quill';</code></li>
<li>初始化Quill：<code>new Quill('#editor', &#123; theme: 'snow' &#125;);</code></li>
</ul>
<p>效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9ffb0defad347f09a7f84edfe011b08~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">API驱动，扩展性好</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9da8c519326451fbcf2d24b1e3c1286~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35909772a3224889a5ee64ca06c2392e~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">插件丰富，生态好</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b74afb34ad84fd698da8ee3e6caa05e~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">扩展Quill</h1>
<h2 data-id="heading-10">插入标签</h2>
<p>比如我想在编辑器里插入标签</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6737dffa2c941af90b02d94e9c3094d~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">上传附件</h2>
<p>比如我想在编辑器里插入附件</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e2810bf57c24d9b9386d695a51b4ca4~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">插入表情</h2>
<p>比如我想在编辑器中插入表情</p>
<p>类似语雀的评论：<a href="https://www.yuque.com/yuque/blog/sguhed" target="_blank" rel="nofollow noopener noreferrer">www.yuque.com/yuque/blog/…</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfcd3e80f95b435ca98d21492303de06~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">个性分割线</h2>
<p>比如我想插入B站这种个性化的分割线</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/957845fac6cd40198c286a41a0537b41~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">超链接卡片</h2>
<p>比如我想插入知乎这样的超链接卡片</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0adcb87ed9ac4e98b6fc2fa34730c849~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">如何插入表情？</h2>
<p>我们从如何插入表情入手，一起看看怎么在Quill中插入自定义的内容。</p>
<p>要在Quill中插入表情，只需要以下四步：</p>
<ul>
<li>第一步：自定义工具栏按钮</li>
<li>第二步：自定义Blot内容EmojiBlot</li>
<li>第三步：在Quill注册EmojiBlot</li>
<li>第四步：调用Quill的API插入表情</li>
</ul>
<h3 data-id="heading-16">第一步：自定义工具栏按钮</h3>
<pre><code class="copyable">const quill = new Quill('#editor', &#123;
  theme: 'snow',
  modules: &#123;
    // 配置工具栏模块
    toolbar: &#123;
      container: [ …, [ 'emoji' ] ], // 增加一个按钮
      handlers: &#123;
        // 添加按钮的处理逻辑
        emoji() &#123;
          console.log('插入表情');
        &#125;
      &#125;
    &#125;,
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">给工具栏按钮增加图标</h3>
<pre><code class="copyable">// 扩展Quill内置的icons配置
const icons = Quill.import('ui/icons');
icons.emoji = ‘<svg>…</svg>’; // 图标的svg可以从iconfont网站复制
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bccd6c8751204c879a32482f0a95dd5e~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>工具栏上已经多了一个表情的按钮，并且能够响应鼠标点击事件，下一步就是要
编写插入表情的具体逻辑，这涉及到Quill的自定义内容相关的知识。</p>
<h3 data-id="heading-18">第二步：自定义Blot内容EmojiBlot</h3>
<p>Quill中的Blot就是一个普通的ES6 Class，由于表情和图片的差别就在于：</p>
<p>Quill内置的图片格式不支持自定义宽高，而我们要插入的表情是需要特定的宽高的。</p>
<p>因此我们可以基于Quill内置的image格式来扩展。</p>
<p>emoji.ts</p>
<pre><code class="copyable">import Quill from 'quill';

const ImageBlot = Quill.import('formats/image');

// 扩展Quill内置的image格式
class EmojiBlot extends ImageBlot &#123;
  static blotName = 'emoji'; // 定义自定义Blot的名字（必须全局唯一）
  static tagName = 'img'; // 自定义内容的标签名

  // 创建自定义内容的DOM节点
  static create(value): any &#123;
    const node = super.create(value);
    node.setAttribute('src', ImageBlot.sanitize(value.url));
    if (value.width !== undefined) &#123;
      node.setAttribute('width', value.width);
    &#125;
    if (value.height !== undefined) &#123;
      node.setAttribute('height', value.height);
    &#125;
    return node;
  &#125;
  
  // 返回options数据
  static value(node): any &#123;
    return &#123;
      url: node.getAttribute('src'),
      width: node.getAttribute('width'),
      height: node.getAttribute('height')
    &#125;;
  &#125;
&#125;

export default EmojiBlot;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">第三步：在Quill注册EmojiBlot</h3>
<p>有了EmojiBlot，要将其插入Quill编辑器中，还需要将这个ES6类注册到Quill中。</p>
<pre><code class="copyable">import EmojiBlot from './formats/emoji';
Quill.register('formats/emoji', EmojiBlot);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">第四步：调用Quill的API插入表情</h3>
<p>EmojiBlot注册到Quill中之后，Quill就能认识它了，也就可以调用Quill的API将其插入到编辑器中。</p>
<pre><code class="copyable">emoji(): void &#123;
  console.log(‘插入表情');
  // 获取当前光标位置
  const index = this.quill.getSelection().index;
  // 在当前光标处插入emoji（blotName）
  this.quill.insertEmbed(index, 'emoji', &#123;
    url: 'assets/emoji/good.png',
    width: '64px',
  &#125;);
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">效果图</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb01c393dcb4e38b1b7e75b1666055a~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-22">Demo源码</h2>
<p>源码链接：<a href="https://gitee.com/kagol/quill-demo" target="_blank" rel="nofollow noopener noreferrer">gitee.com/kagol/quill…</a></p>
<p>也欢迎关注我们DevUI组件库的官网，了解更多有趣又实用的开源组件！</p>
<p>DevUI官网：<a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">devui.design</a></p>
<h1 data-id="heading-23">Quill基本原理</h1>
<p>最后讲一讲Quill的基本原理。</p>
<h2 data-id="heading-24">基本原理</h2>
<ul>
<li>使用Delta数据模型描述富文本内容及其变化，以保证行为的可预测</li>
<li>通过Parchment对DOM进行抽象，以保证平台一致性</li>
<li>通过Mutation Observe监听DOM节点的变化，将DOM的更改同步到Delta数据模型中</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b77e8c6413e442c858e4ddb8c8b216f~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-25">Quill如何表达编辑器内容？</h2>
<h3 data-id="heading-26">Delta数据模型</h3>
<p>通过Delta数据模型来描述富文本内容及其变化</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67da39337d6947a5a28df3f9dbe5280e~tplv-k3u1fbpfcp-watermark.image" alt="19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Delta 是JSON的一个子集，只包含一个 ops 属性，它的值是一个对象数组，每个数组项代表对编辑器的一个操作（以编辑器初始状态为空为基准）。</p>
<pre><code class="copyable">&#123;
  "ops": [
    &#123; "insert": "Hello " &#125;,
    &#123; "insert": "World", "attributes": &#123; "bold": true &#125; &#125;,
    &#123; "insert": "\n" &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">修改编辑器内容</h3>
<p>比如我们把加粗的"World"改成红色的文字"World"，这个动作用 Delta 描述如下：</p>
<pre><code class="copyable">&#123;
  "ops": [
    &#123; "retain": 6 &#125;,
    &#123; "retain": 5, "attributes": &#123; "color": "#ff0000" &#125; &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>意思是：保留编辑器最前面的6个字符，即保留"Hello "不动，保留之后的5个字符"World"，并将这些字符设置为字体颜色为"#ff0000"。</p>
<h3 data-id="heading-28">删除编辑器内容</h3>
<p>如果要删除"World"呢？</p>
<pre><code class="copyable">&#123;
  "ops": [
    &#123; "retain": 6 &#125;,
    &#123; "delete": 5 &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即：保留前面6个字符（’Hello ’），删除之后的5个字符（’World’）</p>
<h2 data-id="heading-29">Quill如何渲染内容？</h2>
<p>渲染富文本内容的基本原理：
遍历Delta数组，将其中描述的内容一个一个应用（插入/格式化/删除）到编辑器中。</p>
<p>详情可参考DevUI专栏文章：</p>
<p><a href="https://juejin.cn/post/6844904145145741326" target="_blank">《Quill的内容渲染机制》</a></p>
<h2 data-id="heading-30">Quill如何扩展编辑器的能力？</h2>
<p>扩展Quill的方式：</p>
<ul>
<li>通过自定义Blot格式来扩展编辑器的内容</li>
<li>通过自定义模块来扩展编辑器的功能</li>
</ul>
<p>详情可参考DevUI专栏文章：</p>
<p><a href="https://juejin.cn/post/6844904073620094990" target="_blank">《现代富文本编辑器Quill的模块化机制》</a></p>
<p>THANK YOU！</p></div>  
</div>
            