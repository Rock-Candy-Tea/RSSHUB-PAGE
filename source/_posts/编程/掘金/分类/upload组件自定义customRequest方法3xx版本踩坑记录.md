
---
title: 'upload组件自定义customRequest方法3.x.x版本踩坑记录'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3265f525964797933a673f2678fcc1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 08:11:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3265f525964797933a673f2678fcc1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h1 data-id="heading-0">介绍</h1>
<p>江流儿是21届毕业生，是个热爱前端开发的好少年，喜欢收藏唯美壁纸与技术交流，此篇文章是江流的首秀，同时也作为笔记，不足之处还希望大佬指点出来，先放壁纸👇👇👇</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a3265f525964797933a673f2678fcc1~tplv-k3u1fbpfcp-watermark.image" alt="3D»æ»­ Å®ÆÍ ÃÀÍÈ ºÚË¿ ¸ß¸úÐ¬ Á½Î»Å®ÆÍ½øÃÅºóµÄÒ»Ä» 4k¶¯Âþ±ÚÖ½_±Ë°¶Í¼Íø.jpg" loading="lazy" referrerpolicy="no-referrer">
（图片来源网络侵权请留言）</p>
<p>这次主要分享的内容是antd的upload组件，我想如果公司业务没有涉及到这个上传业务的话我也不会去阅读upload的源码，为什么阅读这个组件的源码呢？有办法么？业务需要自定义，那为什么做这个分享呢？江流儿这几天一直收集相关的资料，发现关于自定义上传的资料，能让我看懂的实在是少的可怜，有办法嘛？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94b314ac97fb4b6185bfd687fea284cb~tplv-k3u1fbpfcp-watermark.image" alt="src=http---b-ssl.duitang.com-uploads-item-201707-25-20170725091808_ENmW8.thumb.700_0.jpeg&refer=http---b-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg.jpeg" loading="lazy" referrerpolicy="no-referrer">
下面进入正题👇👇👇</p>
<h1 data-id="heading-1">customRequest提供的API</h1>
<p>先上API</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fbaf194ee664db9aa0b22fbd1cc8d25~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-19 下午11.17.01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">onError 参数</h4>
<ol>
<li><code>err</code>: 请求错误信息</li>
<li><code>response</code>: 请求响应，不支持 iframeUpload</li>
<li><code>file</code>： 上传文件</li>
</ol>
<h3 data-id="heading-3"><a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.3.22%3A8000%2F%23onsuccess-arguments" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.3.22:8000/#onsuccess-arguments" ref="nofollow noopener noreferrer"></a>onSuccess 参数</h3>
<ol>
<li><code>result</code>: 响应体</li>
<li><code>file</code>： 上传文件</li>
<li><code>xhr</code>: xhr 标头，仅适用于支持 AJAX 上传的现代浏览器。从 2.4.0 开始</li>
</ol>
<h3 data-id="heading-4"><a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.3.22%3A8000%2F%23customrequest" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.3.22:8000/#customrequest" ref="nofollow noopener noreferrer"></a>自定义请求</h3>
<p>允许通过覆盖 AjaxUploader 中的默认行为进行高级自定义。提供您自己的 XMLHttpRequest 调用以与自定义后端进程交互或通过 aws-sdk-js 包与 AWS S3 服务交互。</p>
<p>customRequest 回调传递一个对象：</p>
<ul>
<li><code>onProgress: (event: &#123; percent: number &#125;): void</code></li>
<li><code>onError: (event: Error, body?: Object): void</code></li>
<li><code>onSuccess: (body: Object): void</code></li>
<li><code>data: Object</code></li>
<li><code>filename: String</code></li>
<li><code>file: File</code></li>
<li><code>withCredentials: Boolean</code></li>
<li><code>action: String</code></li>
<li><code>headers: Object</code></li>
</ul>
<p>以上是源码提供的材料👆👆👆</p>
<p>这几个操作方法有几个值得注意的：</p>
<ol>
<li>onProgress方法：获取进度的方法，但是这个进度每次调用只返回一个百分比，配合antd的Progress组件的话需要自己转化一下</li>
<li>file:这个是你要上传的文件，但是相比较antd已经封装好的会提供一个fileList（受控的），而file是一个对象，所以想要通过遍历的方式创建一个自定义的下载列表，需要包装</li>
<li>onSuccess：上传成功的回调，在这里可以执行自己上传后想要处理的逻辑，下面代码是结合antd的全局提醒，当然你可以写更复杂的逻辑</li>
</ol>
<h1 data-id="heading-5">customRequest例子</h1>
<p>这里废话不多说，直接代码+注释</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/* eslint-disable no-self-compare */</span>

<span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">import</span> &#123; Upload, Button, List,message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>

<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>

<span class="hljs-keyword">const</span> Myupload = <span class="hljs-function">() =></span> &#123;

<span class="hljs-keyword">const</span> [fileList, setFileList] = useState([])

<span class="hljs-keyword">const</span> uploadconfig = &#123;

<span class="hljs-attr">action</span>: <span class="hljs-string">''</span>,<span class="hljs-comment">//必填的url</span>

<span class="hljs-attr">multiple</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">//是否允许一次上传多个文件</span>

<span class="hljs-attr">headers</span>: &#123;

<span class="hljs-attr">Authorization</span>: <span class="hljs-string">'$prefix $token'</span>,<span class="hljs-comment">//请求头</span>

&#125;,

<span class="hljs-function"><span class="hljs-title">onStart</span>(<span class="hljs-params">file</span>)</span> &#123;<span class="hljs-comment">//这是这个函数开始执行时的打印传入的文件</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onStart'</span>, file, file.status);

&#125;,

<span class="hljs-function"><span class="hljs-title">onSuccess</span>(<span class="hljs-params">res, file</span>)</span> &#123;<span class="hljs-comment">//上传成功的回调函数</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onSuccess'</span>, res, file.name);

message.success(<span class="hljs-string">`<span class="hljs-subst">$&#123;file.name&#125;</span>上传成功`</span>)

&#125;,

<span class="hljs-function"><span class="hljs-title">onError</span>(<span class="hljs-params">err</span>)</span> &#123;<span class="hljs-comment">//上传出错的回调函数</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onError'</span>, err);

message.error(<span class="hljs-string">`上传失败`</span>)

&#125;,

<span class="hljs-function"><span class="hljs-title">onProgress</span>(<span class="hljs-params">&#123; percent &#125;, file</span>)</span> &#123;<span class="hljs-comment">//axios提供的获取进度（注意：此处有坑，江流儿尚未解决）</span>
<span class="hljs-comment">//再次回调函数中可以获取到进度，但是想要更新进度条就要在此函数中赋值，就会出现下面描述的bug</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onProgress'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;percent&#125;</span>%`</span>, file.name);

setFileList([&#123;<span class="hljs-attr">name</span>:file.name,<span class="hljs-attr">percent</span>:<span class="hljs-built_in">parseInt</span>(percent),<span class="hljs-attr">uid</span>:file.uid&#125;])
<span class="hljs-comment">//在这里可以看到是给fileList赋值了的，但是这里只允许上传一个文件，如果上传多个，就会出现bug</span>
<span class="hljs-comment">//bug：如果上传多个，会出现自定义下载列表的闪烁问题</span>
<span class="hljs-comment">//（这个问题江流儿也没有解决，希望有大佬指点迷津）</span>
&#125;,

<span class="hljs-attr">onRemove</span>:<span class="hljs-function">() =></span> delPackage,<span class="hljs-comment">//删除的回调</span>

<span class="hljs-function"><span class="hljs-title">customRequest</span>(<span class="hljs-params">&#123;

action,

file,

filename,

headers,

onError,

onProgress,

onSuccess,

withCredentials,

&#125;</span>)</span> &#123;

<span class="hljs-comment">// EXAMPLE: post form-data with 'axios'</span>

<span class="hljs-comment">// eslint-disable-next-line no-undef</span>

<span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData();

formData.append(filename, file);

<span class="hljs-keyword">var</span> CancelToken = axios.CancelToken;<span class="hljs-comment">//拿到中断请求的方法</span>

<span class="hljs-keyword">var</span> source = CancelToken.source();<span class="hljs-comment">//同上</span>

axios

.post(action, formData, &#123;

withCredentials,

headers,

<span class="hljs-attr">onUploadProgress</span>: <span class="hljs-function">(<span class="hljs-params">&#123; total, loaded &#125;</span>) =></span> &#123;

onProgress(&#123; <span class="hljs-attr">percent</span>: <span class="hljs-built_in">Math</span>.round((loaded / total) * <span class="hljs-number">100</span>).toFixed(<span class="hljs-number">2</span>) &#125;, file);

&#125;,

&#125;)

.then(<span class="hljs-function">(<span class="hljs-params">&#123; data: response &#125;</span>) =></span> &#123;

onSuccess(response, file);

&#125;)

.catch(onError);

<span class="hljs-keyword">return</span> &#123;

<span class="hljs-function"><span class="hljs-title">abort</span>(<span class="hljs-params"></span>)</span> &#123;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'终止函数'</span>);<span class="hljs-comment">//此处的函数仅仅是一个函数，而当你创建axios实例时，你会发现根本没有abort方法（应该是我的问题吧）</span>
<span class="hljs-comment">//想要定义终止函数需要以下代码👇</span>
             source.cancel()
<span class="hljs-comment">//为什么不用老的方法呢？是因为axios也变了，有办法么？没有办法。谁让我迭代了个老项目呢（入世太浅，努力学习）</span>
&#125;,

&#125;;

&#125;,

&#125;;

<span class="hljs-keyword">const</span> delPackage = <span class="hljs-function">(<span class="hljs-params">file,index</span>) =></span> &#123;
<span class="hljs-comment">//...你的自定义删除逻辑</span>
&#125;

<span class="hljs-keyword">const</span> &#123; Item &#125; = List;

<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">Upload</span> &#123;<span class="hljs-attr">...uploadconfig</span>&#125; <span class="hljs-attr">showUploadList</span>=<span class="hljs-string">&#123;false&#125;</span>></span>

<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'primary'</span>></span>点击上传<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>

<span class="hljs-tag"></<span class="hljs-name">Upload</span>></span>

<span class="hljs-tag"><<span class="hljs-name">List</span>

<span class="hljs-attr">itemLayout</span>=<span class="hljs-string">'vertical'</span>

></span>

&#123;

fileList.map((item,index) => &#123;

return (<span class="hljs-tag"><<span class="hljs-name">Item</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>&#123;item.name&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>进度：&#123;item.percent&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> &#123; delPackage(item,index) &#125;&#125; type='primary'>删除<span class="hljs-tag"></<span class="hljs-name">Button</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">Item</span>></span>)

&#125;)

&#125;

<span class="hljs-tag"></<span class="hljs-name">List</span>></span>

<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Myupload

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码可以完成的业务仅仅支撑本地上传单个文件，为什么没有讲上传多个文件呢？因为我也不会，等我研究出来在更，如果有大佬能看出我的忧伤～^_^，请帮帮孩子，如果有遇到此类问题的朋友，欢迎留言交流。</p>
<p>江流儿寄语（不是很重要，选择性阅读）：江流儿觉得，如果你能把文章看到这里了，就给江流儿一个赞吧，江流儿也努力成为一个高质量文章输出者，替更多的人解决问题，一路自学过来，就好像很火的一句话，“自己淋过雨，所以想为他人撑把伞吧。”欢迎想学前端，但是迷茫的小伙伴咨询哦😁</p>
<p>感谢阅读哦</p></div>  
</div>
            