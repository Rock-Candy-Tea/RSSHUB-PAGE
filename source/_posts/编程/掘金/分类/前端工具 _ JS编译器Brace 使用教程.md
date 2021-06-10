
---
title: '前端工具 _ JS编译器Brace 使用教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb7b552f83a44fecb7ba05905bf49be5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 01:19:31 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb7b552f83a44fecb7ba05905bf49be5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>开发人员一般是在电脑上面安装了IDE完成日常的开发任务，因为项目业务需求，用户想要在线写JS脚本，纯粹的字符串，很“费用户”。那就需要一个在线JS编译器，需要轻量级，好用，语法高亮，自动换行，语法提示d等功能。</p>
</blockquote>
<h4 data-id="heading-1">Brace</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb7b552f83a44fecb7ba05905bf49be5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>轻量</li>
<li>自动提示</li>
<li>语法高亮</li>
<li>自动换行</li>
<li>序号</li>
<li>代码高亮</li>
<li>自动缩进</li>
<li>更换主题</li>
<li>搜索和替换支持正则表达式</li>
<li>代码折叠</li>
</ul>
<p>老实说：就是因为monaco不好用才有这篇文章，现在一边重新用brace替换monaco，一边写使用文档。为什么要换，因为monaco太笨重了，我们使用场景很简单，不深度。严重拖延了打包的速度，增加包体大小！但是不能否认monaco的强大，当初也是万里挑一。</p>
<h4 data-id="heading-2">使用方法</h4>
<ul>
<li>官网</li>
</ul>
<pre><code class="copyable">[官方文档](https://ace.c9.io/#nav=howto)
[在线demo](https://ace.c9.io/build/kitchen-sink.html)
[github](https://github.com/ajaxorg/ace-builds/blob/master/editor.html)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>安装</li>
</ul>
<pre><code class="copyable">yarn add brace | npm install brace
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>引入</li>
</ul>
<pre><code class="copyable">var ace = require('brace')
require('brace/mode/javascript')
require('brace/theme/monokai')
require('brace/ext/language_tools') //很重要 自动补全 提示 必须要它
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>初始化</li>
</ul>
<pre><code class="copyable">init(script) &#123;
  let self = this
  var editor = ace.edit('javascript-editor')
  editor.getSession().setMode('ace/mode/javascript') //语言
  editor.setOptions(&#123;
    // 默认:false
    wrap: true, // 换行
    autoScrollEditorIntoView: false, // 自动滚动编辑器视图
    enableLiveAutocompletion: true, // 智能补全
    enableBasicAutocompletion: true // 启用基本完成 不推荐使用
  &#125;)
  if (script) &#123;
    editor.setValue(script) //需要主动赋值
  &#125; else editor.setValue(this.code)
  editor.getSession().on('change', function() &#123;
    self.$emit('update:code', editor.getValue()) //js 编辑器作为组件 传参给父组件
  &#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>html</li>
</ul>
<pre><code class="copyable"><template>
  <div id="javascript-editor"></div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="copyable">我是给这个编辑器设置了宽高 以及一些样式的
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>运行效果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d646be44900430fac139938a701193b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>api</li>
</ul>
<pre><code class="copyable">require("lib/ace"); ##引入
editor.setTheme("ace/theme/solarized_dark");##设置模板；引入theme-solarized_dark.js模板文件
editor.getSession().setMode("ace/mode/javascript"); ##设置程序语言模式
editor.setValue("the new text here");##设置内容
editor.getValue(); ##取值
editor.session.getTextRange(editor.getSelectionRange()); ##获取选择内容
editor.insert("Something cool"); ##在光标处插入
editor.selection.getCursor(); ##获取光标所在行或列
editor.gotoLine(lineNumber); ##跳转到行
editor.session.getLength(); ##获取总行数
editor.getSession().setTabSize(4); ##设置默认制表符的大小
editor.getSession().setUseSoftTabs(true); ##使用软标签.
document.getElementById('editor').style.fontSize='12px';  ##设置字体大小
editor.getSession().setUseWrapMode(true); ##设置代码折叠
editor.setHighlightActiveLine(false); ##设置高亮
editor.setShowPrintMargin(false); ##设置打印边距可见度
editor.setReadOnly(true); ##设置编辑器只读
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>事件</li>
</ul>
<pre><code class="copyable">editor.getSession().on('change', function(e) &#123;  
  // e.type, etc  
&#125;);  //change 事件

editor.getSession().selection.on('changeSelection', function(e) &#123;  
&#125;);  //选择事件

editor.getSession().selection.on('changeCursor', function(e) &#123;  
&#125;);  //光标移动事件
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">芳妮酱总结</h4>
<p>基本满足我的需求，再下一篇里面打包速度比对，性能分析（主要与Monaca）
下一篇是monaco的使用教程以及与brace 比对</p></div>  
</div>
            