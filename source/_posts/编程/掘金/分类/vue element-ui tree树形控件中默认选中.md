
---
title: 'vue element-ui tree树形控件中默认选中'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9710'
author: 掘金
comments: false
date: Tue, 25 May 2021 02:07:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=9710'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>方式一:  通过标签内属性: :default-checked-keys来设置</p>
<pre><code class="hljs language-js copyable" lang="js"><el-tree
      :data=<span class="hljs-string">"dataList"</span>
      show-checkbox
      <span class="hljs-keyword">default</span>-expand-all
      check-strictly
      :<span class="hljs-keyword">default</span>-checked-keys=<span class="hljs-string">"defaultList"</span><span class="hljs-comment">//数组中是rightsList中有权限的id值</span>
      :props=<span class="hljs-string">"&#123;label: 'name'&#125;"</span>
    />
    
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">dataList</span>: [name:<span class="hljs-number">123</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">name</span>:<span class="hljs-number">345</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">2</span>],
      <span class="hljs-attr">defaultList</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用element-ui中的tree控件时,我想要默认选中角色拥有权限的复选框时,发现即使设置了:default-checked-keys="[...]",也不能渲染结果,后来发现没有设置 node-key</p>
<pre><code class="hljs language-js copyable" lang="js"><el-tree
      :data=<span class="hljs-string">"dataList"</span>
      show-checkbox
      <span class="hljs-keyword">default</span>-expand-all
      check-strictly
      :<span class="hljs-keyword">default</span>-checked-keys=<span class="hljs-string">"defaultList"</span><span class="hljs-comment">//数组中是rightsList中有权限的id值,与node-key对应</span>
      node-key=<span class="hljs-string">"id"</span>
      :props=<span class="hljs-string">"&#123;label: 'name'&#125;"</span>
    />
    
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">dataList</span>: [name:<span class="hljs-number">123</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">name</span>:<span class="hljs-number">345</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">2</span>],
      <span class="hljs-attr">defaultList</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
方式二: 通过 this.$refs.tree组件上自定义ref名.setCheckedKeys(this.defaultList)
<pre><code class="hljs language-js copyable" lang="js"><el-tree
  ref=<span class="hljs-string">"tree"</span>
  :data=<span class="hljs-string">"dataList"</span>
  show-checkbox
  <span class="hljs-keyword">default</span>-expand-all
  check-strictly
  :<span class="hljs-keyword">default</span>-checked-keys=<span class="hljs-string">"defaultList"</span><span class="hljs-comment">//数组中是rightsList中有权限的id值,与node-key对应</span>
  node-key=<span class="hljs-string">"id"</span> <span class="hljs-comment">// 通过此方式必须设置该项</span>
  :props=<span class="hljs-string">"&#123;label: 'name'&#125;"</span>
/>
<span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">dataList</span>: [name:<span class="hljs-number">123</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">name</span>:<span class="hljs-number">345</span>,<span class="hljs-attr">id</span>:<span class="hljs-number">2</span>],
      <span class="hljs-attr">defaultList</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]
    &#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-number">1.</span><span class="hljs-built_in">this</span>.$refs.tree.setCheckedKeys(<span class="hljs-built_in">this</span>.defaultList) 
    <span class="hljs-comment">// 如果发现还是没有渲染,可能是dom树渲染的问题,通过this.$nextTick(() => &#123;&#125;)解决</span>
    <span class="hljs-number">2.</span><span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.$refs.tree.setCheckedKeys(<span class="hljs-built_in">this</span>.defaultList)
    &#125;)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取被选中节点 通过: this.$refs.tree.getCheckedKeys()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs.tree.getCheckedKeys())
<span class="hljs-comment">// 得到一个数组,数组中是与node-key="id"对应的id值</span>
<span class="hljs-comment">// [1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            