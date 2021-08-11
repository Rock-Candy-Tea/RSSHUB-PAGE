
---
title: '手摸手，带你尝鲜 naiveui 撸 admin 骨架（准备篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df60c08f87c649e2a6195903d0d97932~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 19:40:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df60c08f87c649e2a6195903d0d97932~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近admin骨架，呼声比较多，说好的教程呢，咋也不能做个失言的小伙子，言归正传，第一篇文章主要来说一说在开始写实际业务代码之前的一些准备工作。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df60c08f87c649e2a6195903d0d97932~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-1">目录结构</h1>
<pre><code class="copyable">├── build                      // 构建相关  
├── mock                      // 项目mock 模拟数据
├── types                     // 全局 ts 类型 接口定义
├── config                     // 配置相关
├── src                        // 源代码
│   ├── api                    // 所有请求
│   ├── assets                 // 主题 字体等静态资源
│   ├── components             // 全局公用组件
│   ├── directive              // 全局指令
│   ├── enums                 // 枚举定义
│   ├── hooks                 // 公共hooks
│   ├── layout      //骨架布局
│   ├── plugins     //第三方插件
│   ├── router     //路由配置
│   ├── settings     //配置相关
│   ├── store      //状态管理器
│   ├── styles      //公共样式
│   ├── utils                  // 全局公用方法
│   ├── views                   // 页面
│   ├── App.vue                // 入口页面
│   ├── main.ts                // 入口 加载组件 初始化等
├── .gitignore                 // git 忽略项
├── .eslintignore // eslint 忽略项
├── .eslintrc.js // eslint 配置
├── tailwind.config.js // tailwind 配置
├── stylelint.config.js // stylelint 配置
├── postcss.config.js // postcss 配置
├── prettier.config.js // prettier 配置
├── tsconfig.json // ts 配置
├── vite.config.js// vite 配置
├── index.html                 // html模板
└── package.json               // package.json
└── 省略........// 更多介绍的就不写了哈，然后，没有然后了
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">api 和 views</h1>
<p>目前定义如下，随着页面越来越多，建议还是，api 模块和views对应起来，方便后期维护。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2aac7b571cef4a0aa37b8794fe7e6896~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
src=>api<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f6d898b11c94c4f800f8b2a58fa3d25~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
src=>views<a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-3">components</h1>
<p>这里的 components 放置的都是全局公用的一些组件，如上传组件，表格，弹窗，等等。一些页面级的组件建议还是放在各自views文件下，方便管理。如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e051abcdd16f4dff884e5391a6b74986~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-4">store</h1>
<p>这里我个人建议用 pinia 代替 vuex，也可以说是习惯吧，看你怎么选了，我个人感觉 pinia 优雅一点，具体优点不过多陈述，可移步官网瞧瞧哈。</p>
<h1 data-id="heading-5">vite</h1>
<p>下一代前端开发与构建工具，极速的服务启动，轻量快速地热重载，优化的构建，完全类型化的API，更多优点也不过多陈述，可移步官网瞧瞧哈。</p>
<p>这里说一下，<strong>alias</strong>，和 <strong>plugins</strong></p>
<p><strong>alias，</strong> 当项目逐渐变大之后，文件与文件直接的引用关系会很复杂，这时候就需要使用alias 了， 有的人喜欢alias 指向src目录下，再使用相对路径找文件，因人而异了。</p>
<p><strong>plugins，</strong> 当项目逐渐变大之后，vite.config.js 可能会变得又臭又长，尤其是 <strong>plugins</strong> 所以建议还是，抽离出来，比如下面这样：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63cccf3e3bb64651b6f0a415ef0b60dd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee92684492574d7f857dc006dbe92a82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-6">ESLint</h1>
<p>不管是多人合作还是个人项目，代码规范是很重要的，这样做不仅可以很大程度地避免基本语法错误，也保证了代码的可读性，个人推荐 eslint+vscode | webstorm 来写 vue，绝对有种飞一般的感觉。</p>
<h1 data-id="heading-7">mock</h1>
<p>vite项目推荐用，vite-plugin-mock 来构建mock，使用简单，以下这种写法，只需在mock中创建文件，和api里面的接口对应起来，即可实现mock</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f2a93f1951e40efb0cf37a8256e5fff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3f1224735a443fbb3272203fb57da41~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b42e75a6eec47f9871e17a2c4b564b3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-8">封装 axios</h1>
<pre><code class="copyable">// axios配置  可自行根据项目进行更改，只需更改该文件即可，其他文件可以不动
import &#123; VAxios &#125; from './Axios';
import &#123; AxiosTransform &#125; from './axiosTransform';
import axios, &#123; AxiosResponse &#125; from 'axios';
import &#123; checkStatus &#125; from './checkStatus';
import &#123; joinTimestamp, formatRequestDate &#125; from './helper';
import &#123; RequestEnum, ResultEnum, ContentTypeEnum &#125; from '@/enums/httpEnum';

import &#123; useGlobSetting &#125; from '@/hooks/setting';

import &#123; isString &#125; from '@/utils/is/';
import &#123; setObjToUrlParams &#125; from '@/utils/urlUtils';

import &#123; RequestOptions, Result &#125; from './types';

import &#123; useUserStoreWidthOut &#125; from '@/store/modules/user';

const globSetting = useGlobSetting();
const urlPrefix = globSetting.urlPrefix || '';

import router from '@/router';
import &#123; storage &#125; from '@/utils/Storage';

/**
 * @description: 数据处理，方便区分多种处理方式
 */
const transform: AxiosTransform = &#123;
  /**
   * @description: 处理请求数据
   */
  transformRequestData: (res: AxiosResponse<Result>, options: RequestOptions) => &#123;
    const &#123; $message: Message, $dialog: Modal &#125; = window;
    const &#123;
      isShowMessage = true,
      isShowErrorMessage,
      isShowSuccessMessage,
      successMessageText,
      errorMessageText,
      isTransformResponse,
      isReturnNativeResponse,
    &#125; = options;

    // 是否返回原生响应头 比如：需要获取响应头时使用该属性
    if (isReturnNativeResponse) &#123;
      return res;
    &#125;
    // 不进行任何处理，直接返回
    // 用于页面代码可能需要直接获取code，data，message这些信息时开启
    if (!isTransformResponse) &#123;
      return res.data;
    &#125;

    const reject = Promise.reject;

    const &#123; data &#125; = res;

    if (!data) &#123;
      // return '[HTTP] Request has no return value';
      return reject(data);
    &#125;
    //  这里 code，result，message为 后台统一的字段，需要在 types.ts内修改为项目自己的接口返回格式
    const &#123; code, result, message &#125; = data;
    // 请求成功
    const hasSuccess = data && Reflect.has(data, 'code') && code === ResultEnum.SUCCESS;
    // 是否显示提示信息
    if (isShowMessage) &#123;
      if (hasSuccess && (successMessageText || isShowSuccessMessage)) &#123;
        // 是否显示自定义信息提示
        Message.success(successMessageText || message || '操作成功！');
      &#125; else if (!hasSuccess && (errorMessageText || isShowErrorMessage)) &#123;
        // 是否显示自定义信息提示
        Message.error(message || errorMessageText || '操作失败！');
      &#125; else if (!hasSuccess && options.errorMessageMode === 'modal') &#123;
        // errorMessageMode=‘custom-modal’的时候会显示modal错误弹窗，而不是消息提示，用于一些比较重要的错误
        Modal.info(&#123;
          title: '提示',
          content: message,
          positiveText: '确定',
          onPositiveClick: () => &#123;&#125;,
        &#125;);
      &#125;
    &#125;

    // 接口请求成功，直接返回结果
    if (code === ResultEnum.SUCCESS) &#123;
      return result;
    &#125;
    // 接口请求错误，统一提示错误信息
    if (code === ResultEnum.ERROR) &#123;
      if (message) &#123;
        Message.error(data.message);
        Promise.reject(new Error(message));
      &#125; else &#123;
        const msg = '操作失败,系统异常!';
        Message.error(msg);
        Promise.reject(new Error(msg));
      &#125;
      return reject();
    &#125;

    // 登录超时
    if (code === ResultEnum.TIMEOUT) &#123;
      if (router.currentRoute.value.name == 'login') return;
      // 到登录页
      const timeoutMsg = '登录超时,请重新登录!';
      Modal.warning(&#123;
        title: '提示',
        content: '登录身份已失效，请重新登录!',
        positiveText: '确定',
        negativeText: '取消',
        onPositiveClick: () => &#123;
          storage.clear();
          router.replace(&#123;
            name: 'login',
            query: &#123;
              redirect: router.currentRoute.value.fullPath,
            &#125;,
          &#125;);
        &#125;,
        onNegativeClick: () => &#123;&#125;,
      &#125;);
      return reject(new Error(timeoutMsg));
    &#125;

    // 这里逻辑可以根据项目进行修改
    if (!hasSuccess) &#123;
      return reject(new Error(message));
    &#125;

    return data;
  &#125;,

  // 请求之前处理config
  beforeRequestHook: (config, options) => &#123;
    const &#123; apiUrl, joinPrefix, joinParamsToUrl, formatDate, joinTime = true &#125; = options;

    if (joinPrefix) &#123;
      config.url = `$&#123;urlPrefix&#125;$&#123;config.url&#125;`;
    &#125;

    if (apiUrl && isString(apiUrl)) &#123;
      config.url = `$&#123;apiUrl&#125;$&#123;config.url&#125;`;
    &#125;
    const params = config.params || &#123;&#125;;
    if (config.method?.toUpperCase() === RequestEnum.GET) &#123;
      if (!isString(params)) &#123;
        // 给 get 请求加上时间戳参数，避免从缓存中拿数据。
        config.params = Object.assign(params || &#123;&#125;, joinTimestamp(joinTime, false));
      &#125; else &#123;
        // 兼容restful风格
        config.url = config.url + params + `$&#123;joinTimestamp(joinTime, true)&#125;`;
        config.params = undefined;
      &#125;
    &#125; else &#123;
      if (!isString(params)) &#123;
        formatDate && formatRequestDate(params);
        config.data = params;
        config.params = undefined;
        if (joinParamsToUrl) &#123;
          config.url = setObjToUrlParams(config.url as string, config.data);
        &#125;
      &#125; else &#123;
        // 兼容restful风格
        config.url = config.url + params;
        config.params = undefined;
      &#125;
    &#125;
    return config;
  &#125;,

  /**
   * @description: 请求拦截器处理
   */
  requestInterceptors: (config) => &#123;
    // 请求之前处理config
    const userStore = useUserStoreWidthOut();
    const token = userStore.getToken;
    if (token) &#123;
      // jwt token
      config.headers.token = token;
    &#125;
    return config;
  &#125;,

  /**
   * @description: 响应错误处理
   */
  responseInterceptorsCatch: (error: any) => &#123;
    const &#123; $message: Message, $dialog: Modal &#125; = window;
    const &#123; response, code, message &#125; = error || &#123;&#125;;
    // TODO 此处要根据后端接口返回格式修改
    const msg: string =
      response && response.data && response.data.message ? response.data.message : '';
    const err: string = error.toString();
    try &#123;
      if (code === 'ECONNABORTED' && message.indexOf('timeout') !== -1) &#123;
        Message.error('接口请求超时,请刷新页面重试!');
        return;
      &#125;
      if (err && err.includes('Network Error')) &#123;
        Modal.info(&#123;
          title: '网络异常',
          content: '请检查您的网络连接是否正常!',
          positiveText: '确定',
          onPositiveClick: () => &#123;&#125;,
        &#125;);
        return;
      &#125;
    &#125; catch (error) &#123;
      throw new Error(error);
    &#125;
    // 请求是否被取消
    const isCancel = axios.isCancel(error);
    if (!isCancel) &#123;
      checkStatus(error.response && error.response.status, msg, Message);
    &#125; else &#123;
      console.warn(error, '请求被取消！');
    &#125;
    return error;
  &#125;,
&#125;;

const Axios = new VAxios(&#123;
  timeout: 10 * 1000,
  // 接口前缀
  prefixUrl: urlPrefix,
  headers: &#123; 'Content-Type': ContentTypeEnum.JSON &#125;,
  // 数据处理方式
  transform,
  // 配置项，下面的选项都可以在独立的接口请求中覆盖
  requestOptions: &#123;
    // 默认将prefix 添加到url
    joinPrefix: true,
    // 是否返回原生响应头 比如：需要获取响应头时使用该属性
    isReturnNativeResponse: false,
    // 需要对返回数据进行处理
    isTransformResponse: true,
    // post请求的时候添加参数到url
    joinParamsToUrl: false,
    // 格式化提交参数时间
    formatDate: true,
    // 消息提示类型
    errorMessageMode: 'none',
    // 接口地址
    apiUrl: globSetting.apiUrl as string,
  &#125;,
  withCredentials: false,
&#125;);

export default Axios;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">跨域问题</h1>
<p>首先前后端交互不可避免的就会遇到跨域问题，有些是后端小哥解决好了，如果你司后端小哥嫌麻烦不肯配置的话， 可以通过vite的proxy来解决。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec0595989ae94325b6bccf687ac334ab~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d902c88686e44daa7f5d26d7817c567~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<h1 data-id="heading-10">提示</h1>
<p>此系列教程，持续更新中，直到搭建完整个 Admin Pro 框架，请大家监督我哈~[谢谢]</p>
<h1 data-id="heading-11">结尾</h1>
<p>以上是一些基础建设工作，下一篇，<strong>正式开撸</strong>，好了，你说你都看到这了，免费的关注点一点在走吧，好人一生平安，bug都会远离你O(∩_∩)O哈哈~[奸笑]</p></div>  
</div>
            