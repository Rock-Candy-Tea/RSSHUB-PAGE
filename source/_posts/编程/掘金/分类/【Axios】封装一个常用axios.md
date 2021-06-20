
---
title: '【Axios】封装一个常用axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1425'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:02:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=1425'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第2天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>在平时项目开发当中，避免不了接口请求，这时候，能够封装一组自己习惯的请求方式，能够帮助自己在开发当中提高效率，节省代码的复现率。</p>
</blockquote>
<h2 data-id="heading-0">什么是 axios？</h2>
<p>首先需要知道：axios不是一种新的技术。axios 是一个基于Promise 用于浏览器和 nodejs 的 HTTP 客户端，本质上也是对原生XHR的封装，只不过它是Promise的实现版本，符合最新的ES规范，</p>
<h2 data-id="heading-1">axios 他有哪些特性？</h2>
<ul>
<li>从浏览器中创建 <a href="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest" target="_blank" rel="nofollow noopener noreferrer">XMLHttpRequests</a></li>
<li>从 node.js 创建 <a href="http://nodejs.org/api/http.html" target="_blank" rel="nofollow noopener noreferrer">http</a> 请求</li>
<li>支持 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise" target="_blank" rel="nofollow noopener noreferrer">Promise</a> API</li>
<li>拦截请求和响应</li>
<li>转换请求数据和响应数据</li>
<li>取消请求</li>
<li>自动转换 JSON 数据</li>
<li>客户端支持防御 <a href="http://en.wikipedia.org/wiki/Cross-site_request_forgery" target="_blank" rel="nofollow noopener noreferrer">XSRF</a></li>
</ul>
<h2 data-id="heading-2">开始使用</h2>
<p>使用 npm安装:</p>
<pre><code class="copyable">$ npm install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 bower安装:</p>
<pre><code class="copyable">$ bower install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 cdn:</p>
<pre><code class="copyable"><script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">封装Axios</h2>
<h3 data-id="heading-4">1、设置baseURl，创建config.js文件</h3>
<pre><code class="copyable">export const baseUrl = location.protocol + '//localhost'  //项目域名
const environment = process.env.NODE_ENV === 'production' ? 'pro' : 'dev' //dev开发环境  pro 生产环境
let exports = &#123;&#125;
// 开发环境
if(environment === 'dev')&#123;
  exports = &#123;
    proxyBaseUrl:'/api',
    fyBaseUrl:'/apis' //防疫接口
  &#125;
// 线上环境
&#125;else if(environment === 'pro')&#123;
  exports = &#123;
    // 项目使用到多个域名，可以进行多个入口配置
    proxyBaseUrl:location.protocol + '//localhost', // 应用1
    fyBaseUrl:location.protocol + '//localhost' //应用2
  &#125;
&#125;
export default exports
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2、创建service.js</h3>
<p>配置axios,全局设置请求信息和错误信息处理</p>
<pre><code class="copyable">import axios from 'axios'
import router from './../router' 
const showStatus = (status) => &#123;
  let message = ''
  switch (status) &#123;
    case 400:
      message = '请求错误(400)'
      break
    case 401:
      message = '未授权，请重新登录(401)'
      break
    case 402:
      message = '拒绝访问(402)'
      break
    case 404:
      message = '请求出错(404)'
      break
    case 408:
      message = '请求超时(408)'
      break
    case 500:
      message = '服务器错误(500)'
      break
    case 501:
      message = '服务未实现(501)'
      break
    case 502:
      message = '网络错误(502)'
      break
    case 503:
      message = '服务不可用(503)'
      break
    case 504:
      message = '网络超时(504)'
      break
    case 505:
      message = 'HTTP版本不受支持(505)'
      break
    default:
      message = `连接出错($&#123;status&#125;)!`
  &#125;
  return `$&#123;message&#125;，请检查网络或联系管理员！`
&#125;

const service = axios.create(&#123;
  // 联调
  
  headers: &#123;
    get: &#123;
      'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    &#125;,
    post: &#123;
      'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    &#125;
  &#125;,
  // 是否跨站点访问控制请求
  withCredentials: true,
  timeout: 30000,
  validateStatus() &#123;
    // 使用async-await，处理reject情况较为繁琐，所以全部返回resolve，在业务代码中处理异常
    return true
  &#125;
&#125;)

// 请求拦截器
service.interceptors.request.use(
  config => &#123;
    return config
  &#125;,
  (err) => &#123;
    err.message = '服务器异常，请联系管理员！'
    // 错误抛到业务代码
    return Promise.reject(err)
  &#125;
)

// 响应拦截器
service.interceptors.response.use(
  response => &#123;
    const status = response.status
    let msg = ''
    if (status < 200 || status >= 300 && status != 401 && status != 500) &#123;
      // 处理http错误，抛到业务代码
      msg = showStatus(status)
      if (typeof response.data === 'string') &#123;
        response.data = &#123; msg &#125;
      &#125; else &#123;
        response.data.msg = msg
      &#125;
      return response
    &#125;else if(status == 200)&#123;
      return response
    &#125;else if(status == 500)&#123;
      msg = showStatus(status)
      response.data = &#123;msg:msg&#125;
      router.replace(&#123;name:'exception',query:&#123;type:500&#125;&#125;)
      return response 
    &#125;
    
  &#125;,
  (err)=>&#123;
    err.message =  '请求超时或服务器异常，请检查网络或联系管理员！'
    return Promise.reject(err)
  &#125;
)

export default service
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3、创建接口请求文件</h3>
<p>不同区块的功能的数据，可以创建多个文件，便于区分和后期管理</p>
<pre><code class="copyable">import config from './config' // 基础路径
import service from './service' //封装的axios
/**
 * data 是post传参
 *
 */
export const Upload = (data)=> service(&#123;
  url: `$&#123;config.proxyBaseUrl&#125;/user/upload`,
  method: 'POST',
  data: data,
  headers:&#123;
   //这里可以单独设置headers
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4、实际组件中调用请求</h3>
<pre><code class="copyable">import &#123;Upload&#125; from 你的请求文件地址

Upload(参数).then((res)=>&#123;
  //返回的数据
&#125;)
.catch((err)=>&#123;
  //错误信息
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            