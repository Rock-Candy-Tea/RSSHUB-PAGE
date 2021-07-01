
---
title: '小程序API管理(promise)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2172'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 19:00:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=2172'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>创建HTTP文件夹,并创建request和api两个js文件</strong></p>
<p>创建request.js用来封装小程序的request请求</p>
<pre><code class="copyable">const app = getApp();
const host = app.globalData.URL
// get请求使用 json对象转字符串 （formatParams ）
const formatParams = (data) => &#123;
  let arr = []
  for (let name in data) &#123;
    arr.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]))
  &#125;
  return arr.join('&')
&#125;
// 创建统一调用函数

const httpService = (url, params, method, loading = true) => &#123;
  let header = &#123;
    "content-type": "application/x-www-form-urlencoded"
  &#125;
  let defaultData = &#123;
    token:app.globalData.token,
    source:'wxxcx'
  &#125;
  return new Promise((resolve, reject) => &#123;
    if (method === 'post') &#123;
      wx.request(&#123;
        url: host + url,
        data: Object.assign(defaultData, params),
        method: method,
        header: header,
        timeout: 15000,
        complete: (res) => &#123;
          resolve(res)
        &#125;
      &#125;)
    &#125; else if (method === 'get') &#123;
      wx.request(&#123;
        url: host + url + '?' + formatParams(Object.assign(defaultData, params)),
        method: method,
        header: header,
        timeout: 15000,
        complete: (res) => &#123;
          resolve(res)
        &#125;
      &#125;)
    &#125;

  &#125;)
&#125;

module.exports = &#123;
  httpService
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建api.js用来统一管理api接口</p>
<pre><code class="copyable">//引入封装好的request文件
const &#123; httpService &#125; = require('../http/request')
const app = getApp()
// 职场相关接口

/**
 * 获取职位列表
 */
const getPositionList = (params) => &#123;
  return httpService('/position/jobs', params, 'get')
&#125;
/**
 * 获取公司列表
 */
const getCompanyList = (params) => &#123;
  return httpService('/position/company2', params, 'get')
&#125;
/**
 * 获取轮播数据
 */
const getBanner = (params) => &#123;
  return httpService('/position/fairbanner', params, 'get')
&#125;

/**
 * 获取简历详情
 */
const getCvDetails = (params) => &#123;
  return httpService('/cv/detail', params, 'get')
&#125;
/**
 * 投递简历
 */
const deliveryCv = (params) => &#123;
  return httpService('/cv/deliver', params, 'get')
&#125;
 /**
  * 获取职位详情
  */
 const getJobDetails = (params) => &#123;
  return httpService('/position/jobdetail', params, 'post')
&#125;
 /**
  * 收藏职位
  */
 const collectjob = (params) => &#123;
   return httpService('/position/collectjob',params,'get')
 &#125;

 /**
  * 获取职能类表
  */
 const getFormresource = (params) => &#123;
  return httpService('/position/formresource',params,'get')
&#125;

/**
 * 获取公司详情页中职位列表数据
 */
const getcompanyJob = (params) => &#123;
  return httpService('/position/jobfeed',params,'post')
&#125;

/**
 * 获取公司信息
 */
const getCompanyInfo = (params) => &#123;
  return httpService('/position/moreposition',params,'post')
&#125;

// 登录相关接口

 /**
  * 微信登录
  */
 const wxLogin = (params) => &#123;
  return httpService('/login/xcxlogin', params, 'post')
&#125;
/**
 * 职场状态确认与更新接口
 */
const wxgroupconfirm = (params) => &#123;
  return httpService('/position/groupconfirm', params, 'post')
&#125;
/**
 * 获取验证码
 */
const getCode = (params) => &#123;
  return httpService('/mobile/phonecode', params, 'post')
&#125;

// 会议相关接口

/**
 * 获取我的会议
 */
const getMyMetting = (params) => &#123;
  return httpService('/user/usermeeting', params, 'post')
&#125;
//导出接口
module.exports = &#123;
  getPositionList,
  getBanner,
  getCompanyList,
  getCvDetails,
  wxLogin,
  wxgroupconfirm,
  getCode,
  deliveryCv,
  getJobDetails,
  collectjob,
  getFormresource,
  getcompanyJob,
  getCompanyInfo,
  getMyMetting
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面使用</p>
<p>//引入封装的api文件
import &#123;导出的接口对象&#125; from '封装的api文件相对路径'</p>
<p>例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;
  getPositionList,
  getBanner,
  getCompanyList
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../../http/api"</span>

<span class="hljs-comment">//使用方式</span>

getPositionList(&#123;
    参数
&#125;)
.then(<span class="hljs-function"><span class="hljs-params">res</span> =></span>&#123;
    成功回调
&#125;)
.catch(<span class="hljs-function"><span class="hljs-params">err</span>=></span>&#123;
    失败回调
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种API管理方式对于api数量多的功能不太友好,后期会继续优化</p></div>  
</div>
            