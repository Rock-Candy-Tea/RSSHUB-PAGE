
---
title: '【node实战系列】编写一个重试装饰器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 00:08:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://github.com/bigo-frontend/blog/" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h2 data-id="heading-0">背景</h2>
<p>bigo前端开始推广bff，hello农场作为首个bff落地项目，历经2个月，完成了从0-1的落地实践。</p>
<p>【node实战系列】按照小模块拆分，从开发者的角度讲叙，如何进行bff高可用编码。</p>
<p>本系列文章，基于eggjs框架编码，使用ts语法，为了提升阅读体验，建议大家先了解一下eggjs。</p>
<h2 data-id="heading-1">系列文章</h2>
<ul>
<li><a href="https://github.com/bigo-frontend/blog/issues/49" target="_blank" rel="nofollow noopener noreferrer">【node实战系列】编写一个重试装饰器</a></li>
<li>【node实战系列】自行实现应用缓存</li>
<li>【node实战系列】异步并发，自定义Promise.allSettled</li>
<li>【node实战系列】rpc与http协议通讯</li>
<li>【node实战系列】使用reqId跟踪请求全流程日志</li>
<li>【node实战系列】入参校验validate</li>
<li>【node实战系列】异常中断</li>
<li>【node实战系列】base64编码</li>
<li>【node实战系列】服务发现</li>
<li>【node实战系列】编码与约定</li>
<li>【node实战系列】监控告警</li>
<li>【node实战系列】单元测试</li>
<li>【node实战系列】压测</li>
<li>【node实战系列】灰度</li>
<li>【node实战系列】文档</li>
<li>【node实战系列】系列小结</li>
</ul>
<p>欢迎大家关注我们的github blog，持续更新。
<a href="https://github.com/bigo-frontend/blog/issues" target="_blank" rel="nofollow noopener noreferrer">github.com/bigo-fronte…</a></p>
<h2 data-id="heading-2">为什么要重试</h2>
<p>这个很简单，项目开发中，调用第三方接口会因为网络延迟、异常导致调用的服务出错，重试几次可能就会调用成功（例如上传图片），所以需要一种重试机制进行接口重试来保证接口的正常执行。</p>
<h2 data-id="heading-3">为什么要用装饰器</h2>
<p>其实我们可以在接口调用外面再包装一个重试方法，如下编码。</p>
<pre><code class="copyable">/**
 *
 * @param &#123;number&#125; retries - 重试次数
 * @param &#123;Function&#125; fn - 重试函数
 */
const retry = (retries, fn) => &#123;
  fn().catch((err) => retries > 1 ? retry(retries - 1, fn) :  Promise.reject(err));
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种函数嵌套阅读起来不优雅，并且我们使用了ts进行编码，应该要物尽其用，发挥其装饰器能力。</p>
<p><code>装饰器简单来说就是对类或者其属性进行拓展，便于添加额外的功能。</code></p>
<h2 data-id="heading-4">什么是装饰器</h2>
<p>先来看一下retry装饰器在代码中是长成什么样子吧</p>
<pre><code class="copyable">@retry(3, (res) => res.code !== 0)
public async initFarm() &#123;
  const res = await this.request(&#123;
    opType: Eoperator.BASE_INIT_FARM,
  &#125;);
  return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码中<code>@retry(3, (res) => res.code !== 0)</code>就是一个装饰器了</p>
<p>以 @ 作为标识符，可以作用于类，也可以作用于类的属性，具体使用原理请查看文档 <a href="https://www.tslang.cn/docs/handbook/decorators.html" target="_blank" rel="nofollow noopener noreferrer">www.tslang.cn/docs/handbo…</a></p>
<h2 data-id="heading-5">方法装饰器</h2>
<p>我们的重试装饰器就是一个方法装饰器，我们先讲解一下方法装饰器的各属性</p>
<p>下面是一个方法装饰器（@enumerable）的例子，应用于Greeter类的方法上：</p>
<pre><code class="copyable">class Greeter &#123;
    greeting: string;
    constructor(message: string) &#123;
        this.greeting = message;
    &#125;

    @enumerable(false)
    greet() &#123;
        return "Hello, " + this.greeting;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以用下面的函数声明来定义@enumerable装饰器：</p>
<pre><code class="copyable">function enumerable(value: boolean) &#123;
    console.log(value); // 入参，false
    // target 对于静态成员来说是类的构造函数，对于实例成员是类的原型对象
    // propertyKey 成员的名字
    // descriptor 成员的属性描述符
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) &#123;
      descriptor.enumerable = value;
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">实现重试装饰器</h2>
<pre><code class="copyable">// 休眠，延迟执行
function sleep(duration) &#123;
  return new Promise((reslove) => setTimeout(reslove, duration))
&#125;
/**
 * 重试装饰器
 *
 * @param &#123;number&#125; retries 重试次数
 * @param &#123;*&#125; cb 重试条件
 * @returns
 */
export function retry(retries: number, cb) &#123;
  return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) &#123;
    // 1. 保存原方法体
    const oldMethod = descriptor.value;
    // 2. 重新定义方法体
    descriptor.value = async function(...args) &#123;
      // 重试
      const loop = async (count) => &#123;
        // 3. 执行原来的方法体
        const res = await oldMethod.apply(this, args);
        if (count > 1 && cb(res)) &#123;
          sleep(100); // 休眠100ms，再重试
          return loop(--count);
        &#125; else &#123;
          return res;
        &#125;
      &#125;;
      return loop(retries);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">小结</h2>
<p>回顾全文，我们发现一个小而美的重试装饰器就实现了，希望大家也可以动手，封装自己的装饰器。</p>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div>  
</div>
            