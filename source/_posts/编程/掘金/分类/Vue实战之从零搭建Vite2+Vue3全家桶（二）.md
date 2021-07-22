
---
title: 'Vue实战之从零搭建Vite2+Vue3全家桶（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7147'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:29:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=7147'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇从整体架构上基本上已经搭建完成，遗漏了http请求工具，本篇主要是完善补充http请求工具axios的使用。</p>
<h1 data-id="heading-1">传送门</h1>
<p><a href="https://juejin.cn/post/6987172006747701256" target="_blank" title="https://juejin.cn/post/6987172006747701256">Vue实战之从零搭建Vite2+Vue3全家桶（一）</a></p>
<p><a href="https://juejin.cn/post/6984708706231386119" target="_blank" title="https://juejin.cn/post/6984708706231386119">基于Vue的架构设计</a></p>
<h1 data-id="heading-2">http请求工具</h1>
<p>这里采用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>axios</mtext></mstyle></mrow><annotation encoding="application/x-tex">\textrm\color&#123;red&#125;&#123;axios&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.66786em;vertical-align:0em;"></span><span class="mord text"><span class="mord" style="color:red;"><span class="mord textrm" style="color:red;">a</span><span class="mord textrm" style="color:red;">x</span><span class="mord textrm" style="color:red;">i</span><span class="mord textrm" style="color:red;">o</span><span class="mord textrm" style="color:red;">s</span></span></span></span></span></span></span>来进行http请求调用</p>
<h2 data-id="heading-3">安装axios</h2>
<pre><code class="copyable">  npm install axios -s
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">封装axios请求,新建request.js</h2>
<pre><code class="copyable">  import axios from 'axios'
  import &#123;
    ElLoading,
    ElMessage
  &#125; from 'element-plus';
  //创建axios的一个实例 
  const instance = axios.create(&#123;
    baseURL: import.meta.env.VITE_APP_URL, //接口统一域名
    timeout: 5000, //设置超时
    headers: &#123;
      'Content-Type': 'application/json;charset=UTF-8;',
    &#125;
  &#125;)
  let loading;
  //正在请求的数量
  let requestCount = 0
  //显示loading
  const showLoading = () => &#123;
    if (requestCount === 0 && !loading) &#123;
      loading = ElLoading.service(&#123;
        text: "Loading  ",
        background: 'rgba(0, 0, 0, 0.7)',
        spinner: 'el-icon-loading',
      &#125;)
    &#125;
    requestCount++;
  &#125;
  //隐藏loading
  const hideLoading = () => &#123;
    requestCount--
    if (requestCount == 0) &#123;
      loading.close()
    &#125;
  &#125;
  // instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  // instance.defaults.headers.get['Content-Type'] = 'application/x-www-form-urlencoded';
  // instance.defaults.transformRequest = [function (data) &#123;
  //   let ret = ''
  //   for (let it in data) &#123;
  //     ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
  //   &#125;
  //   return ret
  // &#125;]
  //请求拦截器 
  instance.interceptors.request.use((config) => &#123;
    showLoading()
    // 每次发送请求之前判断是否存在token，如果存在，则统一在http请求的header都加上token，不用每次请求都手动添加了
    const token = window.localStorage.getItem('token');
    token && (config.headers.Authorization = token)
    //若请求方式为post，则将data参数转为JSON字符串
    if (config.method === 'POST') &#123;
      config.data = JSON.stringify(config.data);
    &#125;
    return config;
  &#125;, (error) =>
    // 对请求错误做些什么
    Promise.reject(error));

  //响应拦截器
  instance.interceptors.response.use((response) => &#123;
    hideLoading()
    //响应成功
    return response.data;
  &#125;, (error) => &#123;
    console.log(error)
    //响应错误
    if (error.response && error.response.status) &#123;
      const status = error.response.status
      switch (status) &#123;
        case 400:
          message = '请求错误';
          break;
        case 401:
          message = '请求错误';
          break;
        case 404:
          message = '请求地址出错';
          break;
        case 408:
          message = '请求超时';
          break;
        case 500:
          message = '服务器内部错误!';
          break;
        case 501:
          message = '服务未实现!';
          break;
        case 502:
          message = '网关错误!';
          break;
        case 503:
          message = '服务不可用!';
          break;
        case 504:
          message = '网关超时!';
          break;
        case 505:
          message = 'HTTP版本不受支持';
          break;
        default:
          message = '请求失败'
      &#125;
      ElMessage.error(message);
      return Promise.reject(error);
    &#125;
    return Promise.reject(error);
  &#125;);

  const axios = (&#123;
    method,
    url,
    data,
    config
  &#125;) => &#123;
    method = method.toLowerCase();
    if (method == 'post') &#123;
      return instance.post(url, data, &#123; ...config &#125;)
    &#125; else if (method == 'get') &#123;
      return instance.get(url, &#123;
        params: data,
        ...config
      &#125;)
    &#125; else if (method == 'delete') &#123;
      return instance.delete(url, &#123;
        params: data,
        ...config
      &#125;)
    &#125; else if (method == 'put') &#123;
      return instance.put(url, data, &#123; ...config &#125;)
    &#125; else &#123;
      console.error(`错误的请求方式：$&#123;method&#125;`)
      return false
    &#125;
  &#125;
  export default axios

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">封装api请求</h2>
<pre><code class="copyable">  import request from '@/api/user.js'

  // 用户登录
  export function login(data) &#123;
    return request(&#123;
      url: '/api/login',
      method: 'post',
      data,
      config: &#123;
        headers: &#123;
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        &#125;,
        timeout: 10000
      &#125;
    &#125;)
  &#125;

  // 获取用户信息
  export function getInfo(data) &#123;
    return request(&#123;
      url: '/api/userinfo',
      method: 'get',
      params: data
    &#125;)
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">vue组件中使用</h2>
<pre><code class="copyable">  import &#123; login &#125; from '@/api/user'

  // 请求登录
  function onLogin() &#123;
    login(&#123; username: 'admin', pwd: 'admin' &#125;).then(res => &#123;
      // 业务逻辑
    &#125;)
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            