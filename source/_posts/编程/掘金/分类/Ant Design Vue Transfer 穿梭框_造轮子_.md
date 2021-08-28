
---
title: 'Ant Design Vue Transfer 穿梭框_造轮子_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cbce5d9370344ad97c979857e7a637d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 20:29:18 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cbce5d9370344ad97c979857e7a637d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>人的思想是千变万化的，不可能一套组件满足所有的需求，前端开发总避免不了要“造轮子”的。这次做的穿梭框就是模仿官方来写的，功能基本一样，但不可能完全一样，会在官方的基础上优化，样式也更好看了哟。</p>
<h2 data-id="heading-0">基础穿梭框</h2>
<p>官方基础的穿梭框如下，左右两边都是列表形式，还有搜索框。</p>
<p>具体使用可以查看官方文档，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fantdv.com%2Fcomponents%2Ftransfer-cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://antdv.com/components/transfer-cn/" ref="nofollow noopener noreferrer">带搜索框的穿梭框</a></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cbce5d9370344ad97c979857e7a637d~tplv-k3u1fbpfcp-watermark.image" alt="ic_simple_1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">重写基础穿梭框</h2>
<p>重写穿梭框的原因：</p>
<ol>
<li>样式肯定是不满足 UI 要求的</li>
<li>功能麻烦了一点，操作完数据之后总要点一下“左移”或者“右移”才能完成</li>
<li>当数据很多时，组件渲染会很卡顿，反正我公司的上千条数据都会有点卡了</li>
</ol>
<p>主要实现功能点：</p>
<ol>
<li>头部全选</li>
<li>搜索功能</li>
<li>搜索关键词高亮显示</li>
<li>自动穿梭功能</li>
<li>虚拟滚动列表实现</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc60fae52964ba59465c6e6eda6bace~tplv-k3u1fbpfcp-watermark.image" alt="ic_simple_3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">组件参数和事件</h2>
<p>自定义参数：考虑对外暴露的参数，参数的作用，属性等</p>
<p>自定义事件：考虑暴露出去的回调事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 自定义参数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">dataSource</span>: &#123;
      <span class="hljs-comment">// 数据源</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [],
    &#125;,
    <span class="hljs-attr">targetKeys</span>: &#123;
      <span class="hljs-comment">// 右侧框数据的 key 集合</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [],
    &#125;,
    <span class="hljs-attr">disabledKeys</span>: &#123;
      <span class="hljs-comment">// 禁用 key 集合</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [],
    &#125;,
    <span class="hljs-attr">titles</span>: &#123;
      <span class="hljs-comment">// 标题</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> [<span class="hljs-string">"可选"</span>, <span class="hljs-string">"已选"</span>],
    &#125;,
    <span class="hljs-attr">locale</span>: &#123;
      <span class="hljs-comment">// 语言配置</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">itemUnit</span>: <span class="hljs-string">"项"</span>,
          <span class="hljs-attr">sourceEmptyText</span>: <span class="hljs-string">"暂无可选数据"</span>,
          <span class="hljs-attr">targetEmptyText</span>: <span class="hljs-string">"暂无已选数据"</span>,
        &#125;;
      &#125;,
    &#125;,
    <span class="hljs-attr">searchPlaceholder</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">"请输入搜索关键字"</span>,
    &#125;,
    <span class="hljs-attr">showSelectAll</span>: &#123;
      <span class="hljs-comment">// 是否展示全选勾选框</span>
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">true</span>,
    &#125;,
  &#125;,
&#125;;

<span class="hljs-comment">// 自定义事件</span>
<span class="hljs-comment">// onChange事件：返回显示在目标框数据的 key 集合和 数据列表</span>
<span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">"on-change"</span>, <span class="hljs-built_in">this</span>.sourceTargetKeys, <span class="hljs-built_in">this</span>.targetData);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">组件整体架构</h2>
<p>整体结构是源数据框+目标数据框，而每个数据框由头部、搜索框、数据源列表三部分组成</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-comment"><!-- 基础穿梭框 --></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"m-single-common-transfer"</span>></span>
    <span class="hljs-comment"><!-- 源数据展示 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list"</span>></span>
      <span class="hljs-comment"><!-- 头部 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!-- 主体内容 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-body"</span>></span>
        <span class="hljs-comment"><!-- 搜索框 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-search"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 源列表 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-source"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-comment"><!-- 目标数据展示 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list"</span>></span>
      <span class="hljs-comment"><!-- 头部 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-comment"><!-- 主体内容 --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-body"</span>></span>
        <span class="hljs-comment"><!-- 搜索框 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-search"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 目标列表 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-source"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">头部(全选框，计数项，标题)</h3>
<p>头部主要分为 3 个部分，如下以源数据框为例，目标数据框原理一样：</p>
<ol>
<li>全选框：可进行全选和全不选的切换事件(<code>handleSourceSelectedAll</code>)，可表示全选、部分选、全不选(<code>sourceIsIndeterminate</code>, <code>sourceCheckedAll</code>)三种状态</li>
<li>计数项：可以统计数据源所有项和已选项个数(<code>sourceCheckedKeys</code>, <code>sourceAllKeys</code>)</li>
<li>标题：可自定义展示内容(<code>sourceTitle</code>)</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header"</span>></span>
    <span class="hljs-comment"><!-- showSelectAll：是否展示全选勾选框和计数项 --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showSelectAll"</span>></span>
      <span class="hljs-comment"><!--  sourceCheckedAll：是否全选； sourceIsIndeterminate：是否半选 --></span>
      <span class="hljs-tag"><<span class="hljs-name">a-checkbox</span>
        <span class="hljs-attr">:indeterminate</span>=<span class="hljs-string">"sourceIsIndeterminate"</span>
        <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sourceCheckedAll"</span>
        @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleSourceSelectedAll"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header-checkbox"</span>
      /></span>
      <span class="hljs-comment"><!-- sourceAllKeys：全部key；sourceCheckedKeys：选中key --></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header-selected"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"sourceCheckedKeys.length"</span>
          ></span>&#123;&#123; sourceCheckedKeys.length &#125;&#125;/&#123;&#123; sourceAllKeys.length &#125;&#125; &#123;&#123;
          locale.itemUnit &#125;&#125;</span
        >
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-else</span>></span>&#123;&#123; sourceAllKeys.length &#125;&#125; &#123;&#123; locale.itemUnit &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-header-title"</span>></span>&#123;&#123; sourceTitle &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> R <span class="hljs-keyword">from</span> <span class="hljs-string">"ramda"</span>;
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">computed</span>: &#123;
      <span class="hljs-comment">// 源数据菜单名</span>
      <span class="hljs-function"><span class="hljs-title">sourceTitle</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> [text] = <span class="hljs-built_in">this</span>.titles;
        <span class="hljs-keyword">return</span> text;
      &#125;,
      <span class="hljs-comment">// 目标数据菜单名</span>
      <span class="hljs-function"><span class="hljs-title">targetTitle</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">let</span> [, text] = <span class="hljs-built_in">this</span>.titles;
        <span class="hljs-keyword">return</span> text;
      &#125;,
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
      <span class="hljs-comment">// 左侧 状态监测</span>
      <span class="hljs-function"><span class="hljs-title">sourceCheckedKeys</span>(<span class="hljs-params">val</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (val && val.length > <span class="hljs-number">0</span>) &#123;
          <span class="hljs-comment">// 总半选是否开启</span>
          <span class="hljs-built_in">this</span>.sourceIsIndeterminate = <span class="hljs-literal">true</span>;

          <span class="hljs-comment">// 总全选是否开启 - 根据选中节点的数量是否和源数据长度相等</span>
          <span class="hljs-keyword">let</span> allKeys = <span class="hljs-built_in">this</span>.getAllKeys(<span class="hljs-built_in">this</span>.sourceData);
          <span class="hljs-keyword">let</span> allCheck = R.filter(<span class="hljs-function">(<span class="hljs-params">o</span>) =></span> R.includes(o.key, allKeys), val);
          <span class="hljs-keyword">if</span> (R.length(allKeys) === R.length(allCheck)) &#123;
            <span class="hljs-comment">// 关闭半选 开启全选</span>
            <span class="hljs-built_in">this</span>.sourceIsIndeterminate = <span class="hljs-literal">false</span>;
            <span class="hljs-built_in">this</span>.sourceCheckedAll = <span class="hljs-literal">true</span>;
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 开启半选</span>
            <span class="hljs-built_in">this</span>.sourceIsIndeterminate = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>.sourceCheckedAll = <span class="hljs-literal">false</span>;
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// 未选</span>
          <span class="hljs-built_in">this</span>.sourceIsIndeterminate = <span class="hljs-literal">false</span>;
          <span class="hljs-built_in">this</span>.sourceCheckedAll = <span class="hljs-literal">false</span>;
        &#125;
      &#125;,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-comment">// 源数据全选事件</span>
      <span class="hljs-function"><span class="hljs-title">handleSourceSelectedAll</span>(<span class="hljs-params">e</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.sourceData.length === <span class="hljs-number">0</span>) &#123;
          <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span> (e.target.checked) &#123;
          <span class="hljs-built_in">this</span>.sourceTargetKeys = R.uniq(
            R.concat(<span class="hljs-built_in">this</span>.sourceTargetKeys, <span class="hljs-built_in">this</span>.getAllKeys(<span class="hljs-built_in">this</span>.sourceData))
          );
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-built_in">this</span>.sourceTargetKeys = R.difference(
            <span class="hljs-built_in">this</span>.sourceTargetKeys,
            <span class="hljs-built_in">this</span>.getAllKeys(<span class="hljs-built_in">this</span>.sourceData)
          );
        &#125;
      &#125;,
    &#125;,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">搜索框</h3>
<p>搜索框其实就挺简单了，主要是一个图标的变化。</p>
<p>空值时是放大镜图标；有值时删除图标，可以清空搜索框值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-search"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a-input</span>
    <span class="hljs-attr">v-model</span>=<span class="hljs-string">"sourceKeyword"</span>
    <span class="hljs-attr">:placeholder</span>=<span class="hljs-string">"searchPlaceholder"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-transfer-list-search-input"</span>
    @<span class="hljs-attr">pressEnter</span>=<span class="hljs-string">"handleSourceSearch"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">a-icon</span>
      <span class="hljs-attr">slot</span>=<span class="hljs-string">"suffix"</span>
      <span class="hljs-attr">type</span>=<span class="hljs-string">"close-circle"</span>
      <span class="hljs-attr">theme</span>=<span class="hljs-string">"filled"</span>
      <span class="hljs-attr">v-if</span>=<span class="hljs-string">"sourceKeyword && sourceKeyword.length > 0"</span>
      @<span class="hljs-attr">click</span>=<span class="hljs-string">"sourceKeyword = ''"</span>
    /></span>
    <span class="hljs-tag"><<span class="hljs-name">a-icon</span> <span class="hljs-attr">v-else</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"suffix"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"search"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">a-input</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">数据列表实现</h3>
<p>源数据列表和目标数据列表有相同点，也有不同点：</p>
<ol>
<li>相同点：</li>
</ol>
<ul>
<li>都采用了虚拟列表：<code>RecycleScroller</code></li>
<li>搜索关键词高亮显示：<code>substr</code> 截取标题显示</li>
<li>数据源过滤：数据源根据关键词<code>sourceKeyword</code>过滤</li>
</ul>
<ol start="2">
<li>不同点：</li>
</ol>
<ul>
<li>源数据项包括选择框和标题</li>
<li>源数据禁用处理：<code>disabledKeys</code>， <code>sourceTargetKeys</code></li>
<li>目标数据显示标题和删除按钮</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">a-list</span>
    <span class="hljs-attr">:data-source</span>=<span class="hljs-string">"sourceData"</span>
    <span class="hljs-attr">:locale</span>=<span class="hljs-string">"&#123; emptyText: locale.sourceEmptyText &#125;"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-list"</span>
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">RecycleScroller</span>
      <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-list-recycle"</span>
      <span class="hljs-attr">:items</span>=<span class="hljs-string">"sourceData"</span>
      <span class="hljs-attr">:item-size</span>=<span class="hljs-string">"36"</span>
      <span class="hljs-attr">key-field</span>=<span class="hljs-string">"key"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">a-list-item</span>
        <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"&#123; item, index &#125;"</span>
        <span class="hljs-attr">:key</span>=<span class="hljs-string">"`source-$&#123;index&#125;`"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-list-item"</span>
      ></span>
        <span class="hljs-tag"><<span class="hljs-name">a-checkbox</span>
          <span class="hljs-attr">:checked</span>=<span class="hljs-string">"item.checked"</span>
          <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"item.disabled"</span>
          <span class="hljs-attr">class</span>=<span class="hljs-string">"mct-list-item-checkbox"</span>
          @<span class="hljs-attr">change</span>=<span class="hljs-string">"(e) => handleSourceSelect(e, index, item.key)"</span>
        ></span><span class="hljs-tag"></<span class="hljs-name">a-checkbox</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"['mct-list-item-title', &#123; disabled: item.disabled &#125;]"</span>></span>
          <span class="hljs-comment"><!-- 搜索关键词高亮显示 --></span>
          <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"sourceKeyword && item.title.includes(sourceKeyword)"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"title title-other"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>
                ></span>&#123;&#123; item.title.substr(0, item.title.indexOf(sourceKeyword))
                &#125;&#125;</span
              >
              <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"active"</span>></span>&#123;&#123; sourceKeyword &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>
                ></span>&#123;&#123; item.title.substr( item.title.indexOf(sourceKeyword) +
                sourceKeyword.length ) &#125;&#125;</span
              >
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">a-list-item</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">RecycleScroller</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">a-list</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 虚拟数据列表 RecycleScroller</span>
  <span class="hljs-keyword">import</span> &#123; RecycleScroller &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue-virtual-scroller"</span>;
  <span class="hljs-keyword">import</span> <span class="hljs-string">"vue-virtual-scroller/dist/vue-virtual-scroller.css"</span>;

  computed: &#123;
    <span class="hljs-comment">// 源数据列表</span>
    <span class="hljs-function"><span class="hljs-title">sourceData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> filterKeys =
        <span class="hljs-built_in">this</span>.disabledKeys && <span class="hljs-built_in">this</span>.disabledKeys.length
          ? R.concat(<span class="hljs-built_in">this</span>.disabledKeys, <span class="hljs-built_in">this</span>.sourceTargetKeys)
          : <span class="hljs-built_in">this</span>.sourceTargetKeys;
      <span class="hljs-comment">// 禁用数据处理</span>
      <span class="hljs-keyword">let</span> result = R.map(
        <span class="hljs-function">(<span class="hljs-params">o</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (R.includes(o.key, filterKeys)) &#123;
            o.disabled = <span class="hljs-literal">true</span>;
            o.checked = <span class="hljs-literal">true</span>;
            o.title = <span class="hljs-string">`<span class="hljs-subst">$&#123;o.title&#125;</span>（已配置）`</span>;
          &#125; <span class="hljs-keyword">else</span> &#123;
            o.disabled = <span class="hljs-literal">false</span>;
            o.checked = <span class="hljs-literal">false</span>;
          &#125;
          <span class="hljs-keyword">return</span> o;
        &#125;,
        <span class="hljs-comment">// 数据源过滤</span>
        <span class="hljs-built_in">this</span>.sourceKeyword
          ? R.filter(
              <span class="hljs-function">(<span class="hljs-params">r</span>) =></span> R.includes(<span class="hljs-built_in">this</span>.sourceKeyword, r.title),
              R.clone(<span class="hljs-built_in">this</span>.dataSource)
            )
          : R.clone(<span class="hljs-built_in">this</span>.dataSource)
      );
      <span class="hljs-comment">// 全选，已选处理</span>
      <span class="hljs-built_in">this</span>.sourceAllKeys = <span class="hljs-built_in">this</span>.getAllKeys(result);
      <span class="hljs-built_in">this</span>.sourceCheckedKeys = R.filter(
        <span class="hljs-function">(<span class="hljs-params">o</span>) =></span> R.includes(o, <span class="hljs-built_in">this</span>.sourceAllKeys),
        <span class="hljs-built_in">this</span>.sourceTargetKeys
      );
      <span class="hljs-keyword">return</span> result;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">组件使用</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">single-transfer</span>
    <span class="hljs-attr">:data-source</span>=<span class="hljs-string">"singleDataSource"</span>
    <span class="hljs-attr">:target-keys</span>=<span class="hljs-string">"singleTargetKeys"</span>
    @<span class="hljs-attr">on-change</span>=<span class="hljs-string">"handleSingleChange"</span>
  /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> R <span class="hljs-keyword">from</span> <span class="hljs-string">"ramda"</span>;
  <span class="hljs-keyword">import</span> SingleTransfer <span class="hljs-keyword">from</span> <span class="hljs-string">"@cms/component/transfer/SingleTransfer.vue"</span>;

  <span class="hljs-keyword">const</span> mapIndexed = R.addIndex(R.map);
  <span class="hljs-keyword">const</span> singleDataSource = mapIndexed(<span class="hljs-function">(<span class="hljs-params">o, i</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">key</span>: i + <span class="hljs-number">1</span>,
      <span class="hljs-attr">title</span>:
        i === <span class="hljs-number">0</span> ? <span class="hljs-string">`选项哈哈哈哈哈哈哈哈哈哈哈哈哈嘿嘿`</span> : <span class="hljs-string">`<span class="hljs-subst">$&#123;o.title&#125;</span><span class="hljs-subst">$&#123;i + <span class="hljs-number">1</span>&#125;</span>`</span>,
    &#125;;
  &#125;, R.repeat(&#123; <span class="hljs-attr">key</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"选项"</span> &#125;, <span class="hljs-number">20</span>));

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        singleDataSource,
        <span class="hljs-attr">singleTargetKeys</span>: [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>],
      &#125;;
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
      SingleTransfer,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handleSingleChange</span>(<span class="hljs-params">targetKeys, data</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"singleTransfer"</span>, targetKeys, data);
      &#125;,
    &#125;,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"scss"</span>></span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9435fce30d6844deb0564089ec95bda1~tplv-k3u1fbpfcp-watermark.image" alt="ic_simple_2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">后续优化点</h2>
<p>前端再怎么优化，也是有限制的，更好的方式是前后端结合</p>
<ol>
<li>搜索功能：后端接口支持，加个查询接口，不仅仅是前端过滤</li>
<li>数据源列表处理：后端接口支持分页查询，前端实现滚动分页加载数据</li>
</ol></div>  
</div>
            