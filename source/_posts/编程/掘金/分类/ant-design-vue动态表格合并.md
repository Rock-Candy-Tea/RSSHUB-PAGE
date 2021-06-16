
---
title: 'ant-design-vue动态表格合并'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52e26ac7fd33435981e4a71df7c4d206~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 09:25:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52e26ac7fd33435981e4a71df7c4d206~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">写在前面</h1>
<p>最近接到一个需求，要把后端传过来的数据动态展示在表格上面，并且支持前端筛选，最终实现的效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52e26ac7fd33435981e4a71df7c4d206~tplv-k3u1fbpfcp-watermark.image" alt="n6lpq-q2mui.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">数据格式</h1>
<p>后端会返回给我们一个数组,数组的每一项格式是这样,在这个需求里，我们需要对
<code>title</code>，<code>department</code>,<code>bugType</code> 这三个字段相同的值的单元格进行合并</p>
<pre><code class="hljs language-js copyable" lang="js"> &#123;
          <span class="hljs-attr">fixCount</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">codeType</span>: <span class="hljs-string">'新代码'</span>,
          <span class="hljs-attr">bugType</span>: <span class="hljs-string">'ui展示问题'</span>,
          <span class="hljs-attr">notFixedCount</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">todayAdd</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">totalCount</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">title</span>: <span class="hljs-string">'bug总览'</span>,
          <span class="hljs-attr">department</span>: <span class="hljs-string">'开发一部'</span>
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">ant-desgin-vue表格提供的api</h1>
<p>ant-desigin-vue的table组件提供一个自定义渲染单元格的方法<code>customRender</code>，接收两个参数,一个<code>text</code>当前值，<code>row</code>当前行，我们可以根据我们业务需求对它进行操作，然后把它return 出去就能得到想要的效果</p>
<blockquote>
<p>表格支持行/列合并，使用 render 里的单元格属性 colSpan 或者 rowSpan 设值为 0 时，设置的表格不会渲染。</p>
</blockquote>
<p><a href="https://www.antdv.com/components/table-cn/#components-table-demo-colspan-and-rowspan" target="_blank" rel="nofollow noopener noreferrer">具体可以看下这个链接 <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec4d55c0e2a941718d2084dfd4dc79f3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p>所以先定义<code>columns</code>也就是表头格式</p>
<pre><code class="hljs language-js copyable" lang="js">    columns: [
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">''</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'title'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>,
          <span class="hljs-attr">customRender</span>: <span class="hljs-function">(<span class="hljs-params">text, row</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">children</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;text&#125;</span>`</span>,
              <span class="hljs-attr">attrs</span>: &#123;
                <span class="hljs-attr">rowSpan</span>: row.titleRowSpan
              &#125;
            &#125;
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'部门'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'department'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>,
          <span class="hljs-attr">customRender</span>: <span class="hljs-function">(<span class="hljs-params">text, row, index</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">children</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;text&#125;</span>`</span>,
              <span class="hljs-attr">attrs</span>: &#123;
                <span class="hljs-attr">rowSpan</span>: row.departmentRowSpan
              &#125;
            &#125;
          &#125;
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'代码类型'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'codeType'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'总数'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'totalCount'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'修复'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'fixCount'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'未修复'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'notFixedCount'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'今日新增'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'todayAdd'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>
        &#125;,
        &#123;
          <span class="hljs-attr">title</span>: <span class="hljs-string">'Bug类型'</span>,
          <span class="hljs-attr">dataIndex</span>: <span class="hljs-string">'bugType'</span>,
          <span class="hljs-attr">width</span>: <span class="hljs-number">120</span>,
          <span class="hljs-attr">customRender</span>: <span class="hljs-function">(<span class="hljs-params">text, row, index</span>) =></span> &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">children</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;text&#125;</span>`</span>,
              <span class="hljs-attr">attrs</span>: &#123;
                <span class="hljs-attr">rowSpan</span>: row.bugTypeRowSpan
              &#125;
            &#125;
          &#125;
        &#125;
      ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">合并单元格算法实现</h1>
<p>说下思路：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31e432685c554b428eeddbce363bea69~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实就是类似于双指针的思想</p>
<ol>
<li>需要两次循环，第一次循环<code>i</code>，作为合并单元格后的起始点，</li>
<li>第二次循环<code>j</code>是从起始点找下一个值是否是相同的值，如果相同则合并单元格,合并的数量就是<code>count</code>，然后把本次循环相同值的最后一个序号保存下来，第一次循环就从这个序号开始继续跑</li>
</ol>
<p>具体代码实现如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  合并单元格</span>
    <span class="hljs-function"><span class="hljs-title">combineRow</span>(<span class="hljs-params">key</span>)</span> &#123;
      <span class="hljs-keyword">const</span> tableData = <span class="hljs-built_in">this</span>.tableData
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < tableData.length; i++) &#123;
        <span class="hljs-keyword">const</span> item = tableData[i]
        <span class="hljs-keyword">let</span> count = <span class="hljs-number">1</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < tableData.length; j++) &#123;
          <span class="hljs-comment">// 如果是同一个值，往后递增</span>
          <span class="hljs-keyword">if</span> (item[key] === tableData[j][key]) &#123;
            count++
            <span class="hljs-comment">// 往后相同的值都设为空单元格</span>
            tableData[j][<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>RowSpan`</span>] = <span class="hljs-number">0</span>
            <span class="hljs-comment">// 只有同值第一个才设置合并的单元格数</span>
            item[<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>RowSpan`</span>] = count
            <span class="hljs-comment">// 所有都是为同一个值的情况</span>
            <span class="hljs-comment">// 如果到了尾部，则循环结束</span>
            <span class="hljs-keyword">if</span> (j === tableData.length - <span class="hljs-number">1</span>) &#123;
                <span class="hljs-keyword">return</span>
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 指针跳转到下一个，从下一排开始</span>
            i = j - <span class="hljs-number">1</span>
            count = <span class="hljs-number">1</span>
            tableData[j][<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span>RowSpan`</span>] = <span class="hljs-number">0</span>
            <span class="hljs-keyword">break</span>
          &#125;
        &#125;
      &#125;
      <span class="hljs-built_in">console</span>.log(tableData, <span class="hljs-string">'tabledata'</span>)
      <span class="hljs-built_in">this</span>.tableData = tableData
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们在<code>created</code>中调用</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.combineRow(<span class="hljs-string">'title'</span>) <span class="hljs-comment">// 合并title</span>
    <span class="hljs-built_in">this</span>.combineRow(<span class="hljs-string">'department'</span>) <span class="hljs-comment">// 合并部门</span>
    <span class="hljs-built_in">this</span>.combineRow(<span class="hljs-string">'bugType'</span>) <span class="hljs-comment">// 合并bug类型</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于过滤的效果，就不赘述了，很简单，往键盘上撒把米鸡都能给你敲出来，看下面代码就知道</p>
<h1 data-id="heading-4">效果展示</h1>
<p><a href="http://www.ssgxzt.club/demo/#/" target="_blank" rel="nofollow noopener noreferrer">代码也在这里，点击访问</a></p>
<h1 data-id="heading-5">写在最后</h1>
<p>其实这个需求麻烦在于数据转换上，那会儿后端给的数据太难处理了，非得让我搞个矩阵才能处理，相比之下合并单元格其实也还好，没那么难实现。。。</p></div>  
</div>
            