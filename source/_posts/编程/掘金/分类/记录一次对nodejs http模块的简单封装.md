
---
title: '记录一次对nodejs http模块的简单封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5004'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 22:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5004'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><strong>前言</strong></h3>
<p>    <em>时至2021年，nodejs在web开发领域有着举足轻重的地位，常被应用于各种业务中间件开发以及构建工具插件开发，其web框架如express、koa、fastify、egg、midway、nest等也有一定的应用空间。本文将结合常见mvc框架特性，重点阐述nodejs在web mvc框架领域中的应用价值。希望对有兴趣自己封装框架的童鞋有所帮助！</em></p>
<h3 data-id="heading-1"><strong>正文</strong></h3>
<p>    常见mvc框架核心功能如下：1.请求/响应的统一处理机制；2.静态资源映射；3.http请求分发。本文将对以上3个问题点进行阐述，分别讲述解决方案！</p>
<h4 data-id="heading-2"><strong>1 请求/响应的统一处理机制</strong></h4>
<p>    这个问题利用http模块拦截机制实现，拦截原型如下：</p>
<pre><code class="copyable">function createServer(requestListener?: RequestListener): Server;
function createServer(options: ServerOptions, requestListener?: RequestListener): Server;
type RequestListener = (req: IncomingMessage, res: ServerResponse) => void;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    createServer函数接受一个请求监听器，该监听器包含了请求和响应对象，可以定义拦截器对请求响应的统一处理，如下进行了简单跨域处理：</p>
<pre><code class="copyable">export default function interceptor(req, res) &#123;
    console.log(`request $&#123;req.url&#125; is targeted!`.green.bold);
    // 跨域处理
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "*");
    res.setHeader("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><strong>2 静态资源映射</strong></h4>
<p>     在对静态资源映射前，首先需要区分接口请求和资源请求，如接口请求则转发给业务代码进行处理，资源请求则直接读取本地文件返回即可。因此，需要解决以下问题:</p>
<h5 data-id="heading-4">（1）区分接口请求和资源请求</h5>
<p>     简单区分可以采用url前缀进行区分，以/api开头的为接口请求，否则为资源请求。</p>
<pre><code class="copyable">export default async function(req, res) &#123;
    try &#123;
        if (req.url.startsWith('/api')) &#123; //接口请求
            await dispatchActions(req, res)
        &#125; else &#123; //资源请求
            ...
        &#125;
    &#125; catch (error) &#123;
        console.error(error);
        res.statusCode = 500;
        res.end('服务器异常');
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    资源请求又可细分为后端资源请求和前端资源请求，因此需要添加响应配置项进行处理。</p>
<pre><code class="copyable">let path;
const urlObj = new URL(req.url, globalThis.$HOST);
if (req.url.startsWith('upload')) &#123; // 后端资源请求
         path = join(cwd(), urlObj.pathname);
   &#125; else &#123; // 前端资源请求
         let pathname = urlObj.pathname === '/' ? '/index.html' : urlObj.pathname;
         path = join(cwd(), config.views, pathname);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">（2）对资源请求设置适当的ContentType</h5>
<p>    <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftool.oschina.net%2Fcommons" target="_blank" rel="nofollow noopener noreferrer" title="https://tool.oschina.net/commons" ref="nofollow noopener noreferrer">Content-Type对照表</a>可以获取常用文件后缀以及对应的contentType，通过工具类处理响应即可。</p>
<pre><code class="copyable">async function setContentType(path, res) &#123;
    try &#123;
        let contentType;
        if (path.includes('.')) &#123;
            const suffix = '.' + path.split('.')[1];
            metaData[suffix] ? (contentType = metaData[suffix]) : (contentType = metaData['.*']);
        &#125;
        if (contentType === 'text/html' || contentType === 'text/plain') &#123;
            contentType += ';charset=utf-8';
        &#125;
        if (contentType) &#123;
            res.setHeader('Content-Type', contentType);
        &#125;      
    &#125; catch (error) &#123;
        console.error(error)
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><strong>3 http请求分发</strong></h4>
<h5 data-id="heading-7">(1) 编写请求分发函数</h5>
<pre><code class="copyable">async function dispatchActions(req, res) &#123;
    const urlObj = new URL(req.url, globalThis.$HOST);
    const api = urlObj.pathname.split('/api')[1];
    if (getControllerExport()[api]) &#123;
        await getControllerExport()[api](req, res);
    &#125; else  &#123;
        res.statusCode = 404;
        res.end('not found');
    &#125; 
&#125;
export function setControllerExport(data) &#123;
    globalThis.$CONTROLLER = data;
&#125;

export function getControllerExport() &#123;
    return globalThis.$CONTROLLER;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">(2) 仿照webpack require.context功能实现读取同一文件下的其他文件的默认导出</h5>
<pre><code class="copyable">// controll/index.mjs
async function autoImpotController(dir, exclude) &#123;
    let result = &#123;&#125;;
    const files = await readdir(dir);
    if (files?.length) &#123;
        for (let i = 0; i < files.length; i++) &#123;
            if (exclude !== files[i]) &#123;
                const module = await import('./' + files[i]);
                result = &#123;...result, ...module.default&#125;;
            &#125;
        &#125;
    &#125;
    setControllerExport(result);
&#125;

const fileUrl = import.meta.url;
const dir = dirname(fileURLToPath(fileUrl));
const exclude = basename(fileURLToPath(fileUrl));
autoImpotController(dir, exclude);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">(3) 编写controller</h5>
<pre><code class="copyable">// controll/user.mjs
const base="/user";

const controllers = &#123;
    getUsername : async function (req, res) &#123;
        try &#123;
            res.setHeader('Content-Type', 'application/json;charset=utf-8');
            res.end(getJsonResult(true, 'getUsername'));
        &#125; catch (error) &#123;
            throw new Error(error);
        &#125;
    &#125;
&#125;

const ept = &#123;&#125;;
Object.keys(controllers).forEach(controller => &#123;
    ept[`$&#123;base&#125;/$&#123;controller&#125;`] = controllers[controller];
&#125;)
export default ept;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10"><strong>4 基于注解的controller开发</strong></h4>
<p>    经过查询资料发现，基于typescript的注解开发处于实验阶段，而ecmascript注解提案处于第二阶段，详见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftc39%2Fproposal-decorators" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tc39/proposal-decorators" ref="nofollow noopener noreferrer">github.com/tc39/propos…</a> ,本文暂时不作探究，感兴趣的童鞋可以自行研究下！最终的controller写法应类似：</p>
<pre><code class="copyable">@controller(&#123;baes: 'uesr'&#125;)
class UserController &#123;
     @Request(&#123;path: '/user', method: 'GET', contentType: 'application/json;charset=utf-8'&#125;)
     async getUsername() &#123;
        try &#123;
            res.setHeader('Content-Type', 'application/json;charset=utf-8');
            res.end(getJsonResult(true, 'getUsername'));
        &#125; catch (error) &#123;
            throw new Error(error);
        &#125;
     &#125;
     
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><strong>5 欢迎访问原文链接</strong></h4>
<p>欢迎访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Fyxlolxy.gitee.io%2F%23%2Farticle%2FI42J20" target="_blank" rel="nofollow noopener noreferrer" title="https://yxlolxy.gitee.io/#/article/I42J20" ref="nofollow noopener noreferrer">我的博客-利用nodejs仿express对http模块进行简易封装</a></p></div>  
</div>
            