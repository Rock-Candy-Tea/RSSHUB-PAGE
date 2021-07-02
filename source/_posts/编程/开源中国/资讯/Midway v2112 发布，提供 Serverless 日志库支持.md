
---
title: 'Midway v2.11.2 发布，提供 Serverless 日志库支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.alicdn.com/imgextra/i4/O1CN01fUZcsQ253JIp6Rgsu_!!6000000007470-2-tps-1346-130.png'
author: 开源中国
comments: false
date: Fri, 02 Jul 2021 16:45:00 GMT
thumbnail: 'https://img.alicdn.com/imgextra/i4/O1CN01fUZcsQ253JIp6Rgsu_!!6000000007470-2-tps-1346-130.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>增强</h2> 
<h3>1、@midwayjs/logger 日志库支持多参数输出</h3> 
<p>由于之前 @midwayjs/logger 的日志对接了 winston3，由于 winston 的入参限制，无法支持多个参数。</p> 
<p>比如：</p> 
<pre>logger.info('123', '456', '789')；</pre> 
<p>对于 winston 来说，只会识别第一个字符串，midway 在其之上做了调整和优化，使其能支持最多 2 个参数。</p> 
<p>在新版本上，我们支持了任意数量的参数，原有的写法都恢复支持，用户不需要去记格式了。</p> 
<p>比如下面的格式也能输出的很好。</p> 
<pre>logger.info('123', [1, 2, 3], new Error('abc')；
</pre> 
<h3>2、替换阿里云 FC 环境下的默认日志对象</h3> 
<p>在 FC 下，平台自带的日志输出，会出现无法输出的问题</p> 
<p>比如（使用的是阿里云 context 上自带的 context.logger）：</p> 
<pre>this.ctx.logger.error(new Error('ccc'));</pre> 
<p>这句简单的错误对象输出，原来的效果</p> 
<p><img alt src="https://img.alicdn.com/imgextra/i4/O1CN01fUZcsQ253JIp6Rgsu_!!6000000007470-2-tps-1346-130.png" referrerpolicy="no-referrer"></p> 
<p>新版本我们将 context.logger 切换为了 midway 自带的 @midwayjs/logger 库（<strong><span style="background-color:#fadb14">仅在阿里云 FC 环境</span></strong>），将会更好的输出信息。</p> 
<p>新的错误输出：</p> 
<p><img alt src="https://img.alicdn.com/imgextra/i1/O1CN01vrQQcB1nvfDnTwVHS_!!6000000005152-2-tps-1890-500.png" referrerpolicy="no-referrer"></p> 
<h3>3、 bootstrap 时支持捕获额外的错误</h3> 
<p>之前在 bootstrap 中遗漏了对异步链错误的支持，在一些情况下会导致进程退出，虽然 pm2 等工具会记录最后的 error，但是为了优雅的处理和日志的统一性，还是需要增加这一监听。</p> 
<p>新版本增加了 <code>uncaughtException</code> 和 <code>unhandledRejection</code> 的监听，让一些特殊的错误也能捕获输出。</p> 
<p>比如下面的代码，如果监听了之后，就会输出 'got err'，否则就会报一个全局的错误。</p> 
<pre>let a;

// process.on('uncaughtException', err => &#123;
//console.log('got err');
//&#125;);

async fuction run() &#123;
  setTimeout(()  => &#123;
    a();
  &#125;, 100);
&#125;

run();

// TypeError: a is not a function</pre>
                                        </div>
                                      
</div>
            