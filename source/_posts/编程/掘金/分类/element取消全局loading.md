
---
title: 'element取消全局loading'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1424'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 02:06:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=1424'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">element-ui取消全局loading</h1>
<h2 data-id="heading-1">背景</h2>
<p>前两天在开发一个管理后台项目时， 遇到了一个问题，后端接口返回特别慢，由于该接口调用的是第三方API，无法通过后端去处理。此时想到用loading动画，但随之而来也产生了不少问题， 在此记录一下以方便大家能够遇到此类问题可以借鉴。</p>
<h2 data-id="heading-2">处理方案</h2>
<h3 data-id="heading-3">在表格内添加loading</h3>
<pre><code class="hljs language-vue copyable" lang="vue">      <el-table
        v-loading="loading"
        :data="tableData"
        border
        tooltip-effect="dark"
        :row-class-name="tableRowClassName"
        style="margin-top: 20px"
      >
      ...
      </el-table>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此种方式很简单，在请求开始前设置loading为true，结束后设置为false。element官网也有详细的概述，在此不过多描述。</p>
<h3 data-id="heading-4">在全局内容容器内添加动画</h3>
<p>第一种方式确实简单，但开发后UI效果并不是特别理想，所以考虑在内容容器内添加loading。此时使用了以服务的方式加载loading。</p>
<p>但此时也出现了一些问题， 首先在请求开始后，立即切换到其它页面，此时还在显示全局loading。</p>
<p>而且再次切回该页面又会再次发起请求，loading显示位置也不正常。
切换路由是要取消请求和loading的，我们需要在组件路由生命周期内进行监听。在离开此路由时，取消此次请求。</p>
<p>以下为具体代码：</p>
<p>离开路由生命周期</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">beforeRouteLeave</span>(<span class="hljs-params">to, <span class="hljs-keyword">from</span>, next</span>)</span> &#123;
    <span class="hljs-comment">// 导航离开该组件的对应路由时调用</span>
    <span class="hljs-comment">// 可以访问组件实例 `this`</span>
    <span class="hljs-built_in">this</span>.source.cancel(<span class="hljs-string">"离开此页面取消请求"</span>);
    next();
  &#125;,
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请求事件</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">getTable</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> CancelToken = axios.CancelToken;
      <span class="hljs-built_in">this</span>.source = CancelToken.source();
      <span class="hljs-keyword">const</span> options = &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">".el-main"</span>,
        <span class="hljs-attr">text</span>: <span class="hljs-string">"拼命加载中..."</span>,
        <span class="hljs-attr">spinner</span>: <span class="hljs-string">"el-icon-loading"</span>,
        <span class="hljs-attr">lock</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">background</span>: <span class="hljs-string">"rgba(255,255,255,0.4)"</span>,
      &#125;;
      <span class="hljs-keyword">const</span> loadingInstance = <span class="hljs-built_in">this</span>.$loading(options);
      <span class="hljs-built_in">this</span>.axios
        .post(
          <span class="hljs-string">"***"</span>,
          qs.stringify(&#123;
            <span class="hljs-attr">name</span>: <span class="hljs-built_in">this</span>.q,
            <span class="hljs-attr">page</span>: <span class="hljs-built_in">this</span>.listQuery.page,
          &#125;),
          &#123;
            <span class="hljs-attr">cancelToken</span>: <span class="hljs-built_in">this</span>.source.token,
          &#125;
        )
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-built_in">this</span>.tableData = res.data.data;
          <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 以服务的方式调用的 Loading 需要异步关闭</span>
            loadingInstance.close();
          &#125;);
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">thrown</span>) =></span> &#123;
          <span class="hljs-comment">// 如果请求被取消则进入该方法判断</span>
          <span class="hljs-keyword">if</span> (axios.isCancel(thrown)) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Request canceled"</span>, thrown.message);
            <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
              <span class="hljs-comment">// 以服务的方式调用的 Loading 需要异步关闭</span>
              loadingInstance.close();
            &#125;);
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// handle error</span>
          &#125;
        &#125;);
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在离开页面的同时取消请求，关闭loading动画。</p>
<h2 data-id="heading-5">感悟</h2>
<p>此次为了追求用户体验感更好，为此也走了不少的弯路，但我觉得还是很有意义的。同时也学到了不少新东西，如怎么取消一个请求等。还是很有收获的。</p></div>  
</div>
            