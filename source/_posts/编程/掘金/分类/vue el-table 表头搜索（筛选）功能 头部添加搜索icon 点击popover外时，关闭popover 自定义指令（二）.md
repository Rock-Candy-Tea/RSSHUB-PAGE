
---
title: 'vue el-table 表头搜索（筛选）功能 头部添加搜索icon 点击popover外时，关闭popover 自定义指令（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee473b441419403a97992320d8cea635~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:46:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee473b441419403a97992320d8cea635~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在可以点击打开后 发现和antd还有什么不一样的地方
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee473b441419403a97992320d8cea635~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
原来是在点击icon打开popover时，想关闭这个popover需要再次点击icon
这很明显不合理，更合适的方法是点击其它任何区域，都会隐藏这个popover
于是用到了自定义指令。
在组件内部，新增一个visible变量控制是否显示，在点击外部时，设置为false</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">iconColor</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
<span class="hljs-attr">methods</span>: &#123;
closeOver () &#123;
          <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">false</span>
      &#125;,
&#125;

<span class="hljs-attr">directives</span>: &#123;
        <span class="hljs-attr">clickOutside</span>: &#123;
            bind (el, binding, vnode) &#123;
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickHandler</span> (<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-comment">// 这里判断点击的元素是否是本身，是本身，则返回</span>
                <span class="hljs-keyword">if</span> (el.contains(e.target)) &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
                &#125;
                <span class="hljs-comment">// 判断指令中是否绑定了函数</span>
                <span class="hljs-keyword">if</span> (binding.expression) &#123;
                    <span class="hljs-comment">// 如果绑定了函数 则调用那个函数，此处binding.value就是handleClose方法</span>
                    binding.value(e)
                &#125;
                &#125;
                <span class="hljs-comment">// 给当前元素绑定个私有变量，方便在unbind中可以解除事件监听</span>
                el.__vueClickOutside__ = clickHandler
                <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, clickHandler)
            &#125;,
            update () &#123;&#125;,
            unbind (el, binding) &#123;
                <span class="hljs-comment">// 解除事件监听</span>
                <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'click'</span>, el.__vueClickOutside__)
                <span class="hljs-keyword">delete</span> el.__vueClickOutside__
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自定义指令写好后，在icon外部div上添加即可</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left:5px"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"popClick"</span> <span class="hljs-attr">v-click-outside</span>=<span class="hljs-string">"closeOver"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>完整组件代码如下</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">el-popover</span> <span class="hljs-attr">placement</span>=<span class="hljs-string">"bottom"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">trigger</span>=<span class="hljs-string">"manual"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"visible"</span> @<span class="hljs-attr">show</span>=<span class="hljs-string">"showPopover"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-input</span>
      <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入内容"</span>
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"value"</span>
      <span class="hljs-attr">clearable</span>
      @<span class="hljs-attr">keyup.enter.native</span>=<span class="hljs-string">"confirm"</span>
      <span class="hljs-attr">ref</span>=<span class="hljs-string">"sInput"</span>
    ></span>
      <span class="hljs-comment"><!-- <el-button slot="append" icon="el-icon-search" @click="confirm"> --></span>
      <span class="hljs-comment"><!-- </el-button> --></span>
    <span class="hljs-tag"></<span class="hljs-name">el-input</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"confirm"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-top:5px"</span>></span>搜索<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"resetData"</span>></span>重置<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"reference"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-left:5px"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"popClick"</span> <span class="hljs-attr">v-click-outside</span>=<span class="hljs-string">"closeOver"</span>></span>
      <span class="hljs-comment"><!-- <i class="el-icon-search" :style="&#123;'color':iconColor&#125;" ></i> --></span>
      <span class="hljs-tag"><<span class="hljs-name">svg</span>
        <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"64 64 896 896"</span>
        <span class="hljs-attr">data-icon</span>=<span class="hljs-string">"search"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"1em"</span>
        <span class="hljs-attr">height</span>=<span class="hljs-string">"1em"</span>
        <span class="hljs-attr">fill</span>=<span class="hljs-string">"currentColor"</span>
        <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;'color':iconColor? 'rgb(16, 142, 233)': '', 'margin-top': '5px'&#125;"</span> ></span>
        <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M909.6 854.5L649.9 594.8C690.2 542.7 712 479 712 412c0-80.2-31.3-155.4-87.9-212.1-56.6-56.7-132-87.9-212.1-87.9s-155.5 31.3-212.1 87.9C143.2 256.5 112 331.8 112 412c0 80.1 31.3 155.5 87.9 212.1C256.5 680.8 331.8 712 412 712c67 0 130.6-21.8 182.7-62l259.7 259.6a8.2 8.2 0 0 0 11.6 0l43.6-43.5a8.2 8.2 0 0 0 0-11.6zM570.4 570.4C528 612.7 471.8 636 412 636s-116-23.3-158.4-65.6C211.3 528 188 471.8 188 412s23.3-116.1 65.6-158.4C296 211.3 352.2 188 412 188s116.1 23.2 158.4 65.6S636 352.2 636 412s-23.3 116.1-65.6 158.4z"</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">path</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">el-popover</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">inject</span>: [<span class="hljs-string">'reload'</span>],
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">iconColor</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">tableType</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">type</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">defaultValue</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">options</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> []
      &#125;
    &#125;,
    <span class="hljs-attr">defaultProps</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">label</span>: <span class="hljs-string">'label'</span>,
          <span class="hljs-attr">value</span>: <span class="hljs-string">'value'</span>
        &#125;
      &#125;
    &#125;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    defaultValue (newVal, oldVal) &#123;
      <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
      self.value = newVal
    &#125;

  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
      showPopover () &#123;
        <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.$refs.sInput.focus()
        &#125;)
      &#125;,
      resetData () &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'reset'</span>)
          <span class="hljs-built_in">this</span>.value = <span class="hljs-string">''</span>
          <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">false</span>
          <span class="hljs-built_in">this</span>.iconColor = <span class="hljs-literal">false</span>
          <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
          self.$emit(<span class="hljs-string">'resetChange'</span>, &#123; <span class="hljs-attr">type</span>: self.type, <span class="hljs-attr">value</span>: self.value, <span class="hljs-attr">tableType</span>: self.tableType &#125;)
      &#125;,
      closeOver () &#123;
          <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">false</span>
      &#125;,
      popClick (e) &#123;
          <span class="hljs-comment">// e.stopPropagation()</span>
          <span class="hljs-built_in">this</span>.visible = !<span class="hljs-built_in">this</span>.visible
      &#125;,
      confirm () &#123;
          <span class="hljs-built_in">this</span>.visible = <span class="hljs-literal">false</span>
          <span class="hljs-built_in">this</span>.iconColor = <span class="hljs-literal">true</span>
          <span class="hljs-keyword">const</span> self = <span class="hljs-built_in">this</span>
          <span class="hljs-keyword">if</span> (self.value) &#123;
              self.$emit(<span class="hljs-string">'selectChange'</span>, &#123; <span class="hljs-attr">type</span>: self.type, <span class="hljs-attr">value</span>: self.value, <span class="hljs-attr">tableType</span>: self.tableType &#125;)
          &#125;
      &#125;
    &#125;,
    <span class="hljs-attr">directives</span>: &#123;
        <span class="hljs-attr">clickOutside</span>: &#123;
            bind (el, binding, vnode) &#123;
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clickHandler</span> (<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-comment">// 这里判断点击的元素是否是本身，是本身，则返回</span>
                <span class="hljs-keyword">if</span> (el.contains(e.target)) &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
                &#125;
                <span class="hljs-comment">// 判断指令中是否绑定了函数</span>
                <span class="hljs-keyword">if</span> (binding.expression) &#123;
                    <span class="hljs-comment">// 如果绑定了函数 则调用那个函数，此处binding.value就是handleClose方法</span>
                    binding.value(e)
                &#125;
                &#125;
                <span class="hljs-comment">// 给当前元素绑定个私有变量，方便在unbind中可以解除事件监听</span>
                el.__vueClickOutside__ = clickHandler
                <span class="hljs-built_in">document</span>.addEventListener(<span class="hljs-string">'click'</span>, clickHandler)
            &#125;,
            update () &#123;&#125;,
            unbind (el, binding) &#123;
                <span class="hljs-comment">// 解除事件监听</span>
                <span class="hljs-built_in">document</span>.removeEventListener(<span class="hljs-string">'click'</span>, el.__vueClickOutside__)
                <span class="hljs-keyword">delete</span> el.__vueClickOutside__
            &#125;
        &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000017166675" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000017166675" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a>  表示真诚的感谢</p></div>  
</div>
            