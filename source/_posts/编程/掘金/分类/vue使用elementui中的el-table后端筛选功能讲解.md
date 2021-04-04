
---
title: 'vue使用elementui中的el-table后端筛选功能讲解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8c1a787a7347f09eacdc211489e31a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 23:40:30 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8c1a787a7347f09eacdc211489e31a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">问题描述</h2>
<p>对于后台管理系统，比较常见的功能就是增删改查。对于“查”而言，筛选数据以查看是比较常见的。饿了么ui中自带的有筛选功能。不过官方文档所给到的例子是“前端筛选”，意思就是写死的数据，前端过滤出来以呈现。官方效果图如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e8c1a787a7347f09eacdc211489e31a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是实际开发中数据是后端同事动态从数据库抓取返回给前端的，所以官方案例“前端筛选”的用法用的不多，不过还是可以看看的，本篇文章主要讲一下“后端筛选”的用法步骤</p>
<blockquote>
<p>这里不禁要吐槽一下官方文档写的“不接地气”</p>
</blockquote>
<h2 data-id="heading-1">后端筛选的步骤</h2>
<h4 data-id="heading-2">第一步:搭建一个表格</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span> <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span> <span class="hljs-attr">border</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"age"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"年龄"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"gender"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"性别"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"xueli"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"学历"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"like"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"爱好"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"address"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"地址"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">tableData</span>: [
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"王小虎"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
          <span class="hljs-attr">gender</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">xueli</span>: <span class="hljs-string">"本科"</span>,
          <span class="hljs-attr">like</span>: <span class="hljs-string">"打篮球"</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">"上海闵行"</span>,
        &#125;,
        <span class="hljs-comment">// 省略若干表格数据......</span>
      ],
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初步效果图如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9debac39019b431e8aa57a7d3ac4f67e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">第二步：给要筛选的某一列开启筛选功能</h4>
<p>开启筛选其实很简单，只需要给对应列添加filters属性即可开启该列的筛选。filters是一个数组，数组每一项中有两个属性text和value，分别是呈现的数据，和对应的标识。这里我们先以姓名为例进行筛选</p>
<blockquote>
<p>其他表格字段多条件的筛选后面再补充</p>
</blockquote>
<p><strong>加filters数组写法一：直接写在标签里面（不推荐）</strong></p>
<p>filters数组如果直接写在标签里面就写死了，不是动态的了，不太推荐用这种方法。因为开发情况下，筛选条件filters数组的值也是从后台获取的数据，当然如果就是类似于筛选性别的，男或女；筛选幼儿园班级，小班、中班、大班。这种固定的筛选数据写在标签里面也是可以的。不过大多数情况下都是写在方法里面的，写在方法里面就方便从后台获取数据了</p>
<pre><code class="hljs language-js copyable" lang="js">     <el-table-column
        prop=<span class="hljs-string">"name"</span>
        label=<span class="hljs-string">"姓名"</span>
        width=<span class="hljs-string">"180"</span>
        column-key=<span class="hljs-string">"filterTag"</span>
        :filters=<span class="hljs-string">"[
          &#123; text: '王小虎', value: '王小虎' &#125;,
          &#123; text: '张小花', value: '张小花' &#125;,
          &#123; text: '赵小二', value: '赵小二' &#125;,
          &#123; text: '钱大牛', value: '钱大牛' &#125;,
        ]"</span>
      ></el-table-column>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>加filters数组写法二：数组写在方法methods里面（推荐）</strong></p>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-comment">// html部分</span>
      <el-table-column
        prop=<span class="hljs-string">"name"</span>
        label=<span class="hljs-string">"姓名"</span>
        width=<span class="hljs-string">"180"</span>
        :filters=<span class="hljs-string">"getfilterNameItem()"</span>
      ></el-table-column>
      
      <span class="hljs-comment">//js部分</span>
      <span class="hljs-function"><span class="hljs-title">getfilterNameItem</span>(<span class="hljs-params"></span>)</span> &#123;
          <span class="hljs-keyword">let</span> apiArr = [  <span class="hljs-comment">// 从后端获取筛选的字段</span>
            &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"王小虎"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"王小虎"</span> &#125;,
            &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"张小花"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"张小花"</span> &#125;,
            &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"赵小二"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"赵小二"</span> &#125;,
            &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"钱大牛"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"钱大牛"</span> &#125;,
          ];
          <span class="hljs-keyword">return</span> apiArr; <span class="hljs-comment">// return返回去</span>
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们给某一列开启筛选功能以后，在那一列上的表头就自动会出现对应的一个下拉小箭头，点击就会出现对应筛选项，勾选筛选或者重置清空，如下图：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc8d00b1def846efa58a54d684d4aa56~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">第三步：加上filter-change监听方法</h4>
<p>到这里点击筛选或者重置，没啥反应，因为还不够，我们还需要加一个方法filter-change，这个方法官方介绍如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/983fe0155dbc4baabac407f63f558126~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>filter-change这个方法可以监听筛选项的变化，在用户点击筛选或者重置小按钮的时候会触发，我们加上以后看看有啥变化（加在el-table标签上面）：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">// html部分</span>
    <el-table
      :data=<span class="hljs-string">"tableData"</span>
      border
      style=<span class="hljs-string">"width: 100%"</span>
      @filter-change=<span class="hljs-string">"filterChange"</span>
    >
    </el-table>
    
    <span class="hljs-comment">// js部分</span>
    <span class="hljs-function"><span class="hljs-title">filterChange</span>(<span class="hljs-params">filterObj</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(filterObj);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击筛选或者重置的时候打印看看会发生什么变化</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e5419f01abf448696db6fe5ae6094fd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
使用官方文档提供的column-key修改一下</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ddf968c388b4dacb34a6ffba3cab255~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><!-- column-key=<span class="hljs-string">"filterTag"</span> 这个要配一下，相当于起了个别名，通过这个别名可以访问到变化的对象 -->
     <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>
        <span class="hljs-attr">column-key</span>=<span class="hljs-string">"filterTag"</span>
        <span class="hljs-attr">:filters</span>=<span class="hljs-string">"getfilterNameItem()"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终就变成这样的了：</p>
<h4 data-id="heading-5">第四步：在filter-change的回调函数中做相应处理</h4>
<p>点击筛选</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40079b109c1547b0a58854f761de956b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
点击重置</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62c0e9bcfa6549d798626abf41070083~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
这样的话，就可以带着筛选参数发请求或者清空重置啦...</p>
<h2 data-id="heading-6">补充多条件筛选</h2>
<p>如果表格想要多条件筛选其实也很简单，比如要再加一个筛选性别。只需要在性别那一列再加上一个
column-key和filters（每一列的column-key的值都不能相同），同时在filter-change的回调中判别一下。个人感觉如果要多条件筛选，这样写会不太优雅。</p>
<pre><code class="hljs language-js copyable" lang="js">      <el-table-column
        prop=<span class="hljs-string">"gender"</span>
        label=<span class="hljs-string">"性别"</span>
        column-key=<span class="hljs-string">"filterSex"</span>
        :filters=<span class="hljs-string">"[
          &#123; text: '男', value: '男' &#125;,
          &#123; text: '女', value: '女' &#125;,
        ]"</span>
        width=<span class="hljs-string">"180"</span>
      >
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是多条件筛选，建议把筛选项写在外边，就不写在表格里面了。对应的步骤参见我的另一篇博客：vue仿写teambition的筛选功能（使用饿了么UI）
<a href="https://juejin.cn/post/6933956924509519885" target="_blank">juejin.cn/post/693395…</a></p>
<p>最后附上案例中的完整代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">el-table</span>
      <span class="hljs-attr">:data</span>=<span class="hljs-string">"tableData"</span>
      <span class="hljs-attr">border</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 100%"</span>
      @<span class="hljs-attr">filter-change</span>=<span class="hljs-string">"filterChange"</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span>
        <span class="hljs-attr">prop</span>=<span class="hljs-string">"name"</span>
        <span class="hljs-attr">label</span>=<span class="hljs-string">"姓名"</span>
        <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>
        <span class="hljs-attr">column-key</span>=<span class="hljs-string">"filterTag"</span>
        <span class="hljs-attr">:filters</span>=<span class="hljs-string">"getfilterNameItem()"</span>
      ></span><span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-comment"><!-- column-key="filterTag" 这个要配一下，相当于起了个别名，通过这个别名可以访问到变化的对象 --></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"age"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"年龄"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"gender"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"性别"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"xueli"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"学历"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"like"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"爱好"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-table-column</span> <span class="hljs-attr">prop</span>=<span class="hljs-string">"address"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"地址"</span>></span> <span class="hljs-tag"></<span class="hljs-name">el-table-column</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-table</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">tableData</span>: [],
    &#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 发请求获取表格的数据</span>
    <span class="hljs-built_in">this</span>.getTableData();
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-comment">// 获取表格的数据</span>
    <span class="hljs-function"><span class="hljs-title">getTableData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> apiTableData = [
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"王小虎"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
          <span class="hljs-attr">gender</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">xueli</span>: <span class="hljs-string">"本科"</span>,
          <span class="hljs-attr">like</span>: <span class="hljs-string">"打篮球"</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">"上海闵行"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"张小花"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
          <span class="hljs-attr">gender</span>: <span class="hljs-string">"女"</span>,
          <span class="hljs-attr">xueli</span>: <span class="hljs-string">"本科"</span>,
          <span class="hljs-attr">like</span>: <span class="hljs-string">"画画"</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">"上海松江"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"赵小二"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
          <span class="hljs-attr">gender</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">xueli</span>: <span class="hljs-string">"研究生"</span>,
          <span class="hljs-attr">like</span>: <span class="hljs-string">"航空航天"</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">"上海普陀"</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"钱大牛"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">28</span>,
          <span class="hljs-attr">gender</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">xueli</span>: <span class="hljs-string">"研究生"</span>,
          <span class="hljs-attr">like</span>: <span class="hljs-string">"航空航天"</span>,
          <span class="hljs-attr">address</span>: <span class="hljs-string">"上海奉贤"</span>,
        &#125;,
      ];
      <span class="hljs-built_in">this</span>.tableData = apiTableData;
    &#125;,
    <span class="hljs-comment">// 获取筛选的字段</span>
    <span class="hljs-function"><span class="hljs-title">getfilterNameItem</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">let</span> apiArr = [
        <span class="hljs-comment">// 发请求获取筛选项的数据</span>
        &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"王小虎"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"王小虎"</span> &#125;,
        &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"张小花"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"张小花"</span> &#125;,
        &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"赵小二"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"赵小二"</span> &#125;,
        &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"钱大牛"</span>, <span class="hljs-attr">value</span>: <span class="hljs-string">"钱大牛"</span> &#125;,
      ];
      <span class="hljs-keyword">return</span> apiArr;
    &#125;,
    <span class="hljs-comment">// 监听筛选项的变化</span>
    <span class="hljs-function"><span class="hljs-title">filterChange</span>(<span class="hljs-params">filterObj</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(filterObj.filterTag);
      <span class="hljs-keyword">if</span> (filterObj.filterTag.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"点击筛选"</span>);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"点击重置"</span>);
      &#125;
    &#125;,
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"less"</span> <span class="hljs-attr">scoped</span>></span><span class="css">
<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100vh</span>;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">20px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">20px</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            