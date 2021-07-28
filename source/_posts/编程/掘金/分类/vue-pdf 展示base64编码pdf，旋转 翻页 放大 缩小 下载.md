
---
title: 'vue-pdf 展示base64编码pdf，旋转 翻页 放大 缩小 下载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cafc6cd64f374f89b8be69e996c9674a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 18:39:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cafc6cd64f374f89b8be69e996c9674a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先看一下是不是大家需要的效果
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cafc6cd64f374f89b8be69e996c9674a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
首先安装vue-pdf</p>
<p>yarn add vue-pdf</p>
<p>然后写一个组件</p>
<pre><code class="hljs language-html copyable" lang="html">AppPdf.vue


<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pdf"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"24"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align:center"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"pdfSrc"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-pre"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"clock"</span>></span>顺时针<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-next"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"counterClock"</span>></span>逆时针<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-pre"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"prePage"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"preDisable"</span>></span>上一页<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-next"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"nextPage"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"nextDisable"</span>></span>下一页<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;select:idx==0&#125;"</span> @<span class="hljs-attr">touchstart</span>=<span class="hljs-string">"idx=0"</span> @<span class="hljs-attr">touchend</span>=<span class="hljs-string">"idx=-1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"scaleD"</span>></span>放大 <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;select:idx==1&#125;"</span> @<span class="hljs-attr">touchstart</span>=<span class="hljs-string">"idx=1"</span> @<span class="hljs-attr">touchend</span>=<span class="hljs-string">"idx=-1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"scaleX"</span>></span>缩小<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fileDownload(pdfUrl,'pdf文件')"</span>></span>下载<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123; pageNum &#125;&#125;/&#123;&#123; pageTotalNum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-row</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">pdf</span>
        <span class="hljs-attr">ref</span>=<span class="hljs-string">"pdf"</span>
        <span class="hljs-attr">:src</span>=<span class="hljs-string">"pdfSrc"</span>
        <span class="hljs-attr">:page</span>=<span class="hljs-string">"pageNum"</span>
        <span class="hljs-attr">:rotate</span>=<span class="hljs-string">"pageRotate"</span>
        @<span class="hljs-attr">password</span>=<span class="hljs-string">"password"</span>
        @<span class="hljs-attr">progress</span>=<span class="hljs-string">"loadedRatio = $event"</span>
        @<span class="hljs-attr">page-loaded</span>=<span class="hljs-string">"pageLoaded($event)"</span>
        @<span class="hljs-attr">num-pages</span>=<span class="hljs-string">"pageTotalNum=$event"</span>
        @<span class="hljs-attr">error</span>=<span class="hljs-string">"pdfError($event)"</span>
        @<span class="hljs-attr">link-clicked</span>=<span class="hljs-string">"page = $event"</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">pdf</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">el-row</span> <span class="hljs-attr">:gutter</span>=<span class="hljs-string">"24"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align:center"</span> <span class="hljs-attr">v-show</span>=<span class="hljs-string">"pdfSrc"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;&#123; pageNum &#125;&#125;/&#123;&#123; pageTotalNum &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-pre"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"clock"</span>></span>顺时针<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-next"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"counterClock"</span>></span>逆时针<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-pre"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"prePage"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"preDisable"</span>></span>上一页<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn-def btn-next"</span> @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"nextPage"</span> <span class="hljs-attr">:disabled</span>=<span class="hljs-string">"nextDisable"</span>></span>下一页<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;select:idx==0&#125;"</span> @<span class="hljs-attr">touchstart</span>=<span class="hljs-string">"idx=0"</span> @<span class="hljs-attr">touchend</span>=<span class="hljs-string">"idx=-1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"scaleD"</span>></span>放大 <span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;select:idx==1&#125;"</span> @<span class="hljs-attr">touchstart</span>=<span class="hljs-string">"idx=1"</span> @<span class="hljs-attr">touchend</span>=<span class="hljs-string">"idx=-1"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"scaleX"</span>></span>缩小<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">el-button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fileDownload(pdfUrl)"</span>></span>下载<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">el-row</span>></span>
    <span class="hljs-comment"><!-- <div>进度：&#123;&#123; loadedRatio &#125;&#125;</div>
    <div>页面加载成功: &#123;&#123; curPageNum &#125;&#125;</div> --></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> pdf <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-pdf'</span>
  <span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/index'</span>
  <span class="hljs-keyword">import</span> notification <span class="hljs-keyword">from</span> <span class="hljs-string">'ant-design-vue/es/notification'</span>

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'AppPdf'</span>,
    <span class="hljs-attr">components</span>: &#123;
      pdf
    &#125;,
    <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">pdfSrc</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;,
            <span class="hljs-attr">fileName</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;,
            <span class="hljs-attr">fid</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;,
            <span class="hljs-attr">loadData</span>: &#123;
                <span class="hljs-attr">type</span>: <span class="hljs-built_in">Function</span>,
                <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
            &#125;
        &#125;,
    data () &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">preDisable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">nextDisable</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">pdfUrl</span>: <span class="hljs-string">''</span>,
        <span class="hljs-attr">pageNum</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">pageTotalNum</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">pageRotate</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">loadedRatio</span>: <span class="hljs-number">0</span>, <span class="hljs-comment">// 加载进度</span>
        <span class="hljs-attr">curPageNum</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">scale</span>: <span class="hljs-number">100</span>, <span class="hljs-comment">// 放大系数</span>
        <span class="hljs-attr">idx</span>: -<span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
            pdfSrc () &#123;
                <span class="hljs-built_in">this</span>.curPageNum = <span class="hljs-number">1</span>
                <span class="hljs-built_in">this</span>.pageNum = <span class="hljs-number">1</span>
            &#125;,
            fileName () &#123;
            &#125;,
            pageNum () &#123;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pageNum === <span class="hljs-number">1</span>) &#123;
                    <span class="hljs-built_in">this</span>.preDisable = <span class="hljs-literal">true</span>
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">this</span>.preDisable = <span class="hljs-literal">false</span>
                &#125;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pageNum === <span class="hljs-built_in">this</span>.pageTotalNum) &#123;
                    <span class="hljs-built_in">this</span>.nextDisable = <span class="hljs-literal">true</span>
                    <span class="hljs-comment">// 请求记录接口，保存已读记录</span>
                    <span class="hljs-built_in">this</span>.$http
                        .post(api.ImportantFile, &#123;
                            <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">fid</span>: <span class="hljs-built_in">this</span>.fid &#125;
                        &#125;)
                        .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                            <span class="hljs-keyword">if</span> (res) &#123;
                                <span class="hljs-built_in">this</span>.$message(&#123;
                                    <span class="hljs-attr">message</span>: <span class="hljs-string">'已读 '</span> + <span class="hljs-built_in">this</span>.fileName,
                                    <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>
                                &#125;)
                                <span class="hljs-built_in">this</span>.loadData()
                            &#125;
                        &#125;)
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-built_in">this</span>.nextDisable = <span class="hljs-literal">false</span>
                &#125;
            &#125;
        &#125;,

    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-comment">// 下载PDF</span>
      fileDownload (data) &#123;
        <span class="hljs-keyword">const</span> filename = <span class="hljs-built_in">this</span>.fileName || <span class="hljs-string">'报表.xls'</span>
        <span class="hljs-keyword">var</span> element = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'a'</span>)
        element.setAttribute(<span class="hljs-string">'href'</span>, <span class="hljs-built_in">encodeURI</span>(<span class="hljs-built_in">this</span>.pdfSrc))
        element.setAttribute(<span class="hljs-string">'download'</span>, <span class="hljs-string">'LoginInquiry.pdf'</span>)
        element.setAttribute(<span class="hljs-string">'download'</span>, filename)
        element.style.display = <span class="hljs-string">'none'</span>
        <span class="hljs-built_in">document</span>.body.appendChild(element)
        element.click()
        <span class="hljs-built_in">document</span>.body.removeChild(element)
      &#125;,
      <span class="hljs-comment">// 放大</span>
      scaleD () &#123;
        <span class="hljs-built_in">this</span>.scale += <span class="hljs-number">5</span>
        <span class="hljs-built_in">this</span>.$refs.pdf.$el.style.width = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.scale) + <span class="hljs-string">'%'</span>
      &#125;,

      <span class="hljs-comment">// 缩小</span>
      scaleX () &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.scale === <span class="hljs-number">100</span>) &#123;
          <span class="hljs-keyword">return</span>
        &#125;
        <span class="hljs-built_in">this</span>.scale += -<span class="hljs-number">5</span>
        <span class="hljs-built_in">this</span>.$refs.pdf.$el.style.width = <span class="hljs-built_in">parseInt</span>(<span class="hljs-built_in">this</span>.scale) + <span class="hljs-string">'%'</span>
      &#125;,
      prePage () &#123;
        <span class="hljs-keyword">var</span> p = <span class="hljs-built_in">this</span>.pageNum
        p = p > <span class="hljs-number">1</span> ? p - <span class="hljs-number">1</span> : <span class="hljs-built_in">this</span>.pageTotalNum
        <span class="hljs-built_in">this</span>.pageNum = p
      &#125;,
      nextPage () &#123;
        <span class="hljs-keyword">var</span> p = <span class="hljs-built_in">this</span>.pageNum
        p = p < <span class="hljs-built_in">this</span>.pageTotalNum ? p + <span class="hljs-number">1</span> : <span class="hljs-number">1</span>
        <span class="hljs-built_in">this</span>.pageNum = p
      &#125;,
      clock () &#123;
        <span class="hljs-built_in">this</span>.pageRotate += <span class="hljs-number">90</span>
      &#125;,
      counterClock () &#123;
        <span class="hljs-built_in">this</span>.pageRotate -= <span class="hljs-number">90</span>
      &#125;,
      password (updatePassword, reason) &#123;
        updatePassword(prompt(<span class="hljs-string">'password is "123456"'</span>))
      &#125;,
      pageLoaded (e) &#123;
        <span class="hljs-built_in">this</span>.curPageNum = e
      &#125;,
      pdfError (error) &#123;
        <span class="hljs-built_in">console</span>.error(error)
      &#125;,
      pdfPrintAll () &#123;
        <span class="hljs-built_in">this</span>.$refs.pdf.print()
      &#125;,
      pdfPrint () &#123;
        <span class="hljs-built_in">this</span>.$refs.pdf.print(<span class="hljs-number">100</span>, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>])
      &#125;
    &#125;,
    updated () &#123;
        <span class="hljs-comment">// 在只有一页的时候，直接已读</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pdfSrc) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pageTotalNum === <span class="hljs-number">1</span>) &#123;
                <span class="hljs-comment">// 请求记录接口，保存已读记录</span>
                <span class="hljs-built_in">this</span>.$http
                    .post(api.ImportantFile, &#123;
                        <span class="hljs-attr">params</span>: &#123; <span class="hljs-attr">fid</span>: <span class="hljs-built_in">this</span>.fid &#125;
                    &#125;)
                    .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                        <span class="hljs-keyword">if</span> (res) &#123;
                            notification.success(&#123;
                                <span class="hljs-attr">message</span>: <span class="hljs-string">'完成'</span>,
                                <span class="hljs-attr">description</span>: <span class="hljs-string">'已读 '</span> + <span class="hljs-built_in">this</span>.fileName
                            &#125;)
                            <span class="hljs-comment">// this.$message(&#123;</span>
                            <span class="hljs-comment">//     message: '已读 ' + this.fileName,</span>
                            <span class="hljs-comment">//     type: 'success'</span>
                            <span class="hljs-comment">// &#125;)</span>
                            <span class="hljs-built_in">this</span>.loadData()
                        &#125;
                    &#125;)
            &#125;
        &#125;
    &#125;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在需要用到它的地方引入它</p>
<pre><code class="hljs language-html copyable" lang="html">  import AppPdf from './AppPdf.vue'
  <span class="hljs-tag"><<span class="hljs-name">app-pdf</span> <span class="hljs-attr">:pdfSrc</span>=<span class="hljs-string">"base64Str"</span> <span class="hljs-attr">:fileName</span>=<span class="hljs-string">"fileName"</span> <span class="hljs-attr">:fid</span>=<span class="hljs-string">"fid"</span> <span class="hljs-attr">:loadData</span>=<span class="hljs-string">"loadData"</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"son"</span>></span><span class="hljs-tag"></<span class="hljs-name">app-pdf</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            