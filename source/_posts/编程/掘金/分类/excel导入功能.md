
---
title: 'excel导入功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/255a5dd8f3d043a9b244e130a633c2dd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 08:00:04 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/255a5dd8f3d043a9b244e130a633c2dd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">需求</h1>
<p>我们一次性添加多个员工信息的时候, 需要我们开发一个批量导入的功能：将事先以excel格式保存的文件批量导入进来</p>
<ol>
<li>后端提供一个excel模板文件</li>
<li>用户填写这个excel模板文件</li>
<li>上传这个文件，实现批量导入功能</li>
</ol>
<h2 data-id="heading-1">方式</h2>
<h3 data-id="heading-2">前端主导（工作大量在前端）</h3>
<p>上传excel文件，把excel文件的内容读出来，还原成最基本的行列结构，按后端的接口要求回传过去。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/255a5dd8f3d043a9b244e130a633c2dd~tplv-k3u1fbpfcp-watermark.image" alt="image-20210424145350890.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前端读excel文件，调接口</p>
<h3 data-id="heading-3">后端主导（工作大量在后端）</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9284e33bc0c148bfa27092685bd87ab0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210424145557614.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前端上传excel文件</p>
<h1 data-id="heading-4">步骤</h1>
<h2 data-id="heading-5">安装插件</h2>
<blockquote>
<p>npm install xlsx -S</p>
</blockquote>
<h2 data-id="heading-6">引入UploadExcel组件并注册为全局</h2>
<ul>
<li>
<p>将vue-element-admin提供的组件复制到我们自己的项目 **<code>src/components/UploadExcel</code>**下</p>
</li>
<li>
<p>在index.js将它注册成全局组件</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> PageTools <span class="hljs-keyword">from</span> <span class="hljs-string">'./PageTools'</span>
<span class="hljs-keyword">import</span> UploadExcel <span class="hljs-keyword">from</span> <span class="hljs-string">'./UploadExcel'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// 插件的初始化, 插件给你提供的全局的功能, 都可以在这里配置</span>
  <span class="hljs-function"><span class="hljs-title">install</span>(<span class="hljs-params">Vue</span>)</span> &#123;
    <span class="hljs-comment">// 进行组件的全局注册</span>
    Vue.component(<span class="hljs-string">'PageTools'</span>, PageTools) <span class="hljs-comment">// 注册工具栏组件</span>
    Vue.component(<span class="hljs-string">'UploadExcel'</span>, UploadExcel) <span class="hljs-comment">// 注册导入excel组件</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">建立公共导入的页面路由</h2>
<p>新建一个公共的导入页面，即<strong>import路由组件</strong> <strong><code>src/views/import/index.vue</code></strong></p>
<p>在页面中使用前面封装的excel上传组件，并补充导入成功后的回调函数</p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">upload-excel</span> <span class="hljs-attr">:on-success</span>=<span class="hljs-string">"handleSuccess"</span> /></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Import'</span>,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleSuccess</span>(<span class="hljs-params">&#123; header, results &#125;</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(header, results)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">配置路由</h2>
<p>这个路由不需要根据权限控制，直接定义为静态路由即可。在**<code>src/router/index.js</code>**下的静态路由中添加一个路由</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/import'</span>,
    <span class="hljs-attr">component</span>: Layout,
    <span class="hljs-attr">hidden</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 不显示到左侧菜单</span>
    <span class="hljs-attr">children</span>: [&#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">''</span>, 
      <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/import'</span>)
    &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">excel导入-数据处理</h2>
<p>据格式转换：将excel解析好的数据经过处理后，转成可以传给接口调用的数据</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9c43c04f7f44331a3c5caed4637e387~tplv-k3u1fbpfcp-watermark.image" alt="image-20210521122501810.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调用接口进行excel上传的<strong>重点其实是数据的处理</strong>，我们需要按照接口的要求，把excel表格中经过插件处理好的数据处理成后端接口要求的格式</p>
<h3 data-id="heading-10">后端接口示例格式</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/682d4465373b42ac82eca5dede93ce6a~tplv-k3u1fbpfcp-watermark.image" alt="uploadData.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">字段中文转英文</h3>
<p>excel中读入的是姓名,而后端是username</p>
<p>为了方便维护代码，单独封装一个方法来实现这个转换的功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
     * results excel表格的内容
      // [
          &#123;'姓名'：'小张'， '手机号': '13712345678'&#125;
        , &#123;.....&#125;
        ]

      // 目标
      // [ &#123;'username'：'小张'，'mobile': '13712345678'&#125;, &#123;.....&#125; ]
     */</span>
    <span class="hljs-comment">// 把一个对象数组中的每个对象的属性名，从中文改成英文</span>
    <span class="hljs-comment">// 思路：对于原数组每个对象来说</span>
    <span class="hljs-comment">//    （1） 找出所有的中文key</span>
    <span class="hljs-comment">//     (2)  得到对应的英文key</span>
    <span class="hljs-comment">//     (3)  拼接一个新对象： 英文key:值</span>
    <span class="hljs-function"><span class="hljs-title">transExcel</span>(<span class="hljs-params">results</span>)</span> &#123;
      <span class="hljs-keyword">const</span> mapInfo = &#123;
        <span class="hljs-string">'入职日期'</span>: <span class="hljs-string">'timeOfEntry'</span>,
        <span class="hljs-string">'手机号'</span>: <span class="hljs-string">'mobile'</span>,
        <span class="hljs-string">'姓名'</span>: <span class="hljs-string">'username'</span>,
        <span class="hljs-string">'转正日期'</span>: <span class="hljs-string">'correctionTime'</span>,
        <span class="hljs-string">'工号'</span>: <span class="hljs-string">'workNumber'</span>,
        <span class="hljs-string">'部门'</span>: <span class="hljs-string">'departmentName'</span>,
        <span class="hljs-string">'聘用形式'</span>: <span class="hljs-string">'formOfEmployment'</span>
      &#125;
      <span class="hljs-keyword">return</span> results.map(<span class="hljs-function"><span class="hljs-params">zhObj</span> =></span> &#123;
        <span class="hljs-keyword">const</span> enObj = &#123;&#125;
        <span class="hljs-keyword">const</span> zhKeys = <span class="hljs-built_in">Object</span>.keys(zhObj) <span class="hljs-comment">// ['姓名', '手机号']</span>

        zhKeys.forEach(<span class="hljs-function"><span class="hljs-params">zhKey</span> =></span> &#123;
          <span class="hljs-keyword">const</span> enKey = mapInfo[zhKey]

          enObj[enKey] = zhObj[zhKey]
        &#125;)

        <span class="hljs-keyword">return</span> enObj
      &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">日期处理</h3>
<p>从excel中读到的时间是number值,而后端是标准日期</p>
<p>excel内部进行特殊的编码导致<strong>变形</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0e55b3d43a64cd896a0816c7dc6db8a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210701100438730.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>借助公式还原</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 把excel文件中的日期格式的内容转回成标准时间</span>
<span class="hljs-comment">// https://blog.csdn.net/qq_15054679/article/details/107712966</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">formatExcelDate</span>(<span class="hljs-params">numb, format = <span class="hljs-string">'/'</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>((numb - <span class="hljs-number">25567</span>) * <span class="hljs-number">24</span> * <span class="hljs-number">3600000</span> - <span class="hljs-number">5</span> * <span class="hljs-number">60</span> * <span class="hljs-number">1000</span> - <span class="hljs-number">43</span> * <span class="hljs-number">1000</span> - <span class="hljs-number">24</span> * <span class="hljs-number">3600000</span> - <span class="hljs-number">8</span> * <span class="hljs-number">3600000</span>)
  time.setYear(time.getFullYear())
  <span class="hljs-keyword">const</span> year = time.getFullYear() + <span class="hljs-string">''</span>
  <span class="hljs-keyword">const</span> month = time.getMonth() + <span class="hljs-number">1</span> + <span class="hljs-string">''</span>
  <span class="hljs-keyword">const</span> date = time.getDate() + <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (format && format.length === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> year + format + month + format + date
  &#125;
  <span class="hljs-keyword">return</span> year + (month < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + month : month) + (date < <span class="hljs-number">10</span> ? <span class="hljs-string">'0'</span> + date : date)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            