
---
title: 'vscode使用指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76a7dd2c8934ad995d1184093909b37~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 13 Aug 2021 21:44:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76a7dd2c8934ad995d1184093909b37~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.vscode介绍</h2>
<blockquote>
<p>本文主要介绍vscode在工作中常用的快捷键及插件，目标在于提高工作效率。 本文的快捷键是基于mac的</p>
</blockquote>
<h2 data-id="heading-1">2. vscode快捷键</h2>
<pre><code class="hljs language-h copyable" lang="h"><span class="hljs-comment">// 修改快捷键的位置: </span>
Code => Perferences(首选项) => Keyboard Shortcuts(键盘快捷键方式)
opt + Shift + F <span class="hljs-comment">// 格式化</span>
ctrl + g <span class="hljs-comment">// 跳转到某一行</span>
ctrl + shift + T: <span class="hljs-comment">// 撤销最近关闭的窗口</span>
opt + <span class="hljs-number">1</span>/<span class="hljs-number">2</span>/<span class="hljs-number">3</span>/<span class="hljs-number">4</span>/<span class="hljs-number">5</span>: <span class="hljs-comment">// 在不同文件之间切换 。 vscode自带的是ctrl + 1/2/3/4/5。 我改了一下,因为我的被占用了</span>
shift + opt + up/down <span class="hljs-comment">// 在当前行上下复制当前行</span>
ctrl + shift + k <span class="hljs-comment">// 删除行</span>
opt + <span class="hljs-keyword">delete</span> <span class="hljs-comment">// 删除上一个单词， 很有用</span>
cmd + = 和 cmd + -: <span class="hljs-comment">// 组合来进行字体缩放;</span>
cmd + opt + S: <span class="hljs-comment">// 保存所有文件</span>
cmd + opt + F: <span class="hljs-comment">// 当前文件替换 👍</span>
cmd + d: <span class="hljs-comment">// 当前文件查找选中单词下一目标, 再按一下匹配下一个</span>
cmd + shift + l: <span class="hljs-comment">// 在选中文本的所有相同的内容处, 出现光标 👍</span>
opt + cmd + 上箭头 ：<span class="hljs-comment">// 在上面插入光标</span>
cmd + G / shift + cmd + G ：<span class="hljs-comment">// 查找下一个/上一个</span>
opt + Enter ： 选择查找匹配的所有匹配项 👍
cmd + \ ： 拆分窗口 👍 <span class="hljs-comment">// 重要 抄代码利器</span>
cmd + <span class="hljs-number">1</span>、<span class="hljs-number">2</span>、<span class="hljs-number">3</span>： 聚焦到第<span class="hljs-number">1</span>、<span class="hljs-number">2</span>、<span class="hljs-number">3</span>个编辑器 <span class="hljs-comment">// 同等重要</span>
cmd + opt + 左右方向键 <span class="hljs-comment">// 在已经打开的多个文件之间进行切换 非常实用</span>
cmd + shift + \ <span class="hljs-comment">// 跳转到匹配的括号</span>
cmd + g <span class="hljs-comment">// 在当前文件中搜索代码, 光标仍停留在编辑器里。 很巧妙 👍</span>
ctrl + r <span class="hljs-comment">// 切换工作区 👍</span>
shift + cmd + H ：<span class="hljs-comment">// 在文件中替换</span>
Ctrl+Shift+\: <span class="hljs-comment">// 跳转到与当前括号匹配的括号</span>
cmd + opt + ][ : <span class="hljs-comment">// 展开折叠代码 👍</span>
cmd + ][ : <span class="hljs-comment">// 缩进 和 反缩进 👍</span>

ctrl + cmd + f: <span class="hljs-comment">// 全屏和退出全屏(效果同mac左上角最小化右边那个按钮)</span>
cmd + shift + Z: 取消撤回
cmd + Z: 撤回
cmd + P 快速打开文件；
opt + up/down: 移动行上下
shift + opt + A ：<span class="hljs-comment">// 切换块注释 直接输入 `/**` 然后回车更好用</span>
cmd + P ： <span class="hljs-comment">// 跳到文件</span>
ctr + `: <span class="hljs-comment">// 打开/关闭 终端</span>
cmd + B <span class="hljs-comment">// 关闭左侧菜单栏</span>
control + tab <span class="hljs-comment">// 切换同一编辑器不同的标签页  </span>
cmd + 逗号 <span class="hljs-comment">// 设置</span>

我个人自定义的一些快捷键 ： 
cmd + shift + <span class="hljs-number">1</span> <span class="hljs-comment">// 切换到terminal  </span>
cmd + shift + <span class="hljs-number">2</span> <span class="hljs-comment">// 切换到当前编辑文件区域</span>
cmd + opt + / <span class="hljs-comment">// 将编辑器组与下一组合并</span>
cmd + opt + shift + / <span class="hljs-comment">// 合并所有编辑器组</span>

<span class="hljs-comment">// vscode设置</span>
连字符双击可以全选:   <span class="hljs-string">"editor.wordSeparators"</span>: <span class="hljs-string">"`~!@#$%^&*()=+[&#123;]&#125;\\|;:'\",.<>/?"</span>, <span class="hljs-comment">// 双击选中连字符。 删除了中间有个-</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.1 mac使用<code>code .</code>命令打开VSCode</h3>
<p>需要安装code：打开vscode –> command+shift+p –> 输入shell command –> 点击提示Shell Command: Install ‘code’ command in PATH运行</p>
<p>使用方式：打开终端，cd到要用vscode打开的文件夹，然后输入命令<code>code .</code>即可打开</p>
<h3 data-id="heading-3">3.2 当顶部菜单栏隐藏时候， 如何调出来</h3>
<ul>
<li>设置里的 Show Tabs</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c76a7dd2c8934ad995d1184093909b37~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">3.3 vscode找到全局配置文件<code>settings.json</code></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/662e455581fb4982aa3a09f8da0ae62f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/578989d89d5e4362845e2261954ba030~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
首选项-> 设置 -> 输入(syn)进行搜索 -> 在最底下的Vetur中选择在settings.json中编辑</p>
<h3 data-id="heading-5">3.4 vscode下插件的安装</h3>
<blockquote>
<p>在vscode中使用微信小程序</p>
</blockquote>
<ol>
<li>wechat-snippet</li>
</ol>
<ul>
<li>微信小程序代码辅助， 代码片段自动完成</li>
</ul>
<ol start="2">
<li>minapp</li>
</ol>
<ul>
<li>微信小程序标签、属性的智能补全(同时支持原生小程序、mpvue和wepy框架，并提供snippets)</li>
<li>需要输入<code><</code> 才会触发标签补全</li>
<li>输入空格会触发对应标签的属性补全</li>
</ul>
<h3 data-id="heading-6">3.5 vscode 打开新文件覆盖窗口，始终显示一个窗口</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad32acba2e82468bbd72ba8dd30a5ca3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">。
正常来说vscode打开文件，在可以多窗口展示的。 如果打开新页面会覆盖之前的老页面， 始终只能显示一个窗口， 那就会很麻烦使用起来。 解决办法: ctrl+shift+p打开命令面板。 输入settings， 选择Open Settings(JSON)。 然后在settings.json文件中修改<code>workbench.editor.showTabs:true</code></p>
<ol>
<li>ctrl+shift+p</li>
<li>输入settings打开settings.json</li>
<li>修改<code>workbench.editor.showTabs:true</code></li>
</ol>
<h3 data-id="heading-7">3.6 vue通过<code>@</code>符号导入组件路径提示</h3>
<p><strong>开发场景</strong><br>
当使用 Vue 框架进行项目开发时，在 vue.config.js 中配置好了路径别名后，到其他页面引入组件、引入 css 、引入静态文件路径时，使用路径别名不会智能提示路径。虽然在 vscode 中安装了Path Intellisense 插件，但是并无作用。这样容易出现路径拼写错误的低能问题，同时也会造成开发效率降低。</p>
<p><strong>解决方案</strong><br>
在 vscode 的 setting.json 中给 Path Intellisence 配置（该方案是最优选，能识别任意格式文件，覆盖率最广。当别名发生改变时只需修改配置即可）</p>
<pre><code class="hljs language-h copyable" lang="h"><span class="hljs-comment">// settings.json </span>
<span class="hljs-string">"path-intellisense.mappings"</span>: &#123;
    <span class="hljs-string">"@"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src"</span>,
    <span class="hljs-string">"u"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src/utils"</span>,
    <span class="hljs-string">"c"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src/components"</span>,
    <span class="hljs-string">"v"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src/views"</span>,
    <span class="hljs-string">"a"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src/assets"</span>,
    <span class="hljs-string">"s"</span>: <span class="hljs-string">"$&#123;workspaceRoot&#125;/src/styles"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">3 vue项目自定义<code>alias</code>别名</h2>
<blockquote>
<p>在vue项目中。 不同的文件有不同的路径，有的路径比较深， 有的经常被引用。 所以， 建议使用<code>alias</code>别名对项目文件进行别名引用。 这样引入文件的时候会更加方便。</p>
</blockquote>
<ol>
<li>首先在<code>vue.config.js</code>中的<code>module.exports</code>里配置别名</li>
</ol>
<pre><code class="hljs language-v copyable" lang="v">configureWebpack: &#123;
  <span class="hljs-comment">// provide the app's title in webpack's name field, so that</span>
  <span class="hljs-comment">// it can be accessed in index.html to inject the correct title.</span>
  <span class="hljs-comment">// 自动补全的扩展名</span>
  resolve: &#123;
    <span class="hljs-keyword">alias</span>: &#123;
      '@': resolve('src'),
      'c': resolve('src/components'),
      'u': resolve('src/utils'),
      'v': resolve('src/views'),
      'i': resolve('src/assets/images'),
      's': resolve('src/styles'),
    &#125;
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>新建<code>jsconfig.json</code>， 在这里匹配<code>vue.config.js</code>里的配置</li>
</ol>
<pre><code class="hljs language-v copyable" lang="v">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"target"</span>: <span class="hljs-string">"es2017"</span>,
    <span class="hljs-string">"allowSyntheticDefaultImports"</span>: false,
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"@/*"</span>: [<span class="hljs-string">"src/*"</span>],
      <span class="hljs-string">"u/*"</span>: [<span class="hljs-string">"src/utils/*"</span>],
      <span class="hljs-string">"c/*"</span>: [<span class="hljs-string">"src/components/*"</span>],
      <span class="hljs-string">"v/*"</span>: [<span class="hljs-string">"src/views/*"</span>],
      <span class="hljs-string">"i/*"</span>: [<span class="hljs-string">"src/assets/images/*"</span>],
      <span class="hljs-string">"s/*"</span>: [<span class="hljs-string">"src/styles/*"</span>]
    &#125;
  &#125;,
  <span class="hljs-string">"exclude"</span>: [<span class="hljs-string">"node_modules"</span>, <span class="hljs-string">"dist"</span>],
  <span class="hljs-string">"include"</span>: [<span class="hljs-string">"src/**/*"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小贴士: 以上两个配置只针对当前单一项目进行的配置。 如果想在全局生效。  可以直接在全局设置里配置
3. <code>settings.json</code>里做如下配置</p>
<pre><code class="copyable">"path-intellisense.mappings": &#123;
  "@": "$&#123;workspaceRoot&#125;/src",
  "u": "$&#123;workspaceRoot&#125;/src/utils",
  "c": "$&#123;workspaceRoot&#125;/src/components",
  "v": "$&#123;workspaceRoot&#125;/src/views",
  "a": "$&#123;workspaceRoot&#125;/src/assets",
  "i": "$&#123;workspaceRoot&#125;/src/assets/images",
  "s": "$&#123;workspaceRoot&#125;/src/styles"
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            