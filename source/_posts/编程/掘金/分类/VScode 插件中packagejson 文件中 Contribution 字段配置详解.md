
---
title: 'VScode 插件中package.json 文件中 Contribution 字段配置详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ec12945830b435d8daa38d0b26c2f9d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 05:25:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ec12945830b435d8daa38d0b26c2f9d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><a href="https://code.visualstudio.com/api/references/contribution-points" target="_blank" rel="nofollow noopener noreferrer"><code>Contributes Points</code></a></h3>
<blockquote>
<p><code>contributes points</code> 是在 <code>package.json</code> 中的一组 <code>JSON</code> 声明</p>
</blockquote>
<ul>
<li><code>configuration</code>：设置</li>
<li><code>configurationDefaults</code></li>
<li><code>commands</code>：命令</li>
<li><code>menus</code>：菜单</li>
<li><code>keybindings</code>：快捷键绑定</li>
<li><code>languages</code>：语言支持</li>
<li><code>debuggers</code>：调试</li>
<li><code>breakpoints</code>：断点</li>
<li><code>grammars</code>：</li>
<li><code>themes</code>：主题</li>
<li><code>iconThemes</code>：图标主题</li>
<li><code>productIconThemes</code>：</li>
<li><code>snippets</code>：代码片段</li>
<li><code>jsonValidation</code>：自定义 <code>JSON</code> 校验</li>
<li><code>views</code>：左侧侧边栏视图</li>
<li><code>viewsWelcome</code>：</li>
<li><code>viewsContainers</code>：自定义 <code>activitybar</code></li>
<li><code>walkthroughs</code></li>
<li><code>problemMatchers</code></li>
<li><code>problemPatterns</code></li>
<li><code>taskDefinitions</code></li>
<li><code>colors</code></li>
<li><code>typescriptServerPlugins</code></li>
<li><code>resourceLabelFormatters</code></li>
<li><code>customEditors</code></li>
</ul>
<h4 data-id="heading-1">1、<code>configuration</code></h4>
<p>配置</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"configuration"</span>: &#123;
      <span class="hljs-attr">"title"</span>: <span class="hljs-string">"TypeScript"</span>,
      <span class="hljs-attr">"properties"</span>: &#123;
        <span class="hljs-attr">"typescript.useCodeSnippetsOnMethodSuggest"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"boolean"</span>,
          <span class="hljs-attr">"default"</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Complete functions with their parameter signature."</span>
        &#125;,
        <span class="hljs-attr">"typescript.tsdk"</span>: &#123;
          <span class="hljs-attr">"type"</span>: [<span class="hljs-string">"string"</span>, <span class="hljs-string">"null"</span>],
          <span class="hljs-attr">"default"</span>: <span class="hljs-literal">null</span>,
          <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Specifies the folder path containing the tsserver and lib*.d.ts files to use."</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用 <code>vscode.workspace.getConfiguration('myExtension')</code> 从插件中读取这些值。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ec12945830b435d8daa38d0b26c2f9d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">1. <code>title</code></h5>
<p>标题</p>
<p>标题应该是您的插件的确切名称。</p>
<ul>
<li>✅ <code>"title": "GitMagic"</code></li>
<li>❌ <code>"title": "GitMagic Extension"</code></li>
<li>❌ <code>"title": "GitMagic Configuration"</code></li>
<li>❌ <code>"title": "GitMagic Extension Configuration Settings"</code></li>
</ul>
<h5 data-id="heading-3">2. <code>properties</code></h5>
<p>属性</p>
<p>配置的 <code>key</code> 将用于命名空间和构造标题。<code>key</code> 的大写字母用于表示分词。</p>
<p>例如，如果您的 <code>key</code> 是 <code>gitMagic.blame.dateFormat</code>，则为该设置生成的标题将如下所示：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Blame: Date Format
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会将根据 <code>key</code> 中建立层次结构进行分组。</p>
<p>例如：</p>
<pre><code class="hljs language-shell copyable" lang="shell">gitMagic.blame.dateFormat
gitMagic.blame.format
gitMagic.blame.heatMap.enabled
gitMagic.blame.heatMap.location
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将会出现在一个组中，如：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Blame: Date Format
Blame: Format
Blame › Heatmap: Enabled
Blame › Heatmap: Location
<span class="copy-code-btn">复制代码</span></code></pre>
<p>否则，属性按照字母顺序出现</p>
<h6 data-id="heading-4">1. description / markdownDescription</h6>
<p>描述</p>
<p>描述出现在标题之后和输入字段之前，布尔值除外，其中描述用作复选框的标签。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"gitMagic.blame.heatmap.enabled"</span>: &#123;
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Specifies whether to provide a heatmap indicator in the gutter blame annotations"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您使用 <code>markdownDescription</code> 而不是 <code>description</code>，您的设置描述将在 <code>settings UI</code> 中呈现为 <code>Markdown</code> 模式。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"gitMagic.blame.dateFormat"</span>: &#123;
    <span class="hljs-attr">"markdownDescription"</span>: <span class="hljs-string">"Specifies how to format absolute dates (e.g. using the `$&#123;date&#125;` token) in gutter blame annotations. See the [Moment.js docs](https://momentjs.com/docs/#/displaying/format/) for valid formats"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">2. <code>type</code></h6>
<p>类型：[<code>number</code>, <code>string</code>, <code>boolean</code>, <code>object</code>, <code>array</code>, ...]</p>
<p><code>number</code>、<code>string</code>、<code>boolean</code> 可以直接在 <code>settings UI</code> 中编辑，<code>boolean</code> 将会作为复选框的标签</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"gitMagic.views.pageItemLimit"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"number"</span>,
    <span class="hljs-attr">"default"</span>: <span class="hljs-number">20</span>,
    <span class="hljs-attr">"markdownDescription"</span>: <span class="hljs-string">"Specifies the number of items to show in each page when paginating a view list. Use 0 to specify no limit"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"gitMagic.blame.compact"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"boolean"</span>,
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Specifies whether to compact (deduplicate) matching adjacent gutter blame annotations"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>object</code>、<code>array</code> 等不能在 <code>settings UI</code> 中展示，只能在 <code>JSON</code> 进行修改。</p>
<h6 data-id="heading-6">3. <code>enum</code> / <code>enumDescriptions</code> / <code>markdownEnumDescriptions</code></h6>
<p><code>enum</code>：枚举：如果提供一个数组，则会展示下拉选项
<code>enumDescriptions</code>：枚举描述
<code>markdownEnumDescriptions</code>：将呈现为 <code>markdown</code> 模式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d043d06f6eb341e1a2c02e287062654e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"gitMagic.blame.heatmap.location"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
    <span class="hljs-attr">"default"</span>: <span class="hljs-string">"right"</span>,
    <span class="hljs-attr">"enum"</span>: [<span class="hljs-string">"left"</span>, <span class="hljs-string">"right"</span>],
    <span class="hljs-attr">"enumDescriptions"</span>: [
      <span class="hljs-string">"Adds a heatmap indicator on the left edge of the gutter blame annotations"</span>,
      <span class="hljs-string">"Adds a heatmap indicator on the right edge of the gutter blame annotations"</span>
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">4. <code>deprecationMessage</code> / <code>markdownDeprecationMessage</code></h6>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"json.colorDecorators.enable"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"boolean"</span>,
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Enables or disables color decorators"</span>,
    <span class="hljs-attr">"markdownDeprecationMessage"</span>: <span class="hljs-string">"**Deprecated**: Please use `#editor.colorDecorators#` instead."</span>,
    <span class="hljs-attr">"deprecationMessage"</span>: <span class="hljs-string">"Deprecated: Please use editor.colorDecorators instead."</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">5. <code>default</code></h6>
<p>定义属性的默认值</p>
<h6 data-id="heading-9">6. <code>minimum</code> / <code>maximum</code></h6>
<p>限制数值的最大值和最小值</p>
<h6 data-id="heading-10">7. <code>maxLength</code> / <code>minLength</code></h6>
<p>限制字符串长度</p>
<h6 data-id="heading-11">8. <code>pattern</code></h6>
<p>使用正则限制字符串</p>
<h6 data-id="heading-12">9. <code>format</code></h6>
<p>限制字符串的格式：<code>date</code>、<code>time</code>、<code>ipv4</code>、<code>email</code>、<code>uri</code></p>
<h6 data-id="heading-13">10. <code>maxItems</code> / <code>minItems</code></h6>
<p>限制数组长度</p>
<h6 data-id="heading-14">11. <code>scope</code></h6>
<p>范围</p>
<p>属性值：</p>
<ul>
<li><code>application</code>：适用于所有 <code>VScode</code> 实例的设置，只能在用户设置中设置</li>
<li><code>machine</code>：在用户或远程设置中设置的机器特定设置</li>
<li><code>machine-overridable</code>：可以被工作区或者文件夹设置的机器特定设置</li>
<li><code>window</code>：可以在用户、工作区或远程设置中配置的 <code>windows</code> 特定设置</li>
<li><code>resource</code>：适用于文件和文件夹的资源设置，可以在所有设置级别进行设置，甚至文件夹设置</li>
<li><code>language-overridable</code>：可以在语言级别覆盖的资源设置</li>
</ul>
<p>如果未声明范围，则默认为窗口。</p>
<h6 data-id="heading-15">12. <code>Linking to settings</code></h6>
<p>指向另一个设置的链接</p>
<p>在 <code>markdown</code> 类型属性中使用以下特殊语法：<code>#target.setting.id#</code>。这将适用于 <code>markdownDescription</code>、<code>markdownEnumDescriptions</code> 和 <code>markdownDeprecationMessage</code>。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"files.autoSaveDelay"</span>: &#123;
    <span class="hljs-attr">"markdownDescription"</span>: <span class="hljs-string">"Controls the delay in ms after which a dirty editor is saved automatically. Only applies when `#files.autoSave#` is set to `afterDelay`."</span>,
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>settings UI</code> 界面展示为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ab420cec04641fd9e593bc7cc22fe74~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">2、<code>configurationDefaults</code></h4>
<p>默认配置</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"configurationDefaults"</span>: &#123;
      <span class="hljs-attr">"[markdown]"</span>: &#123;
        <span class="hljs-attr">"editor.wordWrap"</span>: <span class="hljs-string">"on"</span>,
        <span class="hljs-attr">"editor.quickSuggestions"</span>: <span class="hljs-literal">false</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">3、<code>commands</code></h4>
<p>命令</p>
<p>由 <code>title</code>、<code>icon</code>（可选）、<code>category</code>、<code>command</code> 命令组成。默认情况下，命令显示在命令面板 (<code>⇧⌘P</code>) 中，但它们也可以显示在其他菜单中。</p>
<blockquote>
<p>当调用命令时，VS Code 将发出 activationEvent onCommand:$&#123;command&#125;</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"commands"</span>: [
      &#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"extension.sayHello"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Hello World"</span>,
        <span class="hljs-attr">"category"</span>: <span class="hljs-string">"Hello"</span>,
        <span class="hljs-attr">"icon"</span>: &#123;
          <span class="hljs-attr">"light"</span>: <span class="hljs-string">"path/to/light/icon.svg"</span>,
          <span class="hljs-attr">"dark"</span>: <span class="hljs-string">"path/to/dark/icon.svg"</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>command</code> <code>icon</code> 的规格</p>
<ul>
<li>尺寸：图标应为 16x16，内边距为 1 像素（图像为 14x14）并居中。</li>
<li>颜色：图标应使用单一颜色。</li>
<li>格式：建议图标为 SVG，但可以接受任何图像文件类型。</li>
</ul>
<h4 data-id="heading-18">4、<code>menus</code></h4>
<p>菜单项</p>
<h5 data-id="heading-19">1. 可以选择的拓展项</h5>
<ul>
<li>全局命令面板 - <code>commandPalette</code></li>
<li>资源管理器上下文菜单 - <code>explorer/context</code></li>
<li>编辑器上下文菜单 - <code>editor/context</code></li>
<li>编辑器标题菜单栏 - <code>editor/title</code></li>
<li>编辑器标题上下文菜单 - <code>editor/title/context</code></li>
<li>调试调用堆栈视图上下文菜单 - <code>debug/callstack/context</code></li>
<li>调试调用堆栈视图内联操作 - <code>debug/callstack/context group inline</code></li>
<li>调试变量视图上下文菜单 - <code>debug/variables/context</code></li>
<li>调试工具栏 - <code>debug/toolbar</code></li>
<li><code>SCM</code> 标题菜单 - <code>scm/title</code></li>
<li><code>SCM</code> 资源组菜单 - <code>scm/resourceGroup/context</code></li>
<li><code>SCM</code> 资源文件夹菜单 - <code>scm/resourceFolder/context</code></li>
<li><code>SCM</code> 资源菜单 - <code>scm/resourceState/context</code></li>
<li><code>SCM</code> 更改标题菜单 - <code>scm/change/title</code></li>
<li><code>SCM</code> 源代码控制菜单 - <code>scm/sourceControl</code></li>
<li>视图标题菜单 - <code>view/title</code></li>
<li>查看项目菜单 - <code>view/item/context</code></li>
<li><code>macOS</code> 触控栏 - <code>touchBar</code></li>
<li>注释线程标题菜单栏 - <code>comments/commentThread/title</code></li>
<li>注释线程上下文菜单 - <code>comments/commentThread/context</code></li>
<li>注释标题菜单栏 - <code>comments/comment/title</code></li>
<li>注释上下文菜单 - <code>comments/comment/context</code></li>
<li>时间线视图标题菜单栏 - <code>timeline/title</code></li>
<li>时间线视图项目上下文菜单 - <code>timeline/item/context</code></li>
<li>扩展视图上下文菜单 - <code>extension/context</code></li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"menus"</span>: &#123;
      <span class="hljs-attr">"editor/title"</span>: [
        &#123;
          <span class="hljs-attr">"when"</span>: <span class="hljs-string">"resourceLangId == markdown"</span>,
          <span class="hljs-attr">"command"</span>: <span class="hljs-string">"markdown.showPreview"</span>,
          <span class="hljs-attr">"alt"</span>: <span class="hljs-string">"markdown.showPreviewToSide"</span>,
          <span class="hljs-attr">"group"</span>: <span class="hljs-string">"navigation"</span>
        &#125;
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">2. 可以通过 <code>when</code> 来控制何时可见</h5>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"menus"</span>: &#123;
    <span class="hljs-attr">"commandPalette"</span>: [
      &#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"extension.sayHello"</span>,
        <span class="hljs-attr">"when"</span>: <span class="hljs-string">"editorHasSelection"</span>
      &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅当被选中时可见</p>
<h5 data-id="heading-21">3. 分组排序</h5>
<h6 data-id="heading-22">1. <code>editor context menu</code> 默认组</h6>
<ul>
<li><code>navigation</code>：导航组在所有情况下都排在第一位</li>
<li><code>1_modification</code>：该组紧随其后，包含修改代码的命令</li>
<li><code>9_cutcopypaste</code>：带有基本编辑命令的倒数第二个默认组</li>
<li><code>z_commands</code>：带有打开命令面板的条目的最后一个默认组</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a179a000227b4f288c4f26c9a00bf9f8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-23">2. <code>explorer context menu</code> 默认组</h6>
<ul>
<li><code>navigation</code>：与跨 <code>VS Code</code> 导航相关的命令。该组在所有情况下都排在第一位</li>
<li><code>2_workspace</code>：与工作区操作相关的命令</li>
<li><code>3_compare</code>：与在差异编辑器中比较文件相关的命令</li>
<li><code>4_search</code>：在搜索视图中与搜索相关的命令</li>
<li><code>5_cutcopypaste</code>：与剪切、复制和粘贴文件相关的命令</li>
<li><code>6_copypath</code>：与复制文件路径相关的命令</li>
<li><code>7_modification</code>：与文件修改相关的命令</li>
</ul>
<h6 data-id="heading-24">3. <code>editor tab context menu</code> 默认组</h6>
<ul>
<li><code>1_close</code>：与关闭编辑器相关的命令</li>
<li><code>3_preview</code>：与固定编辑器相关的命令</li>
</ul>
<h6 data-id="heading-25">4. <code>editor title menu</code> 默认组</h6>
<ul>
<li><code>navigation</code>：与导航相关的命令</li>
<li><code>1_run</code>：与运行和调试编辑器相关的命令</li>
<li><code>1_diff</code>：与使用差异编辑器相关的命令</li>
<li><code>3_open</code>：与打开编辑器相关的命令</li>
<li><code>5_close</code>：与关闭编辑器相关的命令</li>
</ul>
<h6 data-id="heading-26">5. <code>Timeline view item context menu</code> 默认组</h6>
<ul>
<li><code>inline</code>：重要或常用的时间线项目命令</li>
<li><code>1_actions</code>：与使用时间线项目相关的命令</li>
<li><code>5_copy</code>：与复制时间线项目相关的命令</li>
</ul>
<h6 data-id="heading-27">6. <code>Extensions view context menu</code> 默认组</h6>
<ul>
<li><code>1_copy</code>：与复制扩展信息相关的命令</li>
<li><code>2_configure</code>：与配置扩展相关的命令</li>
</ul>
<h5 data-id="heading-28">4. 在组内排序</h5>
<p>通过 <code>@<number></code> 附加到组内来指定的</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"editor/title"</span>: [
    &#123;
      <span class="hljs-attr">"when"</span>: <span class="hljs-string">"editorHasSelection"</span>,
      <span class="hljs-attr">"command"</span>: <span class="hljs-string">"extension.Command"</span>,
      <span class="hljs-attr">"group"</span>: <span class="hljs-string">"myGroup@1"</span>
    &#125;
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">5、<code>keybindings</code></h4>
<p>快捷键绑定</p>
<p>当 <code>win/linux</code> 触发 <code>Ctrl+F1</code> 或者 <code>MacOS</code> 触发 <code>Cmd + F1</code> 时，调用 <code>extension.sayHello</code> 命令</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"keybindings"</span>: [
      &#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"extension.sayHello"</span>,
        <span class="hljs-attr">"key"</span>: <span class="hljs-string">"ctrl+f1"</span>,
        <span class="hljs-attr">"mac"</span>: <span class="hljs-string">"cmd+f1"</span>,
        <span class="hljs-attr">"when"</span>: <span class="hljs-string">"editorTextFocus"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/829a8901805a4f8fb786fbd5a3f7e6bb~tplv-k3u1fbpfcp-zoom-1.image" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-RflZZRQG-1625145025370)(https://note.youdao.com/src/61A0C7B8C47149D182CEC12D9C361724)]" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-30">6、<code>languages</code></h4>
<p>语言</p>
<p>作用：</p>
<ul>
<li>定义一个可以在 <code>VS Code API</code> 的其他部分重用的 <code>languageId</code></li>
<li>将文件扩展名、文件名模式、以特定行开头的文件、<code>mimetypes</code> 与该语言 <code>ID</code> 相关联。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"languages"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"python"</span>,
        <span class="hljs-attr">"extensions"</span>: [<span class="hljs-string">".py"</span>],
        <span class="hljs-attr">"aliases"</span>: [<span class="hljs-string">"Python"</span>, <span class="hljs-string">"py"</span>],
        <span class="hljs-attr">"filenames"</span>: [],
        <span class="hljs-attr">"firstLine"</span>: <span class="hljs-string">"^#!/.*\\bpython[0-9.-]*\\b"</span>,
        <span class="hljs-attr">"configuration"</span>: <span class="hljs-string">"./language-configuration.json"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">7、<code>debuggers</code></h4>
<p>调试器</p>
<ul>
<li><code>type</code> 是用于在启动配置中标识此调试器的唯一 <code>ID</code></li>
<li><code>label</code> 是此调试器在 UI 中的用户可见名称</li>
<li><code>program</code> 编写调试适配器的路径，该适配器针对实际调试器或运行时实现 <code>VS Code</code> 调试协议</li>
<li><code>runtime</code> 如果调试适配器的路径不是可执行文件但需要运行时</li>
<li><code>configurationAttributes</code> 是特定于此调试器的启动配置参数的架构。 请注意，不支持 <code>JSON</code> 架构构造 <code>$ref</code> 和定义</li>
<li><code>initialConfigurations</code> 列出了用于填充初始 <code>launch.json</code> 的启动配置</li>
<li><code>configurationSnippets</code> 列出了在编辑 <code>launch.json</code> 时通过 <code>IntelliSense</code> 可用的启动配置</li>
<li><code>variables</code> 引入替换变量并将它们绑定到由调试器扩展实现的命令</li>
<li><code>languages</code> 那些调试扩展可以被视为“默认调试器”的语言</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"debuggers"</span>: [
      &#123;
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
        <span class="hljs-attr">"label"</span>: <span class="hljs-string">"Node Debug"</span>,

        <span class="hljs-attr">"program"</span>: <span class="hljs-string">"./out/node/nodeDebug.js"</span>,
        <span class="hljs-attr">"runtime"</span>: <span class="hljs-string">"node"</span>,

        <span class="hljs-attr">"languages"</span>: [<span class="hljs-string">"javascript"</span>, <span class="hljs-string">"typescript"</span>, <span class="hljs-string">"javascriptreact"</span>, <span class="hljs-string">"typescriptreact"</span>],

        <span class="hljs-attr">"configurationAttributes"</span>: &#123;
          <span class="hljs-attr">"launch"</span>: &#123;
            <span class="hljs-attr">"required"</span>: [<span class="hljs-string">"program"</span>],
            <span class="hljs-attr">"properties"</span>: &#123;
              <span class="hljs-attr">"program"</span>: &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
                <span class="hljs-attr">"description"</span>: <span class="hljs-string">"The program to debug."</span>
              &#125;
            &#125;
          &#125;
        &#125;,

        <span class="hljs-attr">"initialConfigurations"</span>: [
          &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
            <span class="hljs-attr">"request"</span>: <span class="hljs-string">"launch"</span>,
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Launch Program"</span>,
            <span class="hljs-attr">"program"</span>: <span class="hljs-string">"$&#123;workspaceFolder&#125;/app.js"</span>
          &#125;
        ],

        <span class="hljs-attr">"configurationSnippets"</span>: [
          &#123;
            <span class="hljs-attr">"label"</span>: <span class="hljs-string">"Node.js: Attach Configuration"</span>,
            <span class="hljs-attr">"description"</span>: <span class="hljs-string">"A new configuration for attaching to a running node program."</span>,
            <span class="hljs-attr">"body"</span>: &#123;
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"node"</span>,
              <span class="hljs-attr">"request"</span>: <span class="hljs-string">"attach"</span>,
              <span class="hljs-attr">"name"</span>: <span class="hljs-string">"$&#123;2:Attach to Port&#125;"</span>,
              <span class="hljs-attr">"port"</span>: <span class="hljs-number">9229</span>
            &#125;
          &#125;
        ],

        <span class="hljs-attr">"variables"</span>: &#123;
          <span class="hljs-attr">"PickProcess"</span>: <span class="hljs-string">"extension.node-debug.pickNodeProcess"</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">8、<code>breakpoints</code></h4>
<p>断点</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"breakpoints"</span>: [
      &#123;
        <span class="hljs-attr">"language"</span>: <span class="hljs-string">"javascript"</span>
      &#125;,
      &#123;
        <span class="hljs-attr">"language"</span>: <span class="hljs-string">"javascriptreact"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">9、<code>grammars</code></h4>
<p>为一种语言写一个 <code>TextMate</code> 语法，包含语法的文件可以是 <code>JSON</code> 或者 <code>XML plist</code> 格式</p>
<p>必须指定一个 <code>label</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"grammars"</span>: [
      &#123;
        <span class="hljs-attr">"language"</span>: <span class="hljs-string">"markdown"</span>,
        <span class="hljs-attr">"scopeName"</span>: <span class="hljs-string">"text.html.markdown"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./syntaxes/markdown.tmLanguage.json"</span>,
        <span class="hljs-attr">"embeddedLanguages"</span>: &#123;
          <span class="hljs-attr">"meta.embedded.block.frontmatter"</span>: <span class="hljs-string">"yaml"</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">10、<code>themes</code></h4>
<p>主题</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"themes"</span>: [
      &#123;
        <span class="hljs-attr">"label"</span>: <span class="hljs-string">"Monokai"</span>,
        <span class="hljs-attr">"uiTheme"</span>: <span class="hljs-string">"vs-dark"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./themes/monokai-color-theme.json"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73b72d1d9ff24645bbbf6e902107d4f1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-35">11、<code>iconThemes</code></h4>
<p>图标主题</p>
<p>必须指定一个 <code>id</code>，一个 <code>label</code> 和一个 <code>path</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"iconThemes"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"metro"</span>,
        <span class="hljs-attr">"label"</span>: <span class="hljs-string">"Metro File Icons"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./fileicons/metro-file-icon-theme.json"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ccbab859837474e9dc1e057dc997383~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-36">12、<code>productIconThemes</code></h4>
<p>产品图标主题</p>
<p>必须指定一个 <code>id</code>，一个 <code>label</code> 和一个 <code>path</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"productIconThemes"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"elegant"</span>,
        <span class="hljs-attr">"label"</span>: <span class="hljs-string">"Elegant Icon Theme"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./producticons/elegant-product-icon-theme.json"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c65c7c734c6454ba0fad771eafd4217~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-37">13、<code>snippets</code></h4>
<p>代码片段</p>
<p>为 <code>go</code> 语言添加一份代码片段</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"snippets"</span>: [
      &#123;
        <span class="hljs-attr">"language"</span>: <span class="hljs-string">"go"</span>,
        <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./snippets/go.json"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">14、<code>jsonValidation</code></h4>
<p><code>JSON</code> 验证</p>
<p>为特定的 <code>JSON</code> 文件提供验证, <code>url</code> 可以时本地文件也可以时网络文件</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"jsonValidation"</span>: [
      &#123;
        <span class="hljs-attr">"fileMatch"</span>: <span class="hljs-string">".jshintrc"</span>,
        <span class="hljs-attr">"url"</span>: <span class="hljs-string">"https://json.schemastore.org/jshintrc"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">15、<code>views</code></h4>
<p>视图</p>
<p>必须为视图指定标识符和名称</p>
<ul>
<li><code>explorer</code>: 活动栏中的资源管理器视图容器</li>
<li><code>scm</code>: 活动栏中的源代码管理 (SCM) 视图容器</li>
<li><code>debug</code>: 在活动栏中运行和调试视图容器</li>
<li><code>test</code>: 活动栏中的测试视图容器</li>
<li><code>Custom view</code>：扩展提供的自定义视图容器</li>
</ul>
<p>当用户打开视图时，<code>VScode</code> 将会发出一个 <code>activationEvent onView:$&#123;viewId&#125;</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"views"</span>: &#123;
      <span class="hljs-attr">"explorer"</span>: [
        &#123;
          <span class="hljs-attr">"id"</span>: <span class="hljs-string">"nodeDependencies"</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Node Dependencies"</span>,
          <span class="hljs-attr">"when"</span>: <span class="hljs-string">"workspaceHasPackageJSON"</span>,
          <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"media/dep.svg"</span>,
          <span class="hljs-attr">"contextualTitle"</span>: <span class="hljs-string">"Package Explorer"</span>
        &#125;
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e65c9cc83f44461d9163694a1c7c7206~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-40">两种方式填充视图内容</h5>
<ol>
<li>通过 <code>createTreeView API</code> 提供数据提供者或直接通过 <code>registerTreeDataProvider API</code> 注册数据提供者来填充数据，从而使用 <code>TreeView</code></li>
<li>通过使用 <code>registerWebviewViewProvider</code> 注册提供程序来使用 <code>WebviewView</code>, <code>Webview</code> 视图允许在视图中呈现任意 <code>HTML</code>。</li>
</ol>
<h4 data-id="heading-41">16、<code>viewsWelcome</code></h4>
<p>欢迎视图，仅适用于空树视图</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"viewsWelcome"</span>: [
      &#123;
        <span class="hljs-attr">"view"</span>: <span class="hljs-string">"scm"</span>,
        <span class="hljs-attr">"contents"</span>: <span class="hljs-string">"In order to use git features, you can open a folder containing a git repository or clone from a URL.\n[Open Folder](command:vscode.openFolder)\n[Clone Repository](command:git.clone)\nTo learn more about how to use git and source control in VS Code [read our docs](https://aka.ms/vscode-scm)."</span>,
        <span class="hljs-attr">"when"</span>: <span class="hljs-string">"config.git.enabled && git.state == initialized && workbenchState == empty"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a038a0eedf684df5a31986999c0d03dd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-42">17、<code>viewsContainers</code></h4>
<p>视图容器，必须为视图容器指定 <code>identifier</code> (标识符)、<code>title</code> (标题)、和 <code>icon</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"viewsContainers"</span>: &#123;
      <span class="hljs-attr">"activitybar"</span>: [
        &#123;
          <span class="hljs-attr">"id"</span>: <span class="hljs-string">"package-explorer"</span>,
          <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Package Explorer"</span>,
          <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"resources/package-explorer.svg"</span>
        &#125;
      ]
    &#125;,
    <span class="hljs-attr">"views"</span>: &#123;
      <span class="hljs-attr">"package-explorer"</span>: [
        &#123;
          <span class="hljs-attr">"id"</span>: <span class="hljs-string">"package-dependencies"</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Dependencies"</span>
        &#125;,
        &#123;
          <span class="hljs-attr">"id"</span>: <span class="hljs-string">"package-outline"</span>,
          <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Outline"</span>
        &#125;
      ]
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/790f0a69041c41f8848e0640ca52fe41~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-43">图标规则</h5>
<ul>
<li>大小：图标应为 24x24 且居中。</li>
<li>颜色：图标应使用单一颜色。</li>
<li>格式：建议图标为 <code>SVG</code>，但可以接受任何图像文件类型。</li>
<li>状态：所有图标都继承以下状态样式：</li>
</ul>





















<table><thead><tr><th align="left">State</th><th align="left">Opacity</th></tr></thead><tbody><tr><td align="left">Default</td><td align="left">60%</td></tr><tr><td align="left">Hover</td><td align="left">100%</td></tr><tr><td align="left">Active</td><td align="left">100%</td></tr></tbody></table>
<h4 data-id="heading-44">18、<code>walkthroughs</code></h4>
<p>演示，在开始页面提供演示，由标题、描述、<code>ID</code> 和一系列步骤组成</p>
<p>演示中每个步骤都有一个标题、描述、<code>ID</code> 和媒体元素(图像或者 <code>markdown</code> 内容)，以及一系列将导致检查步骤的可选择事件</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"walkthroughs"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"sample"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Sample"</span>,
        <span class="hljs-attr">"description"</span>: <span class="hljs-string">"A sample walkthrough"</span>,
        <span class="hljs-attr">"steps"</span>: [
          &#123;
            <span class="hljs-attr">"id"</span>: <span class="hljs-string">"runcommand"</span>,
            <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Run Command"</span>,
            <span class="hljs-attr">"description"</span>: <span class="hljs-string">"This step will run a command and check off once it has been run.\n[Run Command](command:getting-started-sample.runCommand)"</span>,
            <span class="hljs-attr">"media"</span>: &#123; <span class="hljs-attr">"image"</span>: <span class="hljs-string">"media/image.png"</span>, <span class="hljs-attr">"altText"</span>: <span class="hljs-string">"Empty image"</span> &#125;,
            <span class="hljs-attr">"completionEvents"</span>: [<span class="hljs-string">"onCommand:getting-started-sample.runCommand"</span>]
          &#125;,
          &#123;
            <span class="hljs-attr">"id"</span>: <span class="hljs-string">"changesetting"</span>,
            <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Change Setting"</span>,
            <span class="hljs-attr">"description"</span>: <span class="hljs-string">"This step will change a setting and check off when the setting has changed\n[Change Setting](command:getting-started-sample.changeSetting)"</span>,
            <span class="hljs-attr">"media"</span>: &#123; <span class="hljs-attr">"markdown"</span>: <span class="hljs-string">"media/markdown.md"</span> &#125;,
            <span class="hljs-attr">"completionEvents"</span>: [<span class="hljs-string">"onSettingChanged:getting-started-sample.sampleSetting"</span>]
          &#125;
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d753bac6843844b19b36643abf579d5b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-45">1. <code>Completion events</code></h5>
<p>默认情况下，如果没有提供 <code>completion events</code> 事件，单击任何按钮时将关闭该步骤，或者如果该步骤没有按钮，则在打开时将其选中，可以提供一个 <code>completionEvents</code> 列表</p>
<h6 data-id="heading-46">可用的 <code>Completion Events</code> 事件：</h6>
<ul>
<li><code>onCommand:myCommand.id</code>：在命令运行时</li>
<li><code>onSettingChanged:mySetting.id</code>：一旦给定设置被修改</li>
<li><code>onContext:contextKeyExpression</code>：当上下文键表达式计算为真时</li>
<li><code>extensionInstalled:myExt.id</code>：如果安装了给定的扩展</li>
<li><code>onView:myView.id</code>：一旦给定的视图变得可见</li>
<li><code>onLink:https://...</code>：一旦通过演示打开给定链接。</li>
</ul>
<p>一旦一个步骤被选中，它将保持选中状态，直到用户明确取消选中该步骤或重置他们的进度（通过入门：重置进度命令）。</p>
<h4 data-id="heading-47">19、<code>problemMatchers</code></h4>
<p>问题匹配</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"problemMatchers"</span>: [
      &#123;
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"gcc"</span>,
        <span class="hljs-attr">"owner"</span>: <span class="hljs-string">"cpp"</span>,
        <span class="hljs-attr">"fileLocation"</span>: [<span class="hljs-string">"relative"</span>, <span class="hljs-string">"$&#123;workspaceFolder&#125;"</span>],
        <span class="hljs-attr">"pattern"</span>: &#123;
          <span class="hljs-attr">"regexp"</span>: <span class="hljs-string">"^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$"</span>,
          <span class="hljs-attr">"file"</span>: <span class="hljs-number">1</span>,
          <span class="hljs-attr">"line"</span>: <span class="hljs-number">2</span>,
          <span class="hljs-attr">"column"</span>: <span class="hljs-number">3</span>,
          <span class="hljs-attr">"severity"</span>: <span class="hljs-number">4</span>,
          <span class="hljs-attr">"message"</span>: <span class="hljs-number">5</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"2.0.0"</span>,
  <span class="hljs-attr">"tasks"</span>: [
    &#123;
      <span class="hljs-attr">"label"</span>: <span class="hljs-string">"build"</span>,
      <span class="hljs-attr">"command"</span>: <span class="hljs-string">"gcc"</span>,
      <span class="hljs-attr">"args"</span>: [<span class="hljs-string">"-Wall"</span>, <span class="hljs-string">"helloWorld.c"</span>, <span class="hljs-string">"-o"</span>, <span class="hljs-string">"helloWorld"</span>],
      <span class="hljs-attr">"problemMatcher"</span>: <span class="hljs-string">"$gcc"</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过名称引用 <code>$gcc</code> 在 <code>tasks.json</code> 文件中使用此问题匹配器</p>
<h4 data-id="heading-48">20、<code>problemPatterns</code></h4>
<p>问题模式</p>
<h4 data-id="heading-49">21、<code>taskDefinitions</code></h4>
<p>任务定义，至少要有一个类型属性，通常需要定义附加属性</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"taskDefinitions"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"npm"</span>,
      <span class="hljs-attr">"required"</span>: [<span class="hljs-string">"script"</span>],
      <span class="hljs-attr">"properties"</span>: &#123;
        <span class="hljs-attr">"script"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
          <span class="hljs-attr">"description"</span>: <span class="hljs-string">"The script to execute"</span>
        &#125;,
        <span class="hljs-attr">"path"</span>: &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"string"</span>,
          <span class="hljs-attr">"description"</span>: <span class="hljs-string">"The path to the package.json file. If omitted the package.json in the root of the workspace folder is used."</span>
        &#125;
      &#125;
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>JSON</code> 架构语法为 <code>required</code> 和 <code>properties</code> 属性定义的</p>
<ul>
<li><code>"type"</code>: <code>"npm"</code> 将任务定义与 <code>npm</code> 任务相关联</li>
<li><code>"required"</code>: [ <code>"script"</code> ] 将该脚本属性定义为必需的。 <code>path</code> 属性是可选的</li>
<li><code>"properties" : &#123; ... &#125;</code> 定义附加属性及其类型</li>
</ul>
<p>当创建一个任务时，需要传递一个符合 <code>package.json</code> 文件中贡献的任务定义 <code>TaskDefinition</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> task = <span class="hljs-keyword">new</span> vscode.Task(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'npm'</span>, <span class="hljs-attr">script</span>: <span class="hljs-string">'test'</span> &#125;, ....);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">22、<code>colors</code></h4>
<p>主题颜色，定义后，用户可以在 <code>workspace.colorCustomization</code> 设置中自定义颜色，用户主题可以设置颜色值。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"colors"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-string">"superstatus.error"</span>,
        <span class="hljs-attr">"description"</span>: <span class="hljs-string">"Color for error message in the status bar."</span>,
        <span class="hljs-attr">"defaults"</span>: &#123;
          <span class="hljs-attr">"dark"</span>: <span class="hljs-string">"errorForeground"</span>,
          <span class="hljs-attr">"light"</span>: <span class="hljs-string">"errorForeground"</span>,
          <span class="hljs-attr">"highContrast"</span>: <span class="hljs-string">"#010203"</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>插件可以使用 <code>ThemeColor API</code> 使用新的和现有的主题颜色</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> errorColor = <span class="hljs-keyword">new</span> vscode.ThemeColor(<span class="hljs-string">'superstatus.error'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">23、<code>typescriptServerPlugins</code></h4>
<p>提供 <code>TypeScript</code> 服务器插件，以增强 <code>VS Code</code> 的 <code>JavaScript</code> 和 <code>TypeScript</code> 支持</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"typescriptServerPlugins"</span>: [
      &#123;
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"typescript-styled-plugin"</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的示例扩展提供了 <code>typescript-styled-plugin</code>，它为 <code>JavaScript</code> 和 <code>TypeScript</code> 添加了样式组件 <code>IntelliSense</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"typescript-styled-plugin"</span>: <span class="hljs-string">"*"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当用户使用 <code>VS Code</code> 的 <code>TypeScript</code> 版本时，会为所有 <code>JavaScript</code> 和 <code>TypeScript</code> 文件加载 <code>TypeScript</code> 服务器插件。如果用户使用的是 <code>TypeScript</code> 的工作区版本，它们不会被激活，除非插件明确设置 <code>"enableForWorkspaceTypeScriptVersions": true</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"typescriptServerPlugins"</span>: [
      &#123;
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"typescript-styled-plugin"</span>,
        <span class="hljs-attr">"enableForWorkspaceTypeScriptVersions"</span>: <span class="hljs-literal">true</span>
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">24、<code>resourceLabelFormatters</code></h4>
<p>提供资源标签格式化程序，指定如何在工作台中的任何地方显示 <code>URI</code></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"contributes"</span>: &#123;
    <span class="hljs-attr">"resourceLabelFormatters"</span>: [
      &#123;
        <span class="hljs-attr">"scheme"</span>: <span class="hljs-string">"remotehub"</span>,
        <span class="hljs-attr">"formatting"</span>: &#123;
          <span class="hljs-attr">"label"</span>: <span class="hljs-string">"$&#123;path&#125;"</span>,
          <span class="hljs-attr">"separator"</span>: <span class="hljs-string">"/"</span>,
          <span class="hljs-attr">"workspaceSuffix"</span>: <span class="hljs-string">"GitHub"</span>
        &#125;
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">25、<code>customEditors</code></h4>
<p><code>customEditors</code> 是你的差距如何告诉 <code>VS Code</code> 它提供的自定义编辑器</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"contributes"</span>: &#123;
  <span class="hljs-attr">"customEditors"</span>: [
    &#123;
      <span class="hljs-attr">"viewType"</span>: <span class="hljs-string">"catEdit.catScratch"</span>,
      <span class="hljs-attr">"displayName"</span>: <span class="hljs-string">"Cat Scratch"</span>,
      <span class="hljs-attr">"selector"</span>: [
        &#123;
          <span class="hljs-attr">"filenamePattern"</span>: <span class="hljs-string">"*.cscratch"</span>
        &#125;
      ],
      <span class="hljs-attr">"priority"</span>: <span class="hljs-string">"default"</span>
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>customEditors</code> 是一个数组，所以插件可以贡献多个自定义编辑器</p>
<ul>
<li><code>viewType</code> - 自定义编辑器的唯一标识符</li>
</ul>
<p>这就是 <code>VS Code</code> 如何将 <code>package.json</code> 中的自定义编辑器贡献与代码中的自定义编辑器实现联系起来。这在所有扩展中必须是唯一的，因此不要使用通用的 <code>viewType</code>，例如 <code>“preview”</code>，请确保使用对您的扩展而言唯一的视图类型，例如 <code>“viewType”：“myAmazingExtension.svgPreview”</code></p>
<ul>
<li><code>displayName</code> - 在 <code>VS Code</code> 的 <code>UI</code> 中标识自定义编辑器的名称</li>
</ul>
<p><code>display name</code> 是在 <code>VScode UI</code> 中向用户显示的</p>
<ul>
<li><code>selector</code> - 指定自定义编辑器对哪些文件处于活动状态</li>
</ul>
<p><code>selector</code> (选择器)是一个或多个 <code>glob</code> 模式的数组。这些 <code>glob</code> 模式与文件名匹配，以确定是否可以对它们使用自定义编辑器。诸如 <code>*.png</code> 之类的 <code>filenamePattern</code> 将为所有 <code>PNG</code> 文件启用自定义编辑器</p>
<ul>
<li><code>priority</code> - 优先级（可选）指定何时使用自定义编辑器</li>
</ul>
<p>当资源打开时使用自定义编辑器的优先级控制。可能的值为：
- <code>default</code>
- <code>option</code></p></div>  
</div>
            