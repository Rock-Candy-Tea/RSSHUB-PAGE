
---
title: '【uni-app】封装常用方法以及全局数据'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8459'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 20:17:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=8459'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">文章介绍</h1>
<ol>
<li>通用工具方法、全局数据</li>
<li>以下定义的所有方法、计算属性，均会被挂载到所有 .vue 页面的 this 上</li>
</ol>
<p>注意：小程序端，计算属性会以数据对象的形式挂载到所有页面的 Page 对象中
因此，数据量较大的情况下，为优化性能请使用调用方法动态获取的形式，避免占用太多内存</p>
<h2 data-id="heading-1">（1）onBackPress</h2>
<p>介绍: 【App 平台】点击返回键后移除 loading，防止某个页面出错按返回键后还有 loading</p>
<pre><code class="copyable">// #ifdef APP-VUE

 onBackPress() &#123;
uni.hideLoading()
    &#125;
       
// #endif     ----结束条件编译
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">methods</h1>
<h1 data-id="heading-3">路由跳转类方法</h1>
<h2 data-id="heading-4">（2）SET_PARAM</h2>
<p>介绍: 暂存一个跨页面变量 （与 <code>GET_PARAM</code> 成对使用）</p>
<pre><code class="copyable"> SET_PARAM(val) &#123;
this.SET_GLOBAL('pageParam', val)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">（3）GET_PARAM</h2>
<p>介绍: 获取之前暂存的跨页面变量 （与 <code>SET_PARAM</code> 成对使用）</p>
<pre><code class="copyable"> GET_PARAM() &#123;
return this.GET_GLOBAL('pageParam')
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">（4）NAV_TO</h2>
<p>介绍: 进入某个页面</p>
<pre><code class="copyable">NAV_TO(url, param, usePageParam) &#123;
uni.navigateTo(&#123;
url: this.handleNav(url, param, usePageParam)
  &#125;)
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">（5）NAV_BACK</h2>
<p>介绍: 返回上个页面----<code>delta 参数为返回的次数</code></p>
<pre><code class="copyable">NAV_BACK(delta = 1) &#123;
uni.navigateBack(&#123;
delta
 &#125;)
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">（6）JUMP_TO</h2>
<p>介绍: 跳转到某个页面，跳转后无法返回</p>
<pre><code class="copyable">JUMP_TO(url, param, usePageParam) &#123;
uni.redirectTo(&#123;
url: this.handleNav(url, param, usePageParam)
        &#125;)
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">（7）TAB_TO</h2>
<p>介绍: 转到某个 Tab 页</p>
<pre><code class="copyable">TAB_TO(url, param) &#123;
uni.switchTab(&#123;
url: this.handleNav(url, param, true)
        &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">（8）RELAUNCH_TO</h2>
<p>介绍: 重启应用，跳转到指定页面</p>
<pre><code class="copyable">RELAUNCH_TO(url) &#123;
uni.reLaunch(&#123;
url
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">（9）GET_GLOBAL</h2>
<p>介绍: 获取一个全局变量----<code>key 为键名</code></p>
<pre><code class="copyable">GET_GLOBAL(key) &#123;
return this.$store.state[key]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">（10）SET_GLOBAL</h2>
<p>介绍: 设置一个全局变量----<code>key 为键名</code>----<code>val 为值</code></p>
<pre><code class="copyable">SET_GLOBAL(key, val) &#123;
this.$store.commit(key, val)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">（11）CLEAR_GLOBAL</h2>
<p>介绍: 清空全局变量</p>
<pre><code class="copyable">CLEAR_GLOBAL() &#123;
this.$store.commit('clear')
uni.removeStorageSync('token')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">（12）SET_STORAGE</h2>
<p>介绍: 将数据写入本地缓存</p>
<pre><code class="copyable">SET_STORAGE(key, data) &#123;
if (data === null) &#123;
uni.removeStorageSync(key)
&#125; else &#123;
uni.setStorageSync(key, data)
&#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">（13）GET_STORAGE</h2>
<p>介绍: 获取之前写入本地缓存的数据</p>
<pre><code class="copyable">GET_STORAGE(key) &#123;
return uni.getStorageSync(key)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">（14）CLEAR_STORAGE</h2>
<p>介绍: 清空本地缓存</p>
<pre><code class="copyable">CLEAR_STORAGE() &#123;
uni.clearStorageSync()
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-17">提示框类方法</h1>
<h2 data-id="heading-18">（15）TOAST</h2>
<p>介绍: 展示提示框----<code>title 为提示文字</code>----<code>mask 为是否禁止点击</code>----<code>icon 为显示图标,可以改为 'success'</code></p>
<pre><code class="copyable">TOAST(title, icon = 'none', mask = false) &#123;
uni.showToast(&#123;
title,
icon,
mask
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">（16）HIDE_TOAST</h2>
<p>介绍: 停止展示 toast 提示框</p>
<pre><code class="copyable">HIDE_TOAST() &#123;
uni.hideToast()
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">（17）LOADING</h2>
<p>介绍: 显示 loading 提示框----<code>title 为提示文字</code>----<code>mask 为是否禁止点击</code></p>
<pre><code class="copyable">LOADING(title, mask = true) &#123;
uni.showLoading(&#123;
title,
mask
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">（18）HIDE_LOADING</h2>
<p>介绍: 停止展示 loading 提示框</p>
<pre><code class="copyable">HIDE_LOADING() &#123;
uni.hideLoading()
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">（19）CONFIRM</h2>
<p>介绍: 展示确认提示框----<code>title 为标题</code>----<code>content 为提示框文字内容</code>----<code>showCancel 为是否显示取消按钮</code></p>
<pre><code class="copyable">async CONFIRM(title, content, showCancel = false) &#123;
return new Promise(res => &#123;
uni.showModal(&#123;
title,
content,
showCancel,
success: (&#123;
confirm
    &#125;) => &#123;
res(confirm)
     &#125;,
fail: () => &#123;
res(false)
     &#125;
&#125;)
   &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-23">全局事件类方法</h1>
<h2 data-id="heading-24">（20）SET_TITLE</h2>
<p>介绍: 设置页面标题</p>
<pre><code class="copyable">SET_TITLE(title) &#123;
uni.setNavigationBarTitle(&#123;
title
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">（21）CONFIG</h2>
<p>介绍: 从<code>/config.js</code>中获取某条配置项，如果在 <code>/config.js </code>中获取不到，则前往<code> /common/config.default.js</code> 中获取默认值----<code>path 为配置项的访问路径</code></p>
<p>举例：
以下语句获取是否全局开启圆形头像
<code>this.CONFIG('pageConfig.roundAvatar')</code></p>
<pre><code class="copyable">CONFIG(path) &#123;
return get(globalConfig, path, get(defaultConfig, path))
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">（22）ON</h2>
<p>介绍: 监听一个全局事件</p>
<pre><code class="copyable">ON(name, func) &#123;
uni.$on(name, func)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">（23）ONCE</h2>
<p>介绍: 仅单次监听一个全局事件</p>
<pre><code class="copyable">ONCE(name, func) &#123;
uni.$once(name, func)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">（24）EMIT</h2>
<p>介绍: 触发一个全局事件</p>
<pre><code class="copyable">EMIT(name, data) &#123;
uni.$emit(name, data)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">（25）OFF</h2>
<p>介绍: 移除全局事件监听器</p>
<pre><code class="copyable">OFF(name, func) &#123;
uni.$off(name, func)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-30">拉取指定数据类方法</h1>
<h2 data-id="heading-31">（26）FETCH_DATASOURCE</h2>
<p>介绍: 拉取指定 code 值的数据源数据</p>
<pre><code class="copyable">async FETCH_DATASOURCE(code) &#123;
if (!code) &#123;
return []
&#125;

return await this.HTTP_GET('/datasource/map', &#123;
code,
ver: ''
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">（27）FETCH_ENCODE</h2>
<p>介绍: 拉取指定规则编号的表单编码数据</p>
<pre><code class="copyable">async FETCH_ENCODE(rulecode) &#123;
if (!rulecode) &#123;
return ''
&#125;

return await this.HTTP_GET('/coderule/code', rulecode)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">（28）FETCH_FILEINFO</h2>
<p>介绍: 拉取指定 id 的文件信息</p>
<pre><code class="copyable">async FETCH_FILEINFO(fileId) &#123;
if (!fileId) &#123;
return null
&#125;

return await this.HTTP_GET('/annexes/wxfileinfo', fileId)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-34">请求类方法</h1>
<h2 data-id="heading-35">（29）HTTP_GET</h2>
<p>介绍: 封装的 <code>GET</code>请求，集成了验证信息，返回请求结果或 <code>null</code>，对网络错误、返回错误码、登录状态失效等情况做了相应处理，<code>url</code> 为请求地址，<code>data</code> 为请求附带的提交数据</p>
<pre><code class="copyable">async HTTP_GET(url, data, showTips) &#123;
const [err, res] = await this.requestBase(url, data, null, 'GET')
return this.handleResult(err, res, showTips)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-36">（30）HTTP_POST</h2>
<p>介绍: 封装的 <code>POST</code>请求，集成了验证信息，返回请求结果或 <code>null</code>，对网络错误、返回错误码、登录状态失效等情况做了相应处理，<code>url</code> 为请求地址，<code>data</code> 为请求附带的提交数据</p>
<pre><code class="copyable">async HTTP_POST(url, data, showTips) &#123;
const [err, res] = await this.requestBase(url, data, null, 'POST')
                return this.handleResult(err, res, showTips)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">（31）GET</h2>
<p>介绍: 发起一个 <code>GET 请求</code>，封装了身份验证，<code>url</code> 为请求地址，<code>data</code> 为请求附带的提交数据，返回结果是一个数组： <code>[error, result]</code>，<code>error</code> 表示错误，一般是网络错误，请求很可能根本没有发出，<code>result</code> 包含 <code>&#123; statusCode, headers, data &#125;</code> 分别表示状态码、响应头、数据</p>
<pre><code class="copyable">async GET(url, data, header) &#123;
return await this.requestBase(url, data, header, 'GET')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-38">（32）POST</h2>
<p>介绍: 发起一个 <code>POST 请求</code>，封装了身份验证，<code>url</code> 为请求地址，<code>data</code> 为请求附带的提交数据，返回结果是一个数组： <code>[error, result]</code>，<code>error</code> 表示错误，一般是网络错误，请求很可能根本没有发出，<code>result</code> 包含 <code>&#123; statusCode, headers, data &#125;</code> 分别表示状态码、响应头、数据</p>
<pre><code class="copyable">async POST(url, data, header) &#123;
return await this.requestBase(url, data, header, 'POST')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-39">文件上传下载类方法</h1>
<h2 data-id="heading-40">（33）HTTP_UPLOAD</h2>
<p>介绍: 封装的文件上传，集成了验证信息，返回接口返回值或 <code>null</code>，对网络错误、返回错误码、登录状态失效等情况做了相应处理，<code>url</code> 为请求地址，<code>filePath</code> 为临时文件的路径，<code>formData</code> 为请求附带的提交数据</p>
<pre><code class="copyable">async HTTP_UPLOAD(filePath, formData) &#123;
const [err, res] = await this.UPLOAD('/annexes/wxupload', filePath, formData)
        return this.handleResult(err, res)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-41">（34）HTTP_DOWNLOAD</h2>
<p>介绍: 封装的文件下载，集成了验证信息，返回接口返回值或 <code>null</code>，对网络错误、返回错误码、登录状态失效等情况做了相应处理，<code>url</code> 为请求地址，<code>formData</code> 为请求附带的提交数据</p>
<pre><code class="copyable">async HTTP_DOWNLOAD(formData) &#123;
const [err, res] = await this.DOWNLOAD('/annexes/wxdown', formData)
        return this.handleResult(err, res)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-42">（35）UPLOAD</h2>
<p>介绍: 上传一个文件 （本地临时文件），封装了身份验证，<code>url</code> 为提交地址，<code>filePath</code> 为本地临时文件路径，<code>formData</code> 为上传时附带的参数，返回结果是一个数组： <code>[error, result]</code>，<code>error</code> 表示错误，一般是网络错误，请求很可能根本没有发出，<code>result</code> 包含 <code>&#123; statusCode, data &#125;</code> 分别表示状态码、接口返回的数据</p>
<pre><code class="copyable">async UPLOAD(url, filePath, formData) &#123;
const uploadUrl = this.handleUrl(url)
const query = &#123;
loginMark: this.getLoginMark(),
token: this.GET_GLOBAL('token')
  &#125;
          if (formData && typeof formData === 'object') &#123;
Object.assign(query, formData)
  &#125; else if (typeof formData === 'string') &#123;
Object.assign(query, &#123;
data: formData
     &#125;)
  &#125;

 // #ifdef MP-DINGTALK ----钉钉小程序
         
 return new Promise((res, rej) => &#123;
dd.uploadFile(&#123;
url: uploadUrl,
filePath,
fileName: 'file',
fileType: 'image',
formData: query,
success: dt => &#123;
dt.data = JSON.parse(dt.data)
res([null, dt])
&#125;,
fail: rs => &#123;
rej([rs, null])
&#125;
 &#125;)
&#125;)
 // #endif

 // #ifndef MP-DINGTALK ----钉钉小程序
         
return uni.uploadFile(&#123;
url: uploadUrl,
filePath,
name: 'file',
fileType: 'image',
formData: query
&#125;).then(([err, result]) => &#123;
if (!err) &#123;
result.data = JSON.parse(result.data)
return [null, result]
&#125; else &#123;
return [err, null]
&#125;

&#125;)
// #endif
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">（36）DOWNLOAD</h2>
<p>介绍: 下载一个文件（下载后为临时文件），封装了身份验证，<code>url</code> 为请求的地址，<code>formData</code> 为请求时附带的参数，返回结果是一个数组： <code>[error, result]</code>，<code>error</code> 表示错误，一般是网络错误，请求很可能根本没有发出，<code>result</code> 包含 <code>&#123; statusCode, tempFilePath &#125;</code> 分别表示状态码、下载后的临时文件路径</p>
<pre><code class="copyable">async DOWNLOAD(url, formData) &#123;
let downloadUrl = this.handleUrl(url)
        const query = &#123;&#125;
if (formData && typeof formData === 'object') &#123;
Object.assign(query, formData)
&#125; else if (typeof formData === 'string') &#123;
Object.assign(query, &#123;
data: formData
&#125;)
    &#125;
    downloadUrl = downloadUrl + '?' + this.URL_QUERY(query, true)
                  return uni.downloadFile(&#123;
url: downloadUrl
&#125;).then(([err, result]) => &#123;
        if (!err) &#123;
         result.data = &#123;
data: result.tempFilePath
&#125;
result.statusCode = 200
&#125;

return [err, result]
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-44">拉取客户端全局数据</h1>
<h2 data-id="heading-45">（37）FETCH_CLIENTDATA</h2>
<p>介绍: 拉取客户端全局数据，直接写入全局变量，目前包括了：公司、部门、人员、数据字典</p>
<pre><code class="copyable">async FETCH_CLIENTDATA() &#123;
    await Promise.all([
this.HTTP_GET('/company/map').then(res => this.SET_GLOBAL('company', res.data || &#123;&#125;)),
this.HTTP_GET('/department/map').then(res => this.SET_GLOBAL('department', res.data ||         &#123;&#125;)),
this.HTTP_GET('/user/map').then(res => this.SET_GLOBAL('user', res.data || &#123;&#125;)),
this.HTTP_GET('/dataitem/map').then(res => this.SET_GLOBAL('dataDictionary', res.data           || &#123;&#125;))
])
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-46">前端常用方法</h1>
<h2 data-id="heading-47">（38）COPY</h2>
<p>介绍: 使用 <code>JSON</code> 序列化的方式克隆一个对象或数组</p>
<pre><code class="copyable">COPY(val) &#123;
return JSON.parse(JSON.stringify(val))
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-48">（39）GUID</h2>
<p>介绍: 使生成一个32位 <code>GUID</code> 随机字符串，<code>joinChar</code> 为分割符，默认为下划线</p>
<pre><code class="copyable">GUID(joinChar = '_') &#123;
   return `xxxxxxxx$&#123;joinChar&#125;xxxx$&#123;joinChar&#125;4xxx$&#123;joinChar&#125;yxxx$&#123;joinChar&#125;xxxxxxxxxxxx`.replace(/[xy]/g,    c => &#123;
  const r = Math.random() * 16 | 0;
  const v = c === 'x' ? r : (r & 0x3 | 0x8);
          return v.toString(16);
&#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-49">（40）MD5</h2>
<p>介绍: 获取指定字符串的 MD5 码</p>
<pre><code class="copyable">MD5(val = '') &#123;
return md5(val)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">（41）TABLEITEM_DATEFORMAT</h2>
<p>介绍:将时间日期转化为特定格式 （一般用于 <code><l-list-item></code>），<code>datetimeString</code> 为要格式化的日期时间字符串，返回值是一个数组，它也可以当做字符串直接使用</p>
<p>举例：</p>
<ol>
<li>如果日期是当天，则返回<code>['今天 17:32']</code>      或者 <code>'今天 17:32'</code></li>
<li>如果日期是今年，则返回<code>['6月8日', '17:32']</code>  或者 <code>'6月8日 17:32'</code></li>
<li>如果日期不是今年，返回<code>['2018-06-08']</code>      或者 <code>'2018-06-08'</code></li>
</ol>
<pre><code class="copyable">TABLEITEM_DATEFORMAT(datetimeString) &#123;
        const dt = moment(datetimeString)
        let result = []

        if (!dt.isValid()) &#123;
                result.toString = () => ''
                return result
        &#125;

        const now = moment()

        if (dt.isSame(now, 'day')) &#123;
                result = [`今天 $&#123;dt.format('HH:mm')&#125;`]
                result.toString = () => `今天 $&#123;dt.format('HH:mm')&#125;`

        &#125; else if (dt.isSame(now, 'year')) &#123;
                result = [dt.format('M月D日'), dt.format('HH:mm')]
                result.toString = () => dt.format('M月D日') + ' ' + dt.format('HH:mm')

        &#125; else &#123;
                result = [dt.format('YYYY-MM-DD')]
                result.toString = () => dt.format('YYYY-MM-DD')
        &#125;

        return result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-51">（42）URL_QUERY</h2>
<p>介绍: 将一个对象编码并转化为 <code>url</code> 查询字符串，<code>obj</code> 为要转换的对象，值为空则会被忽略，值为对象会被转为 <code>JSON 字符串</code>，<code>auth</code> 为是否编入身份验证信息</p>
<pre><code class="copyable">URL_QUERY(obj, auth = false) &#123;
        let queryObject = obj || &#123;&#125;
        if (typeof obj === 'string') &#123;
                queryObject = &#123;
                        data: obj
                &#125;
        &#125;
        if (auth) &#123;
                Object.assign(queryObject, &#123;
                        loginMark: this.getLoginMark(),
                        token: this.GET_GLOBAL('token')
                &#125;)
        &#125;
        return Object.entries(queryObject)
                .filter(([k, v]) => k && v)
                .map(([k, v]) => encodeURIComponent(k) + '=' + encodeURIComponent(typeof v === 'object' ? JSON.stringify(v) : v))
                .join('&')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-52">（43）CONVERT_HTML</h2>
<p>介绍: 将字符串转化为 <code>HTML</code> 格式 （处理表单页面的 HTML）</p>
<pre><code class="copyable">CONVERT_HTML(str) &#123;
        if (!str) &#123;
                return ''
        &#125;

        return str
                .replace(/&#123;@zuojian@&#125;|&#123;@youjian@&#125;|&#123;@and@&#125;/g, tag => (&#123;
                        '&#123;@zuojian@&#125;': '<',
                        '&#123;@youjian@&#125;': '>',
                        '&#123;@and@&#125;': '&'
                &#125;)[tag] || tag)
                .replace(/&amp;|&lt;|&gt;|&#39;|&quot;/g, tag => (&#123;
                        '&amp;': '&',
                        '&lt;': '<',
                        '&gt;': '>',
                        '&#39;': "'",
                        '&quot;': '"'
                &#125;)[tag] || tag)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-53">（44）MP_SHARE_ENCODE</h2>
<p>介绍: 用于编码小程序分享消息的 <code>url</code> 查询字符串 （开发环境下还会打印出来），<code>pageParam</code> 为点击分享消息跳转时携带的 <code>pageParam</code>，<code>query</code> 为点击分享消息跳转时携带的 <code>query</code>，<code>pagePath</code> 点击分享消息跳转到小程序的页面 (默认为当前页)，返回编码好的查询字符串</p>
<pre><code class="copyable">MP_SHARE_ENCODE(pageParam, query, pagePath) &#123;
        const shareObj = &#123;
                fromUser: this.GET_GLOBAL('loginUser').userId,
                fromPlatform: this.PLATFORM,
                timestamp: new Date().valueOf(),
                pagePath: pagePath || this.pagePath,
                query: query,
                pageParam,
                learun: this.APP_VERSION
        &#125;
        const result = this.URL_QUERY(shareObj)

        if (this.DEV) &#123;
                console.log('【您正在分享***小程序页面】')
                console.log('====分享对象：====')
                console.log(shareObj)
                console.log('====启动路径：====')
                console.log('/pages/home')
                console.log('====启动参数：====')
                console.log(result)
                console.log('====(以上消息仅开发模式可见)====')
        &#125;

        return result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-54">（45）MP_SHARE_DECODE</h2>
<p>介绍: 解析小程序分享字符串 （会自动适配微信小程序的 <code>url</code> 编码）,微信小程序中获取的分享信息是被 <code>url</code> 编码过的，需要解码;支付宝/钉钉小程序不需要解码</p>
<pre><code class="copyable">MP_SHARE_DECODE(info) &#123;
        // #ifdef MP-WEIXIN
        const shareInfo = mapValues(info, decodeURIComponent)
        // #endif

        shareInfo.pageParam = shareInfo.pageParam ? JSON.parse(shareInfo.pageParam) : undefined
        shareInfo.query = shareInfo.query ? this.URL_QUERY(JSON.parse(shareInfo.query)) : undefined

        if (this.DEV) &#123;
                console.log('【您通过小程序消息分享启动了***小程序】')
                console.log('====小程序分享对象：====')
                console.log(shareInfo)
                console.log('====即将转入页面：====')
                console.log(shareInfo.pagePath)
                console.log('====设置的 url query：====')
                console.log(shareInfo.query)
                console.log('====设置的 pageParam：====')
                console.log(shareInfo.pageParam)
                console.log('====(以上消息仅开发模式可见)====')
        &#125;

        this.SET_GLOBAL('pageParam', shareInfo.pageParam)
        uni.navigateTo(&#123;
                url: `$&#123;shareInfo.pagePath&#125;?$&#123;this.URL_QUERY(shareInfo.query)&#125;`
        &#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-55">内部方法</h1>
<h2 data-id="heading-56">（46）handleNav</h2>
<p>介绍: 处理页面跳转 <code>url</code> 和参数</p>
<pre><code class="copyable">handleNav(url, param, usePageParam) &#123;
        let query = ''
        if (param && usePageParam) &#123;
                this.SET_PARAM(param)
        &#125; else if (param && !usePageParam) &#123;
                query += '?' + Object.entries(param).filter(([k, v]) => k && v).map(([k, v]) => k + '=' + v).join('&')
        &#125;

        return url + query
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-57">（47）getLoginMark</h2>
<p>介绍: 从全局变量和缓存中获取 <code>loginMark</code> 设备标识，获取不到则会重新生成一个</p>
<pre><code class="copyable">getLoginMark() &#123;
        if (this.GET_GLOBAL('loginMark')) &#123;
                return this.GET_GLOBAL('loginMark')
        &#125;

        const storageData = uni.getStorageSync('loginMark')
        if (storageData && storageData !== 'null' && storageData !== 'undefined') &#123;
                this.SET_GLOBAL('loginMark', storageData)

                return storageData
        &#125;

        const newLoginMark = this.GUID()
        this.SET_GLOBAL('loginMark', newLoginMark)
        uni.setStorageSync('loginMark', newLoginMark)

        return newLoginMark
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-58">（48）handleUrl</h2>
<p>介绍: 处理 <code>url</code>，判断是否需要添加后台地址前缀</p>
<pre><code class="copyable">handleUrl(url) &#123;
        let result = url
        if (result.startsWith('http://') || result.startsWith('https://')) &#123;
                return result
        &#125;
        if (!result.startsWith(this.API)) &#123;
                result = this.API + result
        &#125;

        return result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-59">（49）requestBase</h2>
<p>介绍: <code>HTTP</code> 请求基础方法</p>
<pre><code class="copyable">async requestBase(url, data, header, method = 'GET') &#123;
        const requestUrl = this.handleUrl(url)
        const requestHeader = header || &#123;&#125;

        let requestData = &#123;
                loginMark: this.getLoginMark(),
                token: this.GET_GLOBAL('token') || ''
        &#125;
        if (data && typeof data === 'object') &#123;
                requestData.data = JSON.stringify(data)
        &#125; else if (data) &#123;
                Object.assign(requestData, &#123;
                        data
                &#125;)
        &#125;

        return uni.request(&#123;
                url: requestUrl,
                method,
                header: &#123;
                        'content-type': 'application/x-www-form-urlencoded',
                        ...requestHeader
                &#125;,
                data: requestData
        &#125;)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-60">（50）handleResult</h2>
<p>介绍: 处理网络请求方法的返回结果</p>
<pre><code class="copyable">handleResult(err, result, tips) &#123;
    // 出现错误，一般是网络连接错误
    if (err || !result) &#123;
            uni.hideLoading()
            uni.showToast(&#123;
                    title: '网络请求失败，请检查您的网络连接',
                    icon: 'none'
            &#125;)

            return null
    &#125;

    // 状态码为 410，登录状态失效
    if (result.statusCode === 410 || (result.data && result.data.code === 410)) &#123;
            uni.hideLoading()
            uni.showToast(&#123;
                    title: '登录状态无效，正在跳转到登录页…',
                    icon: 'none'
            &#125;)
            this.CLEAR_GLOBAL()
            uni.reLaunch(&#123;
                    url: '/pages/login'
            &#125;)

            return null

            uni.hideLoading()
            if (tips) &#123;
                    const errInfo = (result.data && result.data.info) || '(未知原因)'
                    const errTips = typeof tips === 'string' ? tips : '请求数据时发生错误'
                    uni.showToast(&#123;
                            title: `$&#123;errTips&#125;： $&#123;errInfo&#125;`,
                            icon: 'none'
                    &#125;)
            &#125;

            return null
    &#125;

    return result.data.data
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-61">computed</h1>
<h2 data-id="heading-62">（51）API</h2>
<p>介绍: 请求后台接口的地址</p>
<pre><code class="copyable">API() &#123;
        return this.$store.state.apiRoot ||this.CONFIG('apiHost')[this.DEV ?this.CONFIG('devApiHostIndex') : this.CONFIG('prodApiHostIndex')]
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-63">（52）PATH</h2>
<p>介绍: 当前页面的路径</p>
<pre><code class="copyable">PATH() &#123;
        if (!getCurrentPages) &#123;
                return ''
        &#125;
        const pages = getCurrentPages()

        return pages ? '/' + pages.slice(-1)[0].route : ''
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-64">（53）DEV</h2>
<p>介绍: 当前是否为开发环境</p>
<pre><code class="copyable">DEV() &#123;
        return process.env.NODE_ENV === 'development'
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-65">（54）DEV_ONLY_GLOBAL</h2>
<p>介绍: 【仅开发模式】获取当前全局变量，生产环境、正式发行时无效，因为小程序端全局变量会挂载到每个页面，影响性能</p>
<pre><code class="copyable">DEV_ONLY_GLOBAL() &#123;
        return process.env.NODE_ENV === 'development' && this.$store.state
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-66">（55）APP_VERSION</h2>
<p>介绍: 获取当前移动端版本号 （定义在 <code>config.js</code>）</p>
<pre><code class="copyable">APP_VERSION() &#123;
        return this.CONFIG('appVersion')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-67">（56）PLATFORM</h2>
<p>介绍: 当前运行平台，取值 <code>'alipay'</code>/<code>weixin'</code>/<code>'dingtalk'</code>/<code>'h5'</code>/<code>'app'</code>/<code>'unknow'</code></p>
<pre><code class="copyable">PLATFORM() &#123;
        let result = 'unknow'

        // #ifdef MP-ALIPAY
        // #ifndef MP-DINGTALK
        result = 'alipay'
        // #endif
        // #ifdef MP-DINGTALK
        result = 'dingtalk'
        // #endif
        // #endif

        // #ifdef MP-WEIXIN
        result = 'weixin'
        // #endif

        // #ifdef H5
        result = 'h5'
        // #endif

        // #ifdef APP-VUE
        result = 'app'
        // #endif

        return result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-68">（57）PLATFORM_TEXT</h2>
<p>介绍: 获取当前运行平台的中文全称，取值 <code>'支付宝小程序'</code>/<code>微信小程序'</code>/<code>'钉钉小程序'</code>/<code>'移动 H5 '</code>/<code>'手机 App'</code>/<code>'（未知）'</code></p>
<pre><code class="copyable">PLATFORM_TEXT() &#123;
        let result = '（未知）'

        // #ifdef MP-ALIPAY
        // #ifndef MP-DINGTALK
        result = '支付宝小程序'
        // #endif
        // #ifdef MP-DINGTALK
        result = '钉钉小程序'
        // #endif
        // #endif

        // #ifdef MP-WEIXIN
        result = '微信小程序'
        // #endif

        // #ifdef H5
        result = '移动 H5 '
        // #endif

        // #ifdef APP-VUE
        result = '手机 App '
        // #endif

        return result
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            