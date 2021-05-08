
---
title: '解决 Codemirror 5 快速点击导致光标定位不准的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b661d9508ab430c82a660aceb5adf15~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 18:52:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b661d9508ab430c82a660aceb5adf15~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求说明</h1>
<p>数据浏览器对象浏览页面中，鼠标随意快（慢）速点击SQL编辑区，记住鼠标最后一次点击的位置，双击左侧表名（字段名）时自动复制表名（字段名）到最后一次点击的位置。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b661d9508ab430c82a660aceb5adf15~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210508101104.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">解决方案</h1>
<p>1、刚开始走了一些弯路，以为在编辑器中监听获取焦点 focus 事件记录光标最后的位置，然后在左侧双击时自动填充名称到已记录的光标处，这个的确实现了所需功能，但是在后来测试中发现如果鼠标随意快速点击编辑区，记住的最后一次光标位置并不准确，且没有任何规律性，猜测是因为点击过快 focus 监听事件无法实时记录光标位置导致的。</p>
<p>2、在重新查阅官方文档 <a href="https://codemirror.net/" target="_blank" rel="nofollow noopener noreferrer">codemirror.net/</a> 后发现应该用 cursorActivity 监听事件：
Will be fired when the cursor or selection moves, or any change is made to the editor content.（当光标或选区移动或对编辑器内容进行任何更改时，将触发该事件。）
因为官方文档是全英文的，查阅起来有点困难，费了一些时间。</p>
<p>3、在 cursorActivity 事件中就可以实时记录光标的位置了，再也不用担心鼠标的任性快慢操作了，然后双击左侧名称就可以自动填充到最后一次光标记录的位置了，下面贴出部分代码片段仅供参考，需要根据自己项目情况有选择使用。</p>
<h1 data-id="heading-2">代码片段</h1>
<p>codeEditor.vue 组件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"code-editor-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">textarea</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"mycode"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"curCode"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"code-w"</span>></span><span class="hljs-tag"></<span class="hljs-name">textarea</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<script>
<span class="hljs-keyword">import</span> CodeMirror <span class="hljs-keyword">from</span> <span class="hljs-string">'codemirror/lib/codemirror'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"codemirror/theme/ambiance.css"</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">"codemirror/lib/codemirror.css"</span>
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/mode/javascript/javascript"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/mode/sql/sql"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/addon/edit/matchbrackets"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/addon/selection/active-line"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/addon/hint/show-hint"</span>);
<span class="hljs-built_in">require</span>(<span class="hljs-string">"codemirror/addon/hint/sql-hint"</span>);
<span class="hljs-keyword">import</span> <span class="hljs-string">"codemirror/addon/hint/show-hint.css"</span>
<span class="hljs-keyword">import</span> sqlFormatter <span class="hljs-keyword">from</span> <span class="hljs-string">"sql-formatter"</span>
<span class="hljs-keyword">import</span> bus <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/bus'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;&#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">curCode</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">codeE</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">cmOptions</span>: &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">mode</span>: <span class="hljs-string">"text/x-mariadb"</span>,
        <span class="hljs-attr">indentWithTabs</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">smartIndent</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">lineNumbers</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">autoRefresh</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">matchBrackets</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">styleActiveLine</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">lineWrapping</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">hintOptions</span>: &#123;
          <span class="hljs-attr">completeSingle</span>: <span class="hljs-literal">false</span>
        &#125;
      &#125;
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>._initialize();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">_initialize</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 初始化编辑器实例，传入需要被实例化的文本域对象和默认配置</span>
      <span class="hljs-built_in">this</span>.codeE = CodeMirror.fromTextArea(<span class="hljs-built_in">this</span>.$refs.mycode, <span class="hljs-built_in">this</span>.cmOptions);
      <span class="hljs-built_in">this</span>.codeE.on(<span class="hljs-string">'focus'</span>, <span class="hljs-function">(<span class="hljs-params">code</span>) =></span> &#123;
        <span class="hljs-comment">// 记录光标位置的代码不写在这里</span>
      &#125;);
      <span class="hljs-built_in">this</span>.codeE.on(<span class="hljs-string">'cursorActivity'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
        <span class="hljs-comment">// console.log('eee === ', e);</span>
        <span class="hljs-keyword">let</span> codeData = &#123;
          <span class="hljs-attr">getCursor</span>: &#123; <span class="hljs-comment">// 获取光标位置</span>
            <span class="hljs-attr">line</span>: e.doc.getCursor().line,
            <span class="hljs-attr">ch</span>: e.doc.getCursor().ch
          &#125;,
          <span class="hljs-attr">codeE</span>: <span class="hljs-built_in">this</span>.codeE
        &#125;;
        <span class="hljs-comment">// console.log('codeData.getCursor === ', codeData.getCursor);</span>
        bus.$emit(<span class="hljs-string">'codeEditorGetCursor'</span>, codeData);
      &#125;)
    &#125;,
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象浏览 objectBrowse.vue 组件中：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">bus.$on(<span class="hljs-string">'codeEditorGetCursor'</span>, <span class="hljs-function">(<span class="hljs-params">codeData</span>) =></span> &#123; <span class="hljs-comment">// 获取编辑器焦点</span>
  <span class="hljs-built_in">this</span>.codeData = codeData
&#125;);

<span class="hljs-comment">// 双击事件函数中</span>
<span class="hljs-keyword">let</span> pos1 = <span class="hljs-built_in">this</span>.codeData.getCursor;
<span class="hljs-keyword">let</span> pos2 = &#123;&#125;;
<span class="hljs-comment">// console.log('setCode pos1 === ', pos1);</span>
<span class="hljs-keyword">if</span> (pos1) &#123;
  pos2.line = pos1.line;
  pos2.ch = pos1.ch;
  <span class="hljs-built_in">this</span>.codeData.codeE.setCursor(pos2); <span class="hljs-comment">// 设置光标位置</span>
  <span class="hljs-built_in">this</span>.codeData.codeE.replaceRange(<span class="hljs-string">'这里是你要填充的内容'</span>, pos2) <span class="hljs-comment">// 替换光标位置的内容</span>
&#125;



<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，实现所需需求。</p>
<p>如有侵权，请联系我删除！
转载请注明出处！仅供学习交流！</p></div>  
</div>
            