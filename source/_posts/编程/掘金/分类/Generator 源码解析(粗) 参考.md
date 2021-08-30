
---
title: 'Generator 源码解析(粗) 参考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2277'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 01:08:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=2277'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>配合另一篇文章食用~ <a href="https://juejin.cn/post/7001010747400536094" target="_blank" title="https://juejin.cn/post/7001010747400536094"># 一文了解promise generator async的原理</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Copyright (c) 2014-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */</span>

<span class="hljs-keyword">var</span> runtime = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">exports</span></span>) </span>&#123;
<span class="hljs-meta">  "use strict"</span>;

  <span class="hljs-keyword">var</span> Op = <span class="hljs-built_in">Object</span>.prototype;
  <span class="hljs-keyword">var</span> hasOwn = Op.hasOwnProperty;
  <span class="hljs-keyword">var</span> <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// More compressible than void 0.</span>
  <span class="hljs-keyword">var</span> $Symbol = <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Symbol</span> === <span class="hljs-string">"function"</span> ? <span class="hljs-built_in">Symbol</span> : &#123;&#125;;
  <span class="hljs-keyword">var</span> iteratorSymbol = $Symbol.iterator || <span class="hljs-string">"@@iterator"</span>;
  <span class="hljs-keyword">var</span> asyncIteratorSymbol = $Symbol.asyncIterator || <span class="hljs-string">"@@asyncIterator"</span>;
  <span class="hljs-keyword">var</span> toStringTagSymbol = $Symbol.toStringTag || <span class="hljs-string">"@@toStringTag"</span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">define</span>(<span class="hljs-params">obj, key, value</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
      <span class="hljs-attr">value</span>: value,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>
    &#125;);
    <span class="hljs-keyword">return</span> obj[key];
  &#125;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// IE 8 has a broken Object.defineProperty that only works on DOM objects.</span>
    define(&#123;&#125;, <span class="hljs-string">""</span>);
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    define = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj, key, value</span>) </span>&#123;
      <span class="hljs-keyword">return</span> obj[key] = value;
    &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrap</span>(<span class="hljs-params">innerFn, outerFn, self, tryLocsList</span>) </span>&#123;
    <span class="hljs-comment">// If outerFn provided and outerFn.prototype is a Generator, then outerFn.prototype instanceof Generator.</span>
    <span class="hljs-keyword">var</span> protoGenerator = outerFn && outerFn.prototype <span class="hljs-keyword">instanceof</span> Generator ? outerFn : Generator;
    <span class="hljs-keyword">var</span> generator = <span class="hljs-built_in">Object</span>.create(protoGenerator.prototype);
    <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Context(tryLocsList || []);

    <span class="hljs-comment">// The ._invoke method unifies the implementations of the .next,</span>
    <span class="hljs-comment">// .throw, and .return methods.</span>
    generator._invoke = makeInvokeMethod(innerFn, self, context);

    <span class="hljs-keyword">return</span> generator;
  &#125;
  <span class="hljs-built_in">exports</span>.wrap = wrap;

  <span class="hljs-comment">// Try/catch helper to minimize deoptimizations. Returns a completion</span>
  <span class="hljs-comment">// record like context.tryEntries[i].completion. This interface could</span>
  <span class="hljs-comment">// have been (and was previously) designed to take a closure to be</span>
  <span class="hljs-comment">// invoked without arguments, but in all the cases we care about we</span>
  <span class="hljs-comment">// already have an existing method we want to call, so there's no need</span>
  <span class="hljs-comment">// to create a new function object. We can even get away with assuming</span>
  <span class="hljs-comment">// the method takes exactly one argument, since that happens to be true</span>
  <span class="hljs-comment">// in every case, so we don't have to touch the arguments object. The</span>
  <span class="hljs-comment">// only additional allocation required is the completion record, which</span>
  <span class="hljs-comment">// has a stable shape and so hopefully should be cheap to allocate.</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tryCatch</span>(<span class="hljs-params">fn, obj, arg</span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"normal"</span>, <span class="hljs-attr">arg</span>: fn.call(obj, arg) &#125;;
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"throw"</span>, <span class="hljs-attr">arg</span>: err &#125;;
    &#125;
  &#125;

  <span class="hljs-keyword">var</span> GenStateSuspendedStart = <span class="hljs-string">"suspendedStart"</span>;
  <span class="hljs-keyword">var</span> GenStateSuspendedYield = <span class="hljs-string">"suspendedYield"</span>;
  <span class="hljs-keyword">var</span> GenStateExecuting = <span class="hljs-string">"executing"</span>;
  <span class="hljs-keyword">var</span> GenStateCompleted = <span class="hljs-string">"completed"</span>;

  <span class="hljs-comment">// Returning this object from the innerFn has the same effect as</span>
  <span class="hljs-comment">// breaking out of the dispatch switch statement.</span>
  <span class="hljs-keyword">var</span> ContinueSentinel = &#123;&#125;;

  <span class="hljs-comment">// Dummy constructor functions that we use as the .constructor and</span>
  <span class="hljs-comment">// .constructor.prototype properties for functions that return Generator</span>
  <span class="hljs-comment">// objects. For full spec compliance, you may wish to configure your</span>
  <span class="hljs-comment">// minifier not to mangle the names of these two functions.</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Generator</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">GeneratorFunction</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">GeneratorFunctionPrototype</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

  <span class="hljs-comment">// This is a polyfill for %IteratorPrototype% for environments that</span>
  <span class="hljs-comment">// don't natively support it.</span>
  <span class="hljs-keyword">var</span> IteratorPrototype = &#123;&#125;;
  define(IteratorPrototype, iteratorSymbol, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;);

  <span class="hljs-keyword">var</span> getProto = <span class="hljs-built_in">Object</span>.getPrototypeOf;
  <span class="hljs-keyword">var</span> NativeIteratorPrototype = getProto && getProto(getProto(values([])));
  <span class="hljs-keyword">if</span> (NativeIteratorPrototype &&
      NativeIteratorPrototype !== Op &&
      hasOwn.call(NativeIteratorPrototype, iteratorSymbol)) &#123;
    <span class="hljs-comment">// This environment has a native %IteratorPrototype%; use it instead</span>
    <span class="hljs-comment">// of the polyfill.</span>
    IteratorPrototype = NativeIteratorPrototype;
  &#125;

  <span class="hljs-keyword">var</span> Gp = GeneratorFunctionPrototype.prototype =
    Generator.prototype = <span class="hljs-built_in">Object</span>.create(IteratorPrototype);
  GeneratorFunction.prototype = GeneratorFunctionPrototype;
  define(Gp, <span class="hljs-string">"constructor"</span>, GeneratorFunctionPrototype);
  define(GeneratorFunctionPrototype, <span class="hljs-string">"constructor"</span>, GeneratorFunction);
  GeneratorFunction.displayName = define(
    GeneratorFunctionPrototype,
    toStringTagSymbol,
    <span class="hljs-string">"GeneratorFunction"</span>
  );

  <span class="hljs-comment">// Helper for defining the .next, .throw, and .return methods of the</span>
  <span class="hljs-comment">// Iterator interface in terms of a single ._invoke method.</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineIteratorMethods</span>(<span class="hljs-params">prototype</span>) </span>&#123;
    [<span class="hljs-string">"next"</span>, <span class="hljs-string">"throw"</span>, <span class="hljs-string">"return"</span>].forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">method</span>) </span>&#123;
      define(prototype, method, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arg</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._invoke(method, arg);
      &#125;);
    &#125;);
  &#125;

  <span class="hljs-built_in">exports</span>.isGeneratorFunction = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">genFun</span>) </span>&#123;
    <span class="hljs-keyword">var</span> ctor = <span class="hljs-keyword">typeof</span> genFun === <span class="hljs-string">"function"</span> && genFun.constructor;
    <span class="hljs-keyword">return</span> ctor
      ? ctor === GeneratorFunction ||
        <span class="hljs-comment">// For the native GeneratorFunction constructor, the best we can</span>
        <span class="hljs-comment">// do is to check its .name property.</span>
        (ctor.displayName || ctor.name) === <span class="hljs-string">"GeneratorFunction"</span>
      : <span class="hljs-literal">false</span>;
  &#125;;

  <span class="hljs-built_in">exports</span>.mark = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">genFun</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.setPrototypeOf) &#123;
      <span class="hljs-built_in">Object</span>.setPrototypeOf(genFun, GeneratorFunctionPrototype);
    &#125; <span class="hljs-keyword">else</span> &#123;
      genFun.__proto__ = GeneratorFunctionPrototype;
      define(genFun, toStringTagSymbol, <span class="hljs-string">"GeneratorFunction"</span>);
    &#125;
    genFun.prototype = <span class="hljs-built_in">Object</span>.create(Gp);
    <span class="hljs-keyword">return</span> genFun;
  &#125;;

  <span class="hljs-comment">// Within the body of any async function, `await x` is transformed to</span>
  <span class="hljs-comment">// `yield regeneratorRuntime.awrap(x)`, so that the runtime can test</span>
  <span class="hljs-comment">// `hasOwn.call(value, "__await")` to determine if the yielded value is</span>
  <span class="hljs-comment">// meant to be awaited.</span>
  <span class="hljs-built_in">exports</span>.awrap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arg</span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">__await</span>: arg &#125;;
  &#125;;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AsyncIterator</span>(<span class="hljs-params">generator, PromiseImpl</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invoke</span>(<span class="hljs-params">method, arg, resolve, reject</span>) </span>&#123;
      <span class="hljs-keyword">var</span> record = tryCatch(generator[method], generator, arg);
      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
        reject(record.arg);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">var</span> result = record.arg;
        <span class="hljs-keyword">var</span> value = result.value;
        <span class="hljs-keyword">if</span> (value &&
            <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">"object"</span> &&
            hasOwn.call(value, <span class="hljs-string">"__await"</span>)) &#123;
          <span class="hljs-keyword">return</span> PromiseImpl.resolve(value.__await).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>) </span>&#123;
            invoke(<span class="hljs-string">"next"</span>, value, resolve, reject);
          &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err</span>) </span>&#123;
            invoke(<span class="hljs-string">"throw"</span>, err, resolve, reject);
          &#125;);
        &#125;

        <span class="hljs-keyword">return</span> PromiseImpl.resolve(value).then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">unwrapped</span>) </span>&#123;
          <span class="hljs-comment">// When a yielded Promise is resolved, its final value becomes</span>
          <span class="hljs-comment">// the .value of the Promise<&#123;value,done&#125;> result for the</span>
          <span class="hljs-comment">// current iteration.</span>
          result.value = unwrapped;
          resolve(result);
        &#125;, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">error</span>) </span>&#123;
          <span class="hljs-comment">// If a rejected Promise was yielded, throw the rejection back</span>
          <span class="hljs-comment">// into the async generator function so it can be handled there.</span>
          <span class="hljs-keyword">return</span> invoke(<span class="hljs-string">"throw"</span>, error, resolve, reject);
        &#125;);
      &#125;
    &#125;

    <span class="hljs-keyword">var</span> previousPromise;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">enqueue</span>(<span class="hljs-params">method, arg</span>) </span>&#123;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callInvokeWithMethodAndArg</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> PromiseImpl(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
          invoke(method, arg, resolve, reject);
        &#125;);
      &#125;

      <span class="hljs-keyword">return</span> previousPromise =
        <span class="hljs-comment">// If enqueue has been called before, then we want to wait until</span>
        <span class="hljs-comment">// all previous Promises have been resolved before calling invoke,</span>
        <span class="hljs-comment">// so that results are always delivered in the correct order. If</span>
        <span class="hljs-comment">// enqueue has not been called before, then it is important to</span>
        <span class="hljs-comment">// call invoke immediately, without waiting on a callback to fire,</span>
        <span class="hljs-comment">// so that the async generator function has the opportunity to do</span>
        <span class="hljs-comment">// any necessary setup in a predictable way. This predictability</span>
        <span class="hljs-comment">// is why the Promise constructor synchronously invokes its</span>
        <span class="hljs-comment">// executor callback, and why async functions synchronously</span>
        <span class="hljs-comment">// execute code before the first await. Since we implement simple</span>
        <span class="hljs-comment">// async functions in terms of async generators, it is especially</span>
        <span class="hljs-comment">// important to get this right, even though it requires care.</span>
        previousPromise ? previousPromise.then(
          callInvokeWithMethodAndArg,
          <span class="hljs-comment">// Avoid propagating failures to Promises returned by later</span>
          <span class="hljs-comment">// invocations of the iterator.</span>
          callInvokeWithMethodAndArg
        ) : callInvokeWithMethodAndArg();
    &#125;

    <span class="hljs-comment">// Define the unified helper method that is used to implement .next,</span>
    <span class="hljs-comment">// .throw, and .return (see defineIteratorMethods).</span>
    <span class="hljs-built_in">this</span>._invoke = enqueue;
  &#125;

  defineIteratorMethods(AsyncIterator.prototype);
  define(AsyncIterator.prototype, asyncIteratorSymbol, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;);
  <span class="hljs-built_in">exports</span>.AsyncIterator = AsyncIterator;

  <span class="hljs-comment">// Note that simple async functions are implemented on top of</span>
  <span class="hljs-comment">// AsyncIterator objects; they just return a Promise for the value of</span>
  <span class="hljs-comment">// the final result produced by the iterator.</span>
  <span class="hljs-built_in">exports</span>.async = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">innerFn, outerFn, self, tryLocsList, PromiseImpl</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (PromiseImpl === <span class="hljs-keyword">void</span> <span class="hljs-number">0</span>) PromiseImpl = <span class="hljs-built_in">Promise</span>;

    <span class="hljs-keyword">var</span> iter = <span class="hljs-keyword">new</span> AsyncIterator(
      wrap(innerFn, outerFn, self, tryLocsList),
      PromiseImpl
    );

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">exports</span>.isGeneratorFunction(outerFn)
      ? iter <span class="hljs-comment">// If outerFn is a generator, return the full iterator.</span>
      : iter.next().then(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">result</span>) </span>&#123;
          <span class="hljs-keyword">return</span> result.done ? result.value : iter.next();
        &#125;);
  &#125;;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeInvokeMethod</span>(<span class="hljs-params">innerFn, self, context</span>) </span>&#123;
    <span class="hljs-keyword">var</span> state = GenStateSuspendedStart;

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invoke</span>(<span class="hljs-params">method, arg</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (state === GenStateExecuting) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Generator is already running"</span>);
      &#125;

      <span class="hljs-keyword">if</span> (state === GenStateCompleted) &#123;
        <span class="hljs-keyword">if</span> (method === <span class="hljs-string">"throw"</span>) &#123;
          <span class="hljs-keyword">throw</span> arg;
        &#125;

        <span class="hljs-comment">// Be forgiving, per 25.3.3.3.3 of the spec:</span>
        <span class="hljs-comment">// https://people.mozilla.org/~jorendorff/es6-draft.html#sec-generatorresume</span>
        <span class="hljs-keyword">return</span> doneResult();
      &#125;

      context.method = method;
      context.arg = arg;

      <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
        <span class="hljs-keyword">var</span> delegate = context.delegate;
        <span class="hljs-keyword">if</span> (delegate) &#123;
          <span class="hljs-keyword">var</span> delegateResult = maybeInvokeDelegate(delegate, context);
          <span class="hljs-keyword">if</span> (delegateResult) &#123;
            <span class="hljs-keyword">if</span> (delegateResult === ContinueSentinel) <span class="hljs-keyword">continue</span>;
            <span class="hljs-keyword">return</span> delegateResult;
          &#125;
        &#125;

        <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"next"</span>) &#123;
          <span class="hljs-comment">// Setting context._sent for legacy support of Babel's</span>
          <span class="hljs-comment">// function.sent implementation.</span>
          context.sent = context._sent = context.arg;

        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"throw"</span>) &#123;
          <span class="hljs-keyword">if</span> (state === GenStateSuspendedStart) &#123;
            state = GenStateCompleted;
            <span class="hljs-keyword">throw</span> context.arg;
          &#125;

          context.dispatchException(context.arg);

        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"return"</span>) &#123;
          context.abrupt(<span class="hljs-string">"return"</span>, context.arg);
        &#125;

        state = GenStateExecuting;

        <span class="hljs-keyword">var</span> record = tryCatch(innerFn, self, context);
        <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"normal"</span>) &#123;
          <span class="hljs-comment">// If an exception is thrown from innerFn, we leave state ===</span>
          <span class="hljs-comment">// GenStateExecuting and loop back for another invocation.</span>
          state = context.done
            ? GenStateCompleted
            : GenStateSuspendedYield;

          <span class="hljs-keyword">if</span> (record.arg === ContinueSentinel) &#123;
            <span class="hljs-keyword">continue</span>;
          &#125;

          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">value</span>: record.arg,
            <span class="hljs-attr">done</span>: context.done
          &#125;;

        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
          state = GenStateCompleted;
          <span class="hljs-comment">// Dispatch the exception by looping back around to the</span>
          <span class="hljs-comment">// context.dispatchException(context.arg) call above.</span>
          context.method = <span class="hljs-string">"throw"</span>;
          context.arg = record.arg;
        &#125;
      &#125;
    &#125;;
  &#125;

  <span class="hljs-comment">// Call delegate.iterator[context.method](context.arg) and handle the</span>
  <span class="hljs-comment">// result, either by returning a &#123; value, done &#125; result from the</span>
  <span class="hljs-comment">// delegate iterator, or by modifying context.method and context.arg,</span>
  <span class="hljs-comment">// setting context.delegate to null, and returning the ContinueSentinel.</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">maybeInvokeDelegate</span>(<span class="hljs-params">delegate, context</span>) </span>&#123;
    <span class="hljs-keyword">var</span> method = delegate.iterator[context.method];
    <span class="hljs-keyword">if</span> (method === <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// A .throw or .return when the delegate iterator has no .throw</span>
      <span class="hljs-comment">// method always terminates the yield* loop.</span>
      context.delegate = <span class="hljs-literal">null</span>;

      <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-comment">// Note: ["return"] must be used for ES3 parsing compatibility.</span>
        <span class="hljs-keyword">if</span> (delegate.iterator[<span class="hljs-string">"return"</span>]) &#123;
          <span class="hljs-comment">// If the delegate iterator has a return method, give it a</span>
          <span class="hljs-comment">// chance to clean up.</span>
          context.method = <span class="hljs-string">"return"</span>;
          context.arg = <span class="hljs-literal">undefined</span>;
          maybeInvokeDelegate(delegate, context);

          <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"throw"</span>) &#123;
            <span class="hljs-comment">// If maybeInvokeDelegate(context) changed context.method from</span>
            <span class="hljs-comment">// "return" to "throw", let that override the TypeError below.</span>
            <span class="hljs-keyword">return</span> ContinueSentinel;
          &#125;
        &#125;

        context.method = <span class="hljs-string">"throw"</span>;
        context.arg = <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(
          <span class="hljs-string">"The iterator does not provide a 'throw' method"</span>);
      &#125;

      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;

    <span class="hljs-keyword">var</span> record = tryCatch(method, delegate.iterator, context.arg);

    <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
      context.method = <span class="hljs-string">"throw"</span>;
      context.arg = record.arg;
      context.delegate = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;

    <span class="hljs-keyword">var</span> info = record.arg;

    <span class="hljs-keyword">if</span> (! info) &#123;
      context.method = <span class="hljs-string">"throw"</span>;
      context.arg = <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">"iterator result is not an object"</span>);
      context.delegate = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;

    <span class="hljs-keyword">if</span> (info.done) &#123;
      <span class="hljs-comment">// Assign the result of the finished delegate to the temporary</span>
      <span class="hljs-comment">// variable specified by delegate.resultName (see delegateYield).</span>
      context[delegate.resultName] = info.value;

      <span class="hljs-comment">// Resume execution at the desired location (see delegateYield).</span>
      context.next = delegate.nextLoc;

      <span class="hljs-comment">// If context.method was "throw" but the delegate handled the</span>
      <span class="hljs-comment">// exception, let the outer generator proceed normally. If</span>
      <span class="hljs-comment">// context.method was "next", forget context.arg since it has been</span>
      <span class="hljs-comment">// "consumed" by the delegate iterator. If context.method was</span>
      <span class="hljs-comment">// "return", allow the original .return call to continue in the</span>
      <span class="hljs-comment">// outer generator.</span>
      <span class="hljs-keyword">if</span> (context.method !== <span class="hljs-string">"return"</span>) &#123;
        context.method = <span class="hljs-string">"next"</span>;
        context.arg = <span class="hljs-literal">undefined</span>;
      &#125;

    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// Re-yield the result returned by the delegate method.</span>
      <span class="hljs-keyword">return</span> info;
    &#125;

    <span class="hljs-comment">// The delegate iterator is finished, so forget it and continue with</span>
    <span class="hljs-comment">// the outer generator.</span>
    context.delegate = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> ContinueSentinel;
  &#125;

  <span class="hljs-comment">// Define Generator.prototype.&#123;next,throw,return&#125; in terms of the</span>
  <span class="hljs-comment">// unified ._invoke helper method.</span>
  defineIteratorMethods(Gp);

  define(Gp, toStringTagSymbol, <span class="hljs-string">"Generator"</span>);

  <span class="hljs-comment">// A Generator should always return itself as the iterator object when the</span>
  <span class="hljs-comment">// @@iterator function is called on it. Some browsers' implementations of the</span>
  <span class="hljs-comment">// iterator prototype chain incorrectly implement this, causing the Generator</span>
  <span class="hljs-comment">// object to not be returned from this call. This ensures that doesn't happen.</span>
  <span class="hljs-comment">// See https://github.com/facebook/regenerator/issues/274 for more details.</span>
  define(Gp, iteratorSymbol, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
  &#125;);

  define(Gp, <span class="hljs-string">"toString"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"[object Generator]"</span>;
  &#125;);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pushTryEntry</span>(<span class="hljs-params">locs</span>) </span>&#123;
    <span class="hljs-keyword">var</span> entry = &#123; <span class="hljs-attr">tryLoc</span>: locs[<span class="hljs-number">0</span>] &#125;;

    <span class="hljs-keyword">if</span> (<span class="hljs-number">1</span> <span class="hljs-keyword">in</span> locs) &#123;
      entry.catchLoc = locs[<span class="hljs-number">1</span>];
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-number">2</span> <span class="hljs-keyword">in</span> locs) &#123;
      entry.finallyLoc = locs[<span class="hljs-number">2</span>];
      entry.afterLoc = locs[<span class="hljs-number">3</span>];
    &#125;

    <span class="hljs-built_in">this</span>.tryEntries.push(entry);
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resetTryEntry</span>(<span class="hljs-params">entry</span>) </span>&#123;
    <span class="hljs-keyword">var</span> record = entry.completion || &#123;&#125;;
    record.type = <span class="hljs-string">"normal"</span>;
    <span class="hljs-keyword">delete</span> record.arg;
    entry.completion = record;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Context</span>(<span class="hljs-params">tryLocsList</span>) </span>&#123;
    <span class="hljs-comment">// The root entry object (effectively a try statement without a catch</span>
    <span class="hljs-comment">// or a finally block) gives us a place to store values thrown from</span>
    <span class="hljs-comment">// locations where there is no enclosing try statement.</span>
    <span class="hljs-built_in">this</span>.tryEntries = [&#123; <span class="hljs-attr">tryLoc</span>: <span class="hljs-string">"root"</span> &#125;];
    tryLocsList.forEach(pushTryEntry, <span class="hljs-built_in">this</span>);
    <span class="hljs-built_in">this</span>.reset(<span class="hljs-literal">true</span>);
  &#125;

  <span class="hljs-built_in">exports</span>.keys = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">object</span>) </span>&#123;
    <span class="hljs-keyword">var</span> keys = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> object) &#123;
      keys.push(key);
    &#125;
    keys.reverse();

    <span class="hljs-comment">// Rather than returning an object with a next method, we keep</span>
    <span class="hljs-comment">// things simple and return the next function itself.</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">while</span> (keys.length) &#123;
        <span class="hljs-keyword">var</span> key = keys.pop();
        <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> object) &#123;
          next.value = key;
          next.done = <span class="hljs-literal">false</span>;
          <span class="hljs-keyword">return</span> next;
        &#125;
      &#125;

      <span class="hljs-comment">// To avoid creating an additional object, we just hang the .value</span>
      <span class="hljs-comment">// and .done properties off the next function object itself. This</span>
      <span class="hljs-comment">// also ensures that the minifier will not anonymize the function.</span>
      next.done = <span class="hljs-literal">true</span>;
      <span class="hljs-keyword">return</span> next;
    &#125;;
  &#125;;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">values</span>(<span class="hljs-params">iterable</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (iterable) &#123;
      <span class="hljs-keyword">var</span> iteratorMethod = iterable[iteratorSymbol];
      <span class="hljs-keyword">if</span> (iteratorMethod) &#123;
        <span class="hljs-keyword">return</span> iteratorMethod.call(iterable);
      &#125;

      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> iterable.next === <span class="hljs-string">"function"</span>) &#123;
        <span class="hljs-keyword">return</span> iterable;
      &#125;

      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">isNaN</span>(iterable.length)) &#123;
        <span class="hljs-keyword">var</span> i = -<span class="hljs-number">1</span>, next = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">next</span>(<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-keyword">while</span> (++i < iterable.length) &#123;
            <span class="hljs-keyword">if</span> (hasOwn.call(iterable, i)) &#123;
              next.value = iterable[i];
              next.done = <span class="hljs-literal">false</span>;
              <span class="hljs-keyword">return</span> next;
            &#125;
          &#125;

          next.value = <span class="hljs-literal">undefined</span>;
          next.done = <span class="hljs-literal">true</span>;

          <span class="hljs-keyword">return</span> next;
        &#125;;

        <span class="hljs-keyword">return</span> next.next = next;
      &#125;
    &#125;

    <span class="hljs-comment">// Return an iterator with no values.</span>
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">next</span>: doneResult &#125;;
  &#125;
  <span class="hljs-built_in">exports</span>.values = values;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">doneResult</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">value</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-attr">done</span>: <span class="hljs-literal">true</span> &#125;;
  &#125;

  Context.prototype = &#123;
    <span class="hljs-attr">constructor</span>: Context,

    <span class="hljs-attr">reset</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">skipTempReset</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.prev = <span class="hljs-number">0</span>;
      <span class="hljs-built_in">this</span>.next = <span class="hljs-number">0</span>;
      <span class="hljs-comment">// Resetting context._sent for legacy support of Babel's</span>
      <span class="hljs-comment">// function.sent implementation.</span>
      <span class="hljs-built_in">this</span>.sent = <span class="hljs-built_in">this</span>._sent = <span class="hljs-literal">undefined</span>;
      <span class="hljs-built_in">this</span>.done = <span class="hljs-literal">false</span>;
      <span class="hljs-built_in">this</span>.delegate = <span class="hljs-literal">null</span>;

      <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"next"</span>;
      <span class="hljs-built_in">this</span>.arg = <span class="hljs-literal">undefined</span>;

      <span class="hljs-built_in">this</span>.tryEntries.forEach(resetTryEntry);

      <span class="hljs-keyword">if</span> (!skipTempReset) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> name <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>) &#123;
          <span class="hljs-comment">// Not sure about the optimal order of these conditions:</span>
          <span class="hljs-keyword">if</span> (name.charAt(<span class="hljs-number">0</span>) === <span class="hljs-string">"t"</span> &&
              hasOwn.call(<span class="hljs-built_in">this</span>, name) &&
              !<span class="hljs-built_in">isNaN</span>(+name.slice(<span class="hljs-number">1</span>))) &#123;
            <span class="hljs-built_in">this</span>[name] = <span class="hljs-literal">undefined</span>;
          &#125;
        &#125;
      &#125;
    &#125;,

    <span class="hljs-attr">stop</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">this</span>.done = <span class="hljs-literal">true</span>;

      <span class="hljs-keyword">var</span> rootEntry = <span class="hljs-built_in">this</span>.tryEntries[<span class="hljs-number">0</span>];
      <span class="hljs-keyword">var</span> rootRecord = rootEntry.completion;
      <span class="hljs-keyword">if</span> (rootRecord.type === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-keyword">throw</span> rootRecord.arg;
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.rval;
    &#125;,

    <span class="hljs-attr">dispatchException</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">exception</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.done) &#123;
        <span class="hljs-keyword">throw</span> exception;
      &#125;

      <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">this</span>;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handle</span>(<span class="hljs-params">loc, caught</span>) </span>&#123;
        record.type = <span class="hljs-string">"throw"</span>;
        record.arg = exception;
        context.next = loc;

        <span class="hljs-keyword">if</span> (caught) &#123;
          <span class="hljs-comment">// If the dispatched exception was caught by a catch block,</span>
          <span class="hljs-comment">// then let that catch block handle the exception normally.</span>
          context.method = <span class="hljs-string">"next"</span>;
          context.arg = <span class="hljs-literal">undefined</span>;
        &#125;

        <span class="hljs-keyword">return</span> !! caught;
      &#125;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">var</span> record = entry.completion;

        <span class="hljs-keyword">if</span> (entry.tryLoc === <span class="hljs-string">"root"</span>) &#123;
          <span class="hljs-comment">// Exception thrown outside of any try block that could handle</span>
          <span class="hljs-comment">// it, so set the completion value of the entire function to</span>
          <span class="hljs-comment">// throw the exception.</span>
          <span class="hljs-keyword">return</span> handle(<span class="hljs-string">"end"</span>);
        &#125;

        <span class="hljs-keyword">if</span> (entry.tryLoc <= <span class="hljs-built_in">this</span>.prev) &#123;
          <span class="hljs-keyword">var</span> hasCatch = hasOwn.call(entry, <span class="hljs-string">"catchLoc"</span>);
          <span class="hljs-keyword">var</span> hasFinally = hasOwn.call(entry, <span class="hljs-string">"finallyLoc"</span>);

          <span class="hljs-keyword">if</span> (hasCatch && hasFinally) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.catchLoc) &#123;
              <span class="hljs-keyword">return</span> handle(entry.catchLoc, <span class="hljs-literal">true</span>);
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.finallyLoc) &#123;
              <span class="hljs-keyword">return</span> handle(entry.finallyLoc);
            &#125;

          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasCatch) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.catchLoc) &#123;
              <span class="hljs-keyword">return</span> handle(entry.catchLoc, <span class="hljs-literal">true</span>);
            &#125;

          &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasFinally) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.finallyLoc) &#123;
              <span class="hljs-keyword">return</span> handle(entry.finallyLoc);
            &#125;

          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"try statement without catch or finally"</span>);
          &#125;
        &#125;
      &#125;
    &#125;,

    <span class="hljs-attr">abrupt</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">type, arg</span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">if</span> (entry.tryLoc <= <span class="hljs-built_in">this</span>.prev &&
            hasOwn.call(entry, <span class="hljs-string">"finallyLoc"</span>) &&
            <span class="hljs-built_in">this</span>.prev < entry.finallyLoc) &#123;
          <span class="hljs-keyword">var</span> finallyEntry = entry;
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;

      <span class="hljs-keyword">if</span> (finallyEntry &&
          (type === <span class="hljs-string">"break"</span> ||
           type === <span class="hljs-string">"continue"</span>) &&
          finallyEntry.tryLoc <= arg &&
          arg <= finallyEntry.finallyLoc) &#123;
        <span class="hljs-comment">// Ignore the finally entry if control is not jumping to a</span>
        <span class="hljs-comment">// location outside the try/catch block.</span>
        finallyEntry = <span class="hljs-literal">null</span>;
      &#125;

      <span class="hljs-keyword">var</span> record = finallyEntry ? finallyEntry.completion : &#123;&#125;;
      record.type = type;
      record.arg = arg;

      <span class="hljs-keyword">if</span> (finallyEntry) &#123;
        <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"next"</span>;
        <span class="hljs-built_in">this</span>.next = finallyEntry.finallyLoc;
        <span class="hljs-keyword">return</span> ContinueSentinel;
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.complete(record);
    &#125;,

    <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">record, afterLoc</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-keyword">throw</span> record.arg;
      &#125;

      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"break"</span> ||
          record.type === <span class="hljs-string">"continue"</span>) &#123;
        <span class="hljs-built_in">this</span>.next = record.arg;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"return"</span>) &#123;
        <span class="hljs-built_in">this</span>.rval = <span class="hljs-built_in">this</span>.arg = record.arg;
        <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"return"</span>;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-string">"end"</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"normal"</span> && afterLoc) &#123;
        <span class="hljs-built_in">this</span>.next = afterLoc;
      &#125;

      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;,

    <span class="hljs-attr">finish</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">finallyLoc</span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">if</span> (entry.finallyLoc === finallyLoc) &#123;
          <span class="hljs-built_in">this</span>.complete(entry.completion, entry.afterLoc);
          resetTryEntry(entry);
          <span class="hljs-keyword">return</span> ContinueSentinel;
        &#125;
      &#125;
    &#125;,

    <span class="hljs-string">"catch"</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">tryLoc</span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">if</span> (entry.tryLoc === tryLoc) &#123;
          <span class="hljs-keyword">var</span> record = entry.completion;
          <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
            <span class="hljs-keyword">var</span> thrown = record.arg;
            resetTryEntry(entry);
          &#125;
          <span class="hljs-keyword">return</span> thrown;
        &#125;
      &#125;

      <span class="hljs-comment">// The context.catch method must only be called with a location</span>
      <span class="hljs-comment">// argument that corresponds to a known catch block.</span>
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"illegal catch attempt"</span>);
    &#125;,

    <span class="hljs-attr">delegateYield</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">iterable, resultName, nextLoc</span>) </span>&#123;
      <span class="hljs-built_in">this</span>.delegate = &#123;
        <span class="hljs-attr">iterator</span>: values(iterable),
        <span class="hljs-attr">resultName</span>: resultName,
        <span class="hljs-attr">nextLoc</span>: nextLoc
      &#125;;

      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.method === <span class="hljs-string">"next"</span>) &#123;
        <span class="hljs-comment">// Deliberately forget the last sent value so that we don't</span>
        <span class="hljs-comment">// accidentally pass it on to the delegate.</span>
        <span class="hljs-built_in">this</span>.arg = <span class="hljs-literal">undefined</span>;
      &#125;

      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;
  &#125;;

  <span class="hljs-comment">// Regardless of whether this script is executing as a CommonJS module</span>
  <span class="hljs-comment">// or not, return the runtime object so that we can declare the variable</span>
  <span class="hljs-comment">// regeneratorRuntime in the outer scope, which allows this module to be</span>
  <span class="hljs-comment">// injected easily by `bin/regenerator --include-runtime script.js`.</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">exports</span>;

&#125;(
  <span class="hljs-comment">// If this script is executing as a CommonJS module, use module.exports</span>
  <span class="hljs-comment">// as the regeneratorRuntime namespace. Otherwise create a new empty</span>
  <span class="hljs-comment">// object. Either way, the resulting object will be used to initialize</span>
  <span class="hljs-comment">// the regeneratorRuntime variable at the top of this file.</span>
  <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">module</span> === <span class="hljs-string">"object"</span> ? <span class="hljs-built_in">module</span>.exports : &#123;&#125;
));

<span class="hljs-keyword">try</span> &#123;
  regeneratorRuntime = runtime;
&#125; <span class="hljs-keyword">catch</span> (accidentalStrictMode) &#123;
  <span class="hljs-comment">// This module should not be running in strict mode, so the above</span>
  <span class="hljs-comment">// assignment should always work unless something is misconfigured. Just</span>
  <span class="hljs-comment">// in case runtime.js accidentally runs in strict mode, in modern engines</span>
  <span class="hljs-comment">// we can explicitly access globalThis. In older engines we can escape</span>
  <span class="hljs-comment">// strict mode using a global Function call. This could conceivably fail</span>
  <span class="hljs-comment">// if a Content Security Policy forbids using Function, but in that case</span>
  <span class="hljs-comment">// the proper solution is to fix the accidental strict mode problem. If</span>
  <span class="hljs-comment">// you've misconfigured your bundler to force strict mode and applied a</span>
  <span class="hljs-comment">// CSP to forbid Function, and you're not willing to fix either of those</span>
  <span class="hljs-comment">// problems, please detail your unique predicament in a GitHub issue.</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> globalThis === <span class="hljs-string">"object"</span>) &#123;
    globalThis.regeneratorRuntime = runtime;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">Function</span>(<span class="hljs-string">"r"</span>, <span class="hljs-string">"regeneratorRuntime = r"</span>)(runtime);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">大致介绍下</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">yield</span> <span class="hljs-string">"result1"</span>;
  <span class="hljs-keyword">let</span> res2 = <span class="hljs-keyword">yield</span> <span class="hljs-string">"result2"</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">yield</span> <span class="hljs-string">"result3"</span>;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"e"</span>, e);
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"result5"</span>;
&#125;

<span class="hljs-keyword">const</span> gen = foo();
gen.next();
gen.next();
gen.next();
gen.throw();
gen.next();

<span class="hljs-comment">// 上面代码会被编译成下面的代码</span>

<span class="hljs-keyword">var</span> _marked = <span class="hljs-comment">/*#__PURE__*/</span>regeneratorRuntime.mark(foo);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> res2;
  <span class="hljs-keyword">return</span> regeneratorRuntime.wrap(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo$</span>(<span class="hljs-params">_context</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (<span class="hljs-number">1</span>) &#123;
      <span class="hljs-keyword">switch</span> (_context.prev = _context.next) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:
          _context.next = <span class="hljs-number">2</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"result1"</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:
          _context.next = <span class="hljs-number">4</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"result2"</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
          res2 = _context.sent;
          _context.prev = <span class="hljs-number">5</span>;
          _context.next = <span class="hljs-number">8</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-string">"result3"</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-number">8</span>:
          _context.next = <span class="hljs-number">13</span>;
          <span class="hljs-keyword">break</span>;

        <span class="hljs-keyword">case</span> <span class="hljs-number">10</span>:
          _context.prev = <span class="hljs-number">10</span>;
          _context.t0 = _context[<span class="hljs-string">"catch"</span>](<span class="hljs-number">5</span>);
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"e"</span>, _context.t0);

        <span class="hljs-keyword">case</span> <span class="hljs-number">13</span>:
          <span class="hljs-keyword">return</span> _context.abrupt(<span class="hljs-string">"return"</span>, <span class="hljs-string">"result5"</span>);

        <span class="hljs-keyword">case</span> <span class="hljs-number">14</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">"end"</span>:
          <span class="hljs-keyword">return</span> _context.stop();
      &#125;
    &#125;
  &#125;, _marked, <span class="hljs-literal">null</span>, [[<span class="hljs-number">5</span>, <span class="hljs-number">10</span>]]);
&#125;

<span class="hljs-keyword">var</span> gen = foo();
gen.next();
gen.next();
gen.next();
gen[<span class="hljs-string">"throw"</span>]();
gen.next();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1. 初始化(只说涉及的一部分)</h3>
<pre><code class="copyable">1.1 初始化 Gp(generator prototype) 是一个对象,有next,throw,return等方法,作为新生成generator 迭代器对象的原型
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// invoke 就是next,throw,return方法, 内部会做判断</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineIteratorMethods</span>(<span class="hljs-params">prototype</span>) </span>&#123;
    [<span class="hljs-string">"next"</span>, <span class="hljs-string">"throw"</span>, <span class="hljs-string">"return"</span>].forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">method</span>) </span>&#123;
      <span class="hljs-comment">// 下面就相当于 prototype.next = function (arg) &#123; this._invoke('next',arg) &#125;</span>
      define(prototype, method, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arg</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._invoke(method, arg);
      &#125;);
    &#125;);
  &#125;
  <span class="hljs-comment">// 挂在在 Gp 原型上, 所以 Gp 上就有了3方法</span>
  defineIteratorMethods(Gp);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2. 给方法挂在原型</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> _marked = <span class="hljs-comment">/*#__PURE__*/</span>regeneratorRuntime.mark(foo);
<span class="hljs-comment">// 就是给传入的方法挂在一系列的原型  返回方法本身</span>
<span class="hljs-built_in">exports</span>.mark = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">genFun</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Object</span>.setPrototypeOf) &#123;
    <span class="hljs-built_in">Object</span>.setPrototypeOf(genFun, GeneratorFunctionPrototype);
  &#125; <span class="hljs-keyword">else</span> &#123;
    genFun.__proto__ = GeneratorFunctionPrototype;
    define(genFun, toStringTagSymbol, <span class="hljs-string">"GeneratorFunction"</span>);
  &#125;
  <span class="hljs-comment">// !! 重点记一下 给传入方法的原型变更为 继承Gp的对象</span>
  genFun.prototype = <span class="hljs-built_in">Object</span>.create(Gp);
  <span class="hljs-keyword">return</span> genFun;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3. regeneratorRuntime.wrap 介绍</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 第一个参数是 里层的foo$(主要执行的方法) 第二个参数是外层 foo</span>
<span class="hljs-comment">// self: 是 innerFn 的this指向</span>
<span class="hljs-comment">// tryLocsList [[5, 10]] 是个二维数组,因为可能有多个trycatch 每组都要记录try和catch所在代码的 case</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrap</span>(<span class="hljs-params">innerFn, outerFn, self, tryLocsList</span>) </span>&#123;
  <span class="hljs-comment">// outerFn 就是上面mark改变原型过后的foo方法就是判断下原型挂上去没有</span>
  <span class="hljs-keyword">var</span> protoGenerator = outerFn && outerFn.prototype <span class="hljs-keyword">instanceof</span> Generator ? outerFn : Generator;
  <span class="hljs-comment">// 如果挂上去了 就把继承 Gp的对象 再继承一遍 简单说就是继承了 Gp 有了next等方法</span>
  <span class="hljs-comment">// generator__proto__ -> &#123;&#125;.__proto__ -> Gp </span>
  <span class="hljs-keyword">var</span> generator = <span class="hljs-built_in">Object</span>.create(protoGenerator.prototype);
  <span class="hljs-comment">// 每个generator执行 内部都会维护一套状态(用来判断 执行到哪一步prev 下一步哪一步next 上一步的next传入值 sent 等等</span>
  <span class="hljs-keyword">var</span> context = <span class="hljs-keyword">new</span> Context(tryLocsList || []);

  <span class="hljs-comment">// The ._invoke method unifies the implementations of the .next,</span>
  <span class="hljs-comment">// .throw, and .return methods.</span>
  <span class="hljs-comment">// 最后挂载一个_invoke 就是上面第二步说的 next,throw实际调用的方法</span>
  <span class="hljs-comment">// makeInvokeMethod创建一个invoke方法</span>
  generator._invoke = makeInvokeMethod(innerFn, self, context);

  <span class="hljs-keyword">return</span> generator;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4. makeInvokeMethod 生成next,throw,return方法</h3>
<p>这个方法就比较大 去掉相对不重要的部分说明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 作用就是返回一个 invoke 就是实际执行的next throw return</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeInvokeMethod</span>(<span class="hljs-params">innerFn, self, context</span>) </span>&#123;
  <span class="hljs-comment">// 内部维护一个状态 state</span>
  <span class="hljs-comment">// 类型是 string</span>
  <span class="hljs-comment">// 枚举有 suspendedStart开始 suspendedYield(未执行到最后中间步) executing执行中 completed完成</span>
  <span class="hljs-keyword">var</span> state = GenStateSuspendedStart;

  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">invoke</span>(<span class="hljs-params">method, arg</span>) </span>&#123;
     <span class="hljs-comment">// 如果是完成状态 就直接返回 &#123; value: undefined, done: true &#125;</span>
    <span class="hljs-keyword">if</span> (state === GenStateCompleted) &#123;
      <span class="hljs-keyword">if</span> (method === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-keyword">throw</span> arg;
      &#125;
      <span class="hljs-keyword">return</span> doneResult(); <span class="hljs-comment">// &#123; value: undefined, done: true &#125;</span>
    &#125;
    
    <span class="hljs-comment">// 每次执行都改变context的 method 和 arg, 把当前执行方法和参数覆盖上去</span>
    context.method = method;
    context.arg = arg;

    <span class="hljs-comment">// 循环执行 执行到throw return等需要执行下一步的next或最后的case end 所以直接用循环</span>
    <span class="hljs-keyword">while</span> (<span class="hljs-literal">true</span>) &#123;
       <span class="hljs-comment">// 当执行的方法是 next 是 记录传入的值 赋值给 context的sent属性</span>
       <span class="hljs-comment">// sent (next传入值) 下一次next switch case中可以通过context.sent获取</span>
      <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"next"</span>) &#123;
        context.sent = context._sent = context.arg;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"throw"</span>) &#123;
      <span class="hljs-comment">// 当执行的方法是 throw时</span>
        <span class="hljs-keyword">if</span> (state === GenStateSuspendedStart) &#123;
          <span class="hljs-comment">// 如果是一开始就调用 throw方法 就会直接改变state为完成 抛出错误</span>
          <span class="hljs-comment">// 所以generator第一次不执行next 直接执行throw 内部是无法捕获错误的</span>
          state = GenStateCompleted;
          <span class="hljs-keyword">throw</span> context.arg;
        &#125;
        <span class="hljs-comment">// 当throw 不是一开始就执行时这里简单说 详细看第五节</span>
        <span class="hljs-comment">// 改变context.next到catch语句所在的地方 上面的案例就是next=10,[[3,10]] 下一次就直接执行 case10</span>
        <span class="hljs-comment">// throw执行的 case10 后面没有中止语句return或者break所以会直接执行下一个 case 语句,相当于一次next (所以context.method改为next arg改为undefined)</span>
        context.dispatchException(context.arg);

      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (context.method === <span class="hljs-string">"return"</span>) &#123;
        <span class="hljs-comment">// 当执行的是return 就执行context的abupt方法</span>
        <span class="hljs-comment">// 找到匹配位置的try catch对应的context.tryEntries并把错误信息存进去(存储每个trycatch位置和内容)</span>
        <span class="hljs-comment">// abrupt 方法 会调用 context.complete方法</span>
        <span class="hljs-comment">// complete 主要是改变context methe:return next:end(end就是最后一个case) 返回值赋值给context.rval 方法返回值 ContinueSentinel用来再次执行next的判断(下面)</span>
        <span class="hljs-comment">// case end中执行的context.end方法 作用就是 改变done状态返回rval(return的返回值)</span>
        context.abrupt(<span class="hljs-string">"return"</span>, context.arg);
      &#125;
    <span class="hljs-comment">// 改变状态为 执行中</span>
      state = GenStateExecuting;
      <span class="hljs-comment">// 这一步就是实际执行 innerFn的方法就是执行外面那个swich case的方法</span>
      <span class="hljs-comment">// tryCatch 会捕获执行case的错误 </span>
      <span class="hljs-comment">// 正确返回&#123;type:'normal;,arg:innerFn.call(self,context)&#125;</span>
      <span class="hljs-comment">// 错误返回&#123;type:'throw;,arg:捕获到的错误&#125;</span>
      <span class="hljs-keyword">var</span> record = tryCatch(innerFn, self, context);
      <span class="hljs-comment">// 执行没出错时</span>
      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"normal"</span>) &#123;
          <span class="hljs-comment">//判断是否执行到最后一步 来赋值不同的state</span>
        state = context.done
          ? GenStateCompleted <span class="hljs-comment">// 完成</span>
          : GenStateSuspendedYield; <span class="hljs-comment">// 未完成</span>
        
        <span class="hljs-comment">// 上面return执行的语句里有执行到一个context.complete方法 返回就是ContinueSentinel 当执行完return方法 赋值了错误值之后 重新启用循环执行最后的 case end 输入返回值 改变done状态为true 这时候在返回</span>
        <span class="hljs-keyword">if</span> (record.arg === ContinueSentinel) &#123;
          <span class="hljs-keyword">continue</span>;
        &#125;
        
        <span class="hljs-comment">// 正常next就直接返回执行的值</span>
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">value</span>: record.arg,
          <span class="hljs-attr">done</span>: context.done
        &#125;;

      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
      <span class="hljs-comment">// 如果执行innerFn的某个case语句直接报错了,会走到这里</span>
      <span class="hljs-comment">// 改变状态为完成 改变方法为throw 改变参数为报错参数再走一遍循环</span>
      <span class="hljs-comment">// 重新走throw方法 会改变 next为 end 因为没有被trycatch捕获(后面dispatchException中细说什么时候捕获)</span>
      <span class="hljs-comment">// next 改为end 上面走innerFn 最后的end方法 执行context.stop方法 这里会判断会不会被捕获到 没有捕获到就直接抛出异常 运行结束</span>
        state = GenStateCompleted;
        context.method = <span class="hljs-string">"throw"</span>;
        context.arg = record.arg;
      &#125;
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5. dispatchException throw的时候调用的处理异常</h3>
<p>秃了秃了... 看删减版</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Context 原型上的方法</span>
<span class="hljs-attr">dispatchException</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">exception</span>) </span>&#123;
  <span class="hljs-comment">// 如果generator已经结束了done为true 再执行throw方法会直接抛出错误</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.done) &#123;
    <span class="hljs-keyword">throw</span> exception;
  &#125;

  <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">this</span>;
  <span class="hljs-comment">// 综合处理错误情况</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handle</span>(<span class="hljs-params">loc, caught</span>) </span>&#123;
    <span class="hljs-comment">// 改变错误值和type</span>
    record.type = <span class="hljs-string">"throw"</span>;
    record.arg = exception;
    <span class="hljs-comment">// 改变next为catch所在case位置</span>
    context.next = loc;
    
    <span class="hljs-comment">// 当错误被捕获 就走里面代码 改变method为next</span>
    <span class="hljs-keyword">if</span> (caught) &#123;
      context.method = <span class="hljs-string">"next"</span>;
      context.arg = <span class="hljs-literal">undefined</span>;
    &#125;

    <span class="hljs-keyword">return</span> !! caught;
  &#125;
  
  <span class="hljs-comment">// context 初始化的时候会初始化一个记录错误的数组 tryEntries = [&#123;tryLoc:'root',complettion:&#123;type:'normal',arg:undefined&#125;&#125;]</span>
  <span class="hljs-comment">// 上面的案例传入[[3,10]]会遍历这个数据把值复制到 tryEntries中</span>
  <span class="hljs-comment">// 所以上面最后初始化后tryEntries=[&#123; tryLoc: "root",completion:&#123;type:'normal'&#125; &#125;,&#123;tryLoc:3,catchLoc:10,completion:&#123;type:'normal'&#125;&#125;]</span>
  <span class="hljs-comment">// tryLoc 是try所在的case catchLoc是catch所在代码的case</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
   <span class="hljs-comment">// 从后往前遍历</span>
    <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i]; <span class="hljs-comment">//&#123;tryLoc:3,catchLoc:10,completion:&#123;type:'normal'&#125;&#125;</span>
    <span class="hljs-keyword">var</span> record = entry.completion; <span class="hljs-comment">// type 和 arg:就是错误值</span>
    <span class="hljs-comment">// root是初始化第一个默认值 从后往前匹配的 如果没有匹配到 就说明错误没有被捕获 </span>
    <span class="hljs-keyword">if</span> (entry.tryLoc === <span class="hljs-string">"root"</span>) &#123;
      <span class="hljs-keyword">return</span> handle(<span class="hljs-string">"end"</span>);
    &#125;

    <span class="hljs-comment">// 当执行到某个case 改变会改变prev和next prev就是当前的执行case位置</span>
    <span class="hljs-comment">// tryloc就是try里面代码所在的case位置</span>
    <span class="hljs-comment">// try 小于等于当前执行的代码 说明代码在try里或后面 </span>
    <span class="hljs-keyword">if</span> (entry.tryLoc <= <span class="hljs-built_in">this</span>.prev) &#123;
      <span class="hljs-keyword">var</span> hasCatch = hasOwn.call(entry, <span class="hljs-string">"catchLoc"</span>);
      <span class="hljs-keyword">var</span> hasFinally = hasOwn.call(entry, <span class="hljs-string">"finallyLoc"</span>);

      <span class="hljs-keyword">if</span> (hasCatch && hasFinally) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.catchLoc) &#123;
          <span class="hljs-keyword">return</span> handle(entry.catchLoc, <span class="hljs-literal">true</span>);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.finallyLoc) &#123;
          <span class="hljs-keyword">return</span> handle(entry.finallyLoc);
        &#125;

      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasCatch) &#123;
         <span class="hljs-comment">// 主要介绍这里 当前执行的case 小于catch代码所在的位置说明在try里面</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.catchLoc) &#123;
          <span class="hljs-keyword">return</span> handle(entry.catchLoc, <span class="hljs-literal">true</span>);
        &#125;

      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (hasFinally) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.prev < entry.finallyLoc) &#123;
          <span class="hljs-keyword">return</span> handle(entry.finallyLoc);
        &#125;

      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"try statement without catch or finally"</span>);
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6. 最后介绍下 全局状态 Context</h3>
<blockquote>
<p>context构造函数和他原型上的方法~~</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Context</span>(<span class="hljs-params">tryLocsList</span>) </span>&#123;
    <span class="hljs-comment">// 初始化一个记录错误的数组 </span>
    <span class="hljs-comment">// tryLoc 是try所在的case catchLoc是catch所在代码的case</span>
    <span class="hljs-built_in">this</span>.tryEntries = [&#123; <span class="hljs-attr">tryLoc</span>: <span class="hljs-string">"root"</span> &#125;];
    
    <span class="hljs-comment">// 上面的案例传入tryLocsList[[3,10]]会遍历这个数据把值复制到 tryEntries中</span>
    tryLocsList.forEach(pushTryEntry, <span class="hljs-built_in">this</span>);
    <span class="hljs-comment">// 所以上面最后初始化后tryEntries=[&#123; tryLoc: "root",completion:&#123;type:'normal'&#125; &#125;,&#123;tryLoc:3,catchLoc:10,completion:&#123;type:'normal'&#125;&#125;]</span>
    
    <span class="hljs-built_in">this</span>.reset(<span class="hljs-literal">true</span>); <span class="hljs-comment">// 初始化</span>
    <span class="hljs-comment">//初始化生成</span>
    <span class="hljs-comment">/*
      const res = &#123;
        prev: 0,
        next: 0,
        sent: undefined, // 发送
        _sent: undefined,
        done: false,
        delegate: null, // 代表
        method: "next",
        arg: undefined,
        tryEntries: [
          &#123; tryLoc: "root", completion: &#123; type: "normal" &#125; &#125;,
          &#123; tryLoc: 7, catchLoc: 14, completion: &#123; type: "normal" &#125; &#125;,
        ],
        reset: Function,
      &#125;;
    */</span>
  &#125;
  
  Context.prototype = &#123;
    <span class="hljs-attr">constructor</span>: Context,

    <span class="hljs-attr">reset</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">skipTempReset</span>) </span>&#123;
      <span class="hljs-comment">// 初始化方法 初始化一系列的 默认值</span>
      <span class="hljs-built_in">this</span>.prev = <span class="hljs-number">0</span>; <span class="hljs-comment">// 当前执行的位置</span>
      <span class="hljs-built_in">this</span>.next = <span class="hljs-number">0</span>; <span class="hljs-comment">// 下一次执行的位置</span>
      <span class="hljs-comment">// Resetting context._sent for legacy support of Babel's</span>
      <span class="hljs-comment">// function.sent implementation.</span>
      <span class="hljs-built_in">this</span>.sent = <span class="hljs-built_in">this</span>._sent = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">//next传参</span>
      <span class="hljs-built_in">this</span>.done = <span class="hljs-literal">false</span>; <span class="hljs-comment">// 结束状态</span>
      <span class="hljs-built_in">this</span>.delegate = <span class="hljs-literal">null</span>;

      <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"next"</span>;
      <span class="hljs-built_in">this</span>.arg = <span class="hljs-literal">undefined</span>;

      <span class="hljs-comment">// 给对象出事话 complettion:&#123;type: 'normal'&#125;</span>
      <span class="hljs-built_in">this</span>.tryEntries.forEach(resetTryEntry);
    &#125;,

    <span class="hljs-attr">stop</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 停止方法 在switch case的最后执行</span>
      <span class="hljs-comment">// 改变done为true, 并输出rval return的返回值</span>
      <span class="hljs-built_in">this</span>.done = <span class="hljs-literal">true</span>;

      <span class="hljs-keyword">var</span> rootEntry = <span class="hljs-built_in">this</span>.tryEntries[<span class="hljs-number">0</span>];
      <span class="hljs-keyword">var</span> rootRecord = rootEntry.completion;
      <span class="hljs-keyword">if</span> (rootRecord.type === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-comment">// 如果第一个状态未throw说明 报错没有被捕获直接抛出错误</span>
        <span class="hljs-keyword">throw</span> rootRecord.arg;
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.rval;
    &#125;,

    <span class="hljs-attr">dispatchException</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">exception</span>) </span>&#123;
      <span class="hljs-comment">//看上一</span>
    &#125;,

    <span class="hljs-attr">abrupt</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, arg</span>) </span>&#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">if</span> (
          entry.tryLoc <= <span class="hljs-built_in">this</span>.prev &&
          hasOwn.call(entry, <span class="hljs-string">"finallyLoc"</span>) &&
          <span class="hljs-built_in">this</span>.prev < entry.finallyLoc
        ) &#123;
          <span class="hljs-keyword">var</span> finallyEntry = entry;
          <span class="hljs-keyword">break</span>;
        &#125;
      &#125;

      <span class="hljs-keyword">if</span> (
        finallyEntry &&
        (type === <span class="hljs-string">"break"</span> || type === <span class="hljs-string">"continue"</span>) &&
        finallyEntry.tryLoc <= arg &&
        arg <= finallyEntry.finallyLoc
      ) &#123;
        <span class="hljs-comment">// Ignore the finally entry if control is not jumping to a</span>
        <span class="hljs-comment">// location outside the try/catch block.</span>
        finallyEntry = <span class="hljs-literal">null</span>;
      &#125;

      <span class="hljs-comment">// 主要看这部分 创建一个 &#123;type:return,arg:报错返回值&#125;</span>
      <span class="hljs-keyword">var</span> record = finallyEntry ? finallyEntry.completion : &#123;&#125;;
      record.type = type;
      record.arg = arg;

      <span class="hljs-keyword">if</span> (finallyEntry) &#123;
        <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"next"</span>;
        <span class="hljs-built_in">this</span>.next = finallyEntry.finallyLoc;
        <span class="hljs-keyword">return</span> ContinueSentinel;
      &#125;

      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.complete(record);
    &#125;,

    <span class="hljs-attr">complete</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">record, afterLoc</span>) </span>&#123;
        <span class="hljs-comment">//record &#123;type:return,arg:报错返回值&#125;</span>
      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
        <span class="hljs-keyword">throw</span> record.arg;
      &#125;

      <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"break"</span> || record.type === <span class="hljs-string">"continue"</span>) &#123;
        <span class="hljs-built_in">this</span>.next = record.arg;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"return"</span>) &#123;
      <span class="hljs-comment">// 主要看这里 返回值赋值给 context.rval 改变方法为return 改变next为end</span>
        <span class="hljs-built_in">this</span>.rval = <span class="hljs-built_in">this</span>.arg = record.arg;
        <span class="hljs-built_in">this</span>.method = <span class="hljs-string">"return"</span>;
        <span class="hljs-built_in">this</span>.next = <span class="hljs-string">"end"</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"normal"</span> && afterLoc) &#123;
        <span class="hljs-built_in">this</span>.next = afterLoc;
      &#125;
    <span class="hljs-comment">// 返回ContinueSentinel .return .throw方法直接走下一个case</span>
      <span class="hljs-keyword">return</span> ContinueSentinel;
    &#125;,
    <span class="hljs-attr">catch</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">tryLoc</span>) </span>&#123;
    <span class="hljs-comment">// 找到对应错误项 并返回</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-built_in">this</span>.tryEntries.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; --i) &#123;
        <span class="hljs-keyword">var</span> entry = <span class="hljs-built_in">this</span>.tryEntries[i];
        <span class="hljs-keyword">if</span> (entry.tryLoc === tryLoc) &#123;
          <span class="hljs-keyword">var</span> record = entry.completion;
          <span class="hljs-keyword">if</span> (record.type === <span class="hljs-string">"throw"</span>) &#123;
            <span class="hljs-keyword">var</span> thrown = record.arg;
            resetTryEntry(entry);
          &#125;
          <span class="hljs-keyword">return</span> thrown;
        &#125;
      &#125;

      <span class="hljs-comment">// The context.catch method must only be called with a location</span>
      <span class="hljs-comment">// argument that corresponds to a known catch block.</span>
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"illegal catch attempt"</span>);
    &#125;,

  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>over~</p></div>  
</div>
            