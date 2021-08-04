
---
title: 'vue3 + vite 项目搭建 - 封装全局请求axios (单例模式)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=999'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 00:53:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=999'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>安装依赖</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"qs"</span>: <span class="hljs-string">"^6.10.1"</span>,
    <span class="hljs-string">"axios"</span>: <span class="hljs-string">"^0.21.1"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>统一管理配置，创建src/config/net.config.ts</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//src/config/net.config.ts</span>
type NetConfigSuccessCode = <span class="hljs-number">200</span> | <span class="hljs-string">'200'</span> | <span class="hljs-string">'000000'</span>
<span class="hljs-comment">// 正式项目可以选择自己配置成需要的接口地址，如"https://api.xxx.com"</span>
<span class="hljs-comment">// 问号后边代表开发环境，冒号后边代表生产环境</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> baseURL: string = <span class="hljs-keyword">import</span>.meta.env.MODE === <span class="hljs-string">'development'</span>
  ? <span class="hljs-string">'/xz-risk'</span>
  : <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-keyword">import</span>.meta.env.VITE_RES_URL&#125;</span>/xz-risk`</span>
<span class="hljs-comment">// 配后端数据的接收方式application/json;charset=UTF-8 或 application/x-www-form-urlencoded;charset=UTF-8</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> contentType: string = <span class="hljs-string">'application/json;charset=UTF-8'</span>
<span class="hljs-comment">// 最长请求时间</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> requestTimeout: number = <span class="hljs-number">10000</span>
<span class="hljs-comment">// 超时尝试次数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> timeoutNum: number = <span class="hljs-number">3</span>
<span class="hljs-comment">// 超时重新请求间隔</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> intervalTime: number = <span class="hljs-number">1000</span>
<span class="hljs-comment">// 操作正常code，支持String、Array、int多种类型</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> successCode: NetConfigSuccessCode[] = [<span class="hljs-number">200</span>, <span class="hljs-string">'200'</span>, <span class="hljs-string">'000000'</span>]
<span class="hljs-comment">// 数据状态的字段名称</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> statusName: string = <span class="hljs-string">'code'</span>
<span class="hljs-comment">// 状态信息的字段名称</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> messageName: string = <span class="hljs-string">'msg'</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>封装api模块，用于管理请求路径 src/api/index.ts</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/api/index.ts</span>
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/common'</span>

interface UrlDict &#123;
  [key: string]: &#123;
    [key: string]: string
  &#125;
&#125;

<span class="hljs-keyword">const</span> urlDict: UrlDict = &#123;
  common
&#125;

<span class="hljs-keyword">const</span> getUrl = (url: string): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span> (url === <span class="hljs-string">''</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'请求路径为空'</span>)
    <span class="hljs-keyword">const</span> [modelName, urlName] = url.split(<span class="hljs-string">'.'</span>)
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">Object</span>.keys(urlDict).includes(modelName)) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'未获取到请求模块'</span>)
    <span class="hljs-keyword">const</span> reqUrl = urlDict[modelName][urlName]
    <span class="hljs-keyword">if</span> (!reqUrl) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'未获取到请求所需url'</span>)
    <span class="hljs-keyword">return</span> reqUrl
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.error(e)
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> getUrl

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/api/common.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">token</span>: <span class="hljs-string">'/common/token'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>创建请求所需类型</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/types/utils/request.d.ts</span>
declare namespace MyRequest &#123;
  interface response &#123;
    <span class="hljs-attr">code</span>: number | string,
    <span class="hljs-attr">msg</span>: string,
    <span class="hljs-attr">data</span>: any
  &#125;
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">request</span> </span>&#123;
    <span class="hljs-comment">/**
       * POST方法
       * <span class="hljs-doctag">@param </span>url 请求路径，模式：[模块名称.接口名称] 如 common.token
       * <span class="hljs-doctag">@param </span>data 请求参数
       * <span class="hljs-doctag">@param </span>config 请求配置
       */</span>
    public post(url: string, data?: any, config?: object): <span class="hljs-built_in">Promise</span><response>

    <span class="hljs-comment">/**
       * POST方法
       * <span class="hljs-doctag">@param </span>url 请求路径，模式：[模块名称.接口名称] 如 common.token
       * <span class="hljs-doctag">@param </span>params 请求参数
       * <span class="hljs-doctag">@param </span>config 请求配置
       */</span>
    public get(url: string, params?: any, config?: object): <span class="hljs-built_in">Promise</span><response>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>封装请求</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> axios, &#123; AxiosResponse, AxiosRequestConfig, CancelTokenStatic, AxiosInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> &#123;
  baseURL,
  successCode,
  contentType,
  requestTimeout,
  statusName,
  messageName
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/config/net.config'</span>
<span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>
<span class="hljs-keyword">import</span> getUrl <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api'</span>

<span class="hljs-keyword">const</span> CODE_MESSAGE: any = &#123;
  <span class="hljs-number">200</span>: <span class="hljs-string">'服务器成功返回请求数据'</span>,
  <span class="hljs-number">201</span>: <span class="hljs-string">'新建或修改数据成功'</span>,
  <span class="hljs-number">202</span>: <span class="hljs-string">'一个请求已经进入后台排队(异步任务)'</span>,
  <span class="hljs-number">204</span>: <span class="hljs-string">'删除数据成功'</span>,
  <span class="hljs-number">400</span>: <span class="hljs-string">'发出信息有误'</span>,
  <span class="hljs-number">401</span>: <span class="hljs-string">'用户没有权限(令牌失效、用户名、密码错误、登录过期)'</span>,
  <span class="hljs-number">402</span>: <span class="hljs-string">'前端无痛刷新token'</span>,
  <span class="hljs-number">403</span>: <span class="hljs-string">'用户得到授权，但是访问是被禁止的'</span>,
  <span class="hljs-number">404</span>: <span class="hljs-string">'访问资源不存在'</span>,
  <span class="hljs-number">406</span>: <span class="hljs-string">'请求格式不可得'</span>,
  <span class="hljs-number">410</span>: <span class="hljs-string">'请求资源被永久删除，且不会被看到'</span>,
  <span class="hljs-number">500</span>: <span class="hljs-string">'服务器发生错误'</span>,
  <span class="hljs-number">502</span>: <span class="hljs-string">'网关错误'</span>,
  <span class="hljs-number">503</span>: <span class="hljs-string">'服务不可用，服务器暂时过载或维护'</span>,
  <span class="hljs-number">504</span>: <span class="hljs-string">'网关超时'</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyRequest</span> </span>&#123;
  <span class="hljs-comment">// `baseURL` 将自动加在 `url` 前面，除非 `url` 是一个绝对 URL。</span>
  protected service: AxiosInstance = axios
  protected pending: <span class="hljs-built_in">Array</span><&#123; <span class="hljs-attr">url</span>: string, <span class="hljs-attr">cancel</span>: <span class="hljs-built_in">Function</span> &#125;> = []
  protected CancelToken: CancelTokenStatic = axios.CancelToken
  protected axiosRequestConfig: AxiosRequestConfig = &#123;&#125;
  private <span class="hljs-keyword">static</span> _instance: MyRequest;

  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">this</span>.requestConfig()
    <span class="hljs-built_in">this</span>.service = axios.create(<span class="hljs-built_in">this</span>.axiosRequestConfig)
    <span class="hljs-built_in">this</span>.interceptorsRequest()
    <span class="hljs-built_in">this</span>.interceptorsResponse()
  &#125;

  <span class="hljs-comment">/**
     * 初始化配置
     * <span class="hljs-doctag">@protected</span>
     */</span>
  protected requestConfig (): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-built_in">this</span>.axiosRequestConfig = &#123;
      <span class="hljs-attr">baseURL</span>: baseURL,
      <span class="hljs-attr">headers</span>: &#123;
        <span class="hljs-attr">timestamp</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime(),
        <span class="hljs-string">'Content-Type'</span>: contentType
      &#125;,
      <span class="hljs-comment">// transformRequest: [obj => qs.stringify(obj)],</span>
      <span class="hljs-attr">transformResponse</span>: [<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data: AxiosResponse</span>) </span>&#123;
        <span class="hljs-keyword">return</span> data
      &#125;],
      <span class="hljs-attr">paramsSerializer</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">params: any</span>) </span>&#123;
        <span class="hljs-keyword">return</span> qs.stringify(params, &#123; <span class="hljs-attr">arrayFormat</span>: <span class="hljs-string">'brackets'</span> &#125;)
      &#125;,
      <span class="hljs-attr">timeout</span>: requestTimeout,
      <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">responseType</span>: <span class="hljs-string">'json'</span>,
      <span class="hljs-attr">xsrfCookieName</span>: <span class="hljs-string">'XSRF-TOKEN'</span>,
      <span class="hljs-attr">xsrfHeaderName</span>: <span class="hljs-string">'X-XSRF-TOKEN'</span>,
      <span class="hljs-attr">maxRedirects</span>: <span class="hljs-number">5</span>,
      <span class="hljs-attr">maxContentLength</span>: <span class="hljs-number">2000</span>,
      <span class="hljs-attr">validateStatus</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">status: number</span>) </span>&#123;
        <span class="hljs-keyword">return</span> status >= <span class="hljs-number">200</span> && status < <span class="hljs-number">500</span>
      &#125;
      <span class="hljs-comment">// httpAgent: new http.Agent(&#123;keepAlive: true&#125;),</span>
      <span class="hljs-comment">// httpsAgent: new https.Agent(&#123;keepAlive: true&#125;)</span>
    &#125;
  &#125;

  <span class="hljs-comment">/**
     * 请求拦截
     * <span class="hljs-doctag">@protected</span>
     */</span>
  protected interceptorsRequest (): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-built_in">this</span>.service.interceptors.request.use(
      <span class="hljs-function">(<span class="hljs-params">config: AxiosRequestConfig</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> keyOfRequest = <span class="hljs-built_in">this</span>.getKeyOfRequest(config)
        <span class="hljs-built_in">this</span>.removePending(keyOfRequest, <span class="hljs-literal">true</span>)
        config.cancelToken = <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.CancelToken(<span class="hljs-function">(<span class="hljs-params">c: any</span>) =></span> &#123;
          <span class="hljs-built_in">this</span>.pending.push(&#123;
            <span class="hljs-attr">url</span>: keyOfRequest,
            <span class="hljs-attr">cancel</span>: c
          &#125;)
        &#125;)
        <span class="hljs-built_in">this</span>.requestLog(config)
        <span class="hljs-keyword">return</span> config
      &#125;,
      <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
      &#125;
    )
  &#125;

  <span class="hljs-comment">/**
     * 响应拦截
     * <span class="hljs-doctag">@protected</span>
     */</span>
  protected interceptorsResponse (): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-built_in">this</span>.service.interceptors.response.use(<span class="hljs-function">(<span class="hljs-params">response: AxiosResponse</span>) =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handleResponse(response)
    &#125;, <span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; response &#125; = error
      <span class="hljs-keyword">if</span> (response === <span class="hljs-literal">undefined</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(error))
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.handleResponse(response)
      &#125;
    &#125;)
  &#125;

  protected handleResponse (response: AxiosResponse): <span class="hljs-built_in">Promise</span><AxiosResponse<any>> &#123;
    <span class="hljs-built_in">this</span>.responseLog(response)
    <span class="hljs-built_in">this</span>.removePending(<span class="hljs-built_in">this</span>.getKeyOfRequest(response.config))
    <span class="hljs-keyword">const</span> &#123; data, status, config, statusText &#125; = response
    <span class="hljs-keyword">let</span> code = data && data[statusName]
      ? data[statusName]
      : status
    <span class="hljs-keyword">if</span> (successCode.indexOf(data[statusName]) + <span class="hljs-number">1</span>) code = <span class="hljs-number">200</span>
    <span class="hljs-keyword">switch</span> (code) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-number">200</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(response)
      <span class="hljs-keyword">case</span> <span class="hljs-number">401</span>:
        <span class="hljs-comment">// TODO token失效,跳转登录页</span>
        <span class="hljs-keyword">break</span>
      <span class="hljs-keyword">case</span> <span class="hljs-number">403</span>:
        <span class="hljs-comment">// TODO 没有权限,跳转403页面</span>
        <span class="hljs-keyword">break</span>
    &#125;
    <span class="hljs-comment">// 异常处理</span>
    <span class="hljs-keyword">const</span> errMsg = data && data[messageName]
      ? data[messageName]
      : CODE_MESSAGE[code]
        ? CODE_MESSAGE[code]
        : statusText
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(errMsg)
  &#125;

  <span class="hljs-comment">/**
     * 取消重复请求
     * <span class="hljs-doctag">@protected</span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">key</span></span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">request</span></span>
     */</span>
  protected removePending (key: string, <span class="hljs-attr">request</span>: boolean = <span class="hljs-literal">false</span>): <span class="hljs-keyword">void</span> &#123;
    <span class="hljs-built_in">this</span>.pending.some(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (item.url === key) &#123;
        <span class="hljs-keyword">if</span> (request) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'=====  取消重复请求  ====='</span>, item)
        item.cancel()
        <span class="hljs-built_in">this</span>.pending.splice(index, <span class="hljs-number">1</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;)
  &#125;

  <span class="hljs-comment">/**
     * 获取请求配置拼装的key
     * <span class="hljs-doctag">@param <span class="hljs-variable">config</span></span>
     * <span class="hljs-doctag">@protected</span>
     */</span>
  protected getKeyOfRequest (config: AxiosRequestConfig): string &#123;
    <span class="hljs-keyword">let</span> key = config.url
    <span class="hljs-keyword">if</span> (config.params) key += <span class="hljs-built_in">JSON</span>.stringify(config.params)
    <span class="hljs-keyword">if</span> (config.data) key += <span class="hljs-built_in">JSON</span>.stringify(config.data)
    key += <span class="hljs-string">`&request_type=<span class="hljs-subst">$&#123;config.method&#125;</span>`</span>
    <span class="hljs-keyword">return</span> key <span class="hljs-keyword">as</span> string
  &#125;

  <span class="hljs-comment">/**
     * 请求日志
     * <span class="hljs-doctag">@param <span class="hljs-variable">config</span></span>
     * <span class="hljs-doctag">@protected</span>
     */</span>
  protected requestLog (config: any): <span class="hljs-keyword">void</span> &#123;
  &#125;

  <span class="hljs-comment">/**
     * 响应日志
     * <span class="hljs-doctag">@protected</span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">response</span></span>
     */</span>
  protected responseLog (response: AxiosResponse) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">import</span>.meta.env.MODE === <span class="hljs-string">'development'</span>) &#123;
      <span class="hljs-keyword">const</span> randomColor = <span class="hljs-string">`rgba(<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">255</span>)&#125;</span>,<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.round(
        <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">255</span>
      )&#125;</span>,<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.round(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">255</span>)&#125;</span>)`</span>
      <span class="hljs-built_in">console</span>.log(
        <span class="hljs-string">'%c┍------------------------------------------------------------------┑'</span>,
        <span class="hljs-string">`color:<span class="hljs-subst">$&#123;randomColor&#125;</span>;`</span>
      )
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'| 请求地址：'</span>, response.config.url)
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'| 请求参数：'</span>, qs.parse(response.config.data))
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'| 返回数据：'</span>, response.data)
      <span class="hljs-built_in">console</span>.log(
        <span class="hljs-string">'%c┕------------------------------------------------------------------┙'</span>,
        <span class="hljs-string">`color:<span class="hljs-subst">$&#123;randomColor&#125;</span>;`</span>
      )
    &#125;
  &#125;

  <span class="hljs-comment">/**
     * post方法
     * <span class="hljs-doctag">@param <span class="hljs-variable">url</span></span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">data</span></span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">config</span></span>
     */</span>
  public post (url: string, <span class="hljs-attr">data</span>: any = &#123;&#125;, <span class="hljs-attr">config</span>: object = &#123;&#125;): <span class="hljs-built_in">Promise</span><MyRequest.response> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.service.post(getUrl(url), data, config).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
        resolve(&#123;
          <span class="hljs-attr">msg</span>: result.data.msg,
          <span class="hljs-attr">data</span>: result.data.data,
          <span class="hljs-attr">code</span>: result.data.code
        &#125;)
      &#125;, reject)
    &#125;)
  &#125;

  <span class="hljs-comment">/**
     * post方法
     * <span class="hljs-doctag">@param <span class="hljs-variable">url</span></span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">params</span></span>
     * <span class="hljs-doctag">@param <span class="hljs-variable">config</span></span>
     */</span>
  public get (url: string, <span class="hljs-attr">params</span>: any = &#123;&#125;, <span class="hljs-attr">config</span>: object = &#123;&#125;): <span class="hljs-built_in">Promise</span><MyRequest.response> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">this</span>.service.get(<span class="hljs-string">`<span class="hljs-subst">$&#123;getUrl(url)&#125;</span>?<span class="hljs-subst">$&#123;qs.stringify(params)&#125;</span>`</span>, config).then(<span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
        resolve(&#123;
          <span class="hljs-attr">msg</span>: result.data.msg,
          <span class="hljs-attr">data</span>: result.data.data,
          <span class="hljs-attr">code</span>: result.data.code
        &#125;)
      &#125;, reject)
    &#125;)
  &#125;

  <span class="hljs-comment">/**
     * 创建唯一实例（单例模式）
     */</span>
  public <span class="hljs-keyword">static</span> getInstance (): MyRequest &#123;
    <span class="hljs-comment">// 如果 instance 是一个实例 直接返回，  如果不是 实例化后返回</span>
    <span class="hljs-built_in">this</span>._instance || (<span class="hljs-built_in">this</span>._instance = <span class="hljs-keyword">new</span> MyRequest())
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._instance
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> MyRequest.getInstance()

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>全局注册，这里是挂载到globalProperties</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/vab/plugins/globaProperties.ts</span>
<span class="hljs-keyword">import</span> &#123; App &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/request'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'@/router'</span>
<span class="hljs-keyword">import</span> &#123; store &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store'</span>
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@name</span>: sww
 * <span class="hljs-doctag">@date</span>: 2021-06-29
 * <span class="hljs-doctag">@desc</span>: 获取表格高度
 */</span>
<span class="hljs-keyword">const</span> baseTableHeight = (formType: number = <span class="hljs-number">1</span>): <span class="hljs-function"><span class="hljs-params">number</span> =></span> &#123;
  <span class="hljs-keyword">const</span> mainInfo = store.getters.layoutMainInfo
  <span class="hljs-keyword">return</span> (mainInfo.height - <span class="hljs-number">130</span>) * formType
&#125;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@name</span>: sww
 * <span class="hljs-doctag">@date</span>: 2021-07-19
 * <span class="hljs-doctag">@desc</span>: 格式化网络资源
 */</span>
<span class="hljs-keyword">const</span> formatImage = (src: string): <span class="hljs-function"><span class="hljs-params">string</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (!src) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  <span class="hljs-keyword">if</span> (src.includes(<span class="hljs-string">'http'</span>)) <span class="hljs-keyword">return</span> src
  <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-keyword">import</span>.meta.env.VITE_RES_URL&#125;</span><span class="hljs-subst">$&#123;src&#125;</span>`</span>
&#125;

<span class="hljs-keyword">const</span> install = <span class="hljs-function">(<span class="hljs-params">app: App</span>) =></span> &#123;
  <span class="hljs-comment">// 注册请求实例</span>
  app.config.globalProperties.$request = request
  app.config.globalProperties.$baseTableHeight = baseTableHeight
  app.config.globalProperties.$image = formatImage
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> install

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>全局声明，如果不声明，在组件中使用 this.没有代码提示</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/types/vab/plugins/globalProperties.d.ts</span>
<span class="hljs-keyword">export</span> &#123;&#125;
declare <span class="hljs-built_in">module</span> <span class="hljs-string">'@vue/runtime-core'</span> &#123;
  interface ComponentCustomProperties &#123;
    <span class="hljs-comment">// this.代码补全配置</span>
    <span class="hljs-attr">$request</span>: MyRequest.request,
    <span class="hljs-attr">$baseTableHeight</span>: <span class="hljs-function">(<span class="hljs-params">formType?: number</span>) =></span> number,
    <span class="hljs-attr">$image</span>: <span class="hljs-function">(<span class="hljs-params">src: string</span>) =></span> <span class="hljs-keyword">void</span>
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>使用</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//组件中使用</span>
<span class="hljs-built_in">this</span>.$request.post(<span class="hljs-string">'common.token'</span>, &#123;&#125;)
<span class="hljs-built_in">this</span>.$request.get(<span class="hljs-string">'common.token'</span>, &#123;&#125;)
<span class="hljs-comment">//ts文件中使用</span>
<span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">'@/utils/request'</span>
request.post(<span class="hljs-string">'common.token'</span>, &#123;&#125;)
request.get(<span class="hljs-string">'common.token'</span>, &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li>注意新增api模块后，要在 api/index.ts中导入，比如新增一个用户模块</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/api/user.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">list</span>: <span class="hljs-string">'/user/list'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/api/index.ts</span>
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/common'</span>
<span class="hljs-comment">// 导入新增模块</span>
<span class="hljs-keyword">import</span> user <span class="hljs-keyword">from</span> <span class="hljs-string">'@/api/user'</span>

interface UrlDict &#123;
  [key: string]: &#123;
    [key: string]: string
  &#125;
&#125;

<span class="hljs-keyword">const</span> urlDict: UrlDict = &#123;
  common,
  user <span class="hljs-comment">//新增模块</span>
&#125;

<span class="hljs-comment">// 使用</span>
<span class="hljs-built_in">this</span>.$request.get(<span class="hljs-string">'user.list'</span>, &#123;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            