
---
title: 'chrome插件开发-自动化脚本(4)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44bd4ec8b5da43539bf273af7669d5ca~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 18:55:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44bd4ec8b5da43539bf273af7669d5ca~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>接上一篇文章 <a href="https://juejin.cn/post/6973905015320625189" target="_blank">chrome插件开发-自动化脚本(3)</a></p>
<h3 data-id="heading-0">导入导出脚本</h3>
<p>使用<code>sheet.js js-xlsx库</code>可以很方便的实现导入导出功能.</p>
<ol>
<li>导出功能</li>
</ol>
<p>为了方便不同人员录制的脚本可以分享实现了这一功能,也是为了之后的批量导入脚本.导出的文件格式如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44bd4ec8b5da43539bf273af7669d5ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以在脚本中设置多个自定义字段,为了方便使用并不和固定字段冲突,尽量用中文命名.</p>
<p><code>自定义字段</code>只能在<code>set-input-value</code>事件中设置, 设置的方法为<code>设置字段key</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e536729f41fa40c6adb45663d50d2907~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_16239793523106.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">exportScript () &#123;
  // 创建一个工作薄
  let workBook = XLSX.utils.book_new()

  // 一个脚本一个sheet 方便之后批量导入运行
  this.caseList.forEach(item => &#123;
    // 创建sheet对象
    let sheetData = []
    let headers = JSON.parse(JSON.stringify(fixedHeader))
    // 抽出 eventList 输入事件中定义字段名称的列
    item.eventList
      .filter(event => event.type === 'set-input-value' && event.key && !headers.includes(event.key))
      .forEach(event => &#123;
        item[event.key] = event.value
        headers.unshift(event.key)
      &#125;)
    let caseRow = &#123;
      ...item,
      eventList: JSON.stringify(item.eventList)
    &#125;
    if (Array.isArray(item.responseConfig)) &#123;
      caseRow.responseConfig = JSON.stringify(item.responseConfig)
    &#125;
    sheetData.push(caseRow)

    let sheet = XLSX.utils.json_to_sheet(sheetData, &#123;header: headers&#125;)

    // 在工作簿中添加sheet页
    XLSX.utils.book_append_sheet(workBook, sheet, item.name)
  &#125;)

  // 转化格式，导出文件
  // 创建工作薄blob
  const workbookBlob = workbook2blob(workBook)
  // 导出工作薄
  openDownloadDialog(workbookBlob, '自动化脚本.xlsx')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>导入功能</li>
</ol>
<p>有些场景可能需要重复执行脚本, 没有批量导入的话,需要每次去修改<code>自定义字段</code>,如果设置了很多的话改起来会很麻烦. 我们可以在xlsx文件中先编辑好再直接导入进去,像这样
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2692a9869b5a42f58531f757d30342bc~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_16239798235768.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>导入后的devtool:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23c131e34104405380932402060a9695~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_16239799523785.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解析xlsx的代码</p>
<pre><code class="copyable">importScript (file) &#123;
  readWorkbookFromLocalFile(file, wb => &#123;
    /**
     * workBook => caseList:[]
     * 1. 先把sheets循环,知道有几个脚本
     * 2. 再把每个sheet中有几行循环, 知道每个脚本有几个用例
     * 3. 再整合成一个大的caseList
     */
    let caseList = []
    wb.SheetNames.forEach(sheetName => &#123;
      let xlsxData = XLSX.utils.sheet_to_json(wb.Sheets[sheetName])
      let allKeyList = getHeaderKeyList(wb.Sheets[sheetName])
      let customKeyList = allKeyList.filter(key => !fixedHeader.includes(key))
      let baseCaseDetail = &#123;&#125;
      let baseEventList = []
      xlsxData.forEach((data, index)=> &#123;
        // 表格里可以只保留第一行的脚本数据 其他行配置变量 节省空间
        if (index === 0) &#123;
          baseCaseDetail = &#123;
            name: data.name,
            urlPath: data.urlPath,
            width: data.width,
            height: data.height
          &#125;
          if (data.responseConfig && data.responseConfig.length > 5) &#123;
            baseCaseDetail.responseConfig = JSON.parse(data.responseConfig)
          &#125;
          try &#123;
            baseEventList = JSON.parse(data.eventList) || []
          &#125; catch (e) &#123;
            console.error('解析eventList失败', e)
          &#125;
        &#125;
        // 处理eventList 把变量塞进去
        let eventList = []
        baseEventList.forEach(event => &#123;
          if (event.type === 'set-input-value' && customKeyList.includes(event.key)) &#123;
            event.value = data[event.key]
          &#125;
          eventList.push(event)
        &#125;)
        caseList.push(&#123;
          ...baseCaseDetail,
          name: baseCaseDetail.name + '-' + index,
          eventList: JSON.parse(JSON.stringify(eventList))
        &#125;)
      &#125;)
    &#125;)
    this.$store.commit('setCaseList', caseList)
    this.importFlag = true
  &#125;)
  return false
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">单个脚本-不同变量多次运行</h3>
<p>使用场景: 各个网站表单自动输入提交, 上面的导入功能已包含这个功能</p>
<h3 data-id="heading-2">公司网站 传参调用 第三方网站的脚本</h3>
<p>本次优化最大的功能就是这个了, 可以有很多想象的空间, 由于我们公司是做人力资源外包的, 办理人员一直需要在<code>政府社保网站</code>操作人员的入职,转入,封存,启封 这种频繁的操作. 所以想做这个功能节省人员的工作量,并且提高效率.</p>
<h4 data-id="heading-3">第一步 配置<code>manifest.json</code></h4>
<p><code>externally_connectable</code>字段定义可以直接使用 <code>chrome.*</code> api的站点,通配符配置有一些是不支持的,所以域名需要精确一点.</p>
<pre><code class="copyable">"externally_connectable": &#123;
  "matches": ["http://localhost:63342/*"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">第二步 网页中通知第三方网站执行哪个脚本</h4>
<p>这里我们要知道用什么方式通知第三方网站, 首先第三方网站需要打开<code>devtool</code>工具我们才能执行脚本.</p>
<p>然后就可以在配置页面使用 chrome.* api 发消息给 background.js</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>本地测试页面</title>
</head>
<body>
<div>
  <span>tabId</span> <input id="tabId" value="759"/>
</div>
<div>
  <span>脚本名称</span> <input id="name" value="掘金搜索"/>
</div>
<div>
  <span>搜索关键字</span> <input id="key" value="哈哈"/>
</div>
<button id="button-1">调用其他页面脚本</button>
<div>
  <span>执行结果</span> <pre id="response"></pre>
</div>
<script src="autoScript/js/jquery-1.8.3.js"></script>
<script>

  $('#button-1').on('click', sendMessage)
  function sendMessage () &#123;
    let editorExtensionId = 'odfckenjjgjokihccfabfoecjclggmka'
    let tabId = $('#tabId')[0].value
    let name = $('#name')[0].value
    let key = $('#key')[0].value
    chrome.runtime.sendMessage(
      editorExtensionId,
      &#123;tabId: tabId, data: &#123;type: 'run-case', name: name, customKey: &#123;'搜索关键字': key&#125;&#125;&#125;,
      (response) => &#123;
        $('#response').text(JSON.stringify(response, null, 2))
        console.log(response.success)
      &#125;
    )
  &#125;
</script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">第三步 background.js 分发请求</h4>
<p>这部分相对简单, 不使用长连接postMessage因为不能回调,不能很方便的通知到原网页请求的结果.</p>
<pre><code class="copyable">// 监听externally_connectable配置的正常网页发送的消息
chrome.runtime.onMessageExternal.addListener(function(request, sender, sendResponse) &#123;
  if (request.tabId in connections) &#123;
    // 不使用长连接发送消息 原因是不能设置回调
    // connections[request.tabId].postMessage(request.data)

    chrome.runtime.sendMessage(request, response => &#123;
      sendResponse(response)
    &#125;)
    return true // 返回 true 表示是异步回调
  &#125; else &#123;
    sendResponse(&#123;error: 'onMessageExternal Tab not found in connection list.'&#125;)
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">第四步 第三方网页的 devtool 监听消息 执行并返回</h4>
<pre><code class="copyable">Main.vue
 /**
 * 长连接没有sendResponse回调, 所以使用这种方式回调
 */
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => &#123;
  let message = msg.data
  console.log('devtool chrome.runtime.onMessage', msg)
  if (+msg.tabId === +chrome.devtools.inspectedWindow.tabId && message) &#123;
    switch (message.type) &#123;
      case 'run-case':
        // 1. 找到脚本 并替换变量
        // 2. 执行脚本
        let index = this.caseList.findIndex(item => item.name === message.name)
        if (index < 0) &#123;return&#125;
        let newCase = JSON.parse(JSON.stringify(this.caseList[index]))
        newCase.eventList = newCase.eventList.map(event => &#123;
          if (event.type === 'set-input-value' && event.key in message.customKey) &#123;
            event.value = message.customKey[event.key]
          &#125;
          return event
        &#125;)
        Vue.set(this.caseList, index, newCase)
        this.$EventBus.$emit('run-case', &#123;index, sendResponse&#125;) // 发送给真正执行的页面
        return true
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">home.vue

this.$EventBus.$on('run-case', async (&#123;index, sendResponse&#125;) => &#123;
  await this.runCase(index)
  sendResponse(this.result[this.caseList[index].name])
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止, 我们就可以在自己做的页面上调用其他网页上已经录制过的脚本了.</p>
<h3 data-id="heading-7">完整演示</h3>
<p><a href="https://www.bilibili.com/video/BV1g5411T7JL/" target="_blank" rel="nofollow noopener noreferrer">导入导出演示</a></p>
<p><a href="https://www.bilibili.com/video/BV1864y1r73e/" target="_blank" rel="nofollow noopener noreferrer">调用第三方网站脚本演示</a></p></div>  
</div>
            