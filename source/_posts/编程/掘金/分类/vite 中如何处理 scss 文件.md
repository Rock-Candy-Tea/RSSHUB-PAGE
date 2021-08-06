
---
title: 'vite 中如何处理 scss 文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9073'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:41:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=9073'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>热乎～～～</p>
<h3 data-id="heading-0">页面(client)与vite启的服务(server)之间是如何处理 scss 资源的</h3>
<ol>
<li>访问 localhost:3000 页面</li>
<li>页面发送请求获取 app.scss</li>
<li>vite server 接收请求走到函数 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2FtransformRequest.ts%23L39" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/node/server/transformRequest.ts#L39" ref="nofollow noopener noreferrer">transformRequest</a> ，接着开始根据请求的地址获取文件 scss 源码</li>
<li>将得到的源码传入 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2FtransformRequest.ts%23L131" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/node/server/transformRequest.ts#L131" ref="nofollow noopener noreferrer">pluginContainer.transform((code, id, map, ssr))</a>。pluginContainer.transform 开始处理scss源码，会调用对应的插件来处理scss源码，内置插件是有顺序的。
1. 预处理解析 sccs 得到 css：调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2Fcss.ts%23L131" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/node/plugins/css.ts#L131" ref="nofollow noopener noreferrer">cssPlugin</a> 解析 scss 得到 css 代码。中间利用了 postcss
2.  后处理将 css 包装成 js 代码：调用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fplugins%2Fcss.ts%23L244" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/node/plugins/css.ts#L244" ref="nofollow noopener noreferrer">cssPostPlugin</a>。</li>
<li>处理完资源之后返回给 client，原理类似 jsonp。client 接受到的js中有 css 的数据，会调用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fclient%2Fclient.ts%23L241" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/client/client.ts#L241" ref="nofollow noopener noreferrer">updateStyle</a> 将数据更新到页面上，updateStyle 是 vite 提前注入的，用来创建一个 style 标签，并将 css 的数据放到 style 标签上，然后插入页面，样式生效。</li>
</ol>
<h3 data-id="heading-1">热更新与缓存</h3>
<blockquote>
<p>封装了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Fblob%2F8c5ac3f89c69717b3bddedc229b77fabb9239085%2Fpackages%2Fvite%2Fsrc%2Fnode%2Fserver%2Fsend.ts%23L14" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/blob/8c5ac3f89c69717b3bddedc229b77fabb9239085/packages/vite/src/node/server/send.ts#L14" ref="nofollow noopener noreferrer">send</a>，默认只有协商缓存etag，强缓存设置为 no-cache。强缓存和协商缓存同时存在的时候，先强缓存后协商缓存。</p>
</blockquote>
<p>如果是利用 http 强缓存，不用再次编译。</p>
<p>如果是协商缓存，利用 etag，client会一直询问server的etag签名是否匹配，否则重新编译。</p>
<ol>
<li>** css 资源则是利用的协商缓存 **</li>
<li>依赖比如 react 这种走的强缓存：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fguide%2Fdep-pre-bundling.html%23browser-cache" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/guide/dep-pre-bundling.html#browser-cache" ref="nofollow noopener noreferrer">浏览器缓存</a></li>
</ol></div>  
</div>
            