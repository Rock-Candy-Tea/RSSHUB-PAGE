
---
title: '使用ant design vue的日历组件，实现一个简单交易日与非交易日的切换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/424c7ea0cc2f40749b94921f538ce9ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 01:00:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/424c7ea0cc2f40749b94921f538ce9ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="image-20210320163944258.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/424c7ea0cc2f40749b94921f538ce9ca~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>需求：</p>
<ol>
<li>日历区分交易日、非交易日</li>
<li>可以切换面板查看整年交易日信息</li>
<li>可以在手动调整交易日、非交易日</li>
</ol>
</blockquote>
<h2 data-id="heading-0">演示实例</h2>
<p><img alt="a-calendar日历组件使用.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8afb265413324e56b7e4c668c082a350~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">序——使用软件及框架版本</h2>
<ol>
<li>vue 2.6.11</li>
<li>ant-design-vue 1.7.1</li>
<li>moment.js（日期转换依赖）</li>
</ol>
<h2 data-id="heading-2">设计思路</h2>
<ol>
<li>使用组件库的a-calendar标签可以实现一个日历的基本框架</li>
<li>每日模块实现交易日、非交易日的区分显示</li>
<li>以及过期和当日的日期灰色显示，且不能切换交易状态</li>
<li>将来的日期可以点击使用a-popconfirm标签来切换交易状态，或者使用右键点击切换</li>
</ol>
<h2 data-id="heading-3">具体代码过程</h2>
<h3 data-id="heading-4">1. template模板区域</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin: 0 auto"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"text-align: center"</span>></span>日历组件<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a-row</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"calendarContent"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin: 0 auto; width: 100%"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"calendarBox"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a-calendar</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">panelChange</span>=<span class="hljs-string">"panelChange"</span> @<span class="hljs-attr">select</span>=<span class="hljs-string">"selectDate"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"dateCellRender"</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"value"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"events"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in getListData(value)"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.date"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">a-tooltip</span>
                <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.date<nowDate || item.date == nowDate"</span>
              ></span>
                <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"title"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>只能在下个交易日才可设置<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cellBlockOld"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.date < nowDate"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag=='0'"</span>></span>交易日<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag=='1' && item.date !=next"</span>></span>非交易日<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cellBlockNow"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.date == nowDate"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag=='0' && item.date == nowDate"</span>></span>交易日<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag=='1' && item.date == nowDate"</span>></span>非交易日<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">a-tooltip</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">a-popconfirm</span>
                <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag == '1' && item.date>nowDate"</span>
                <span class="hljs-attr">title</span>=<span class="hljs-string">"设为交易日"</span>
                @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"setDate(0)"</span>
                @<span class="hljs-attr">cancel</span>=<span class="hljs-string">"cancel"</span>
              ></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cellBlockNext1"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag== '1'"</span>></span>非交易日
                <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">a-popconfirm</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">a-popconfirm</span>
                <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag == '0' && item.date>nowDate"</span>
                <span class="hljs-attr">title</span>=<span class="hljs-string">"设为非交易日"</span>
                @<span class="hljs-attr">confirm</span>=<span class="hljs-string">"setDate(1)"</span>
                @<span class="hljs-attr">cancel</span>=<span class="hljs-string">"cancel"</span>
              ></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"cellBlockNext0"</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag== '0' && item.date != next"</span>></span>交易日<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"item.workFlag== '0' && item.date == next"</span>></span>下一交易日
                <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">a-popconfirm</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">a-calendar</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">a-row</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意事项与难点：</strong></p>
<ol>
<li>
<p>a-calendar标签的数据绑定，与数据遍历逻辑，这里数据绑定在a- calendar标签上，日期面板的切换和选中日期的事件都在绑定在此；内层嵌套插槽渲染以一周7天渲染日期，绑定数据几乎不用变化，可以直接拿来用。</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">a-calendar</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"value"</span> @<span class="hljs-attr">panelChange</span>=<span class="hljs-string">"panelChange"</span> @<span class="hljs-attr">select</span>=<span class="hljs-string">"selectDate"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"dateCellRender"</span> <span class="hljs-attr">slot-scope</span>=<span class="hljs-string">"value"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"events"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in getListData(value)"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.date"</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">a-calendar</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>交易状态与样式的控制，在模板区域添加多个判断条件区分</p>
</li>
<li>
<p>嵌入<code>a-popconfirm</code>来通过气泡事件修改交易状态</p>
</li>
</ol>
<h3 data-id="heading-5">2. js区域</h3>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">import</span> moment <span class="hljs-keyword">from</span> <span class="hljs-string">'moment'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">components</span>: &#123;&#125;,
  <span class="hljs-attr">watch</span>: &#123;&#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: moment(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()),
      <span class="hljs-attr">dataList</span>: [
        &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'20210228'</span>,
          <span class="hljs-attr">workFlag</span>: <span class="hljs-string">'1'</span>
        &#125;,
        &#123;
          <span class="hljs-attr">date</span>: <span class="hljs-string">'20210301'</span>,
          <span class="hljs-attr">workFlag</span>: <span class="hljs-string">'0'</span>
        &#125;
        <span class="hljs-comment">// 此处省略造的数据，大家可以使用mock或者在data中造一些数据，此案例简单造了一个月的数据用与演示</span>
      ],
      <span class="hljs-attr">now</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(),
      <span class="hljs-attr">selectDateValue</span>: <span class="hljs-string">''</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    moment,
    panelChange (value) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'面板中点击、切换事件'</span>)
      <span class="hljs-built_in">console</span>.log(value)
      <span class="hljs-built_in">this</span>.value = value
    &#125;,
    selectDate (value) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'选中日期事件'</span>)
      <span class="hljs-built_in">console</span>.log(value)
      <span class="hljs-built_in">this</span>.selectDateValue = value.format(<span class="hljs-string">'YYYYMMDD'</span>)
    &#125;,
    <span class="hljs-comment">// 切换交易日与非交易日方法，切换交易状态的同时面板交易状态改变，同时向后台发送请求（自行添加请求）</span>
    setDate (val) &#123;
      <span class="hljs-built_in">console</span>.log(val)
      <span class="hljs-keyword">var</span> newDataList = []
      <span class="hljs-comment">// 此处大家可以思考一下，forEach和map两种方法对数组的操作</span>
      <span class="hljs-built_in">this</span>.dataList.forEach(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (e.date === <span class="hljs-built_in">this</span>.selectDateValue) &#123;
          e.workFlag = val
          newDataList.push(e)
        &#125; <span class="hljs-keyword">else</span> &#123;
          newDataList.push(e)
        &#125;
      &#125;)
      <span class="hljs-built_in">this</span>.dataList = newDataList
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.dataList)
    &#125;,
    cancel () &#123;

    &#125;,
    getListData (value) &#123;
      <span class="hljs-keyword">var</span> listData = []
      <span class="hljs-comment">// 注意事项1：通过比对日期确定将每日的交易状态与日历日期匹配</span>
      <span class="hljs-built_in">this</span>.dataList.forEach(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        <span class="hljs-comment">// 让数组与日历日期匹配</span>
        <span class="hljs-keyword">if</span> (e.date === value.format(<span class="hljs-string">'YYYYMMDD'</span>)) &#123;
          listData.push(e)
        &#125;
      &#125;)
      <span class="hljs-keyword">return</span> listData
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-attr">nowDate</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">const</span> nowDate = moment(<span class="hljs-built_in">this</span>.now).format(<span class="hljs-string">'YYYYMMDD'</span>)
      <span class="hljs-keyword">return</span> nowDate
    &#125;,
    <span class="hljs-attr">next</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> next
      <span class="hljs-keyword">var</span> nextDate = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-built_in">this</span>.now - <span class="hljs-number">0</span> + <span class="hljs-number">86400000</span>)
      next = moment(nextDate).format(<span class="hljs-string">'YYYYMMDD'</span>)
      <span class="hljs-keyword">return</span> next
    &#125;
  &#125;,
  created () &#123;
  &#125;,
  mounted () &#123;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">注意事项与难点：</h4>
<ol>
<li>通过比对日期确定每日的交易状态与日历日期匹配</li>
<li>修改交易状态的方法</li>
</ol>
<h2 data-id="heading-7">总结</h2>
<p>一个简单的日历组件就算搭建这样就基本完成了，具体代码可以到下面gitee里面看，如果有错误和改进的地方，欢迎大家指正交流。</p>
<h2 data-id="heading-8">Find me</h2>
<p>Gitee：<a href="https://gitee.com/heyhaiyon/ant-vue-admin.git" target="_blank" rel="nofollow noopener noreferrer">gitee.com/heyhaiyon/a…</a></p>
<p>微信公众号：heyhaiyang</p>
<p>掘金：<a href="https://juejin.cn/user/3113464436127608" target="_blank">heyhaiyang</a></p>
<p>博客园：<a href="https://www.cnblogs.com/heyhaiyang/" target="_blank" rel="nofollow noopener noreferrer">heyhaiyang</a></p>
<p>头条号：heyhaiyang</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            