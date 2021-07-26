
---
title: '一种Vue应用程序错误_异常处理机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3070'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 01:41:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=3070'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>现在构建前端应用程序不像以前那么简单，现在，应用程序更加复杂和多样。这就需要在构建前端应用程序的时候考虑很多，错误/异常处理是最重要的方面之一。在应用程序中拥有良好的错误处理机制可以带来很多的好处，如下：</p>
<ul>
<li>良好的错误处理机制可以避免应用程序在出现未处理的异常时崩溃</li>
<li>在生产环境下，可以轻松地存储或者跟踪错误记录日志，以便异常的处理</li>
<li>可以统一处理错误信息，例如在不破坏应用程序交互的情况下，更改错误信息展示UI</li>
<li>有助于改善用户体验</li>
</ul>
<p>在前端应用程序中，最常见的错误/异常类型可能包括以下几种：</p>
<ul>
<li><strong>语法错误</strong>：使用了一些错误的语法</li>
<li><strong>运行时错误</strong>：由于执行期间的非法操作导致的</li>
<li><strong>逻辑错误</strong>：由于程序逻辑错误</li>
<li><strong>Http 错误</strong>：API 返回的错误</li>
</ul>
<p>有很多方法可以解决上面的问题，例如使用 <code>eslint</code> 来检查语法错误，使用适当的 <code>try-catch</code> 语句处理运行时错误，通过适当的<strong>单页或者集成</strong>测试减少逻辑错误，<code>http</code> 错误可以通过使用 <code>Promise</code> 来处理。</p>
<p>之前在文章《<a href="https://juejin.cn/post/6963977794715926536" target="_blank" title="https://juejin.cn/post/6963977794715926536">浅谈前端异常监控平台实现方案</a>》中简单介绍前端异常监控的实现方案，在本文中，将推荐一种在 Vue 应用程序中实现<strong>错误/异常</strong>处理机制。</p>
<h3 data-id="heading-0">全局配置</h3>
<p>Vue 应用程序有一个全局配置 <code>Vue.config</code>，可以配置禁止日志和告警、devtools、错误处理程序等等。</p>
<p>可以用自己的配置覆盖这些配置，对于错误处理，可以为其分配一个处理函数 <code>Vue.config.errorHandler</code>。在整个应用程序中，任何 Vue实例（Vue组件）中的任何未捕获异常都会调用该处理程序。以下代码片段为Vue 应用程序注册一个错误处理方法（一般在项目的 <code>main.js</code> 文件中）：</p>
<pre><code class="copyable">/**
 *
 * @param &#123;*&#125; error 错误跟踪
 * @param &#123;*&#125; vm 组件错误
 * @param &#123;*&#125; info 特定的错误信息，如生命周期钩子、事件等。
 */
Vue.config.errorHandler = (error, vm, info) => &#123;
    console.info(error);
    console.info(vm);
    console.info(info);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理程序包含 3 个参数：</p>
<ul>
<li><code>error</code>：完整的错误跟踪，包含 <code>message</code> 和 <code>error stack</code></li>
<li><code>vm</code>：发生错误的Vue组件/实例</li>
<li><code>info</code>： 特定的错误信息，例如生命周期钩子、事件等。</li>
</ul>
<blockquote>
<p><code>Vue.config.errorHandler</code> 捕获特定于Vue实例的错误，但无法捕获 Vue 实例之外的错误，如服务。</p>
</blockquote>
<p>要捕获 Vue 实例之外的错误，可以使用 <code>window.onerror</code> 事件，可以注册一个错误处理函数，该函数将捕获所有非特定于 Vue 实例的未处理异常。下面的代码片段为其应用注册<code>window.onerror</code> 异常处理函数：</p>
<pre><code class="copyable">window.onerror = function(message, source, lineno, colno, error) &#123;
  // TODO: 定义跟踪逻辑
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">自定义异常组件</h3>
<p>通常项目中有一些可预知的异常需要自定义 UI ，可以自定义异常组件来统一接管异常的处理。实现的逻辑是如果有异常显示异常信息，否则就显示组件信息，代码如下：</p>
<pre><code class="copyable"><template>
    <div>
        <slot v-if="errors" name="errors">
            <a-alert
                :message="errors.title"
                :description="errors.description"
                show-icon
                type="warning"
                class="mb-2"
            >
            </a-alert>
        </slot>
        <slot v-else></slot>
    </div>
</template>

<script>
export default &#123;
    name: "QtErrorContainer",
    props: &#123;
        errors: Object, // &#123;title:"500错误",description:"数据库连接超时"&#125;
    &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上面的组件作为容器来加载其他组件，如通过后台接口拉取列表数据，调用如下：</p>
<pre><code class="copyable"><QtErrorContainer :errors="errors">
    <a-table ></a-table>
</QtErrorContainer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码在 <code>errors</code> 为 <code>null</code> 或者 <code>false</code> 的时候，显示表格组件 <code><a-table></a-table></code>，否则不显示而显示异常信息。这样实现好处就是所有可预知的异常都由统一的组件来处理，提高复用和灵活性。</p>
<h3 data-id="heading-2">日志处理</h3>
<p>对于日志处理，可以封装为一个独立的类，如 <code>logger</code> ，负责收集Vue中所有的异常日志，输出到控制台或者通过接口发送到服务器存储或借助第三方日志跟踪平台，只需要修改 <code>logger</code> 的处理方式即可，如下：</p>
<pre><code class="copyable">import &#123; environment &#125; from "@/environment/";

/**
 * Logger 日志类
 */
class Logger &#123;
    /**
     * @constructor AppLogger
     */
    constructor() &#123;
        this.init();
    &#125;

    init() &#123;
        if (environment !== "production") &#123;
            this.log = console.log.bind(console);
            this.debug = console.debug.bind(console);
            this.info = console.info.bind(console);
            this.warn = console.warn.bind(console);
            this.error = console.error.bind(console);
            this.toServer = this.error;
        &#125; else &#123;
            /** 在生产的情况下，替换函数定义 */
            this.log = this.debug = this.info = this.warn = this.error = () => &#123;&#125;;
            /** TODO: 方法中可以增加接口或者第三方平台跟踪的逻辑 */
            this.toServer = (err) => &#123;
                console.error(err);
            &#125;;
        &#125;
    &#125;
&#125;

const logger = new Logger();

export &#123; logger &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以将 <code>logger</code> 类引用到上面的全局配置的处理方法中，如下：</p>
<pre><code class="copyable">import Vue from "vue";
import &#123; logger &#125; from "@/logger";
/**
 *
 * @param &#123;*&#125; error 错误跟踪
 * @param &#123;*&#125; vm 组件错误
 * @param &#123;*&#125; info 特定的错误信息，如生命周期钩子、事件等。
 */
Vue.config.errorHandler = (error, vm, info) => &#123;
    logger.toServer(&#123; error, vm, info &#125;);
&#125;;

window.onerror = function (message, source, lineno, colno, error) &#123;
    logger.toServer(&#123; message, source, lineno, colno, error &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">总结</h3>
<p>错误处理对于应用程序非常重要，在本文中，讨论了<code>Vue.config.errorHandler</code> 使用生命周期钩子的全局错误处理程序和自定义组件来处理可预知的异常。本文提供了基本细节，借助这些细节，可以轻松实现应用程序的错误处理并记录它们，这将有助于创建更好的用户体验。</p></div>  
</div>
            